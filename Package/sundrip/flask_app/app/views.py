# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个flask-app的视图函数类，主要包括信息视图功能和插件视图功能
"""
模块介绍
-------

这是一个flask-app的视图函数类，主要包括信息视图功能和插件视图功能

设计模式：

    无

关键点：    

    （1）view

主要功能：            

    （1）为flask-app提供视图函数
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import calendar
from flask import g
from flask_appbuilder import ModelView
### 后来添加的依赖
from flask_appbuilder.api import BaseApi,expose
from flask import redirect
from flask import render_template
from flask import current_app
###
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
### 
from . import appbuilder
### 重新添加的数据模型
from .models import AlgorithmInfo,ModelInfo,ParameterInfo,ApplicationInfo,DataInfo,ModelStore,ManualLog



####### 视图函数类 ###########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）view                                                             ###
### 主要功能：                                                            ###
### （1）为flask-app提供视图函数                                           ###
############################################################################



####### 视图函数 #####################################################################
#####################################################################################



### AlgorithmInfoView
class AlgorithmInfoView(ModelView):
    '''
    类介绍：

        这是一个算法信息视图函数类
    '''

    ### 数据模型
    datamodel = SQLAInterface(AlgorithmInfo)
    ### 可展示数据列
    list_columns = ["index",
                    "name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "homepage",
                    "author",
                    "authoremail",
                    "license",
                    "requires",
                    "requiredby"]
    ### 可搜索数据列
    search_columns = ["index",
                      "name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "homepage",
                      "author",
                      "authoremail",
                      "license",
                      "requires",
                      "requiredby"]

    
    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### ModelInfoView
class ModelInfoView(ModelView):
    '''
    类介绍：

        这是一个模型信息视图函数类
    '''

    ### 数据模型
    datamodel = SQLAInterface(ModelInfo)
    ### 可展示数据列
    list_columns = ["index",
                    "name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "requires",
                    "data",
                    "algorithm"]
    ### 可搜索数据列
    search_columns = ["index",
                      "name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "requires",
                      "data",
                      "algorithm"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### ParameterInfoView
class ParameterInfoView(ModelView):
    '''
    类介绍：

        这是一个参数信息视图函数类
    '''

    ### 数据模型
    datamodel = SQLAInterface(ParameterInfo)
    ### 可展示数据列
    list_columns = ["index",
                    "name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "datatype",
                    "requiredby"]
    ### 可搜索数据列
    search_columns = ["index",
                      "name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "datatype",
                      "requiredby"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### ApplicationInfoView
class ApplicationInfoView(ModelView):
    '''
    类介绍：：

        这是一个应用信息视图函数类
    '''

    ### 数据模型
    datamodel = SQLAInterface(ApplicationInfo)
    ### 可展示数据列
    list_columns = ["index",
                    "name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "requires",
                    "project"]
    ### 可搜索数据列
    search_columns = ["index",
                      "name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "requires",
                      "project"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### DataInfoView
class DataInfoView(ModelView):
    '''
    类介绍：

        这是一个数据集信息视图函数类
    '''

    ### 数据模型
    datamodel = SQLAInterface(DataInfo)
    ### 可展示数据列
    list_columns = ["index",
                    "name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "requiredby",
                    "datatype",
                    "project"]
    ### 可搜索数据列
    search_columns = ["index",
                      "name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "requiredby",
                      "datatype",
                      "project"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



### ModelStoreView
class ModelStoreView(ModelView):
    '''
    类介绍：

        这是一个日志信息视图函数类
    '''

    ### 数据模型
    datamodel = SQLAInterface(ModelStore)
    ### 可展示数据列
    list_columns = ["index",
                    "name",
                    "version",
                    "summary",
                    "config",
                    "remark",
                    "data"]
    ### 可搜索数据列
    search_columns = ["index",
                      "name",
                      "version",
                      "summary",
                      "config",
                      "remark",
                      "data"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name
    


### ManualLogView
class ManualLogView(ModelView):
    '''
    类介绍：

        这是一个日志信息视图函数类
    '''

    ### 数据模型
    datamodel = SQLAInterface(ManualLog)
    ### 可展示数据列
    list_columns = ["index",
                    "msg",
                    "levelname",
                    "filename",
                    "module",
                    "lineno",
                    "time"]
    ### 可搜索数据列
    search_columns = ["index",
                      "msg",
                      "levelname",
                      "filename",
                      "module",
                      "lineno",
                      "time"]


    def __repr__(self):
        '''
        方法功能：

            定义一个string魔法方法

        参数：
            无

        返回：
            无
        '''

        return self.name



####### 添加功能视图 #####################################################################
#########################################################################################



### add AlgorithmInfoView
appbuilder.add_view(
    AlgorithmInfoView,
    "AlgorithmInfo",
    icon="fas fa-cube",
    category="AlgorithmInfo",
    category_icon="fas fa-table",
)



### add ModelInfoView
appbuilder.add_view(
    ModelInfoView,
    "ModelInfo",
    icon="fas fa-puzzle-piece",
    category="AlgorithmInfo",
    category_icon="fas fa-table"
)



### add ParameterInfoView
appbuilder.add_view(
    ParameterInfoView,
    "ParameterInfo",
    icon="fas fa-th",
    category="AlgorithmInfo",
    category_icon="fas fa-table"
)



### add ApplicationInfoView
appbuilder.add_view(
    ApplicationInfoView,
    "ApplicationInfo",
    icon="fas fa-rocket",
    category="ApplicationInfo",
    category_icon="fas fa-table"    
)



### add DataInfoView
appbuilder.add_view(
    DataInfoView,
    "DataInfo",
    icon="fas fa-database",
    category="ApplicationInfo",
    category_icon="fas fa-table"    
)



### add ModelStoreView
appbuilder.add_view(
    ModelStoreView,
    "ModelStore",
    icon="fas fa-database",
    category="ApplicationInfo",
    category_icon="fas fa-table"    
)


### add ManualLogView
appbuilder.add_view(
    ManualLogView,
    "ManualLog",
    icon="fas fa-clipboard",
    category="ApplicationInfo",
    category_icon="fas fa-table"    
)



####### 安全清空视图 ##########################################################################
##############################################################################################



appbuilder.security_cleanup()



#################################################################################################
#################################################################################################


