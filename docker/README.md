# Docker関連
## ビルド
docker build -t sample:1.0 .

##実行(ポストOSの任意のポートをコンテナに割り当てるケース)
docker run -d -P sample:1.0 python sample.py<br/>
  *CMDで指定してるコマンドを 上記のように python sample.py でパラメータとしてで指定するとDockerfile設定内容を上書きできる

##実行(ポストOSの指定ポートをコンテナの指定ポートに割り当てるケース)
docker run -d -p 80:5000 sample:1.0 python sample.py<br/>
  *CMDで指定してるコマンドを 上記のように python sample.py でパラメータとしてで指定するとDockerfile設定内容を上書きできる

## プロセス確認（CONTAINER IDもこれで確認）
docker ps

## コンテナ起動
docker start [CONTAINER ID]

## コンテナ停止
docker stop [CONTAINER ID]

## コンテナのログ出力
docker logs [CONTAINER ID]


# 参考資料
Docker Fundamentals Python Sample WebApp https://github.com/docker-training/webapp<br/>
Run a simple application https://docs.docker.com/engine/tutorials/usingdocker/