#!/usr/bin/env python
# -*- coding: utf-8 -*-
# start server
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# 输入配置，比如default，development
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


# shell可以自动导入特定的对象
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


# 提供shell和db命令，附加到manager上，程序可以运行python manager.py db upgade
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
