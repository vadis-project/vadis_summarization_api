# VADIS summarization api


## Installation

Requires [poetry](https://python-poetry.org/docs/).

```bash
poetry install
```

## Configure

This API loads configuration from `./.env` file.
There is a sample included in this repository as `./.sample.env`.
You can start by copying this by `cp ./sample.env ./.env`.
You can set `AUTH_KEY` to any string.
For `LANGUAGE`, pick one of en, ja, zh, it or de, to change the language for summaries.

## Run

First, activate the enviroment created by poetry by running following,
```bash
poetry shell
```

Then, start the api, this may take some time for the first time because of model downloading,
```bash
uvicorn main:app
```

## Try

While the app is running by the command above, you can access to the automatically generated documentations where you can actually try out the API.
Just open the [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
Make sure the app is running.
