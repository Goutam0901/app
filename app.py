import pickle
from flask import Flask, render_template, request

app= Flask(__name__)
loaded_model= pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('form.html')


@app.route('/prediction',methods=["POST"])
def prediction():
    battery_power = request.form['batterypower']
    int_memory = request.form['int_memory']
    ram = request.form['ram']

    prediction=loaded_model.predict([[battery_power,int_memory,ram]])
    if prediction[0]==0:
        prediction = "Low Cost"
        
    elif prediction==1:
        prediction = "Medium Cost"
        
    elif prediction==2:
        prediction = "High Cost"
        
    else:        
        prediction = "Very High Cost"        
 
    
    return render_template('form.html', api_output=prediction)
    
if __name__ == '__main__':
    app.run(debug=True) 
