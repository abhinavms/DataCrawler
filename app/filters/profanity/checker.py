import os
import numpy as np
import joblib

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

vectorizer = joblib.load(os.path.join(path, 'vectorizer.joblib'))
model = joblib.load(os.path.join(path, 'model.joblib'))

def predict(texts):
    # return model.predict(vectorizer.transform(texts))
    return model.predict_proba(vectorizer.transform(texts)).reshape((-1, 1))[1]