# VADIS summarization api

## Requirements

Models will be download from the vadis private org on huggingface platform.
To run this application, you need to have access to the [org](https://huggingface.co/vadis).


## Installation

### pkgs
Requires [poetry](https://python-poetry.org/docs/).

```bash
poetry install
```

### huggingface authentication

Login to the huggingface vadis org by running,

```bash
huggingface-cli login
```

it will show prompts asking for your authentication token.
If you are a member of the org, you should have it [here](https://huggingface.co/settings/tokens).


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
uvicorn vadis_summarization_api.main:app
```

## Try

While the app is running by the command above, you can access to the automatically generated documentations where you can actually try out the API.
Just open the [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
Make sure the app is running.
