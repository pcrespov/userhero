
.PHONY: help
help: ## This nice help (thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html)
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

.venv: ## Creates a python virtual environment with dev tools (pip, pylint, ...)
	@python3 -m venv .venv
	@.venv/bin/pip3 install --upgrade pip wheel setuptools
	@echo "To activate the venv, execute 'source .venv/bin/activate' or '.venv/bin/activate.bat' (WIN)"

.PHONY: clean
clean:  ## Cleans all unversioned files in project
	@git clean -dxf -e .vscode/

