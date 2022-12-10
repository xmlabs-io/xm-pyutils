BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
VENV=.venv/bin/activate

## make help  # prints the help message
.PHONY: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: clean
clean:
	rm -rf .venv && rm -rf tmp

.PHONY: venv
venv:
	python3 -m venv .venv && . ${VENV} && pip install -r dev-requirements.txt

.PHONY: tests
tests:
	. ${VENV} && dotenv -f .env run pytest -vv --cov=. --cov-report=term-missing tests/
