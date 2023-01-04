from flask import Flask, jsonify, request
import pandas
import pickle
from Controllers import transformText

app = Flask(__name__)

model = pickle.load(open('./Model/model.pkl', 'rb'))
tfidf = pickle.load(open('./Model/vectorizer.pkl', 'rb'))

@app.route('/predict', methods=['GET'])
def predict():
    data = request.json
    transformed_sms = transformText.transform_text(data['sentence'])
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    return jsonify({'result': int(result)})


if __name__ == "__main__":
    app.run(debug=True)
