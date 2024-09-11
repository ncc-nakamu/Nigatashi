# 使用するベースイメージを指定
FROM python:3.11

# 必要なパッケージをインストール
RUN apt-get update && \
    apt-get install -y mecab libmecab-dev mecab-ipadic-utf8

# Pythonパッケージのインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# アプリケーションのコピー
COPY . /app
WORKDIR /app

# アプリケーションを実行
CMD ["python", "app.py"]
