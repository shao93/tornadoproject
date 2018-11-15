#coding=utf-8
#用户登录
from control.base.base_handler import BaseHandler
from models.models import *
from models.db.dbsession import dbSession

class LoginHandler(BaseHandler):

    def get(self):
        self.render("user/login.html")

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")

        #根据用户名去查找数据库
        search_user = dbSession.query(PersonalTable).filter_by(username=username,password=password).first()
        if search_user:
            #登录成功调用方法
            self.session.set('username', search_user.username)
            self.redirect('/index')
        else:
            self.write(u"登录失败")
