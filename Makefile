build:
	docker-compose build

run:
	docker-compose up

clean:
	docker-compose down --remove-orphans --volumes

shell:
	docker-compose exec consumer bash


.PHONY: run clean shell
