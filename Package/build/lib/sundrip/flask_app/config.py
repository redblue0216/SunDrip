# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个flask-app的配置类，主要包括后端数据库和前端主题相关配置
"""
模块介绍
-------

这是一个flask-app的配置类，主要包括后端数据库和前端主题相关配置

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）为flask-app提供配置功能
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import os
import yaml
# import sundrip as sdp



####### 配置管理 ############################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）为flask-app提供配置功能                                           ###
############################################################################



####### 配置整理 #######################################################################
#######################################################################################



### 从配置文件中获取具体配置信息
# sundrip_package_path = sdp.__file__.replace('__init__.py','') ### 打包后取消注释
sundrip_package_path = '../'
sundrip_config_file = open('{}sundrip_config.yaml'.format(sundrip_package_path),encoding='UTF-8')
sundrip_config_yaml = yaml.load(sundrip_config_file,Loader=yaml.FullLoader)
sundrip_sqlite_path = sundrip_config_yaml['sqlite_db_uri']



### 基础配置
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

OPENID_PROVIDERS = [
    {"name": "Google", "url": "https://www.google.com/accounts/o8/id"},
    {"name": "Yahoo", "url": "https://me.yahoo.com"},
    {"name": "AOL", "url": "http://openid.aol.com/<username>"},
    {"name": "Flickr", "url": "http://www.flickr.com/<username>"},
    {"name": "MyOpenID", "url": "https://www.myopenid.com"},
]

# SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,sundrip_sqlite_path)
SQLALCHEMY_DATABASE_URI = sundrip_sqlite_path
# SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
                    
BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_FOLDER = "translations"
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "es": {"flag": "es", "name": "Spanish"},
    "de": {"flag": "de", "name": "German"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ru": {"flag": "ru", "name": "Russian"},
}

### 主题配置
# ------------------------------
# GLOBALS FOR GENERAL APP's
# ------------------------------
UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_URL = "/static/uploads/"
AUTH_TYPE = 1
# AUTH_LDAP_SERVER = "ldap://dc.domain.net"
# AUTH_LDAP_USE_TLS = False
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"
APP_NAME = "sundrip"# "F.A.B. Example"
APP_THEME = ""  # default
# APP_THEME = "cerulean.css"      # COOL
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"       # COOL
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
# APP_THEME = "slate.css"          # COOL
# APP_THEME = "spacelab.css"      # NICE
# APP_THEME = "united.css"



##############################################################################################
##############################################################################################


