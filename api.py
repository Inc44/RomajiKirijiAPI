from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pykakasi import kakasi
from romaji_kiriji import romaji_kiriji_mapping
import re

api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
kks = kakasi()
parentheses_content_removal_pattern = re.compile("（[^）]*）")
romaji_kiriji_mapping_sorted = sorted(
    romaji_kiriji_mapping.keys(), key=len, reverse=True
)


class JapaneseInput(BaseModel):
    japanese_text: str


class JapaneseOutput(BaseModel):
    romaji_text: str
    kiriji_text: str


@api.post("/translate/", response_model=JapaneseOutput)
async def translate(input: JapaneseInput):
    japanese_text = input.japanese_text.strip()
    japanese_text = japanese_text.replace("\u3000", "")
    japanese_text = parentheses_content_removal_pattern.sub("", japanese_text)
    japanese_sentences = japanese_text.strip().splitlines()
    romaji_sentences = []
    kiriji_sentences = []
    for sentence in japanese_sentences:
        romaji_sentence = " ".join([item["hepburn"] for item in kks.convert(sentence)])
        kiriji_sentence = romaji_sentence
        for match in romaji_kiriji_mapping_sorted:
            kiriji_sentence = kiriji_sentence.replace(
                match, romaji_kiriji_mapping[match]
            )
        romaji_sentences.append(romaji_sentence)
        kiriji_sentences.append(kiriji_sentence)
    romaji_text = "\n".join(romaji_sentences)
    kiriji_text = "\n".join(kiriji_sentences)
    # print(japanese_sentences, "\n")
    # print(romaji_sentences, "\n")
    # print(kiriji_sentences, "\n")
    # print(japanese_text, "\n")
    # print(romaji_text, "\n")
    # print(kiriji_text, "\n")
    return JapaneseOutput(romaji_text=romaji_text, kiriji_text=kiriji_text)
