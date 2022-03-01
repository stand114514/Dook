import re
from nonebot.plugin import on_notice,on_command
from nonebot.adapters.onebot.v11 import Bot, Event,PokeNotifyEvent,Message
from .mola_def import acc_mola
import random

acc = ['那...那里...那里不能戳...绝对...','嘤嘤嘤,好疼','你再戳，我就把你的作案工具没收了，哼哼~','别戳了别戳啦...要坏掉了...',
   '要变得奇怪了…','戳人什么的...真是讨厌','啊我错了我错了，别戳了','属实给我戳傻了..','手感怎么样','戳够了吗？该学习了','戳什么戳，没戳过吗',
   '你用左手戳的还是右手戳的？','哼哼哼啊啊啊啊啊','死变态，别碰我','你再戳一个试试！','你能rick roll吗？','哼，爬去学习']
master=123 #主人qq

poke=on_notice()
@poke.handle()
async def _(bot:Bot,event:Event):
    if isinstance(event,PokeNotifyEvent) :
        abc=event.get_session_id
        qq=re.findall(r"target_id=\d*",str(abc))
        qq=int(qq[0].replace('target_id=',''))
        qqid=event.get_user_id()
        if event.is_tome() :
            if qqid==str(master):
                await poke.finish('最喜欢被主人戳了')
            else:
                l = len(acc)
                k = random.randint(0,l-1)
                name=acc_mola(qqid)
                db=name.select()
                await poke.finish(message=db[1]+'，'+acc[k])
                # at_sender=True

        elif qqid == qq == master:
                name=acc_mola(qq)
                db=name.select()
                await poke.finish(db[1]+'主人在玩什么呢...')
        elif qq ==str(master):
            name=acc_mola(qqid)
            db=name.select()
            await poke.finish(db[1]+'不要戳我主人',)
        elif qqid == qq:
                await poke.finish('主人你看，有个笨蛋自己戳自己'
            )    


chuo=on_command('戳',priority=2)
@chuo.handle()
async def chuo_(bot:Bot,event:Event):
    try:
        args = str(event.get_message()).strip() #对方qq
        args=args.split('qq=')
        arg=args[1].split(']')#返回qq
        name=acc_mola(int(arg[0]))
        db=name.select()
        await chuo.send('好，戳'+db[1])
        await chuo.finish(Message('[CQ:poke,qq='+arg[0]+']'))    
    except IndexError as bb:
        await chuo.finish('你想戳谁？\n'+str(bb),at_sender=True)


chuome=on_command('戳我',priority=2)
@chuome.handle()
async def chuome_(bot:Bot,event:Event):
    name=acc_mola(event.get_user_id())
    db=name.select()
    await chuome.send(db[1]+'真是的，居然要求人家做这种事')
    await chuome.finish(Message('[CQ:poke,qq='+event.get_user_id()+']'))