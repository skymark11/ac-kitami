## セッション引き継ぎ

最終更新: 2026-06-07

### 作業中だったこと
- なし（リポジトリ整合性整理を完了し、次は kitami-001 着手予定）

### 今回完了したこと（2026-06-07）
- **abashiri/works/* のFTP公開済み内容をGitに反映**（c4ab384 / 73ファイル）
  - 施工事例ハブ + 詳細001/002 ページ
  - 既存画像のWebP再変換による大幅軽量化（after-04: 1.9MB→78KB 等、合計数十MB削減）
  - sitemap.xml、index.html フッター・対応エリアリンク整備
  - DEPLOY-STATUS.md 更新
- **`.agents/skills/`** （unified-header-footer / works-case-builder）を Git 管理に追加
- **Dropbox同期競合コピー**（`.claude/settings.local (...競合コピー...).json`）を削除
- **スマホ作業ブランチ5件をすべて整理**:
  | ブランチ | 判定 |
  |---|---|
  | claude/ac-2027-kitami-page-YxKMG | mainに別実装で取込み済み → 削除 |
  | claude/ac-lab-landing-page-L8yXi | 古いLP試作 → 削除 |
  | claude/fix-construction-examples-jIzqM | 北見side works/ 試作（別案件）→ 削除 |
  | claude/issue-content-review-7Gmgv | お客様の声セクション → 後日改めるとして削除 |
  | claude/kitami-gbp-local-seo-ohvfJ | LocalBusiness強化 → 別タスク化して削除 |

### 決定事項
- **整合性**: ローカル = GitHub main = FTP公開状態 が揃った
- **kitami-001 計画は有効**: 画像WebP変換（Step 1）は完了済み（`images/works/kitami/001/` に15枚配置済み）
- **お客様の声セクション再実装**は別タスク
- **構造化データ強化スプリント**は別タスク

### 次にやるべきこと（優先順位）

#### 1. kitami-001 施工事例ページ作成（最優先・継続中）
- ✅ Step 1 画像WebP変換: 完了済み
- ⬜ Step 2: index.html 施工事例セクション（行719-778付近）を実データカードに置換
- ⬜ Step 3: `kitami/works/001/index.html` 新規作成（`abashiri/works/001/` をテンプレに）
- ⬜ Step 4: Rubric採点 80点以上確認
- **プランファイル**: `C:\Users\shishido\.claude\plans\twinkling-snuggling-ocean.md`
- **施工情報**: 下記「kitami-001 施工情報」参照

#### 2. お客様の声セクション再実装（別タスク・後日）
- 旧ブランチ claude/issue-content-review-7Gmgv の方向性を参考に:
  - 独立した `#reviews` セクションを作る
  - 3カードグリッド形式・星評価付き
  - LINE / Googleレビュー投稿の誘導CTA
- 現在 main の「お客様満足度98.5%」セクションを土台に統合する形で

#### 3. 構造化データ強化スプリント（別タスク・後日）
旧ブランチ claude/kitami-gbp-local-seo-ohvfJ の内容を**現main基準で再実装**。

- **index.html の LocalBusiness JSON-LD に追加**:
  - `@type` を `["LocalBusiness", "HVACBusiness"]` 併用に
  - `address`（北海道北見市）
  - `geo`（緯度経度: 43.8024, 143.8913）
  - `openingHoursSpecification`（毎日 09:00-19:00）
  - `priceRange`（$$）
  - `image`（ヒーロー画像）
- **about/index.html の LocalBusiness にも**:
  - `address` / `geo` / `openingHoursSpecification` を追加
- 効果: GBP（Googleビジネスプロフィール）連携・ローカルSEO向上

#### 4. その他保留中
- **ローカルブランチ `feature/200v-column`** の処置（中身要確認）
- `/monbetsu/` 内容確定後のFTP公開
- `/bihoro/` 内容確定後のFTP公開
- `/abashiri/works/003/` 駒場入れ替え事例の生成（works-case-builder スキル使用予定）

---

### 参考: kitami-001 施工情報（確定済み）

| 項目 | 内容 |
|---|---|
| 施工日 | 2025年7月 |
| 地域 | 北見市中央三輪 |
| 建物 | 戸建て（平屋） |
| 機種 | 三菱 霧ヶ峰 GV2825（10畳用） |
| 費用 | 209,220円（税込）※請求額を掲載 |
| 工期 | 1日（約5-8時間） |
| 担当者 | 宍戸 尚貴（第二種電気工事士） |
| 追加工事 | 屋根付き据置金具、室外化粧カバー、専用回路増設 |

**使用画像（info-template.txt 記載）**:
- before: before-00, before-02
- after: after-02, 05, 06, 08, 09, 11, 17, 20
- process: process-01, 02, 14, 19
- アンケート: kitami-chuomiwa-aircon-review-001.jpg

**画像ソース**: `assets/photos/_inbox/エアコン写真素材/北見市/kitami-001_中央三輪_梅津様/`
**画像出力先**: `htdocs/ac-kitami/images/works/kitami/001/`（既存IMG_*.jpgと共存）

### 注意事項・文脈
- **網走市ページとの改善点**: 費用表示追加、4軸タグ、width/height属性、担当者名・資格記載、アンケート画像追加
- **process-18.jpg vs process-19.jpg**: info-template には process-18 とあるが、_inbox フォルダには process-19.jpg が存在。要確認
- **002/003 の画像**: 分類未完了のため、`htdocs/ac-kitami/images/works/kitami/002/, 003/` の IMG_*.jpg から代表1枚を選定して使う
- **index.html の施工事例セクション**: 現在位置は行719-778
- **info-template.txt**: `assets/photos/_inbox/エアコン写真素材/北見市/kitami-001_中央三輪_梅津様/info-template.txt` に施工ポイントの詳細テキストあり（ストーリー化の元ネタ）
