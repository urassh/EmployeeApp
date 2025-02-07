### ☑ 最新コードの取得
このリポジトリの`main`ブランチにはアプリの完成版が含まれています。以下のコマンドで最新の完成コードを取得できます:

```bash
git clone https://github.com/urassh/docker-flask-app/
```

---

## プロジェクト構成

- **フロントエンド:** CSS
- **バックエンド:** Flask (Python)
- **データベース:** PostgreSQL
- **環境構築:** Docker

---

### ⚠ 前提条件
- 事前に[Docker Desktop](https://www.docker.com/ja-jp/products/docker-desktop/)をインストールしておいてく。

---

## 起動方法
- このプロジェクトではDockerを使用しているので、`docker`コマンドを使います。

### 起動
```bash
docker compose up
```

### 更新ビルド
```bash
docker compose up --build -d
```

### コンテナ削除(作業終了したら...)
```bash
docker compose down --rmi all
```

---

## 講座ステップ

### Step 1: 簡単なAPIを作ってみよう!!
- **コードダウンロード:** [Step 1 コード](https://github.com/urassh/docker-flask-app/releases/tag/tx-v1.0)
- **Git操作に慣れている方:**
  ```bash
  git fetch origin tx-v1
  git checkout tx-v1
  ```

---

### Step 2: 画面を作ってみよう!!
- **コードダウンロード:** [Step 2 コード](https://github.com/urassh/docker-flask-app/releases/tag/tx-v2.0)
- **Git操作に慣れている方:**
  ```bash
  git fetch origin tx-v2
  git checkout tx-v2
  ```

---

### Step 3: データベースと繋げよう！ [データ取得編]
- **コードダウンロード:** [Step 3 コード](https://github.com/urassh/docker-flask-app/releases/tag/tx-v3.0)
- **Git操作に慣れている方:**
  ```bash
  git fetch origin tx-v3
  git checkout tx-v3
  ```

#### 📌 `.env`ファイルを作成しよう

**配置場所:**
```
.
├── .env
├── app/
├── db/
├── .gitignore
├── Dockerfile
├── README.md
└── compose.yml
```

**内容:**
```dotenv
# COMMON
API_PORT=3000
DB_PORT=5432

# PostgreSQL Settings
POSTGRES_USER=guest
POSTGRES_PASSWORD=password
POSTGRES_DB=guest
POSTGRES_HOST=db
```

---

### Step 4: データベースと繋げよう！ [データ追加編]
- **コードダウンロード:** [Step 4 コード](https://github.com/urassh/docker-flask-app/releases/tag/tx-v4.0)
- **Git操作に慣れている方:**
  ```bash
  git fetch origin tx-v4
  git checkout tx-v4
  ```

#### 📌 `.env`ファイルを作成しよう

**配置場所:**
```
.
├── .env
├── app/
├── db/
├── .gitignore
├── Dockerfile
├── README.md
└── compose.yml
```

**内容:**
```dotenv
# COMMON
API_PORT=3000
DB_PORT=5432

# PostgreSQL Settings
POSTGRES_USER=guest
POSTGRES_PASSWORD=password
POSTGRES_DB=guest
POSTGRES_HOST=db
```

---

### Step 5: データベースと繋げよう！ [データ削除編]
- **コードダウンロード:** [Step 5 コード](https://github.com/urassh/docker-flask-app/releases/tag/tx-v5.0)
- **Git操作に慣れている方:**
  ```bash
  git fetch origin tx-v5
  git checkout tx-v5
  ```

#### 📌 `.env`ファイルを作成しよう

**配置場所:**
```
.
├── .env
├── app/
├── db/
├── .gitignore
├── Dockerfile
├── README.md
└── compose.yml
```

**内容:**
```dotenv
# COMMON
API_PORT=3000
DB_PORT=5432

# PostgreSQL Settings
POSTGRES_USER=guest
POSTGRES_PASSWORD=password
POSTGRES_DB=guest
POSTGRES_HOST=db
```

