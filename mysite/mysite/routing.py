from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatbox.routing

ASGI_APPLICATION = "mysite.routing.application"
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(chatbox.routing.websocket_urlpatterns)),
    })
