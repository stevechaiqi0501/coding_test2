# TODOアプリ (FastAPI + SQLite)

このアプリケーションは、TODOのCRUD操作を提供するWeb APIサーバーです。OpenAPIの仕様に従って実装されています。

## 1. 事前準備
- Docker, Docker Compose などをインストールしておいてください。
- Docker は事前にアクティブにしておくことをおすすめします。

## 2. ビルドと起動方法

### 2.1 イメージのビルド
```bash
coding_test/prob2/todoapp　より
docker build -t todo_app:latest .

### 2.2 コンテナの起動
docker run -p 8080:8080 todoapp

## 3. API仕様
2.2までの処理を終わらせたあと、別のターミナルで3.1以降を入力してください

### 3.1 POST（Create Task）
リクエスト例：
```bash
curl -X 'POST' \
  'http://localhost:8080/api/v1/tasks' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "example_title",
  "description": "example_description"
}'
```
成功時のレスポンス例（ステータスコード: 201）:
```json
{
  "id": 1,
  "title": "example_title",
  "description": "example_description",
  "isDone": false
}
```

失敗時のレスポンス例（ステータスコード: 400）:
```json
{
  "detail": "Title is required."
}
```

### 3.2 GET（Read All Tasks）
リクエスト例：
```bash
curl -X 'GET' \
  'http://localhost:8080/api/v1/tasks' \
  -H 'accept: application/json'
```

(id別に取得したい場合、tasks/{id}を挿入)
成功時のレスポンス例（ステータスコード: 200）:
```json
[
  {
    "id": 1,
    "title": "example_title",
    "description": "example_description",
    "isDone": false
  }
]
```

### 3.3 PUT（Update Task）
リクエスト例：
```bash
curl -X 'PUT' \
  'http://localhost:8080/api/v1/tasks/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "updated_example",
  "description": "updated_example",
  "isDone": true
}'
```
成功時のレスポンス例（ステータスコード: 200）:
```json
{
  "id": 1,
  "title": "updated_example",
  "description": "updated_example",
  "isDone": true
}
```

### 3.4 DELETE（Delete Task）
リクエスト例：
```bash
curl -X 'DELETE' \
  'http://localhost:8080/api/v1/tasks/1' \
  -H 'accept: */*'
```
成功時のレスポンス例（ステータスコード: 204）:

（レスポンスボディなし）

## 4. デバッグ方法

- **ポート競合:** 他のプロセスが8080ポートを使用している場合は、`docker run -p 8081:8080`のようにポート番号を変更してください。
