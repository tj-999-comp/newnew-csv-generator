# NEWnew CSV Generator

暗記カードアプリ「NEWnew - お手軽暗記アプリ」で利用する学習デッキを、CSV形式で作成・管理するためのリポジトリです。

スマートフォンで素早く反復学習できるように、1カード1知識の短い一問一答と、理解を補う解説を組み合わせています。

## 収録デッキ

現在は、AWS Certified Cloud Practitioner（CLF-C02）対策デッキを収録しています。

| デッキ | 内容 | 問題数 |
| --- | --- | ---: |
| `clf_c02_deck1_cloud_concepts.csv` | クラウドの概念 | 25 |
| `clf_c02_deck2_shared_responsibility_iam_governance.csv` | 責任共有モデル・IAM・ガバナンス | 25 |
| `clf_c02_deck3_security_audit_compliance.csv` | セキュリティ・監査・コンプライアンス | 25 |
| `clf_c02_deck4_compute_storage.csv` | コンピューティング・ストレージ | 25 |
| `clf_c02_deck5_database_network.csv` | データベース・ネットワーク | 20 |
| `clf_c02_deck6_analytics_integration_ai_operations.csv` | 分析・統合・AI・運用 | 20 |
| `clf_c02_deck7_billing_pricing_support.csv` | 請求・料金・サポート | 20 |

合計160問です。各CSVは [`decks/`](decks/) にあります。

## CSV仕様

NEWnew向けデッキは、次の3列で構成します。

```csv
"問題","解答","解説"
"HTTPステータスコードでリソースが見つからないことを示す番号は？","404 (Not Found)","URLの誤りや対象ページが削除された場合などに返される。"
```

- 文字コード: UTF-8（BOMなし）
- 改行コード: LF
- ヘッダー: `問題,解答,解説`
- フィールド数: 3列固定
- `問題`と`解答`: 必須
- `解説`: 任意
- すべてのフィールドをダブルクォートで囲む
- セル内には改行を含めず、1レコードを1行にする

詳しい作成ルールと品質基準は [`AGENTS.md`](AGENTS.md) を参照してください。

## ディレクトリ構成

```text
.
├── AGENTS.md
├── README.md
├── decks/
│   └── *.csv
└── scripts/
    ├── 20261127_generate_clf_c02_decks.py
    └── 20261127_validate_clf_c02_decks.py
```

## 使い方

### デッキを利用する

[`decks/`](decks/) から目的のCSVを選び、NEWnewへインポートしてください。

### 収録中のCLF-C02デッキを再生成する

Python 3が利用できる環境で、次のコマンドを実行します。外部パッケージは不要です。

```bash
python scripts/20261127_generate_clf_c02_decks.py
```

このスクリプトは、対象となる7つのCSVを上書きします。編集済みのCSVがある場合は、実行前に差分を確認してください。

### デッキを検証する

```bash
python scripts/20261127_validate_clf_c02_decks.py
```

検証スクリプトでは、次の項目を確認します。

- UTF-8（BOMなし）か
- 改行コードがLFか
- ヘッダーとカラム数が正しいか
- 問題と解答が空でないか
- セル内改行がないか
- 各デッキの問題数が想定どおりか

## 新しいデッキを追加する

1. テーマと対象レベルを決めます。
2. 1カード1知識を原則に、問題・解答・解説を作成します。
3. Pythonの標準`csv`モジュールなどを使い、`quoting=csv.QUOTE_ALL`で書き出します。
4. `decks/<テーマ名_英語またはローマ字>.csv`として保存します。
5. ヘッダー、3列構成、必須項目、文字コード、改行コードを検証します。

問題数の指定がない場合は、1デッキ20問程度が目安です。既存ファイルと同名になる場合は、上書き前に内容を確認するか、ファイル名に連番を付けてください。

## ライセンス

ライセンスは現在設定されていません。再配布や外部公開を行う場合は、事前にリポジトリ管理者へ確認してください。
