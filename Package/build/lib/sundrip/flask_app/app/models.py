# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个flask-app的数据模型类，主要包括算法信息、模型信息、参数信息、应用信息、数据集信息、日志信息和模型对象数据七大数据模型
"""
模块介绍
-------

这是一个flask-app的数据模型类，主要包括算法信息、模型信息、参数信息、应用信息、数据集信息、日志信息和模型对象数据七大数据模型

设计模式：

    无

关键点：    

    （1）SQLite

主要功能：            

    （1）为flask-app提供数据模型
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import datetime
from flask_appbuilder import Model
from sqlalchemy import Column, String, create_engine, Integer, DateTime,Text,LargeBinary



####### 数据模型类 ###########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）SQLite                                                          ###
### 主要功能：                                                            ###
### （1）为flask-app提供数据模型                                          ###
############################################################################



####### 具体数据信息类 ###########################################################
#################################################################################



### AlgorithmInfo
class AlgorithmInfo(Model):
    '''
    类介绍：

        这是一个算法信息数据模型类
    '''

    __tablename__='AlgorithmInfo'
    index = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Text)
    version = Column(Text)
    summary = Column(Text)
    config = Column(Text)
    remark = Column(Text)
    homepage = Column(Text)
    author = Column(Text)
    authoremail = Column(Text)
    license = Column(Text)
    requires = Column(Text)
    requiredby = Column(Text)



### ModelInfo
class ModelInfo(Model):
    '''
    类介绍：

        这是一个模型信息数据模型类
    '''

    __tablename__='ModelInfo'
    index = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Text)
    version = Column(Text)
    summary = Column(Text)
    config = Column(Text)
    remark = Column(Text)
    requires = Column(Text)
    data = Column(Text)
    algorithm = Column(Text)



### ParameterInfo
class ParameterInfo(Model):
    '''
    类介绍：

        这是一个参数信息数据模型类
    '''

    __tablename__='ParameterInfo'
    index = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Text)
    version = Column(Text)
    summary = Column(Text)
    config = Column(Text)
    remark = Column(Text)
    datatype = Column(Text)
    requiredby = Column(Text)



### ApplicationInfo
class ApplicationInfo(Model):
    '''
    类介绍：

        这是一个应用信息数据模型类
    '''

    __tablename__='ApplicationInfo'
    index = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Text)
    version = Column(Text)
    summary = Column(Text)
    config = Column(Text)
    remark = Column(Text)
    requires = Column(Text)
    project = Column(Text)



### DataInfo
class DataInfo(Model):
    '''
    类介绍：

        这是一个数据集信息数据模型类
    '''

    __tablename__='DataInfo'
    index = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Text)
    version = Column(Text)
    summary = Column(Text)
    config = Column(Text)
    remark = Column(Text)
    requiredby = Column(Text)
    datatype = Column(Text)
    project = Column(Text)
    


### ModelStore
class ModelStore(Model):
    '''
    类介绍：

        这是一个模型存储数据模型类
    '''

    __tablename__='ModelStore'
    index = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Text)
    version = Column(Text)
    summary = Column(Text)
    config = Column(Text)
    remark = Column(Text)
    data = Column(LargeBinary)



### ManualLog
class ManualLog(Model):
    '''
    类介绍：

        这是一个日志信息数据模型类
    '''

    __tablename__='ManualLog'
    index = Column(Integer, autoincrement=True, primary_key=True)
    msg = Column(Text)
    levelname = Column(Text)
    filename = Column(Text)
    module = Column(Text)
    lineno = Column(Integer)
    time = Column(Text)



#######################################################################################
#######################################################################################


