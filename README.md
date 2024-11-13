<!-- PROJECT SHIELDS -->
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">VADIS Summarization API</h3>

  <p align="center">
    An API that provides text summarization services in both English and German.
    <br />
    <br />
    <a href="https://github.com/vadis-project/vadis_summarization_api/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/vadis-project/vadis_summarization_api/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#contact">Citation</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
![vadis_summarization_api](https://github.com/user-attachments/assets/88e60bf3-80f0-43cb-bfd3-0ad15d02eb45)

VADIS Summarization API is an easy-to-use API that provides automatic text summarization services in both English and German. It processes individual documents, detects their language, and summarizes them accordingly. If the input document is in German, it will first translate it to English before summarizing.

- Input: A text document that can be in either English or German.
- Output: A summarized version of the input document, available in English (if the input is German, it will be translated first).
- Noteworthy Feature: The API automatically detects the language of the input text and, if necessary, translates German input into English for summarization.
- Demo: You can interact with the API by visiting [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

For more information on the underlying summarization models and translation mechanisms, check the documentation at [VADIS GitHub Repository](https://github.com/vadis-project).

<!-- GETTING STARTED -->
## Getting Started

Follow these steps to get a local copy of the VADIS Summarization API up and running on your machine.

### Prerequisites

Before you begin, ensure that you have the following installed:
* **Python 3.10**
* **Poetry** (A package manager for Python projects)
  - Install Poetry by following [the official documentation](https://python-poetry.org/docs/#installation)

### Installation

1. Clone the repository:
   ```sh
   git clone git@github.com:vadis-project/vadis_summarization_api.git
   ```
2. Navigate into the project directory:
   ```sh
   cd vadis_summarization_api
   ```
3. Install the project dependencies using Poetry:
   ```sh
   poetry install
   ```

<!-- USAGE EXAMPLES -->
## Usage

### Configure

The API loads its configuration from a `.env` file. You can start by copying the sample configuration file:

```sh
cp ./sample.env ./.env
```

You can customize the following settings:
- `AUTH_KEY`: Set this to any string. You will need this key when accessing the API.
- `LANGUAGE`: Set this to either `en` (English) or `de` (German). This determines the language of the summaries. If you choose `de`, the API will summarize in English, even if the input is in German.

### Run the API

Start the API within the virtual environment created by Poetry:
```sh
poetry run uvicorn vadis_summarization_api.main:app
```

This will start the API, and it may take some time for the first run as models need to be downloaded.

### Try

Once the API is running, you can access the automatically generated documentation and interact with the API directly at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

You can call it to generate summaries. Following is one example which uses curl command.

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/summarize' \
  -H 'accept: application/json' \
  -H 'auth-key: YOUR-AUTH-KEY' \
  -H 'Content-Type: application/json' \
  -d '{
  "documents": [
    "TEXT OF THE PAPER TO BE SUMMARIZED",
    "YOU CAN SUMMARIZE MORE THAN ONE PAPER IN ONE API CALL"
  ]
}'
```

The `/summarize` endpoint detects the language of the input document. If the document is in German, it will first translate the text to English before summarizing it.

<!-- ROADMAP -->
## Roadmap

- [ ] Improve summarization models for better accuracy

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

For any questions or inquiries, please feel free to raise an issue in this repository or contact me at

Sotaro Takeshita - sotaro.takeshita@uni-mannheim.de

<!--
## Citation

If you use this API in your research or project, please cite it as follows:

```
@misc{vadis2024,
  author = {VADIS Team},
  title = {VADIS Summarization API},
  year = {2024},
  url = {https://github.com/vadis-project/vadis_summarization_api}
}
```
-->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/vadis-project/vadis_summarization_api.svg?style=for-the-badge
[issues-url]: https://github.com/vadis-project/vadis_summarization_api/issues
[license-shield]: https://img.shields.io/github/license/vadis-project/vadis_summarization_api.svg?style=for-the-badge
[license-url]: https://github.com/vadis-project/vadis_summarization_api/blob/master/LICENSE
[product-screenshot]: images/screenshot.png
