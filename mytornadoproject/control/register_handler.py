#coding=utf-8
#用户注册的视图
from control.base.base_handler import BaseHandler
from models.models import PersonalTable
from models.db.dbsession import dbSession

class RegisterHandler(BaseHandler):
    def get(self):
        self.render("user/register.html")

    def post(self):
        username = self.get_argument("name", "")
        password = self.get_argument("pass", "")
        if not username and not password:
            self.write(u"用户名或密码输入有错误")
        # 先查询数据库是否已经存在该用户
        search_name = dbSession.query(PersonalTable).filter_by(username=username).first()
        # search_name = user_model.by_name(username)
        if search_name:
            self.write(u"该用户名已经存在，不能重复注册")
        else:
            user = PersonalTable()
            user.username = username
            user.password = password
            self.db.add(user)
            self.db.commit()
            self.write(u"注册成功")