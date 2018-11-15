#coding=utf-8

from control import views
handlers = [
    (r'/index', views.MainHandler),
    (r"/login", views.LoginHandler),
    (r"/register", views.RegisterHandler)
]
