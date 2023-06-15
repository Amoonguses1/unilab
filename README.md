# unilab

# stftをするとき
以下の手順でdockerのコンテナ内に入る
```
make build
make run
make exec
```
dockerのイメージを作ったとき`apt-get`の動きがうまくないのでシェルファイルを実行して必要なパッケージをインストール
```
bash setup.sh
```
9行目`librosa.road()`の引数に音声ファイルの文字列を指定して実行する