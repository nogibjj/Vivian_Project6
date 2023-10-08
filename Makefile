install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	#ruff linting is 10-100X faster than pylint
	# ruff check *.py mylib/*.py

# container-lint:
# 	docker run --rm -i hadolint/hadolint < Dockerfile

# refactor: format lint

# deploy:
# 	#deploy goes here
		
all: install lint format test


query: 
	python main.py test_query "select city,count(city) from Bars b left join (select s.bar from Sells s where s.price >5) a on a.bar=b.name where a.bar IS NULL group by city"

