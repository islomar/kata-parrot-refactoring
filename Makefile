.DEFAULT_GOAL := help

help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup: ## Set up the local environment (e.g. install git hooks)
	scripts/local-setup.sh

.PHONY: add-package
add-package: ## Add package to the project: 'make add-package package=<package-name>'
	docker compose run --rm --no-deps kata-parrot-refactoring poetry add $(package)
	make build

.PHONY: add-dev-package
add-dev-package: ## Add dev package to the project: 'make add-dev-package package=<package-name>'
	docker compose run --rm --no-deps kata-parrot-refactoring poetry add $(package) -G dev
	make build

.PHONY: build
build: ## Builds the Docker image
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker compose build

.PHONY: build-with-updated-packages
build-with-updated-packages: ## Rebuild the docker image with updated python packages
	rm -f poetry.lock
	docker compose run --rm --no-deps kata-parrot-refactoring poetry update
	make build

.PHONY: update-python-packages
update-python-packages: ## Updates the Python packages
	docker compose run --rm --no-deps kata-parrot-refactoring poetry update

.PHONY: check-dockerfile
check-dockerfile: ## Validate the Dockerfile
	docker run --rm -i hadolint/hadolint:latest-alpine < Dockerfile

.PHONY: check-style
check-style:  ## Check style (using flake8)
	docker compose run --rm --no-deps kata-parrot-refactoring poetry run flake8 .

.PHONY: check-typing
check-typing:  ## Check types (using mypy)
	docker compose run --rm --no-deps kata-parrot-refactoring poetry run mypy .

.PHONY: check-format
check-format: ## Check the format (using black)
	docker compose run --rm --no-deps kata-parrot-refactoring poetry run black --check .

.PHONY: fix-format
fix-format:  ## Format Python code
	docker compose run --rm --no-deps kata-parrot-refactoring poetry run black .

.PHONY: test
test: ## Run all the tests
	docker compose run --rm --no-deps kata-parrot-refactoring poetry run pytest -n auto tests -ra

.PHONY: test-coverage
test-coverage: ## Generate an HTML test coverage report after running all the tests
	docker compose run --rm kata-parrot-refactoring poetry run coverage run --branch -m pytest tests
	docker compose run --rm kata-parrot-refactoring poetry run coverage html
	@echo "You can find the generated coverage report here: ${PWD}/htmlcov/index.html"

.PHONY: test-run-mutation
test-run-mutation: ## Run mutation testing
	docker compose run --rm kata-parrot-refactoring poetry run mutmut run --rerun-all --no-progress --CI

.PHONY: test-show-mutants
test-show-mutants-results: ## Show mutants found (it requires having run 'make test-run-mutation')
	docker compose run --rm kata-parrot-refactoring poetry run mutmut results

.PHONY: test-generate-mutation-html-report
test-generate-mutation-html-report: ## Generate HTML mutation report
	docker compose run --rm kata-parrot-refactoring poetry run mutmut html
	@echo "The HTML report can be accessed here: http://localhost:63342/kata-parrot-refactoring/html/index.html"

.PHONY: test-generate-mutation-junit-report
test-generate-mutation-junit-report: ## Generate JUnit XML mutation report
	docker compose run --rm kata-parrot-refactoring poetry run mutmut junitxml --suspicious-policy=ignore --untested-policy=ignore

.PHONY: pre-commit
pre-commit: check-format check-typing check-style test

.PHONY: shell
shell: ## Get into the Docker container
	docker compose run --rm python-kata-name sh

.PHONY: rename-project
rename-project: ## Rename project: 'make rename new-name=<new-name>'
	sed -i 's/kata-parrot-refactoring/$(new-name)/' docker-compose.yaml
	sed -i 's/kata-parrot-refactoring/$(new-name)/' Makefile
	sed -i 's/kata-parrot-refactoring/$(new-name)/' pyproject.toml
	sed -i 's/python-kata-template/$(new-name)/' README.md
	sed -i 's/python-kata-template/$(new-name)/' Makefile
