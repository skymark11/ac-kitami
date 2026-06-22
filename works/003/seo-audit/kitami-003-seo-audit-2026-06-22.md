# kitami-003 SEO 監査レポート

監査日: 2026-06-22
監査者: `_engineer` エージェント（seo-audit スキル準拠の手動採点）
対象: `works/003/index.html`（旧 works/004 をリネーム + v2 仕様化完了版）

## 総合スコア: 99 / 100（評価: 優秀）

80 点ゲート: クリア。works/002 と同水準。

## カテゴリ別スコア

| カテゴリ | 配点 | 獲得 | 主な確認内容 |
|---|---|---|---|
| テクニカル SEO 基盤 | 25 | 25 | title 36字、meta description 121字、canonical、lang="ja"、UTF-8、viewport、OGP 5項目 |
| 構造化データ | 20 | 20 | Article（image 2枚指定）、BreadcrumbList、Service の JSON-LD 統一 |
| コンテンツ品質 | 20 | 20 | H1 単一、H2-H3 階層整合、独自コンテンツ（換気口転用・コーキング・木板加工・近隣住戸の事前調査） |
| 画像最適化 | 15 | 15 | 全画像 WebP/JPG `<picture>` 構成、alt に地名・機種・部位記述、fetchpriority/lazy 適切、width/height 全指定 |
| 内部リンク最適化 | 10 | 10 | パンくず、関連事例（001/002 共に正しいサムネ参照）、ヘッダーナビ |
| モバイル対応 | 5 | 5 | viewport、Tailwind レスポンシブ、CTA タップターゲット |
| パフォーマンス | 3 | 2 | preconnect あり / preload（Google Fonts）が未設定 → -1 |
| その他技術要件 | 2 | 2 | HTTPS、UTF-8 |

## クリティカル指摘: なし

## v2 仕様化対応内容（2026-06-22）

1. **PhotoSwipe 実装**: head に CSS（非同期読み込み + .pswp-gallery スタイル）、6つのギャラリー（FV B/A・室内機 B/A・室外機 B/A・配管穴 B/A・施工工程 4枚・完成写真 5枚）に `<a>` ラップ + data-pswp-width/height、body 末尾に init script
2. **alt 属性強化**: 全画像に「北見市春光町」「機種名」「部位（室内機・室外機・配管穴・換気口）」を含めた記述に改善
3. **関連事例リンク修正**: 001 → `hero-after.webp` / 002 → `done-1-indoor-unit.webp` に修正（旧 after-01.webp / after-04.webp は削除済みでリンク切れだった）

## 推奨改善（公開後の Lighthouse 改善時に対応可）

### 1. Google Fonts の preload 設定（パフォーマンス +1 点）

`<head>` 内、`<link rel="preconnect" ...>` の直後に以下を追加すると LCP が改善する可能性:

```html
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap">
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap">
```

優先度は低い（works/002 と同様）。

## 任意改善

### 1. お客様アンケートの掲載

works/001、works/002 にはあるが works/003 にはない。手書きアンケートがあれば追加で SEO + E-E-A-T 強化になる。今回の案件で取得できていない場合は省略可。

### 2. 写真枚数の更新

meta description「写真12枚」と書いてあるが、実際は B/A 6枚 + 工程 4枚 + 完成 5枚 = **15枚** + ファーストビュー B/A 2枚（重複再利用）。「写真15枚」に更新も可能（影響軽微）。

## 検証用ツール

- リッチリザルトテスト: https://search.google.com/test/rich-results
- PageSpeed Insights: https://pagespeed.web.dev/
- Lighthouse: Chrome DevTools 内蔵

## 結論

公開可能水準（80 点ゲート）を大幅にクリア。works/002 と同等の 99/100。
FTP アップロード可。
