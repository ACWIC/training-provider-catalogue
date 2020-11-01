STAGE = dev  # this is the environment we deploy to

test:
	docker-compose -f local.yml run --rm app python -m pytest
build:
	docker-compose -f local.yml build

deploy_lambda:
	pip3 install -r requirements/serverless.txt --target libs
	cd libs; zip -r9 ../function.zip .; cd ..
	zip -rg function.zip app
	zip -g function.zip handler.py
	aws lambda update-function-code --function-name training-provider-api-$(STAGE)-catalogue --zip-file fileb://function.zip

up:
	docker-compose -f local.yml up -d

down:
	docker-compose -f local.yml down

precom:
    pre-commit run -a
