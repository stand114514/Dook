from .mola_def import *
import re
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Event,Bot

name1=on_command('以后叫我',priority=2)
@name1.handle()
async def name_(bot:Bot,event:Event):
    qq_1=event.get_user_id()
    a=str(event.get_message())
    ab=a.replace('以后叫我','')
    if len(ab) > 12:
        await name1.finish('这么长怎么可能有人记得住啊...')
    else:
        a='"'+ab+'"'
        name=acc_mola(qq_1)
        name.up_name(a)
        await name1.finish('那dook以后就叫你'+ab+'了')

name2=on_command('我是谁',priority=2)
@name2.handle()
async def name_(bot:Bot,event:Event):
    qq_1=event.get_user_id()
    name=acc_mola(qq_1)
    db=name.select()
    await name2.finish('你是'+db[1]+'啊，人家才没有忘呢~哼哼')

name3=on_command('他是谁',priority=2)
@name3.handle()
async def name_(bot:Bot,event:Event):
    qq=re.findall("qq=[0-9]*",str(event.get_session_id))
    qq_1=qq[0].replace("qq=",'')
    name=acc_mola(qq_1)
    db=name.select()
    await name3.finish('他是'+db[1]+'啊，这么快你就忘了？')

upname = on_command("更新名字",priority=2)
@upname.handle()
async def handle_first_receive(bot: Bot, event: Event):
    if event.get_user_id() != '1687771866': #管理员qq
        await upname.finish('你没有权限！嘿嘿~')
    else:
        global qq_2
        qq_2=re.findall("qq=[0-9]*",str(event.get_session_id))
        qq_2=qq_2[0].replace("qq=",'')

@upname.got("name",prompt="请输入更新的昵称")
async def handle_first_receive(bot: Bot, event: Event):
   name_1=str(event.get_message())
   name_1='"'+name_1+'"'
   name=acc_mola(qq_2)
   name.up_name(name_1)
   await upname.finish('那他以后就叫'+name_1+'好了~')
