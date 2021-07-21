# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:24
Author:   panyuangao@foxmail.com
File:     HomePage.py
Describe: 登录126邮箱后，主页操作方法封装
"""
from Conf.ProjVar import conf_file_path
from Util.ReadConfig import read_ini_file_option
from Util.LocateElement import find_element

class HomePage():
    def __init__(self,driver):
        self.driver  = driver
        if "main.jsp" not in driver.current_url:
            print("此页面未处于登录状态后的首页")

    def get_address_link(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_homePage","homePage.addressLink").split(">")
        address_link = find_element(self.driver, locate_method, locate_exp)
        return address_link

    def click_address_link(self):
        address_link = self.get_address_link()
        address_link.click()
        import time
        time.sleep(4)
