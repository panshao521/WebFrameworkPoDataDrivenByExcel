# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:27
Author:   panyuangao@foxmail.com
File:     ProjVar.py
Describe: 项目常用变量，如各类项目路径及excel的列号
"""

import os
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#当前工程在硬盘上的绝对路径
proj_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(proj_dir_path)

#配置文件的绝对路径
conf_file_path = os.path.join(proj_dir_path,"Conf","ElementsRepository.ini")
# print(conf_file_path)

#浏览器驱动的位置
chrome_driver_path = "/usr/local/bin/chromedriver"
# ie_driver_path = "e:\\IEDriverServer"
# firefox_driver_path = "e:\\geckodriver"

#测试数据文件路径
test_data_file_path_126 = os.path.join(proj_dir_path,"TestData",'126邮箱联系人.xlsx')

#测试数据文件第一个登录sheet的列号设置
login_username_col_no = 1
login_passwd_col_no = 2
test_data_sheet_name_col_no = 3 # 数据表名称的列数
login_data_valid_col_no = 4
login_end_time_col_no = 5
login_test_result_col_no = 6

#取系人sheet数据中列号设置
contact_name_col_no = 1
contact_email_col_no = 2
contact_phone_col_no = 4
contact_info_col_no = 5
assert_word_col_no = 6
contact_data_valid_col_no = 7
test_end_time_col_no = 8
test_result_col_no = 9
pic_path_col_no = 10

#截图目录
pic_capture_dir = os.path.join(proj_dir_path,"ScreenCapture")


if __name__ == '__main__':
    print(test_data_file_path_126)
    print(conf_file_path)
