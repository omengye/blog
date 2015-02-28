from application.handlers import base, auth


urls = [
    (r"/", base.HomeHandler),
    (r"/ws", auth.CheckPageHandler),
    (r"/socket", auth.WebSocketHandler)
]