<b>Machine Learning-based Text Classification Web App using Flask </b>
<br>
This project is a Flask-based web application that allows users to classify text input using a pre-trained machine learning model. 
The core functionality involves processing user-entered text through a TF-IDF vectorizer and predicting categories using a RidgeClassifier pipeline.

🔧 Key Features:
<br>
✅ Frontend Input: A simple HTML form allows users to submit a text query.

✅ Backend (Flask): Receives input, loads a serialized machine learning model using joblib, processes the input, and returns the predicted category.

✅ ML Model: Built using a pipeline with TfidfVectorizer, TfidfTransformer, LabelBinarizer, and RidgeClassifier.
