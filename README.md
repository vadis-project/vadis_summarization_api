# VADIS summarization api

## Requirements

- Python 3.10
- [Poetry](https://python-poetry.org/docs/)
  - A package manager for Python projects
  - Follow [the official documentation](https://python-poetry.org/docs/#installation) for its installation

## Setup

```bash
git clone git@github.com:vadis-project/vadis_summarization_api.git
cd vadis_summarization_api
poetry install
```

## Configure

This API loads configuration from `./.env` file.
There is a sample included in this repository as `./.sample.env`.
You can start by copying this by `cp ./sample.env ./.env`.
You can set `AUTH_KEY` to any string.

For `LANGUAGE`, pick one of en, ja, zh, it or de, to change the language for summaries.
Note that input documents need to be in English in any settings.
Ff you set `LANGUAGE="de"`, this API will return you summaries in German for the English inputs.

## Run

First, activate the enviroment created by poetry by running following,
```bash
poetry shell
```

Then, start the api, this may take some time for the first time because of model downloading,
```bash
uvicorn vadis_summarization_api.main:app
```

## Try

While the app is running by the command above, you can access to the automatically generated documentations where you can actually try out the API.
Just open the [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
Make sure the app is running.

## Translate German input

If you use `/summarize` end-point (which now only can process one document a time, no batch processing), it first detects the language that the document is written in, the if it's in German, it first translates into English, then summarize in English.
