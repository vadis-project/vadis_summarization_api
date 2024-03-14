import os
from typing import List, Union

import langdetect
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from schnitsum import SchnitSum
from summarizer.sbert import SBertSummarizer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers.pipelines import pipeline

app = FastAPI()
load_dotenv()


class Texts(BaseModel):
    documents: List[str]


lang2model_name = {
    "en": "sobamchan/bart-large-scitldr",
    "de": "sobamchan/mbart-large-xscitldr-de",
}

lang2lang_code = {
    "en": "en_XX",
    "de": "de_DE",
    "ja": "ja_XX",
    "it": "it_IT",
    "zh": "zh_CN",
}


class Model:
    def __init__(self, tgt_lang: str = "en", use_gpu=False):
        print(f"Initializing a model in {tgt_lang}...")
        model_name = lang2model_name[tgt_lang]

        model_name = lang2model_name[tgt_lang]
        self.schnitsum_model = SchnitSum(model_name, tgt_lang=tgt_lang, use_gpu=use_gpu)

        self.use_gpu = use_gpu
        self.tgt_lang = tgt_lang
        self.model_name = model_name

        self.translator = None
        print("loaded!")

    def summarize(self, text: str) -> str:
        do_translation = True if langdetect.detect(text) == "de" else False
        if do_translation:
            print("German!!! Translate to English first.")
            if self.translator is None:
                self.translator = pipeline(model="facebook/wmt19-de-en")
            text = self.translator([text])[0]["translation_text"]

        return self.schnitsum_model([text])[0]

    def summarize_batch(self, texts: List[str]) -> List[str]:
        return self.schnitsum_model(texts)


model = Model(os.environ.get("LANGUAGE", "en"))


@app.post("/summarize_batch")
def summarize_batch(texts: Texts, auth_key: Union[str, None] = Header(default=None)):
    if os.environ["AUTH_KEY"] == auth_key:
        return model.summarize_batch(texts.documents)
    else:
        return HTTPException(status_code=401, detail="Wrong key.")


@app.post("/summarize")
def summarize(texts: Texts, auth_key: Union[str, None] = Header(default=None)):
    if os.environ["AUTH_KEY"] == auth_key:
        return model.summarize(texts.documents[0])
    else:
        return HTTPException(status_code=401, detail="Wrong key.")


ext_model = SBertSummarizer("all-distilroberta-v1")


@app.post("/ext_summarize")
def ext_summarize(texts: Texts, auth_key: Union[str, None] = Header(default=None)):
    if os.environ["AUTH_KEY"] == auth_key:
        return ext_model(texts.documents[0], num_sentences=3)
    else:
        return HTTPException(status_code=401, detail="Wrong key.")
