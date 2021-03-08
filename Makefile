.PHONY: init test

test:
	pytest -s -v

init:
	pip3 install -r requirements.txt
