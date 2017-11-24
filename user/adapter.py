from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        import requests
        from skatelife.settings.test import API_KEY, API_USER

        msg = self.render_mail(template_prefix, email, context)

        url = "http://api.sendcloud.net/apiv2/mail/send"

        # 您需要登录SendCloud创建API_USER，使用API_USER和API_KEY才可以进行邮件的发送。
        params = {"apiUser": API_USER,
                  "apiKey": API_KEY,
                  "from": "admin@skatelife.com",
                  "fromName": "admin@skatelife.com",
                  "to": email,
                  "subject": msg.subject,
                  "html": msg.body,
                  }
        requests.post(url, files={}, data=params)



