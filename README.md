# API Rest Project for save file on Google Store

[![Build Status](https://travis-ci.org/luizender/filesave-api.svg?branch=master)](https://travis-ci.org/luizender/filesave-api)

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
* [Accessing API URLs](#accessing-api-urls)
    * [Upload file](#upload-file)
    * [Get the list of files](#get-the-list-of-files)
    * [Get specific file](#get-specific-file)
    * [Delete file](#delete-file)

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

But, you need to get the credential file of Storage and save as ```service-account.json```. See the documentation of Authentication for more details ([Link of documentation](https://cloud.google.com/docs/authentication/getting-started))

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

## Accessing API URLs

To access the URLs of API, you can use the command line [curl](https://curl.haxx.se/) or the [Postman](https://www.getpostman.com/)

### Upload file

To upload a file to the Storage, you need to execute:
```
touch test.txt
curl -X POST -F 'file=@./test.txt' http://127.0.0.1:5000/file
```

### Get the list of files

To get the list of file, you need to execute the following command:

```
curl -X GET http://127.0.0.1:5000/file
```

### Get specific file

To get the the specific file, you need to execute the following command:

```
curl -X GET http://127.0.0.1:5000/file/test.txt
```

### Delete file

To delete the file you need to execute:

```
curl -X DELETE http://127.0.0.1:5000/file/test.txt
```
