import random
import urllib.request,urllib.parse
from urllib import parse
import re
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, Message,MessageSegment
'''
我乱写的，大佬看看就好
'''

sou1=on_command('bing搜图',priority=1) #使用方法：搜图xx，不用加空格
@sou1.handle()
async def sou1_(bot: Bot, event: Event):
    xinxi=str(event.get_message()) #获取消息转str
    xinx=xinxi.replace('bing搜图','')  #把搜图两个字换成空
    if xinx =='':
        await sou1.finish('内容呢？？？')
    else:
        msg=parse.quote(xinx)  #把搜图的对象转码
        url="https://cn.bing.com/images/search?q="+msg
        headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "cookie": "cookie",
        "sec-ch-ua": ' " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96" '}
        req=urllib.request.Request(url=url,headers=headers)  #发送请求
        response=urllib.request.urlopen(req)  #打开网页内容
        # try:
        abc=response.read().decode('utf-8')
        b = re.compile('htt[p|ps]://[\w][^;&]*jpg')  #正则
        ab=re.findall(b,abc)
        list_2=[]
        for i in ab:
            list_2.append(i)
        k=random.randint(0,len(list_2)-1)
        url_=list_2[k]
        print('链接:',url_)
        tu = MessageSegment.image(file=url_) #cq码
        await sou1.finish(message=Message(tu))
    # except:
    #     await sou1.finish('url错误，请再试一次')

sou2=on_command('搜图',priority=1)
@sou2.handle()
async def sou2_(bot: Bot, event: Event):
    xinxi=str(event.get_message()) #获取消息转str
    xinx=xinxi.replace('搜图','')  #把搜图两个字换成空
    # print(xinx)
    if xinx =='':
        await sou1.finish('内容呢？？？')
    else:
        msg=parse.quote(xinx)  #把搜图的对象转码
        url="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1643096234404_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&ctd=1643096234405%5E00_683X789&sid=&word="+msg
        headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Cookie": "cookie",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",  
        "Accept-Language": "zh-CN,zh;q=0.9"}
        req=urllib.request.Request(url=url,headers=headers)  #发送请求
        response=urllib.request.urlopen(req)  #打开网页内容
            # print(response)
        # try:
        abc=response.read().decode('utf-8')  #读取网页内容
        a = re.compile(r'[a-zA-z]+://gimg[^"\s]*.jpg')  
        list_1=re.findall(a,abc) #正则搜索图片链接，返回一个列表
        l = len(list_1)
        k = random.randint(0,l-1)
        url_=str(list_1[k]) #列表随机
        print('链接:',url_)
        tu = MessageSegment.image(file=url_) #cq码 
        await sou2.finish(message=Message(tu))

        # except UnicodeDecodeError as aaa:
        #     await sou2.finish('发生了错误,请使用 bing搜图\n'+str(aaa))