from skatelife.celery import app


@app.task
def send_email(url, params):

    import requests
    requests.post(url, files={}, data=params)

