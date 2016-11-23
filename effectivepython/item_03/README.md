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