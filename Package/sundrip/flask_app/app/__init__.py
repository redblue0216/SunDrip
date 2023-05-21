# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个flask-app的基础应用管理类
"""
模块介绍
-------

这是一个flask-app的基础应用管理类

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）为flask-app提供基础应用管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import logging
###
from flask import Flask
###
from flask_appbuilder import AppBuilder,SQLA
### 
from app.index import MyIndexView
### 
from sqlalchemy import event
from sqlalchemy.engine import Engine
### 
from .security import MySecurityManager



####### 基础应用管理 ##########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）为flask-app提供基础应用管理                                        ###
#############################################################################



####### 基础应用管理 ###################################################################
#######################################################################################



### 
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)



### 
app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, security_manager_class=MySecurityManager,indexview=MyIndexView)



### 
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()



### 
from . import models, views  # noqa



##########################################################################################
##########################################################################################


