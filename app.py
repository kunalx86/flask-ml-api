from flask import Flask, request, jsonify, render_template
import numpy as np 
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def default():
    return render_template('index.html')

@app.route('/mobile', methods=['POST'])
def mobile_output():
    return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    pred = model.predict([np.array(list(data.values()))])
    output = pred[0]
    return jsonify(output)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    data = list(data.values())
    data = data[:5]
    data = list(map(float, data))
    data = np.array(data).reshape(1, 5)
    to_predict = model.predict(data)
    return render_template('index.html', prediction=to_predict[0])

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5500, debug=False)