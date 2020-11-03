from selenium import webdriver
import time
import os
import subprocess
import base64
from lxml import etree
from win32com.client import Dispatch
driver = webdriver.Chrome()
profile_dir = r"C:\Users\ThinkPad\AppData\Local\Google\Chrome\User Data"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))
driver = webdriver.Chrome(chrome_options=chrome_options) 
#thunder_path = 'E:\Thunder\Program\Thunder.exe'

# def Url2Thunder(url):
#     url = 'AA' + url + 'ZZ'
#     url = base64.b64encode(url.encode('ascii'))
#     url = b'thunder://' + url
#     thunder_url = url.decode()
#     return thunder_url
#
#
# def download_with_thunder(file_url):
#     thunder_url = Url2Thunder(file_url)
    #subprocess.call([thunder_path, thunder_url])

thunder = Dispatch("ThunderAgent.Agent64.1")



driver.get('https://www.pixiv.net/ranking.php?mode=daily&content=illust')
#time.sleep(30)
page = driver.page_source
#print(page)
page = driver.page_source
dom = etree.HTML(page)
ids = dom.xpath('//img[contains(@src,"")]//@src')
#print(ids)
num = 0
file = open('tempdata.txt','w')
for id in ids:
    if ('240x480' in id) == True:
        #print(id)
        num = num + 1
        data_id = id.strip('https://i.pximg.net/c/240x480/img-maste')
        data_id = data_id.strip('r/')
        #print(data_id)
        data_id = data_id.strip('master1200.jpg')
        data_id = data_id.strip('_')
        # print(data_id)
        img_url1 = 'https://i.pximg.net/img-original/' + data_id + '.png'
        img_url2 = 'https://i.pximg.net/img-original/' + data_id + '.jpg'
        thunder.AddTask(img_url1)
        thunder.AddTask(img_url2)
        #download_with_thunder(img_url1)
        #file.write(img_url1)
        #file.write('\n')
        #download_with_thunder(img_url2)
        #file.write(img_url2)
        #file.write('\n')
        #time.sleep(1)
        #print(img_url1)
        #print(img_url2)
        #https://i.pximg.net/c/240x480/img-master/img/2020/10/23/00/30/00/85177342_p0_master1200.jpg
        #https://i.pximg.net/img-original/img/2020/10/23/00/30/00/85177342_p0.jpg
print(num)
thunder.CommitTasks()
# file.close()
# datas = open("tempdata.txt","r")
# for data in datas:
#     if data =='\n':
#         pass
#     else:
#         download_with_thunder(data)
# datas.close()
# if os.path.exists("tempdata.txt"):
#     os.remove("tempdata.txt")