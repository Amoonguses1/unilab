# unilab


# 環境構築
```
bash setup.sh
```
stftのみを行うならdockerのコンテナで完結するのて不要
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

# 音声認識をする
voice_get.pyを実行するだけでよい
```
python voice_to_text.py
```
wavファイルを経由してSpeechRecognitionに渡しているのでうまくいかない場合はplotdataのdtypeを変更し、音声が再生できる型に直すとよい。
その際変更が必要になるのは
13行目 `scipy.io.wavfile.write(filename, rate=44100, data=data.astype(np.int16))`
25行目 `if(val > 500):` 音声切り出しのための閾値設定
53行目 `ax.set_ylim([-1000, 1000])` 音声波形表示範囲
60行目 `dtype='int16',`