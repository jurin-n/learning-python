## 初期設定(自分の環境用) 
. ~/development/virtualenv/venv27/bin/activate

## 初期設定(自分の環境用２) 
conda create -n selenium_py36 python=3.6
source activate selenium_py36

## selenium関連モジュールインストール 
pip install selenium

## ChromeDriver
https://sites.google.com/a/chromium.org/chromedriver/downloads

## Geckodriver
https://github.com/mozilla/geckodriver/releases

## 実行
### 初期設定(driverへのパスを通す)
export PATH=$PATH:~/development/selenium

### Chrome Driverで実行の場合
python sample.py Chrome

### Firefox Driverで実行の場合
python sample.py Firefox
