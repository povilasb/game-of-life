src_dir := game_of_life

virtualenv_dir := pyenv
pip := $(virtualenv_dir)/bin/pip
pytest := $(virtualenv_dir)/bin/py.test
coverage := $(virtualenv_dir)/bin/coverage


test: $(virtualenv_dir)
	PYTHONPATH=$(PYTHONPATH):. $(coverage) run \
		--source $(src_dir) $(pytest) -s tests
	$(coverage) report -m
.PHONY: test

$(virtualenv_dir): requirements.txt
	virtualenv --python=python3 $@
	$(pip) install -r $^
