.PHONY: help
help:
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:' Makefile | grep -v '^_' | cut -d: -f1 | xargs -n1 echo "  -"

.PHONY: setup
setup:
	poetry install
	poetry run pre-commit install

.PHONY: start
start:
	docker compose up --build -d

.PHONY: stop
stop:
	docker compose down

.PHONY: test
test:
	docker compose exec app poetry run pytest src/tests
