# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个flask-app的权限管理类
"""
模块介绍
-------

这是一个flask-app的权限管理类

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）为flask-app提供权限管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



###
__author__ = "shihua"
###
from flask import redirect
from flask_appbuilder.actions import action
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder.security.views import UserDBModelView



####### 权限管理 ############################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）为flask-app提供权限管理                                           ###
#############################################################################



####### 权限管理 #######################################################################
#######################################################################################



### 
class MyUserDBView(UserDBModelView):
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket", single=False)
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())



### 
class MySecurityManager(SecurityManager):
    userdbmodelview = MyUserDBView



##############################################################################################
##############################################################################################


