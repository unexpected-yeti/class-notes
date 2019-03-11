.PHONY: pull
pull:
	docker pull postgres

.PHONY: run
run: pull
	docker run --name dbs-postgres -e POSTGRES_PASSWORD=dbs4life -d postgres

.PHONY: repl
repl:
	docker run -it --rm --link dbs-postgres:postgres postgres psql -h postgres -U postgres

