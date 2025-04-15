from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', sum_result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        sum_result = num1 + num2
        return render_template('index.html', sum_result=sum_result)
    except ValueError:
        return "Invalid input. Please enter valid numbers.", 400

if __name__ == '__main__':
    app.run(debug=True)
