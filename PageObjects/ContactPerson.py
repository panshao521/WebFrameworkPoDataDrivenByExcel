# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:26
Author:   panyuangao@foxmail.com
File:     ContactPerson.py
Describe: 添加联系人页面操作方法封装
"""
from Conf.ProjVar import conf_file_path
from Util.ReadConfig import read_ini_file_option
from Util.LocateElement import find_element

class ContactPerson():
    def __init__(self,driver):
        self.driver = driver

    #获得添加联系人的按钮
    def get_create_contact_person_button(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_contactPersonPage",
                                                         "contactPersonPage.createButton").split(">")
        create_contact_person_button = find_element(self.driver, locate_method, locate_exp)
        return  create_contact_person_button
    #获得联系人名字的网页对象
    def get_name(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_contactPersonPage",
                                                         "contactPersonPage.name").split(">")
        name = find_element(self.driver, locate_method, locate_exp)
        return name
    #获得练习人电子邮件地址的网页对象
    def get_email(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_contactPersonPage", "contactPersonPage.email").split(">")
        email = find_element(self.driver, locate_method, locate_exp)
        return email
    #获得电话号码的网页对象
    def get_phone(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path,  "126mail_contactPersonPage","contactPersonPage.phone").split(">")
        phone = find_element(self.driver, locate_method, locate_exp)
        return phone
    #获得备注字段的网页对象
    def get_other_info(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_contactPersonPage", "contactPersonPage.otherinfo").split(">")
        other_info = find_element(self.driver, locate_method, locate_exp)
        return other_info
    #获得确定按钮
    def get_confirm_button(self):
        locate_method, locate_exp = read_ini_file_option(conf_file_path, "126mail_contactPersonPage", "contactPersonPage.confirmButton").split(">")
        confirm_button = find_element(self.driver, locate_method, locate_exp)
        return confirm_button
    #点击新建联系人按钮
    def click_create_contact_person_button(self):
        create_contact_person_button = self.get_create_contact_person_button()
        create_contact_person_button.click()
        import time
        time.sleep(2)

    #在名字输入框中输入内容
    def input_name(self,name):
        name_box = self.get_name()
        if not name:
            return
        name_box.send_keys(name)
    #在电子邮件输入框中输入内容
    def input_email(self,email):
        email_box = self.get_email()
        if not email:
            return
        email_box.send_keys(email)
    #在电话号码输入框中输入内容
    def input_phone(self,phone):
        phone_box = self.get_phone()
        if not phone:
            return
        phone_box.send_keys(phone)
    #在备注信息中输入内容
    def input_other_info(self,info):
        info_box = self.get_other_info()
        if not info:
            return
        info_box.send_keys(info)
    #点击确定按钮
    def click_confirm_button(self):
        confirm_button = self.get_confirm_button()
        confirm_button.click()
        import time
        time.sleep(3)
