import random
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from .mola_def import *
import re
zb=on_command("同归于尽",priority=1)
@zb.handle()
async def hand(bot: Bot, event: Event):   
    x=event.get_session_id() #获取会话
    rea = x.split('_')
    x=rea.pop(1) #群号
    qq_2=event.get_user_id()
    try:
        qq=re.findall("qq=[0-9]*",str(event.get_session_id)) 
        qq_1=qq[0].replace("qq=",'') #对方
    
        acc_1=acc_mola(qq_1)
        acc_2=acc_mola(qq_2)
        na_1=acc_1.select()[1]
        na_2=acc_2.select()[1]

        bei=random.randint(1,4)
        try:
            try:
                if qq_1==qq_2:
                    await zb.finish(na_2+'，你想自爆吗？')
                else:
                    await bot.call_api('set_group_ban',user_id=qq_1,group_id=x,duration=60*bei)
                    await zb.send(na_2+"，你对 "+na_1+' 发动了【同归于尽】\n造成 '+str(bei)+' 倍伤害')
            except:
                await zb.finish('无法禁言'+na_1)                
            await bot.call_api('set_group_ban',user_id=qq_2,group_id=x,duration=60)
        except:
            # await bot.call_api('set_group_ban',user_id=qq_1,group_id=x,duration=60)
            await zb.finish('无法禁言 '+na_2)
    except IndexError as bb:
        await zb.send("找不到你要迫害的对象(请正确@)\n"+str(bb),at_sender=True) 
        try:
            await bot.call_api('set_group_ban',user_id=qq_2,group_id=x,duration=60) 
        except:
            await zb.finish('无权限')
