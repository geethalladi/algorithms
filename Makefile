.PHONY: init test

test:
	pytest -s -v; echo $$?

init:
	pip3 install -r requirements.txt
