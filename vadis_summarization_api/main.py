import os
from typing import List, Union

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = FastAPI()
load_dotenv()


class Texts(BaseModel):
    documents: List[str]


lang2model_name = {
    "en": "vadis/bart_scitldr",
    "ja": "vadis/xscitldr_ja",
    "zh": "vadis/xscitldr_zh",
    "it": "vadis/xscitldr_it",
    "de": "vadis/xscitldr_de",
}

lang2lang_code = {
    "en": "en_XX",
    "de": "de_DE",
    "ja": "ja_XX",
    "it": "it_IT",
    "zh": "zh_CN",
}


class Model:
    def __init__(self, lang: str = "en", use_gpu=False):
        print(f"Initializing a model in {lang}...")
        model_name = lang2model_name[lang]

        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
        bart = AutoModelForSeq2SeqLM.from_pretrained(model_name, use_auth_token=True)

        if use_gpu:
            bart = bart.to("cuda")

        self.use_gpu = use_gpu
        self.bart = bart
        self.lang = lang
        self.model_name = model_name
        print("loaded!")

    def summarize(self, text: str) -> str:
        inputs = self.tokenizer(
            [text], padding="max_length", truncation=True, return_tensors="pt"
        )
        if self.lang == "en":
            summary_ids = self.bart.generate(
                inputs["input_ids"].to("cuda" if self.use_gpu else "cpu"),
                max_length=250,
                num_beams=1,
                early_stopping=True,
            )
        else:
            summary_ids = self.bart.generate(
                inputs["input_ids"].to("cuda" if self.use_gpu else "cpu"),
                max_length=250,
                num_beams=1,
                early_stopping=True,
                decoder_start_token_id=self.tokenizer.lang_code_to_id[
                    lang2lang_code[self.lang]
                ],
            )
        return self.tokenizer.batch_decode(summary_ids, skip_special_tokens=True)[0]

    def summarize_batch(self, texts: List[str]) -> List[str]:
        inputs = self.tokenizer(
            texts, padding="max_length", truncation=True, return_tensors="pt"
        )
        summary_ids = self.bart.generate(
            inputs["input_ids"].to("cuda") if self.use_gpu else inputs["input_ids"],
            max_length=50,
            num_beams=1,
            early_stopping=True,
        )
        return self.tokenizer.batch_decode(summary_ids, skip_special_tokens=True)


model = Model(os.environ.get("LANGUAGE", "en"))


@app.post("/summarize")
def summarize(texts: Texts, auth_key: Union[str, None] = Header(default=None)):
    if os.environ["AUTH_KEY"] == auth_key:
        return model.summarize_batch(texts.documents)
    else:
        return HTTPException(status_code=401, detail="Wrong key.")
