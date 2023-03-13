from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app=None)
form_submissions = metrics.counter(
    'form_submissions',
    'Number of form submissions'
)
