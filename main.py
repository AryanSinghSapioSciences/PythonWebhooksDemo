from sapiopylib.rest.WebhookService import AbstractWebhookHandler, WebhookConfiguration, WebhookServerFactory
from sapiopylib.rest.pojo.webhook.WebhookContext import SapioWebhookContext
from sapiopylib.rest.pojo.webhook.WebhookResult import SapioWebhookResult


"""
This is a demo class that shows how a webhook can be invoked via Python
"""
class HelloWorldWebhookHandler(AbstractWebhookHandler):
    """
    Prints "Hello World" in the python console whenever the webhook handler is invoked.
    """

    def run(self, context: SapioWebhookContext) -> SapioWebhookResult:
        print("Hello World!")
        return SapioWebhookResult(True)

# Note: the registration points here are directly under root.
# In this example, we are listening to 8090. So the endpoint URL to be configured in Sapio is:
# http://[webhook_server_hostname]:8090/hello_world

config: WebhookConfiguration = WebhookConfiguration(verify_sapio_cert=False, debug=True)
config.register('/hello_world', HelloWorldWebhookHandler)

app = WebhookServerFactory.configure_flask_app(app=None, config=config)
# UNENCRYPTED! This should not be used in production. You should give the "app" a ssl_context or set up a reverse-proxy.

# Dev Mode:
# app.run(host="0.0.0.0", port=8090)

if __name__ == '__main__':
    app.run(host="localhost", port=8090, debug=True)