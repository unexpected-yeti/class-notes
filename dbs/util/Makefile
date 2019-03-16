.PHONY: pull
pull:
	docker pull postgres

.PHONY: run
run: pull
	docker run -v `pwd`/sql:/sql --name dbs-postgres -e POSTGRES_PASSWORD=dbs4life -d postgres 

.PHONY: stop
stop:
	docker rm -fv dbs-postgres

.PHONY: logs
logs:
	docker logs dbs-postgres

.PHONY: bash
bash:
	docker exec -it dbs-postgres bash
