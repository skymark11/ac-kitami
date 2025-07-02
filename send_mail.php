<?php
header('Content-Type: application/json; charset=UTF-8');

// CORS対応（必要に応じて）
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// POSTリクエストのみ許可
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => '不正なリクエストです。']);
    exit;
}

// 送信先メールアドレス（管理者）
$admin_email = 'shishido@js-farty.jp';
$admin_name = 'エアコンラボ北見店';

// フォームデータの取得とサニタイズ
$name = isset($_POST['name']) ? trim($_POST['name']) : '';
$phone = isset($_POST['phone']) ? trim($_POST['phone']) : '';
$email = isset($_POST['email']) ? trim($_POST['email']) : '';
$address = isset($_POST['address']) ? trim($_POST['address']) : '';
$inquiry_type = isset($_POST['inquiry_type']) ? trim($_POST['inquiry_type']) : '';
$message = isset($_POST['message']) ? trim($_POST['message']) : '';
$privacy_agreement = isset($_POST['privacy_agreement']) ? $_POST['privacy_agreement'] : '';

// バリデーション
$errors = [];

if (empty($name)) {
    $errors[] = 'お名前は必須です。';
}

if (empty($phone)) {
    $errors[] = '電話番号は必須です。';
}

if (empty($inquiry_type)) {
    $errors[] = 'お問い合わせ内容の選択は必須です。';
}

if (empty($privacy_agreement)) {
    $errors[] = '個人情報の取り扱いに同意していただく必要があります。';
}

// メールアドレスの形式チェック（入力されている場合のみ）
if (!empty($email) && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = 'メールアドレスの形式が正しくありません。';
}

// エラーがある場合は返す
if (!empty($errors)) {
    echo json_encode(['success' => false, 'message' => implode("\n", $errors)]);
    exit;
}

// お問い合わせ内容の日本語変換
$inquiry_types = [
    'estimate' => 'お見積り依頼',
    'product' => 'エアコン本体について',
    'installation' => '設置工事について',
    'other' => 'その他'
];
$inquiry_type_jp = isset($inquiry_types[$inquiry_type]) ? $inquiry_types[$inquiry_type] : $inquiry_type;

// 現在の日時
$datetime = date('Y年m月d日 H:i:s');

// 管理者向けメール内容
$admin_subject = '【エアコンラボ北見店】新しいお問い合わせ';
$admin_body = "エアコンラボ北見店のWebサイトより、新しいお問い合わせがありました。\n\n";
$admin_body .= "■ 受信日時: {$datetime}\n";
$admin_body .= "■ お名前: {$name}\n";
$admin_body .= "■ 電話番号: {$phone}\n";
$admin_body .= "■ メールアドレス: " . ($email ? $email : '未入力') . "\n";
$admin_body .= "■ ご住所: " . ($address ? $address : '未入力') . "\n";
$admin_body .= "■ お問い合わせ内容: {$inquiry_type_jp}\n";
$admin_body .= "■ 詳細内容:\n" . ($message ? $message : '未入力') . "\n\n";
$admin_body .= "─────────────────────────\n";
$admin_body .= "※このメールは自動送信です。\n";
$admin_body .= "お客様への対応をお願いいたします。\n";

// お客様向け自動返信メール内容
$customer_subject = '【エアコンラボ北見店】お問い合わせありがとうございます';
$customer_body = "{$name} 様\n\n";
$customer_body .= "この度は、エアコンラボ北見店にお問い合わせいただき、誠にありがとうございます。\n";
$customer_body .= "以下の内容でお問い合わせを承りました。\n\n";
$customer_body .= "■ 受信日時: {$datetime}\n";
$customer_body .= "■ お名前: {$name}\n";
$customer_body .= "■ 電話番号: {$phone}\n";
$customer_body .= "■ メールアドレス: " . ($email ? $email : '未入力') . "\n";
$customer_body .= "■ ご住所: " . ($address ? $address : '未入力') . "\n";
$customer_body .= "■ お問い合わせ内容: {$inquiry_type_jp}\n";
$customer_body .= "■ 詳細内容:\n" . ($message ? $message : '未入力') . "\n\n";
$customer_body .= "担当者より2営業日以内にご連絡させていただきます。\n";
$customer_body .= "お急ぎの場合は、お電話（070-4080-0965）にてお問い合わせください。\n\n";
$customer_body .= "今後ともエアコンラボ北見店をよろしくお願いいたします。\n\n";
$customer_body .= "─────────────────────────\n";
$customer_body .= "エアコンラボ北見店\n";
$customer_body .= "電話: 070-4080-0965\n";
$customer_body .= "営業時間: 9:00～19:00（年中無休）\n";
$customer_body .= "─────────────────────────\n";

// メールヘッダー設定
$headers_admin = [];
$headers_admin[] = 'From: ' . mb_encode_mimeheader($admin_name) . ' <' . $admin_email . '>';
$headers_admin[] = 'Reply-To: ' . ($email ? $email : $admin_email);
$headers_admin[] = 'Content-Type: text/plain; charset=UTF-8';
$headers_admin[] = 'Content-Transfer-Encoding: 8bit';

$headers_customer = [];
$headers_customer[] = 'From: ' . mb_encode_mimeheader($admin_name) . ' <' . $admin_email . '>';
$headers_customer[] = 'Reply-To: ' . $admin_email;
$headers_customer[] = 'Content-Type: text/plain; charset=UTF-8';
$headers_customer[] = 'Content-Transfer-Encoding: 8bit';

// メール送信フラグ
$admin_sent = false;
$customer_sent = false;

try {
    // 管理者にメール送信
    $admin_sent = mb_send_mail(
        $admin_email,
        $admin_subject,
        $admin_body,
        implode("\r\n", $headers_admin)
    );

    // お客様に自動返信メール送信（メールアドレスが入力されている場合のみ）
    if (!empty($email)) {
        $customer_sent = mb_send_mail(
            $email,
            $customer_subject,
            $customer_body,
            implode("\r\n", $headers_customer)
        );
    } else {
        $customer_sent = true; // メールアドレス未入力の場合は成功扱い
    }

    if ($admin_sent && $customer_sent) {
        echo json_encode([
            'success' => true,
            'message' => 'お問い合わせありがとうございます。確認メールを送信いたしました。当日～2営業日以内にご連絡させていただきます。'
        ]);
    } else {
        throw new Exception('メール送信に失敗しました。');
    }

} catch (Exception $e) {
    error_log('Contact form error: ' . $e->getMessage());
    echo json_encode([
        'success' => false,
        'message' => '送信に失敗しました。お手数ですが、お電話（070-4080-0965）にてお問い合わせください。'
    ]);
}
?>