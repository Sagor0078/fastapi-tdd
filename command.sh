sudo docker-compose exec web-db psql -U postgres -d web_dev -c "\dt"

http --json POST http://localhost:8004/summaries/ url=http://testdriven.io