#-*-coding:utf-8-*-
import time
import requests
import win32api
import win32con

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command
from pymouse import PyMouse
from pykeyboard import PyKeyboard



driver = webdriver.Chrome()

driver.get('http://www.attop.com/')
driver.add_cookie({'name':'JSESSIONID','value':''})
driver.add_cookie({'name':'dang_ticket','value':''})
driver.refresh()
time.sleep(1)
list1 = ['http://www.attop.com/wk/learn.htm?id=42&jid=1042',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1043',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1044',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1045',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1046',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1047',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1048',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1049',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1050',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1051',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1052',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1053',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1054',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1055',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1057',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1058',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1059',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1060',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1061',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1062',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1063',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1064',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1065',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1066',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1067',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1068',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1069',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1070',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1071',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1072',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1073',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1074',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1075',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1076',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1077',\
'http://www.attop.com/wk/learn.htm?id=42&jid=1085']

x = -1
n = 0
while n < 37:
    x = x+1
    n = n+1
    driver.get(list1[x])
    time.sleep(1)
    win32api.keybd_event(17,0,0,0)      # Control
    win32api.keybd_event(16,0,0,0)      # Shift
    win32api.keybd_event(74,0,0,0)      # J
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键
    win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(74,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1)
    win32api.keybd_event(17,0,0,0)      # Control
    win32api.keybd_event(86,0,0,0)      # V
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(13,0,0,0)     #ENTER
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(15)
    win32api.keybd_event(17,0,0,0)      # Control
    win32api.keybd_event(16,0,0,0)      # Shift
    win32api.keybd_event(74,0,0,0)      # J
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键
    win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(74,0,win32con.KEYEVENTF_KEYUP,0)
    






















