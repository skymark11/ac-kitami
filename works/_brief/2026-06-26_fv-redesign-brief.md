# ac-kitami FV 改善ブリーフ — ac-kitami セッション向け引き継ぎ書

| 項目 | 内容 |
|---|---|
| 起票元 | チーフデザイナー（_designer） |
| 起票日 | 2026-06-26 朝 |
| 完全版ブリーフ | `_designer/briefs/2026-06-26_ac-kitami-fv-redesign.md`（17 セクション・詳細はこちら） |
| バージョン | v0.9（参考サイト調査結果を v1.0 で反映予定） |
| 着手前提 | Phase 1+2 FTP アップ完了 + PageSpeed 再計測完了後 |
| 担当 | ac-kitami セッション + 現場サブエージェント `web-designer` |

---

## 1. このファイルの位置付け

- このファイルは **ac-kitami セッションで作業する人（または現場サブエージェント `web-designer`）が直接読む用** の引き継ぎ書
- 完全版ブリーフ（`_designer/briefs/2026-06-26_ac-kitami-fv-redesign.md`）の要約 + 実装に必要な具体指示
- **完全版の Section 番号への参照**を入れているので、判断に迷ったら必ず完全版を読むこと

---

## 2. 着手前のチェックリスト（必須）

以下すべてクリアしてから着手すること。

```
□ Phase 1+2 の FTP アップ完了（.htaccess + 16 HTML ファイル）
□ アップ後 PageSpeed Insights モバイル再計測 → スコア確認
□ seo-audit/baseline-2026-06-25.md に「改修後」セクション追記
□ 本ブリーフ v0.9 を Joe が承認
□ _researcher からの参考サイト調査結果が _designer/research/ に格納（または v1.0 待ち）
□ ベースライン記録（Section 9 参照）完了
□ Git タグ before-fv-redesign-2026-06-XX 作成 + push
```

---

## 3. 現状の問題点（7 不満点・要約）

詳細は完全版 Section 3。

1. ヘッダー下〜H2 までの巨大な余白（`py-16` 入れ子で 256px）
2. ヒーロー画像が霧化（`.hero-overlay` の白グラデ 95% が原因）
3. H2 改行破綻（`<span>` 区切りでの折り返し）
4. 画面上 60% が白〜薄グレー
5. 「設置工事のみ」白ボタンの低コントラスト
6. 浮いた「お電話」「LINE」ボタン（スマホで右カラム下回り込み）
7. 赤帯「LINE で簡単お見積もり」が装飾なしで浮いて見える

---

## 4. SEO 死守ライン（絶対変更禁止）

完全版 Section 4 を必ず確認。要点は以下。

| 触らない | 詳細 |
|---|---|
| `<title>` 文言 | 「北見市エアコン販売・設置取付工事 \| 地域密着のエアコン専門店」 |
| `<meta name="description">` 文言 | 既存のまま |
| `og:title` / `og:description` | 既存のまま |
| `<h1>` 文言 | 「エアコンラボ北見店」 |
| `<h2>` 文言 | 「北見市でエアコン取付なら地域密着の当店へ」（**CSS で改行位置制御は OK**） |
| canonical URL | `https://ac-kitami.com/` |
| 構造化データ JSON-LD | LocalBusiness / FAQPage / WebSite 3 種類 |
| 既存画像 URL パス | `images/hero-bg.webp` 等（**中身入替は OK・URL は固定**） |
| alt 属性内のキーワード | 「北見市」「エアコン取付」等 |

---

## 5. 自由に整えてよい領域

| 自由 | 例 |
|---|---|
| CSS 全般 | フォント・色・余白・シャドウ・トランジション・グラデーション |
| ヒーロー画像の中身 | 同 URL で別写真（スマホで主題が分かるもの） |
| ヘッダー装飾・赤帯デザイン | 色・パディング・アイコン追加 |
| CTA ボタン形状・色・サイズ・配置 | **文言の変更は要 A/B 検証** |
| 余白の取り方・改行制御 | `py-16` 入れ子解消 / `word-break` / `<span>` 区切り |

---

## 6. 顧客像コンテキスト（必読）

詳細は完全版 Section 7。

| 観点 | 内容 |
|---|---|
| 年齢層 | 40〜60 代・戸建て持ち・ある程度の経済力 |
| 最終決定者 | **奥さん** |
| 連絡好み | LINE > 電話 |
| 紹介・指名 | ほぼゼロ（**初見「初めまして」がほとんど**） |
| 決め手 | **信頼感 + 人柄** |
| 顔出し | **顔 NG。手元・背中・養生写真は OK** |

### デザインへの示唆

- 「**奥さん刺さり**」がキーワード（養生・清潔・誠実・家庭への配慮）
- **派手・男性的なプロ感は不要**
- 「**こんな人がやります**」訴求が「最安!」訴求より効く

---

## 7. 3 パターン提案 — 事前見立て

詳細は完全版 Section 8。

| パターン | マッチ度 | 推奨 |
|---|---|---|
| A: モダン・洗練系 | ★★★★☆ | サブ案・40〜60 代に「安っぽくない品格」 |
| **B: 信頼・安心系** | **★★★★★ 本命** | Joe の決め手「信頼 + 人物」と完全一致 |
| C: インパクト系 | ★☆☆☆☆ | 非推奨・信頼勝負と逆行 |

**推奨方向: B を主軸に、A の品格要素を取り込む中道案**。

---

## 8. 現場サブエージェント `web-designer` 召喚

### 8-1. 召喚タイミング

Section 2 のチェックリスト完了後、以下のコマンドで召喚。

### 8-2. 召喚プロンプト例

ac-kitami セッション内で以下を入力。

```
@.claude/agents/05.5_web-designer.md を読んで、ac-kitami の FV 改善 3 パターン提案を作成してください。

【必読ブリーフ】
- 完全版ブリーフ: _designer/briefs/2026-06-26_ac-kitami-fv-redesign.md
- 本引き継ぎ書: works/_brief/2026-06-26_fv-redesign-brief.md

【出力先】
- 3 パターン提案: works/_brief/2026-06-26_fv-redesign-3patterns.md
- ユーザー選定後のパッチ案: works/_brief/2026-06-26_fv-redesign-patch.md

【SEO 死守ライン】
- 本引き継ぎ書 Section 4 を必ず厳守
- 文言系（title / description / H1 / H2 / alt / og:* / 構造化データ）は触らない
- CSS / 装飾 / 画像中身 / 改行制御は自由

【3 パターンに含めるもの】
- コンセプト・Awwwards 4軸予測（合計32点以上）
- カラースキーム（既存ベース推奨・本命 B は青継続+緑+オレンジ）
- タイポグラフィ
- FV 構造図（テキスト or ASCII）
- 想定 CSS 抜粋（変更箇所のみ）
- 想定 Search Console 影響（順位への影響なし / 軽微 / 要検証 の判定）

【期待タイミング】
- 急ぎではない（Phase 1+2 完了後でOK）
- 3 パターン提示 → ユーザー選定 → 選定案の HTML/CSS パッチ案作成

【絶対NG】
- 顔出し写真の追加（Joe 明示）
- 「最安!」「激安!」等の価格訴求
- 派手すぎる配色・男性的すぎるプロ感
```

### 8-3. 召喚後の流れ

```
1. web-designer が 3 パターン提案書を出力（works/_brief/2026-06-26_fv-redesign-3patterns.md）
2. ユーザー（Joe）に提示して 1 パターン選定（または折衷指示）
3. web-designer が選定案の HTML/CSS パッチを作成（works/_brief/2026-06-26_fv-redesign-patch.md）
4. パッチ案レビュー → 承認 → 適用 → ローカル動作確認
5. ベースライン記録最終確認 → FTP アップ → モニタリング開始
```

---

## 9. ベースライン記録（着手前必須）

詳細は完全版 Section 9。

### 9-1. 取得項目

| 項目 | デバイス・期間 |
|---|---|
| Search Console「北見市エアコン取付」順位 / CTR / 表示回数 | 直近 30 日 |
| Search Console「北見市エアコン」順位 / CTR / 表示回数 | 直近 30 日 |
| PageSpeed Insights Performance / LCP / INP / CLS | モバイル + PC |
| 実機スクショ（iPhone / Android / PC）| スクロールなし FV |

### 9-2. 出力先

- 数値類: `seo-audit/baseline-2026-06-XX-fv-redesign.md`
- スクショ: `seo-audit/screenshots-2026-06-XX/`

### 9-3. Git タグ

```bash
git tag before-fv-redesign-2026-06-XX
git push origin before-fv-redesign-2026-06-XX
```

---

## 10. 採用後モニタリング

詳細は完全版 Section 10。4 週間継続。

| 指標 | 許容 |
|---|---|
| 「北見市エアコン取付」順位 | 1〜2 位維持 |
| 「北見市エアコン」順位 | 上位維持 |
| トップページ流入数 | 直近 30 日比 -10% 以内 |
| LCP | 2.5 秒以下 |
| INP | 200ms 以下 |
| CLS | 0.05 以下 |
| LINE 問い合わせ件数 | デプロイ前 30 日平均 比 +10% 目標 |

### 撤退基準

- 主要 KW が 3 位以下に転落
- 流入が直近 30 日比 -20% 超
- LCP が 3.0 秒超

→ いずれかで**即ロールバック検討**。

---

## 11. ロールバック手順

詳細は完全版 Section 11。

### Git タグから

```bash
cd e:/Dropbox/apps/remotely-save/htdocs/ac-kitami
git checkout before-fv-redesign-2026-06-XX -- index.html css/styles.css
git commit -m "rollback: FV redesign reverted"
git push origin main
```

### FTP 再アップ

1. ローカル確認
2. FTP で該当ファイル上書きアップ
3. PageSpeed で LCP が元水準に戻ったか確認
4. Search Console URL 検査 → インデックス登録リクエスト
5. サイトマップ再送信

---

## 12. 完了報告

| 段階 | 通知先 |
|---|---|
| `web-designer` 召喚 → 3 パターン提案完了 | Joe へ提示・選定を仰ぐ |
| 選定案のパッチ作成完了 | Joe へレビュー依頼 |
| FTP デプロイ完了 | `_secretary/INBOX.md` + `_designer/INBOX.md` |
| 4 週間モニタリング途中経過 | 週次で `_secretary/INBOX.md` に報告 |

---

## 13. 注意事項

- **判断に迷ったら現状維持**（SEO 死守最優先）
- **CSS 追加で LCP 悪化チェック必須**
- **顔出しを誤って入れない**
- **モバイル実機確認必須**（iPhone + Android）
- **prefers-reduced-motion 対応必須**（WCAG 2.2 AA）
- **完全版ブリーフを必ず参照**

---

## 14. 参考リンク

| 種別 | パス |
|---|---|
| 完全版ブリーフ | `_designer/briefs/2026-06-26_ac-kitami-fv-redesign.md` |
| 現場サブエージェント定義 | `.claude/agents/05.5_web-designer.md` |
| 親デザインルール | `.claude/rules/design.md` |
| 親コーディング規約 | `.claude/rules/coding.md` |
| Design-Knowledge-Base | `.claude/agents/knowledge/Design-Knowledge-Base.md` |
| ac-kitami NOW.md | `htdocs/ac-kitami/NOW.md` |
| 旧 FV 経緯 LOG | `htdocs/ac-kitami/LOG/2026-06-and-earlier.md`（L132-183） |
