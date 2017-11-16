from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        import requests
        from skatelife.settings.test import API_KEY, API_USER

        url = "http://api.sendcloud.net/apiv2/mail/send"

        # 您需要登录SendCloud创建API_USER，使用API_USER和API_KEY才可以进行邮件的发送。
        params = {"apiUser": API_USER,
                  "apiKey": API_KEY,
                  "from": "test@skatelife.com",
                  "fromName": "test@skatelife.com",
                  "to": "createcheng@yeah.net",
                  "subject": "skatelife激活邮件",
                  "html": "点击以下链接激活您的帐号：\n{activate_url}".format(activate_url=context['activate_url']),
                  }
        r = requests.post(url, files={}, data=params)

        print(r.text)

