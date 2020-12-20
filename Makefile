init:
	pip3 install -r requirements.txt

test:
	pytest -s

.PHONY: init test
