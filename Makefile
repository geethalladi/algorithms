.PHONY: init test

test:
	pytest; echo $$?

init:
	pip3 install -r requirements.txt
