import random
import time
from importlib_metadata import os
from .mola_def import *
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Event,Bot,Message,MessageSegment
import urllib.request

def qiandao_o(num,day,name,mola,qq):
    url='https://q1.qlogo.cn/g?b=qq&nk='+str(qq)+'&s=640'  #获取QQ头像
    urllib.request.urlretrieve(url, filename='image\qqhead.jpg')

    image_1=Image.open('image\签到'+str(num)+'.png').convert('RGB') 
    image_2=Image.open('image\qqhead.jpg').convert('RGB').convert('RGB') 

    size=(280,280)
    image_2=image_2.resize(size)
    box=(0,0,280,280)   
    image_1.paste(image_2,box)
    
    draw = ImageDraw.Draw(image_1)  #绘制
    arial_day = ImageFont.truetype('fonts\杨任东竹石体Semibold.ttf',20) #字体路径
    draw.text((165,295),str(day),font =arial_day, fill='black') #fill为字体颜色
    
    arial_2 = ImageFont.truetype('fonts\方正像素14.ttf',15)
    draw.text((10,335),'@'+name,font =arial_2, fill='#58585a')

    arial_2 = ImageFont.truetype('fonts\GenShinGothicBold.ttf',15)
    draw.text((45,356),'+'+str(mola),font =arial_2, fill='#020202')

    image_1.save('image\qiandao.png')

qiandao = on_command("签到",priority=2)
@qiandao.handle()
async def qiandap_(bot: Bot, event: Event):
    qqid=event.get_user_id()
    day=time.strftime("%Y-%m-%d")
    day_1=int(time.strftime("%Y%m%d"))
    acc=acc_mola(qqid)
    db=acc.select()
    day_2=db[3]
    name=db[1]
    mola=db[2]
    mola_add=random.randint(100,1000)
    num=random.randint(1,5)
    if day_2 == None : #为空则存
        acc.up_day(day_1) #存入日期
        acc.up_mola(mola_add,mola) #增加摩拉
        qiandao_o(num,day,name,mola_add,qqid)
        img = MessageSegment.image(file='file:///'+os.getcwd()+'\image\qiandao.png')
        await qiandao.finish(message=Message(img))
    else:
        if day_1==day_2: #同样的日期
           await qiandao.finish(name+" 你今天已经签过到了")
        else:
           acc.up_day(day_1) #存入日期
           acc.up_mola(mola_add,mola) #增加摩拉
           qiandao_o(num,day,name,mola_add,qqid)
           img = MessageSegment.image(file='file:///'+os.getcwd()+'\image\qiandao.png')
           await qiandao.finish(message=Message(img))