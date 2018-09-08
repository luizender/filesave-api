# API Rest Project for save file on Google Store

This project is an API to save file on Google Store for the technical test of MOVTI

## Table of Contents

* [Requirements](#requirements)
* [Environment Variables](#environment-variables)
* [Setup](#setup)
* [Running](#running)
* [Running with Shell](#running-with-shell)
* [Code Documentation](#code-documentation)
* [Code Analysis](#code-analysis)
* [Execute Unit Test](#execute-unit-test)
* [Access the API](#access-the-api)

## Requirements

To run this project, you need to install the [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

## Environment Variables

The Environment Variables of this container are:
* API_MODE: The mode of API. The mode can be 'prod' or 'devel' (Default: prod)
* GCLOUD_PROJECT: The name of Google Cloud Project (Default: filesave)
* GCLOUD_STORAGE_BUCKET: The name of Google Cloud Storage (Default: filesave-storage)
* GCLOUD_STORAGE_CHUNK_SIZE: The chunk size must be a multiple of 256KB (Default: 524288)

## Setup

To set up the container, you need to execute:

```
docker-compose build
```

This command will build the container follow the steps in ```Dockerfile```.

## Running

After setup the container, you can run the services with the following command:

```
docker-compose up
```

## Running with Shell

To run with shell, you need to execute

```
docker-compose run --service-ports api sh
```

After that, you run with the following command:

```
make run
```

## Code Documentation

If you want to see the documentation of code, you need to execute the following command after run the container with shell:

```
make docs
```

Now, you can access the code documentation opening the file ```docs/build/index.html```

## Code Analysis

If you want to analyze your python code that was written inside the ```src``` folder, you need to execute the following command after run the container with shell:

```
make lint
```

## Execute Unit Test

If you want to execute the unittest, you need to execute the following command after run the container with shell:

```
make tests
```

## Access the API

You can access the API using the follow step:

```
curl -X GET http://127.0.0.1:8000/
```

Or, you can access using your browser with the address ```http://127.0.0.1:8000/```
