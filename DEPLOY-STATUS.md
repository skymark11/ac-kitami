# デプロイ状況

最終更新: 2026-06-22

## FTP公開済み
- / (トップページ)
- /about/
- /abashiri/
- /abashiri/works/ - 施工事例ハブ（2026-05-30公開）
- /abashiri/works/001/ - 潮見アパート施工事例（2026-05-30公開）
- /abashiri/works/002/ - 南窓用エアコン施工事例（2026-05-30公開）
- /kitami/works/001/ - 北見市中央三輪 施工事例（2026-06-16公開・要注意：将来 /works/001/ への統合予定。301リダイレクト対応必要）
- /relocation/
- /column/200v-aircon-check/
- /column/aircon-2027-mondai/
- /privacy-policy/

## 公開準備中（今回FTPアップ予定）
- /works/002/ - 北見市相ノ内 施工事例（v2仕様・SEO 99/100・2026-06-22準備完了）
- / (トップページ) - 事例2サムネ画像パス修正 + 「詳細を見る」リンク追加
- /sitemap.xml - /works/002/ URL追加

## 未公開（作成中・別途対応）
- /works/001/ - 北見市中央三輪（kitami/works/001/ と重複。統合タスク要）
- /works/004/ - 北見市春光町 市営団地（ローカルにのみ存在。内容レビュー後判断）
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
