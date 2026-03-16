## セッション引き継ぎ

最終更新: 2026-03-03

### 作業中だったこと
- kitami-001（中央三輪_梅津様）の施工事例作成（画像WebP変換の直前で中断）

### 今回完了したこと
- js-case-studies-section スキルと js-local-seo-master スキルの全内容を調査・把握
- 網走市（abashiri）の既存施工事例ページ（一覧・詳細001/002）をスキル基準で評価
- kitami-001 の施工情報を見積書・請求書の画像から抽出・確定
- 実装プラン作成・承認済み

### 決定事項
- **使用スキル**: js-case-studies-section + js-local-seo-master を融合
- **スコープ**: index.html施工事例セクション入れ替え + works/001/詳細ページ作成
- **使用事例**: kitami-001のみ実データ、002/003は「準備中」として参考配置
- **施工情報（確定済み）**:
  - 施工日: 2025年7月
  - 地域: 北見市中央三輪
  - 建物: 戸建て（平屋）
  - 機種: 三菱 霧ヶ峰 GV2825（10畳用）
  - 費用: 209,220円（税込）※請求額を掲載
  - 工期: 1日（約5-8時間）
  - 担当者: 宍戸 尚貴（第二種電気工事士）
  - 追加工事: 屋根付き据置金具、室外化粧カバー、専用回路増設
- **使用画像（info-template.txt記載）**:
  - before: before-00, before-02
  - after: after-02,05,06,08,09,11,17,20
  - process: process-01,02,14,19
  - アンケート: kitami-chuomiwa-aircon-review-001.jpg
- **画像ソース**: `assets/photos/_inbox/エアコン写真素材/北見市/kitami-001_中央三輪_梅津様/`
- **画像出力先**: `htdocs/ac-kitami/images/works/kitami/001/`（既存IMG_*.jpgと共存）

### 次にやるべきこと
1. **画像WebP変換**（Step 1）: _inboxから指定画像をWebP変換（品質80、最大幅800px）して出力先に配置
2. **index.html施工事例セクション入れ替え**（Step 2）: 行719-778のreaddy.ai偽画像を実データカードに置換
3. **works/001/index.html作成**（Step 3）: abashiri/works/001/index.htmlをテンプレートとして詳細ページ新規作成
4. **品質検証**（Step 4）: Rubric採点80点以上確認

### 注意事項・文脈
- **プランファイル**: `C:\Users\shishido\.claude\plans\twinkling-snuggling-ocean.md` に詳細プランあり（必ず読むこと）
- **info-template.txt**: `assets/photos/_inbox/エアコン写真素材/北見市/kitami-001_中央三輪_梅津様/info-template.txt` に施工ポイントの詳細テキストあり（ストーリー化の元ネタ）
- **網走市ページとの改善点**: 費用表示追加、4軸タグ、width/height属性、担当者名・資格記載、アンケート画像追加
- **process-18.jpg vs process-19.jpg**: info-templateにはprocess-18とあるが、_inboxフォルダにはprocess-19.jpgが存在。要確認
- 002/003の画像は分類未完了のため、htdocs/ac-kitami/images/works/kitami/002/,003/のIMG_*.jpgから代表1枚を選定して使う
- index.htmlの施工事例セクションの現在位置は行719-778
