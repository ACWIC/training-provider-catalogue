# Deployment

This is a python FastAPI app that is built to run on AWS Lambda
via the API Gateway.
It should also be able to run on other platfroms
(such as MS Azure, or any platform supporting docker containers)
although those are not currently being actively tested
by the development team. 

Deployments are managed with the `serverless` tool,
which manges dealing underlying plaform.

It can also run locally with `serverless-offline`
in a mode which mimics API Gateway/lambda infrastructure.
This mode leverages local services
like Minio as replacements for AWS resources like S3.


## Installation

Everything is managed with docker-compose. The configuration for this is stored in
`local.yml`, so it can be convenient to set this in your shell first:
```
export COMPOSE_FILE=local.yml
```

1. `docker-compose build` - build everything
2. `docker-compose up -d` - run everything in daemon mode

There are two components:
2. API documentation (via uvicorn/FastAPI directly)
3. minio


## Configuration

Default configuration is provided under `.envs/.local/`, which includes
everything required for the components to work together.


### Running locally
```
docker-compose up
```

The service will be available on port 8082

Open `localhost:8082/docs` for swagger documentation.

## Configuration:

There's two expected environment variables:

`STAGE_PREFIX`: API gateways add a prefix after the domain, but it's not passed down to the service.
But if the service is called from a Javascript application like swagger UI, the prefix has be provided.
`STAGE_PREFIX` should is expected to be provided by the serverless runner.


`SERVICE_PREFIX`: When deploying more than one service under the same API gateway, a prefix is used to
map to each service. this prefix is passed to the service itself, and all URLs are expected to be prepended
with it. (unlike the `STAGE_PREFIX`)

Note that all both variables are managed and provided from serverless, and you don't need to think about them
during development.


**A note about local resources**

docker-compose will not auto-create S3 buckets in minio,
so this must be done manually first.
See the configuration in .envs/.local/.sls
to determine what buckets are needed.
