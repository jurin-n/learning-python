# 概要
* Effective Python 項番3ためしました。
* Python2ではstrは8ビットの文字列を含み、unicodeはUnicode文字列を含む。このしようはPython3と異なる。

# virtualenv有効化
. ~/development/virtualenv/venv27/bin/activate

# カバレッジ計測ツール
### インストール
pip install coverage
### カバレッジ計測
coverage run sample_test.py
### HTMLレポート
coverage html

### テストメソッドの命名について
doingSomeOperationGeneratesSomeResult
(なんらかの処理を行うとなんらかの結果が発生する)

someResultOccursUnderSomeCondition
(なんらかの条件下ではなんらかの結果が発生する)