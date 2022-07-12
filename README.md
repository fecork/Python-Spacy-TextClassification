
## Fuente
[Text Classification with Spacy 3.0](https://catherinebreslin.medium.com/text-classification-with-spacy-3-0-d945e2e8fc44)
## Descarga de datos:

[Kaggle](https://www.kaggle.com/datasets/rmisra/news-category-dataset)

## Instrucciones

```python

# Plantilla de Configuración
python -m spacy init config --pipeline textcat config.cfg

# Ejecutar Entrenamiento

python -m spacy train config.cfg --paths.train ./train.spacy  --paths.dev ./dev.spacy --output textcat_model

# Probar Mejor modelo
python -m spacy evaluate textcat_model/model-best/ --output metrics.json ./test.spacy

#Package
python -m spacy package textcat_model/model-best packages --name news_cat --version 0.0.0

```