import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import date
from flask import Flask, render_template
from flask import request
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
  if request.method == 'POST':
    stock_name = request.form['stock_name']
    years = request.form['years']

    today = date.today()
    END_DATE = today.isoformat()
    START_DATE = date(today.year - int(years), today.month, today.day).isoformat()
    data = yf.download(stock_name, start=START_DATE, end=END_DATE)


    # EMA
    data['EMA-50'] = data['Close'].ewm(span=50, adjust=False).mean()
    data['EMA-200'] = data['Close'].ewm(span=200, adjust=False).mean()
    plt.figure(figsize=(8, 4))
    plt.plot(data['EMA-50'], label="EMA for 50 days")
    plt.plot(data['EMA-200'], label="EMA for 200 days")
    plt.plot(data['Close'], label="Close")
    plt.title(f'Exponential Moving Average for {stock_name}')
    plt.ylabel('Price (in USD)')
    plt.xlabel("Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/plt_ema.png')
    plt.close()

    # Low vs High
    plt.figure(figsize=(8, 4))
    plt.plot(data['Low'], label="Low", color="indianred")
    plt.plot(data['High'], label="High", color="mediumseagreen")
    plt.ylabel('Price (in USD)')
    plt.xlabel("Time")
    plt.title(f"High vs Low of {stock_name}")
    plt.tight_layout()
    plt.legend()
    plt.savefig('static/plt_highlow.png')
    plt.close()

    # Linear Regression model
    x = data[['Open', 'High', 'Low', 'Volume', 'EMA-50', 'EMA-200']]
    y = data['Close']
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    pred = lr_model.predict(X_test)
    plt.figure(figsize = (8, 4))
    plt.scatter(y_test, pred, color="black")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color = 'mediumseagreen', label='Correct Predictions')
    plt.xlabel('Real Values')
    plt.ylabel('Predicted Values')
    plt.title('Real Values vs Predicted Values')
    plt.legend()
    plt.savefig('static/plt_realvsvalue.png')
    plt.close()

    # Closing vs Volume
    plt.figure(figsize = (8, 4))
    plt.scatter(X_test['Volume'], y_test, label = 'Real Values')
    plt.scatter(X_test['Volume'], pred, label = 'Predictions')
    plt.title('Predicted vs Actual Closing Price based on Volume')
    plt.xlabel('Volume')
    plt.ylabel('Closing Price (in USD)')
    plt.legend()
    plt.savefig('static/plt_closingvsvolume.png')
    plt.close()

    return render_template('predict.html', plot_ema = 'static/plt_ema.png', plot_highlow= 'static/plt_highlow.png', plot_real='static/plt_realvsvalue.png', plot_closevolume='static/plt_closingvsvolume.png', mean_squared_error= str(mean_squared_error(y_test, pred)), mean_absolute=str(mean_absolute_error(y_test, pred)), r2_score=str(r2_score(y_test, pred)))
  elif request.method == 'GET':
    return render_template('index.html')
  

@app.route('/predict')
def predict(): 
  return render_template('predict.html')

if __name__ == '__main__':
  app.run(debug=True)
