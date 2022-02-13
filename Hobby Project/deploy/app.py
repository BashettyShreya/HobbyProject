from flask import Flask, render_template, request
import pickle as pkl
from sklearn.linear_model import LinearRegression
app = Flask(__name__)
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/demo')
def demo():
    return render_template('demo.html')
@app.route('/')
def home():
    return render_template('Home.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST" :
        age = request.form['age']
        Gender = request.form['Gender']
        BMI = request.form['BMI']
        Children = request.form['Children']
        Smoker = request.form['Smoker']
        Region = request.form['Region']
        data = [[int(age),int(Gender),float(BMI),int(Children),int(Smoker),int(Region)]]
        lr = pkl.load(open('charge.pkl','rb'))
        prediction = lr.predict(data)[0]
        if prediction<15000:
            tot = prediction + prediction*0.05
        else:
            tot = prediction + prediction*0.10
        r1 = prediction*0.75
        r2 = prediction*0.5
        r3 = prediction*0.25
   
    return render_template('index.html',prediction=prediction,tot=tot,r1=r1,r2=r2,r3=r3)
if __name__ == '__main__':
    app.run(debug=True)