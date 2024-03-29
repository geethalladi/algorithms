.PHONY: init test

test:
	pytest; echo $$?

all:
	make install && make test

install:
	pip3 install -r requirements.txt

clean:
	rm -vf *.gv *.gv.pdf
	rm -rf htmlcov/

report:
	coverage run -m pytest && coverage html && open htmlcov/index.html
