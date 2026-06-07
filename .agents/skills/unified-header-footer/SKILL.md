---
name: unified-header-footer
description: ac-kitami.com 全ページで使うヘッダー・フッター・フローティングCTAの統一テンプレ。新規ページ作成時や既存ページ修正時に、このテンプレに従って統一する。
metadata:
  type: site-template
  scope: ac-kitami.com
---

# ヘッダー・フッター統一テンプレート

## 用途

ac-kitami.com 全ページで使うヘッダー・フッター・フローティングCTAの統一テンプレ。
新規ページ作成時・既存ページ修正時にこのテンプレに従う。

## 設計判断の根拠

- **SEO**: 全ページから全地域ページに内部リンクが張られると、新地域ページのインデックスが早く、サイト全体のクロール効率が上がる。フッター全ページ共通は Google にボイラープレートとして扱われペナルティ対象外。
- **UX**: ブランド統一感（電話番号・営業時間・LINEなどがどこでも同じ）。「網走を見に来た人が美幌・紋別も対応していると気づける」=取りこぼし防止。
- **拡張性**: 美幌・紋別・訓子府・置戸が増えても、フッターの「対応エリア」列のリンク追加だけで全ページに反映できる。

---

## ファイル位置別パスprefix表

各ページの位置に応じて、テンプレ中の `{{PATH}}` を以下の値に置換する。

| ファイル位置 | `{{PATH}}` 値 |
|---|---|
| `/index.html`（トップ） | `""`（空文字） |
| `/about/index.html` | `"../"` |
| `/abashiri/index.html` | `"../"` |
| `/relocation/index.html` | `"../"` |
| `/privacy-policy/index.html` | `"../"` |
| `/bihoro/index.html` | `"../"` |
| `/monbetsu/index.html` | `"../"` |
| `/column/200v-aircon-check/index.html` | `"../../"` |
| `/column/aircon-2027-mondai/index.html` | `"../../"` |
| `/works/index.html` | `"../"` |
| `/abashiri/works/index.html` | `"../../"` |
| `/works/001/index.html` 等 | `"../../"` |
| `/abashiri/works/001/index.html` 等 | `"../../../"` |

---

## ヘッダーHTMLテンプレ

```html
<header class="bg-white shadow-md sticky top-0 z-50">
<div class="container mx-auto px-4 py-3">
<div class="flex justify-between items-center">
<div class="flex items-center">
<a href="{{PATH}}" class="text-2xl font-['Pacifico'] text-primary">エアコンラボ北見店</a>
</div>
<div class="hidden md:flex items-center space-x-6">
<a href="{{PATH}}" class="text-gray-700 hover:text-primary font-medium">ホーム</a>
<a href="{{PATH}}#area" class="text-gray-700 hover:text-primary font-medium">対応エリア</a>
<a href="{{PATH}}#works" class="text-gray-700 hover:text-primary font-medium">施工事例</a>
<a href="{{PATH}}#contact" class="text-gray-700 hover:text-primary font-medium">お問い合わせ</a>
</div>
<div class="flex items-center space-x-4">
<a href="tel:070-4080-0965" class="hidden md:flex items-center text-gray-800 hover:text-primary">
<div class="w-10 h-10 flex items-center justify-center bg-primary rounded-full text-white mr-2">
<i class="ri-phone-fill ri-lg"></i>
</div>
<div>
<p class="text-xs">お電話でのお問い合わせ</p>
<p class="font-bold">070-4080-0965</p>
</div>
</a>
<a href="https://lin.ee/uGVDwT4" target="_blank" rel="noopener" class="hidden md:flex items-center bg-[#06C755] text-white px-4 py-2 rounded-button whitespace-nowrap">
<div class="w-6 h-6 flex items-center justify-center mr-1">
<i class="ri-line-fill ri-lg"></i>
</div>
<span>LINE相談</span>
</a>
<button class="md:hidden w-10 h-10 flex items-center justify-center" id="mobile-menu-button" aria-label="メニューを開く" aria-expanded="false" aria-controls="mobile-menu">
<i class="ri-menu-line ri-2x text-gray-700"></i>
</button>
</div>
</div>
</div>
<!-- モバイルメニュー -->
<div id="mobile-menu" class="hidden md:hidden bg-white border-t">
<div class="container mx-auto px-4 py-2">
<div class="flex flex-col space-y-3">
<a href="{{PATH}}" class="text-gray-700 hover:text-primary py-2">ホーム</a>
<a href="{{PATH}}#area" class="text-gray-700 hover:text-primary py-2">対応エリア</a>
<a href="{{PATH}}#works" class="text-gray-700 hover:text-primary py-2">施工事例</a>
<a href="{{PATH}}#contact" class="text-gray-700 hover:text-primary py-2">お問い合わせ</a>
<div class="flex space-x-4 py-2">
<a href="tel:070-4080-0965" class="flex items-center text-gray-800 hover:text-primary">
<div class="w-8 h-8 flex items-center justify-center bg-primary rounded-full text-white mr-2">
<i class="ri-phone-fill"></i>
</div>
<span class="font-bold">070-4080-0965</span>
</a>
<a href="https://lin.ee/uGVDwT4" target="_blank" rel="noopener" class="flex items-center bg-[#06C755] text-white px-3 py-1 rounded-button">
<div class="w-5 h-5 flex items-center justify-center mr-1">
<i class="ri-line-fill"></i>
</div>
<span>LINE相談</span>
</a>
</div>
</div>
</div>
</div>
</header>
```

---

## フッターHTMLテンプレ

```html
<footer class="bg-gray-800 text-white py-12">
<div class="container mx-auto px-4">
<div class="flex flex-wrap -mx-4">
<div class="w-full md:w-3/12 px-4 mb-8 md:mb-0">
<h3 class="text-xl font-['Pacifico'] mb-4">エアコンラボ北見店</h3>
<p class="text-gray-300 mb-4">北見市を中心に、エアコンの販売・設置取付・メンテナンスを行う地域密着型の専門店です。</p>
<p class="text-xs text-gray-400 mb-4">電気工事業登録 / 第二種電気工事士 / 石綿作業主任者 / 一般建築物石綿含有建材調査者</p>
</div>
<div class="w-full md:w-6/12 px-4 mb-8 md:mb-0">
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
<div>
<h3 class="text-lg font-bold mb-4">サービス</h3>
<ul class="space-y-2">
<li><a href="{{PATH}}#aircon-purchase-section" class="text-gray-300 hover:text-white">エアコン販売</a></li>
<li><a href="{{PATH}}#installation-work-section" class="text-gray-300 hover:text-white">設置工事</a></li>
<li><a href="{{PATH}}#installation-work-section" class="text-gray-300 hover:text-white">料金案内</a></li>
<li><a href="{{PATH}}#works" class="text-gray-300 hover:text-white">施工事例</a></li>
</ul>
</div>
<div>
<h3 class="text-lg font-bold mb-4">対応エリア</h3>
<ul class="space-y-2">
<li><a href="{{PATH}}" class="text-gray-300 hover:text-white">北見市（拠点）</a></li>
<li><a href="{{PATH}}abashiri/" class="text-gray-300 hover:text-white">網走市</a></li>
<li class="text-gray-500">美幌町 <span class="text-xs">※準備中</span></li>
<li class="text-gray-500">紋別市 <span class="text-xs">※準備中</span></li>
<li class="text-gray-500">訓子府町 <span class="text-xs">※対応</span></li>
<li class="text-gray-500">置戸町 <span class="text-xs">※対応</span></li>
</ul>
</div>
<div>
<h3 class="text-lg font-bold mb-4">当店について</h3>
<ul class="space-y-2">
<li><a href="{{PATH}}about/" class="text-gray-300 hover:text-white">代表者紹介・取得資格</a></li>
<li><a href="{{PATH}}relocation/" class="text-gray-300 hover:text-white">移設工事のご注意</a></li>
<li><a href="{{PATH}}column/200v-aircon-check/" class="text-gray-300 hover:text-white">200Vエアコン購入前の確認</a></li>
<li><a href="{{PATH}}column/aircon-2027-mondai/" class="text-gray-300 hover:text-white">エアコンの2027年問題</a></li>
</ul>
</div>
</div>
</div>
<div class="w-full md:w-3/12 px-4 mb-8 md:mb-0">
<h3 class="text-lg font-bold mb-4">お問い合わせ</h3>
<div class="space-y-2 text-gray-300">
<p><i class="ri-phone-fill mr-2"></i>070-4080-0965</p>
<p><i class="ri-time-fill mr-2"></i>9:00～19:00（年中無休）</p>
</div>
</div>
</div>
<div class="border-t border-gray-700 mt-8 pt-8">
<div class="flex flex-col md:flex-row justify-between items-center">
<div class="mb-4 md:mb-0">
<p class="text-sm text-gray-400">&copy; 2025-2026 <a href="{{PATH}}" class="hover:text-white">エアコンラボ北見店</a> All Rights Reserved.</p>
</div>
<div class="flex space-x-4">
<a href="{{PATH}}privacy-policy/" class="text-sm text-gray-400 hover:text-white">プライバシーポリシー</a>
</div>
</div>
</div>
</div>
</footer>
```

---

## フローティングCTAテンプレ

`</footer>` の後ろに配置。

```html
<!-- フローティングCTA -->
<div class="floating-cta">
<div class="flex flex-col space-y-2">
<a href="tel:070-4080-0965" class="bg-primary hover:bg-blue-700 text-white px-4 py-3 rounded-full shadow-lg transition duration-300 flex items-center whitespace-nowrap">
<div class="w-6 h-6 flex items-center justify-center mr-2">
<i class="ri-phone-fill"></i>
</div>
<span>お電話</span>
</a>
<a href="https://lin.ee/uGVDwT4" target="_blank" rel="noopener" class="bg-[#06C755] hover:bg-[#05a648] text-white px-4 py-3 rounded-full shadow-lg transition duration-300 flex items-center whitespace-nowrap">
<div class="w-6 h-6 flex items-center justify-center mr-2">
<i class="ri-line-fill"></i>
</div>
<span>LINE</span>
</a>
</div>
</div>
```

フローティングCTAに必要なCSS（`css/styles.css` または `<style>` に追加）:

```css
.floating-cta {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 100;
}
```

---

## 適用手順

### 新規ページ作成時
1. このスキルを開く
2. ページの位置から `{{PATH}}` を決定（上の表を参照）
3. ヘッダー・フッター・フローティングCTAをコピペ
4. テンプレ中の `{{PATH}}` を全て置換
5. ローカルでブラウザ確認（リンクが正しく飛ぶか）

### 既存ページの更新時
1. このスキルを開く
2. 既存ページの`<header>`から`</header>`、`<footer>`から`</footer>`を、テンプレの内容で置換
3. `{{PATH}}` を置換
4. フローティングCTAが無ければ追加

### 新地域ページが公開された時（例: 美幌町）
1. このスキル本文の「対応エリア」リストを編集:
   - `<li class="text-gray-500">美幌町 <span class="text-xs">※準備中</span></li>`
   - ↓
   - `<li><a href="{{PATH}}bihoro/" class="text-gray-300 hover:text-white">美幌町</a></li>`
2. 全ページのフッター「対応エリア」リストを同じく更新（Grep で「※準備中」を探して該当箇所を修正）
3. sitemap.xml に URL 追加
4. DEPLOY-STATUS.md を更新

---

## 注意事項

1. **CSSパスは別管理**: テンプレの `{{PATH}}` 置換は、ヘッダー・フッター内のリンクとフローティングCTAのみ。`<link rel="stylesheet" href="css/styles.css">` などのCSSパスは各ページの相対位置で別途調整。
2. **未公開地域のリンクは付けない**: 美幌・紋別など個別ページ未公開地域は、テキスト表示のみ（404を防ぐ）。
3. **モバイルメニュー**: `id="mobile-menu"` は `js/main.js` から制御される。idを変えないこと。
4. **JS依存**: ヘッダーは `js/main.js` が必要（モバイルメニュー開閉）。全ページで `<script src="{{PATH}}js/main.js" defer></script>` を読み込む。
5. **絶対パスとの違い**: テンプレでは相対パスを使用。ルートからの絶対パス（`/about/` 等）を使うと file:// プロトコルで開発時に動かないため。

---

## 関連スキル

- [[js-case-studies-section]] - 施工事例の量産レーン
- [[image-to-webp]] - 画像変換
- [[seo-audit]] - SEO監査
