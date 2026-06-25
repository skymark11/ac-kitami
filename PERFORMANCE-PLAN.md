# PERFORMANCE-PLAN.md — ac-kitami.com パフォーマンス改善計画

作成日: 2026-06-25 夜
発端: works/004 PageSpeed Insights モバイル 57 点・LCP 9.4 秒判明
作業対象: 全 works/* + トップ + 共通レイアウト + .htaccess
最終目標: モバイル LCP 2.5 秒以下、Performance 80 点以上

---

## 🎯 ゴール

| 指標 | 現状（works/004 モバイル） | 目標 |
|---|---|---|
| Performance | 57 | 80+ |
| LCP | 9.4 秒 | 2.5 秒以下 |
| FCP | 8.4 秒 | 1.8 秒以下 |
| TBT | 0 ms | 0 ms 維持 |
| CLS | 0 | 0 維持 |
| ユーザー補助 | 89 | 95+ |
| SEO スコア | 100 | 100 維持 |

**絶対条件**: 「北見市エアコン取付」「北見市エアコン」検索順位 1〜2 位を維持。下落兆候があれば即ロールバック。

---

## 📊 現状調査結果

### .htaccess（重大欠落）

現在 11 行しか書かれていない。infrastructure.md ルールに記載されている以下が**全て欠落**:

- ❌ Gzip 圧縮（mod_deflate）
- ❌ ブラウザキャッシュ（mod_expires）
- ❌ セキュリティヘッダー（Options -Indexes 含む）
- ❌ ETag 無効化
- ❌ KeepAlive

PageSpeed の「効率的なキャッシュ保存期間を使用する 16 KiB」が該当。
現在の本番キャッシュ Expires は 1 週間（Apache デフォルト）。infrastructure.md ルールでは画像/CSS/JS は 1 年。

### CSS ファイル

| ファイル | サイズ | 状態 |
|---|---|---|
| `css/icons.css` | **52 KB** | 🔴 Remix Icon 全アイコン読込（使用していない CSS 89 KiB の主因） |
| `css/tailwind.css` | 21 KB | 🟡 ローカル化済み（purge 状況未確認） |
| `css/styles.css` | 5 KB | 🟢 適正 |

### Google Fonts 読込

| ページ | 状態 |
|---|---|
| `index.html`（トップ） | 🟢 `media="print" + onload` で非同期化済み |
| `about/index.html` | 未確認 |
| `works/001/`〜`004/` | 🔴 同期読込（works/004 で確認・他も同様の可能性大） |

### FV 画像（works/004）

| 画像 | JPG | WebP | 状態 |
|---|---|---|---|
| `before-01` | 120 KB | 77 KB | 🔴 JPG のみ参照（`<picture>` タグ未使用） |
| `after-01` | 99 KB | 56 KB | 🔴 同上 |

WebP に切替で **約 86 KB 削減 / LCP 短縮**。`fetchpriority="high"` は既に付与済み。

### HTML サイズ

works/004 は 38 KB（gzip 後）。本体は適正サイズ。

### Tailwind の状況

`tailwind-input.css` 59 バイト（最小入力）から 21 KB の `tailwind.css` をビルド。`tailwind.config.js` の content 設定によっては purge 不十分の可能性。

---

## ⚠️ リスク・SEO 死守ルール

### 触ってはいけない（SEO 死守）

- `<title>` / `<meta name="description">` / `og:title` / `og:description`
- 構造化データ（JSON-LD 全種）
- `<h1>` / `<h2>` メインキャッチコピー
- canonical URL
- 既存画像 URL パス（OGP・CDN キャッシュ崩れ防止）
- 既存画像 alt 属性内の地域名・キーワード
- 内部リンク構造

### 自由に整えてよい

- CSS（フォント・色・余白・レスポンシブ）
- 画像の WebP 追加（同 URL の JPG は維持し `<picture>` の `<source>` として WebP 追加）
- フォント読込タイミング
- .htaccess のキャッシュ・圧縮設定
- icons.css の中身軽量化（見た目は維持）

### 慎重に変更

- Tailwind purge（クラス漏れで見た目崩れ可能性 → 全ページ目視確認必須）
- icons.css 削減（使用アイコンの洗い出し必須）

---

## 📋 Phase 0: ベースライン記録（必須・着手前）

改修前に以下を記録し、`seo-audit/baseline-2026-06-25.md` として保存:

### Search Console（直近 30 日）

- 「北見市エアコン取付」順位・CTR・表示回数
- 「北見市エアコン」順位・CTR・表示回数
- 「北見 エアコン 工事」順位・CTR・表示回数
- 「網走市 エアコン」など主要 KW 全数
- works/001〜004 個別の表示回数・クエリ

### PageSpeed Insights（全主要ページ・モバイル & PC）

- `https://ac-kitami.com/`
- `https://ac-kitami.com/works/`
- `https://ac-kitami.com/works/001/` 〜 `004/`
- `https://ac-kitami.com/about/`
- `https://ac-kitami.com/abashiri/works/001/` `002/`

各ページについて Performance / LCP / FCP / TBT / CLS / Speed Index を記録。

### Git タグ

```bash
git tag before-perf-2026-06-25
git push origin before-perf-2026-06-25
```

ロールバック用ポイント確保。

---

## 🛠️ Phase 1: .htaccess 強化（リスク極小・効果大）

infrastructure.md ルールに従い不足項目を追加。

**実装内容**:
- `Options -Indexes`（ディレクトリリスティング無効化）
- `<Files ~ "^\.ht">` で .htaccess アクセス拒否
- 隠しファイル全般のアクセス拒否
- `mod_deflate` で text/html, text/css, application/javascript の Gzip 圧縮
- `mod_expires` でキャッシュ設定
  - HTML: 1 日 (no-cache, must-revalidate)
  - CSS/JS/画像/フォント: 1 年
  - PDF: 1 ヶ月
- `Header unset ETag` + `FileETag None`（ETag 無効化）
- `Header set Connection keep-alive`

**期待効果**:
- 「効率的なキャッシュ保存期間」インサイトの解消（16 KiB 削減）
- 2 回目以降のページ訪問が大幅高速化（再訪 LCP は 1-2 秒帯に）
- Gzip でテキスト系リソースが 60-70% 圧縮

**SEO リスク**: ゼロ（インフラ層のみの変更）

**検証**: 本番 .htaccess アップ後、`curl -I` で Cache-Control / Expires ヘッダー確認、PageSpeed 再測定

---

## 🛠️ Phase 2: works/* の Google Fonts 非同期化（リスク小・効果中）

トップ `index.html` で既に実装済みの方式を `works/001/`〜`004/`・`works/index.html` に展開。

**差し替え内容**:

```html
<!-- 改修前 -->
<link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">

<!-- 改修後 -->
<link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet"></noscript>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet"></noscript>
```

トップに既にある「Font fallback to reduce CLS」の `@font-face` ブロックも、可能なら共通 CSS 化して works/* にも適用（CLS が 0 を維持できる前提のみ）。

**期待効果**: レンダーブロック解消の一部・LCP 1-2 秒短縮

**SEO リスク**: ゼロ（見た目は変わらず、表示順序のみ変化）

**検証**: 表示崩れがないか目視確認（フォント読込前後の FOIT/FOUT）

---

## 🛠️ Phase 3: FV 画像 WebP 化（リスク小・効果中）

works/001〜004 の FV B/A 画像を `<picture>` タグでフォールバック化。WebP は既にローカルに存在するため作業はマークアップのみ。

**差し替え内容**:

```html
<!-- 改修前 -->
<img src="../../images/works/kunneppu/001/before-01.jpg" alt="..." width="800" height="600" fetchpriority="high">

<!-- 改修後 -->
<picture>
  <source srcset="../../images/works/kunneppu/001/before-01.webp" type="image/webp">
  <img src="../../images/works/kunneppu/001/before-01.jpg" alt="..." width="800" height="600" fetchpriority="high">
</picture>
```

works/001〜003 についても同様に FV B/A 画像を確認・WebP 化。

**期待効果**: FV 画像配信 86 KB 削減 / LCP 1-1.5 秒短縮

**SEO リスク**: ゼロ（既存 JPG URL は維持・alt 属性も変えない）

**検証**: `<picture>` タグでブラウザが WebP を選択することを DevTools Network タブで確認

---

## 🛠️ Phase 4: icons.css 軽量化（リスク中・効果大）

現在 52 KB の `icons.css` から、実際に使用しているアイコンクラスのみを抽出。

**手順**:

1. 全 HTML から `class="ri-..."` `class="...ri-..."` の使用一覧を抽出（PowerShell or grep）
2. `icons.css` から該当クラス + 必須の `@font-face` のみ抽出した軽量版 `icons.min.css` を生成
3. 旧 `icons.css` は残し、各ページの参照を `icons.min.css` に切替
4. 全ページ目視で表示崩れ確認

**期待効果**: CSS 30-40 KB 削減（推定 80% カット）/ レンダーブロック大幅短縮

**SEO リスク**: ゼロ（HTML マークアップ・URL・JSON-LD は変更なし）。表示リスクは中程度（漏れがあるとアイコンが表示されない）。

**検証**: トップ・全 works/*・about を目視確認

---

## 🛠️ Phase 5: Tailwind purge 強化（リスク中・効果中）

`tailwind.config.js` の content 設定を確認し、全 HTML ファイルをスキャンするように設定。再ビルドで未使用クラスを除去。

**期待効果**: tailwind.css 21 KB → 5-10 KB に削減 / レンダーブロック短縮

**SEO リスク**: ゼロ。表示リスクは中（動的に生成されるクラスがあれば safelist 必要）。

**検証**: 全ページ目視確認 + PageSpeed 再測定

---

## 🛠️ Phase 6: 検証 + ベースラインと比較

全 Phase 完了後:

1. PageSpeed Insights で全ページ再測定 → Phase 0 ベースラインと比較
2. 1-2 週間 Search Console で順位モニタリング
3. 順位下落兆候があれば `git tag before-perf-2026-06-25` で即ロールバック
4. 問題なければ `PERFORMANCE-PLAN.md` を `seo-audit/perf-improvement-report-2026-XX-XX.md` として成果記録

---

## 📅 推奨実施スケジュール

| Phase | 所要 | 推奨タイミング |
|---|---|---|
| 0 ベースライン | 30 分 | 改修前必須 |
| 1 .htaccess | 30 分 | 単独セッション・即時検証可能 |
| 2 Font 非同期 | 30 分 | Phase 1 と同セッション可 |
| 3 FV 画像 WebP | 30 分 | Phase 2 と同セッション可 |
| 4 icons.css 軽量化 | 1-2 時間 | 単独セッション・全ページ目視必須 |
| 5 Tailwind purge | 1 時間 | Phase 4 同セッション可 |
| 6 検証・モニタリング | 1-2 週間 | 全 Phase 完了後 |

**実施推奨順序**:
1. Phase 0（ベースライン）
2. Phase 1 + 2 + 3（リスク極小・最大効果・1 セッションで完結可）
3. ここで一旦 PageSpeed 再測定 → 改善幅を確認
4. Phase 4 + 5（リスク中・効果次第で実施判断）
5. Phase 6（モニタリング）

Phase 1-3 だけで LCP 9.4 → 4-5 秒帯まで改善見込み。Phase 4-5 でさらに 2-3 秒帯を狙う。

---

## 🚨 ロールバック手順

順位下落・表示崩れを検知した場合:

```bash
git reset --hard before-perf-2026-06-25
git push -f origin main  # ※force push は要承認
```

FTP 側も、改修前にバックアップ取得しておく（FFFTP の「ローカル↔ホスト」同期で全体ダウンロード推奨）。

---

## 📌 注意事項

- 各 Phase ごとに commit を分けて、戻しやすい状態を維持
- FTP アップ前にローカルで `npm run dev` で必ず動作確認
- works/001〜004 + about + index + abashiri の全ページ目視確認
- Search Console での KW モニタリングは最低 1 週間続ける
- 「触ってはいけない」リストの項目は絶対に変更しない
