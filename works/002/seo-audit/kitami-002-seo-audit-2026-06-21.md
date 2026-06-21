# kitami-002 SEO 監査レポート

監査日: 2026-06-21
監査者: `_engineer` エージェント（seo-audit スキル準拠の手動採点）
対象: `works/002/index.html`（v2 ステップ 3 フェーズ 5 修正完了版）

## 総合スコア: 99 / 100（評価: 優秀）

80 点ゲート: クリア。

## カテゴリ別スコア

| カテゴリ | 配点 | 獲得 | 主な確認内容 |
|---|---|---|---|
| テクニカル SEO 基盤 | 25 | 25 | title 35字、meta description 120字、canonical、lang="ja"、UTF-8、viewport、OGP 5項目 |
| 構造化データ | 20 | 20 | Article（image 2枚指定）、BreadcrumbList、Service の JSON-LD 統一 |
| コンテンツ品質 | 20 | 20 | H1 単一、H2-H3 階層整合、独自コンテンツ（担当者コメント・お客様の声・30年ストーリー） |
| 画像最適化 | 15 | 15 | 全画像 WebP/JPG `<picture>` 構成、alt 記述、fetchpriority/lazy 適切、width/height 全指定 |
| 内部リンク最適化 | 10 | 10 | パンくず、関連事例、ヘッダーナビ |
| モバイル対応 | 5 | 5 | viewport、Tailwind レスポンシブ、CTA タップターゲット |
| パフォーマンス | 3 | 2 | preconnect あり / preload（Google Fonts）が未設定 → -1 |
| その他技術要件 | 2 | 2 | HTTPS、UTF-8 |

## クリティカル指摘: なし

## 推奨改善（公開後の Lighthouse 改善時に対応可）

### 1. Google Fonts の preload 設定（パフォーマンス +1 点）

`<head>` 内、`<link rel="preconnect" ...>` の直後に以下を追加すると LCP が改善する可能性:

```html
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap">
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap">
```

ただし Pacifico は装飾的なロゴ部分のみで使用されており、本文表示には影響しないため、優先度は低い。

## 任意改善

### 1. meta description の枚数記述の更新

現状: 「写真13枚・お客様アンケートも掲載」
新スキームでの実枚数: ファーストビュー 2枚 + B/A 6枚 + 化粧モール 3枚 + 完成写真 7枚 + アンケート 1枚 = **19枚**

公開直前に「写真19枚・お客様アンケートも掲載」へ更新を推奨（影響軽微）。

## 検証用ツール

- リッチリザルトテスト: https://search.google.com/test/rich-results
- PageSpeed Insights: https://pagespeed.web.dev/
- Lighthouse: Chrome DevTools 内蔵

## 結論

公開可能水準（80 点ゲート）を大幅にクリア。フェーズ 7（旧画像削除 → Joe 承認 → 公開準備）に進んで問題ない。
