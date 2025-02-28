FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# 設定ファイルやトレース用の環境変数を設定するためのエントリポイントを設定
CMD ["tail", "-f", "/dev/null"]
