from nonebot.adapters.onebot.v11 import Bot,Message, GroupDecreaseNoticeEvent,GroupIncreaseNoticeEvent
from nonebot import on_notice
from .mola_def import acc_mola

welcom = on_notice()
# 友入群
@welcom.handle()  # 监听 welcom
async def h_r(bot: Bot, event: GroupIncreaseNoticeEvent):  # event: GroupIncreaseNoticeEvent  群成员增加事件
    x=event.get_session_id()
    re = x.split('_')
    x=re.pop(1)
    
    user = event.get_user_id()  # 取取新员的id
    name=acc_mola(user)
    name=name.select()[1]
    at_ = "本次通过祈愿召唤者：\n【"+name+"】"  #将任意字符转化字符串存入{}
    msg = at_ + '\n[CQ:at,qq={}]欢迎勇者大人进入本群！'.format(user)
    jin = Message(msg)
        # print(at_)
    await welcom.finish(message=Message(f'{jin}'))  # 送

                                        # 友友退群
@welcom.handle()
async def h_r(bot: Bot, event: GroupDecreaseNoticeEvent):  # event: GroupDecreaseNoticeEvent  群成员减少事件
    user = event.get_user_id()  # 新的id
    name=acc_mola(user)
    name=(name.select())[1]
    at_ = "[CQ:at,qq={}]".format(user)  
    msg =  at_ + '\n勇者【'+name+'】离开了，大家快出来送别吧！'
    chu = Message(msg)
    await welcom.finish(message=Message(f'{chu}'))
    # print(at_)
