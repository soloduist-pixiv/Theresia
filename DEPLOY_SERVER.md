# 服务器上线说明

## 1. 服务器准备

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo systemctl enable docker
sudo systemctl start docker
```

## 2. 上传项目

```bash
scp -r MyProject user@your-server:/opt/
ssh user@your-server
cd /opt/MyProject
```

## 3. 配置生产环境变量

```bash
cp .env.prod.example .env.prod
```

修改 `.env.prod`：
- `POSTGRES_PASSWORD` 改为强密码
- `OPENAI_API_KEY` 填入真实值
- 其他值按需调整

## 4. 启动生产服务

```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml up -d --build
```

访问：
- `http://服务器IP`

## 5. 初始化数据库与索引

执行 PostgreSQL 建表：

```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml exec -T postgres psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" < sql/postgres_users.sql
```

先拷贝索引 JSON 到容器：

```bash
docker cp sql/elasticsearch_articles.json myproject_elasticsearch:/tmp/elasticsearch_articles.json
```

执行 Elasticsearch 索引创建：

```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml exec -T elasticsearch \
  curl -X PUT "http://localhost:9200/articles" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/elasticsearch_articles.json
```

## 6. 常用运维命令

查看服务状态：

```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml ps
```

查看日志：

```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml logs -f backend
docker compose --env-file .env.prod -f docker-compose.prod.yml logs -f frontend
```

重启：

```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml restart
```

停止：

```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml down
```
