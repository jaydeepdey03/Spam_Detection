from flask import Flask, jsonify, request
import pandas,pickle
from Controllers import transformText
from flask_cors import CORS
from waitress import serve
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False

model = pickle.load(open('./Model/model.pkl', 'rb'))
tfidf = pickle.load(open('./Model/vectorizer.pkl', 'rb'))

@app.route('/')
def func():
    return "Its working"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    transformed_sms = transformText.transform_text(data['sentence'])
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    return jsonify({'result': int(result)})
    # print(data)
    # return jsonify(data)


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
    # app.run(debug=True)