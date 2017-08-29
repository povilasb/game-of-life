src_dir := gol

python ?= python3.6
virtualenv_dir := pyenv
pip := $(virtualenv_dir)/bin/pip
pytest := $(virtualenv_dir)/bin/py.test
coverage := $(virtualenv_dir)/bin/coverage
linter := $(virtualenv_dir)/bin/python -m flake8
py_requirements ?= requirements/prod.txt requirements/dev.txt


.PHONY: test
test: $(virtualenv_dir)
	PYTHONPATH=$(PYTHONPATH):. $(coverage) run \
		--source $(src_dir) $(pytest) -s tests
	$(coverage) report -m

.PHONY: lint
lint: $(virtualenv_dir)
	$(linter) $(src_dir)

$(virtualenv_dir): $(py_requirements)
	$(python) -m venv $@
	for r in $^ ; do \
		$(pip) install -r $$r ; \
	done
