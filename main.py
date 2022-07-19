from flask import Flask, render_template
from cloudpayments import CloudPayments

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/buy')
def about():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
