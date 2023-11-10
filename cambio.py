from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__, template_folder='templates')
app.secret_key = 'e2277eb0e898401e839242d24c90833d'
API_KEY = 'e2277eb0e898401e839242d24c90833d'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))
    return render_template('/templates/login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/convert', methods=['POST'])
def convert_currency():
    amount = request.form['amount']
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    url = f'https://api.currencyfreaks.com/v2.0/rates/latest?apikey=e2277eb0e898401e839242d24c90833d&symbols=EUR,GBP,COP,ARS,MXN,PKR,INR,CAD,AUD,AED,ILS,RUB,CHF,JPY,CNY,BRL&base=USD'
    response = requests.get(url)
    data = response.json()
    result = data['result']
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
