init:
	pip3 install -r requirements.txt

test:
	pytest -s -v

.PHONY: init test
