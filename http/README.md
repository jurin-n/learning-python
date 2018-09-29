### python2と3の文字コードの扱いの違い
#### サンプル実行方法
```
python sample.py
```

### 自己証明書
#### サンプル実行方法
```
# ca.crtはsample2.pyでアクセスしているWebサイトの証明書を発行しているCA
export REQUESTS_CA_BUNDLE=/xxx/xxx/ca.crt 
python sample2.py
```
