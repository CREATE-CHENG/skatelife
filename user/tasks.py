from skatelife.celery import app

@app.task
def send_register_email():
    import requests

    url = "http://api.sendcloud.net/apiv2/mail/sendtemplate"

    # 您需要登录SendCloud创建API_USER，使用API_USER和API_KEY才可以进行邮件的发送。
    params = {"apiUser": "create_email_send",
              "apiKey": "VPYgm3AchzEePfnR",
              "from": "test@createcheng.com",
              "fromName": "createcheng测试邮件",
              "to": "createcheng@yeah.net",
              "templateInvokeName": "user_register",
              }

    r = requests.post(url, files={}, data=params)


@app.task
def test():
    print('test success')
