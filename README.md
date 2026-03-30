# MyProject - 个人技术博客

## 后端

- 框架：FastAPI
- API：
  - `POST /login`
  - `POST /register`
  - `POST /chat`
  - `POST /article`
  - `GET /article`
  - `GET /article/{article_id}`

### 启动后端

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 数据库脚本

- PostgreSQL 用户表脚本：`sql/postgres_users.sql`
- Elasticsearch 文章索引脚本：`sql/elasticsearch_articles.http`
- Elasticsearch 索引 JSON：`sql/elasticsearch_articles.json`

## 前端

- 框架：Vue3 + Vite
- 页面：
  - `/login`
  - `/register`
  - `/main`
  - `/article/:id`
  - `/aichat`

### 启动前端

```bash
cd web
npm install
npm run dev
```

## 生产部署

- Docker 编排文件：`docker-compose.prod.yml`
- 后端镜像文件：`Dockerfile.backend`
- 前端镜像文件：`web/Dockerfile`
- Nginx 反向代理：`web/nginx.conf`
- 生产环境变量模板：`.env.prod.example`
- 上线手册：`DEPLOY_SERVER.md`
