import spacy
nlp = spacy.load("textcat_model/model-best")
doc=nlp("History is made: 10 new UK attractions for day trips and short breaks")
print(doc.cats)