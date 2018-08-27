from discord_hooks import Webhook

url = 'https://discordapp.com/api/webhooks/482162188753174528/zRg-hcpL2ZHbB8-e2Md9MAHRRKGaTNrHEuQ4ZbYmcSM8-d-zrX1jp0aBLgvs5O1CJKYR'

msg = Webhook(url,msg=r"Hello there! I'm a webhook \U0001f62e")

msg.post()
