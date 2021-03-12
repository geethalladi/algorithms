.PHONY: init test

test:
	pytest; echo $$?

all:
	make install && make test

install:
	pip3 install -r requirements.txt
