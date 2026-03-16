# ac-kitami.com サイト固有ルール

このファイルは **ac-kitami.com（エアコンラボ北見店）** 専用のルールです。
他サイトには適用しないでください。

---

## Google Analytics

**全ページの `<head>` 内に以下のコードを挿入すること（`<meta charset="UTF-8">` の直後）。**

```html
<!-- Google tag (gtag.js) - 本番環境のみ計測 -->
<script>
    if (location.hostname === 'ac-kitami.com') {
        var script = document.createElement('script');
        script.async = true;
        script.src = 'https://www.googletagmanager.com/gtag/js?id=G-0VXBBQV2PW';
        document.head.appendChild(script);

        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-0VXBBQV2PW');
    }
</script>
```

**注意事項:**
- 測定ID: `G-0VXBBQV2PW`（変更禁止）
- `location.hostname` チェックにより、ローカル開発環境では計測されない
- 新規ページ作成時に入れ忘れないこと（施工事例詳細ページ、エリアページ等も含む）

---

## サイト基本情報

| 項目 | 値 |
|------|-----|
| ドメイン | ac-kitami.com |
| 屋号 | エアコンラボ北見店 |
| 電話番号 | 070-4080-0965 |
| 対応エリア | 北見市、網走市、美幌町、訓子府町、置戸町 |
