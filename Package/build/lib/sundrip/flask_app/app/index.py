# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个flask-app的首页管理类
"""
模块介绍
-------

这是一个flask-app的首页管理类

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）为flask-app提供首页管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from flask_appbuilder import IndexView



####### 首页管理 ############################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）为flask-app提供首页管理                                            ###
#############################################################################



####### 首页管理 ###################################################################
###################################################################################



class MyIndexView(IndexView):
    index_template = 'index.html'



######################################################################################
######################################################################################


