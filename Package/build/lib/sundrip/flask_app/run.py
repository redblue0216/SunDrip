# -*- coding: utf-8 -*-
# author:shihua
# designer:shihua
# coder:shihua
# 这是一个flask-app的运行管理类
"""
模块介绍
-------

这是一个flask-app的运行类

设计模式：

    无

关键点：    

    （1）无

主要功能：            

    （1）为flask-app提供运行管理
                                                     
使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from app import app
import yaml
# import sundrip as sdp



####### 配置管理 ############################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）为flask-app提供配置功能                                           ###
#############################################################################



####### 运行管理 ###################################################################
###################################################################################



### 从配置文件中获取具体配置信息
# sundrip_package_path = sdp.__file__.replace('__init__.py','') ### 打包后取消注释
sundrip_package_path = '../'
sundrip_config_file = open('{}sundrip_config.yaml'.format(sundrip_package_path),encoding='UTF-8')
sundrip_config_yaml = yaml.load(sundrip_config_file,Loader=yaml.FullLoader)
dirp_webui_port = sundrip_config_yaml['sundrip_webui_port']
sundrip_web_host = sundrip_config_yaml['sundrip_webui_host']
app.run(host=sundrip_web_host, port=dirp_webui_port, debug=True)



#######################################################################################
#######################################################################################


