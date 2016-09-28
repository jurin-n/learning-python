## ビルド
docker build -t sample:1.0 .

##実行(ポストOSの任意のポートをコンテナに割り当てるケース)
docker run -d -P sample:1.0 python sample.py

##実行(ポストOSの指定ポートをコンテナの指定ポートに割り当てるケース)
docker run -d -p 80:5000 sample:1.0 python sample.py