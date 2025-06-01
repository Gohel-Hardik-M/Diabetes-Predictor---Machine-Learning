from flask  import Flask , render_template , request
import pickle 
import numpy as np 

app = Flask(__name__)
model = pickle.load(open('C:/Users/hardi/Downloads/CS(EH)/DS/projects/Diabetes Prediction/model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    features = np.array([data])
    predictions = model.predict(features)
    
    result = 'Diabetes' if predictions[0]==1 else 'No Diabetes'
    return render_template("index.html", prediction_text = f'Result : {result}')

if __name__ == "__main__":
    app.run(debug=True)