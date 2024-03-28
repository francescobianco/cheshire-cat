
build:
	@docker compose build cheshire-cat-core

start:
	@docker compose up -d --force-recreate
	@echo
	@echo "Talk with the cat: <http://localhost:1865/admin/>"

debug: build start
	@docker-compose logs -f cheshire-cat-core