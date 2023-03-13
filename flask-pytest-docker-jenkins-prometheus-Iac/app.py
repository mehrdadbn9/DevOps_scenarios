from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return 'Welcome to the User Collector App!'

if __name__ == '__main__':
    app.run()
