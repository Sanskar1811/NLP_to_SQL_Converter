import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import RidgeClassifier
import pickle
import os

# Load data
df = pd.read_csv('data/query_dataset.csv')
X = df['natural_language_query']
y = df['sql_query']

# ML pipeline
model = make_pipeline(
    TfidfVectorizer(),
    RidgeClassifier()
)

model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
with open("model/sql_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as sql_model.pkl")
