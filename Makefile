init:
	pip3 install -r requirements.txt

test:
	nosetests tests

.PHONY: init test
