## 初期セットアップ
### python3へアップデート
brew install pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT
eval "$(pyenv init -)"

pyenv install --list
pyenv install 3.5.2
pyenv versions

pyenv global 3.5.2
pyenv rehash

python --version

