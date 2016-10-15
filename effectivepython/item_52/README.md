## 参考
https://github.com/bslatkin/effectivepython/tree/master/example_code/item_52

## 各ディレクトリ内部のコードについて
* recursive_import_bad -> 実行時エラーになるだめな例。
* recursive_import_ordering -> 実行時にエラーにならないが、モジュールのインポートがファイルの先頭でおこなわれてないため扱いにくいコードになる。PEP8スタイルにも違反。
* recursive_import_nosideeffects -> 多くの状況でうまく働き、依存注入(Dependency Injection)のようなパターンを可能にする。しかし、コードが読みにくくなる場合がある。

## 個人的な見解
新規開発なら、recursive_import_nosideeffects で対応。既存コードの修正の場合は、別の方法で。
