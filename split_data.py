from spacy.tokens import DocBin
import spacy
import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def convert(infile, outfile):

    with open(infile) as f:
        lines = f.readlines()

    train, test = train_test_split(lines, test_size=0.2, random_state=42)
    # df_test = pd.DataFrame(test, columns=["headline"])
    # df_train = pd.DataFrame(train, columns=["headline"])
        
    iterate("train", train)
    iterate("test", test)


def iterate(outfile, lines):
    outfile = "data//{0}.spacy".format(outfile)
    categories = ["POLITICS", "WELLNESS", "ENTERTAINMENT", "TRAVEL"]
    nlp = spacy.blank("en")
    db = DocBin()

    for line in lines:
        l = json.loads(line)
        doc = nlp.make_doc(l["headline"])
        doc.cats = {category: 0 for category in categories}
        doc.cats[l["category"]] = 1
        db.add(doc)
    db.to_disk(outfile)


convert("data//News_Category_Dataset_v2.json", "data//train.spacy")
