# デプロイ状況

最終更新: 2026-06-25

## 案件 ID とパスの対応表（命名規則）

施工事例の命名は **意図的に二重構造** で運用している。SEO 上 URL 変更を最小化するため:

- **ページ URL**: `/works/{通し番号}/` — 北見・近郊エリアの全体公開順（地域問わず）
- **画像フォルダ**: `/images/works/{地域}/{地域内番号}/` — 地域別管理（対応エリア拡大時の整理性）
- **案件 ID（内部参照）**: `{地域}-{地域内番号}` — `/case-study` スラッシュコマンド・スキル・NOW.md 内で使う識別子

| 案件 ID | ページ URL | 画像フォルダ | 公開状態 |
|---|---|---|---|
| kitami-001 | `/works/001/` | `/images/works/kitami/001/` | FTP公開済み（2026-06-25）|
| kitami-002 | `/works/002/` | `/images/works/kitami/002/` | FTP公開済み（2026-06-25）|
| kitami-003 | `/works/003/` | `/images/works/kitami/003/` | FTP公開済み（2026-06-25）|
| kunneppu-001 | `/works/004/` | `/images/works/kunneppu/001/` | FTP公開済み（2026-06-25）|

### 新規案件追加時のルール

1. 案件 ID は `{地域ローマ字}-{地域内 3桁番号}` で振る（例: `abashiri-003`, `bihoro-001`）
2. 画像フォルダは `/images/works/{地域ローマ字}/{地域内番号}/` に作る
3. ページ URL は `/works/{次の通し番号}/` を使う（地域を含めない）
4. このセクションの対応表に 1 行追加する

### URL 変更を避ける理由

直近の 2026-06-22 に `/kitami/works/001/` → `/works/001/` の URL 統合を実施したばかり。さらに別の URL 変更を加えると SEO 評価がリセットされるリスクが高い。命名の不整合は「文書化で補う」方針で運用する。

---

## FTP公開済み
- / (トップページ) - 2026-06-25 事例カード更新版に再アップ
- /about/ - 2026-06-25 防虫キャップ削除版に再アップ
- /abashiri/
- /abashiri/works/ - 施工事例ハブ（2026-05-30公開）
- /abashiri/works/001/ - 潮見アパート施工事例（2026-05-30公開）
- /abashiri/works/002/ - 南窓用エアコン施工事例（2026-05-30公開）
- /kitami/works/001/ - 北見市中央三輪 施工事例（2026-06-16公開）→ **2026-06-25 に /works/001/ へ統合**。/.htaccess の 301 リダイレクト動作確認済み。サーバー側の旧フォルダ削除は任意（実害なし、いずれ削除推奨）
- /works/ - 北見・近郊エリア 施工事例ハブ（2026-06-25公開・カード 4 件）
- /works/001/ - 北見市中央三輪 施工事例（2026-06-25公開・v2 仕様・SEO 93点）
- /works/002/ - 北見市相ノ内 施工事例（2026-06-25公開・v2 仕様・SEO 99/100・PhotoSwipe）
- /works/003/ - 北見市春光町 市営団地 施工事例（2026-06-25公開・v2 仕様化済み・SEO 99/100）
- /works/004/ - 訓子府町 小林様 軒天天吊り施工事例（2026-06-25公開・v2 仕様・三菱ズバ暖・リフォーム外壁無傷・SEO 99/100）
- /images/works/kunneppu/001/ - kunneppu-001 用画像 20 ファイル（2026-06-25 新規アップ）
- /images/works/kitami/001/002/003/ - 2026-06-25 ローカル最新を上書きアップ（旧ファイル併存・無害）
- /js/photoswipe/ - PhotoSwipe v5 三点セット（2026-06-25 新規アップ）
- /sitemap.xml - 2026-06-25 全 URL を最新化（/works/001-004/ 含む 15 件）
- /.htaccess - 2026-06-25 301 リダイレクト追加（`/kitami/works/001/` → `/works/001/`）動作確認済み
- /relocation/
- /column/200v-aircon-check/
- /column/aircon-2027-mondai/
- /privacy-policy/

## 公開後のフォローアップタスク（次回 PC 帰宅後）

| 優先 | タスク | URL/内容 |
|---|---|---|
| 中 | Search Console B-4: リッチリザルトテスト | https://search.google.com/test/rich-results で `/works/004/` |
| 中 | Search Console B-5: PageSpeed Insights | https://pagespeed.web.dev/ で `/works/004/` 中心に |
| 低 | FTP 側の `/kitami/works/001/` フォルダ削除 | 301 動作確認済みで実害なしだが、いずれ削除推奨 |
| 低 | FTP 側の `_classification/` `seo-audit/` 等の掃除 | 全部アップした際に上がっている可能性。FFFTP で確認 → 削除 |
| 低 | NOW.md 圧縮（500 行超） | 直近 1 ヶ月より古い経緯を `LOG/` に切り出し → 150-200 行に圧縮 |

## 未公開（作成中・別途対応）
- /works/003/ の v2 仕様化（PhotoSwipe・semantic命名・SEO監査）は別タスク
- /monbetsu/ - 内容確定後にアップ
- /bihoro/ - プレースホルダー。内容確定後にアップ
- /abashiri/works/003/ - 駒場入れ替え事例。画像はあるがページ未生成（works-case-builderスキルで生成予定）

## FTP不要（管理用ファイル）
- /line/ - LINE公式アカウントの応答テンプレート（mdファイル）
- /.agents/ - スキル定義（unified-header-footer, works-case-builder）
- /.claude/ - Claude 設定
- /CLAUDE.md, /DEPLOY-STATUS.md, /NOW.md - プロジェクト管理ファイル
- /abashiri/works/PLAN.md - 作業計画書
- /images/works/*/raw/ - 元写真バックアップ（容量大きい、公開不要）
- /images/works/abashiri/001/info.txt, /images/works/abashiri/*/info.txt - 案件情報メモ
- すべての `*.tmp` `*.tmp.*` ファイル - Dropbox同期残骸
