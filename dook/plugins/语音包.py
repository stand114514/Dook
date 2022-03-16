# -*- coding: utf-8 -*-
import random
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event,MessageSegment,Message
import os

a=['鸡汤来咯0','鸡汤来咯1','鸡汤来咯2','鸡汤来咯3','鸡汤来咯4','鸡汤来咯5',
   '鸡汤来咯6','鸡汤来咯7','鸡汤来咯8','鸡汤来咯9','鸡汤来咯10','鸡汤来咯11',
   '鸡汤来咯12','鸡汤来咯14','鸡汤来咯15','鸡汤来咯16','鸡汤来咯18','鸡汤来咯19',
   '鸡汤来咯20','鸡汤来咯21','鸡汤来咯22','鸡汤来咯23','鸡汤来咯24','鸡汤来咯25',
   '鸡汤来咯26','鸡汤来咯27','鸡汤来咯28','鸡汤来咯29','鸡汤来咯30','鸡汤来咯31']

b=['哥谭噩梦0','哥谭噩梦1','哥谭噩梦2','哥谭噩梦3']

jitang=on_command('鸡汤来咯',priority=1)
@jitang.handle()
async def jitang_(bot:Bot,event:Event):
    path_=os.getcwd()
    l = len(a)
    k = random.randint(0,l-1)    
    path_b=path_+'\\yuyin\\'+str(a[k])+'.mp3'
    mypath='file:///'+path_b
    print(mypath)
    sst = MessageSegment.record(file=str(mypath))
    await jitang.finish(message=Message(sst))


aoli=on_command('奥利给',priority=1)
@aoli.handle()
async def aoli_(bot:Bot,event:Event):
    path_=os.getcwd()
    path_a=path_+'\\yuyin\\奥利给.mp3'
    mypath='file:///'+path_a
    print(mypath)
    sst = MessageSegment.record(file=str(mypath))
    await aoli.finish(message=Message(sst))

chao=on_command('焯',priority=1)
@chao.handle()
async def chao_(bot:Bot,event:Event):
    path_=str(os.getcwd())
    l = len(b)
    k = random.randint(0,l-1)    
    ssh= b[k]
    path_=path_+'\\yuyin\\'+ssh+'.mp3'
    mypath='file:///'+path_
    print(mypath)
    sst = MessageSegment.record(file=str(mypath))
    await chao.finish(message=Message(sst))