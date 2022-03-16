import time
from .redbag_def import *
from .mola_def import *
from nonebot.adapters.onebot.v11 import Event,Bot
from nonebot import on_command
import json
import asyncio

async def time_(cdd,qq,bot:Bot,event:Event):
    await asyncio.sleep(cdd)
    acc=acc_redbag(qq)
    db=acc.select()
    mola1=db[1]
    if mola1 == 0:
        return
    else:
       acc.send_red(0,0)  #清空红包大小个数已领取QQ
       acc=acc_mola(qq)
       db=acc.select()
       mola2=db[2]
       name=db[1]
       acc.up_mola(mola1,mola2) 
       await send_re.finish(name+'，你的红包过期了，剩余'+str(mola1)+'摩拉已返回账户',at_sender=True)

send_re=on_command('发红包',priority=1)
@send_re.handle()
async def send_(bot:Bot,event:Event):
    qq=event.get_user_id()
    acc=acc_redbag(qq)
    time1=acc.select()[5]  #发红包的时间戳
    time2=int(time.time())  #当前时间戳
    cdd=time2-time1
    print(cdd)
    if cdd < 180:
        cdd=180-cdd
        await send_re.send('你已经发过一个红包了，红包过期时会将剩余摩拉返回你的账户（你的红包还有'+str(cdd)+'秒过期）',at_sender=True)
        await time_(cdd,qq,bot,event)
    else:
        await send_re.send('发红包格式：大小 数量\n（数字，空格隔开）')

@send_re.got('redbag')  
async def send_(bot:Bot,event:Event):  
    qq=event.get_user_id()
    msg=str(event.get_message()).split(' ')
    print(msg)
    try:
        size=int(msg[0])
        num=int(msg[1])
        acc=acc_mola(qq)
        db=acc.select()
        mola=db[2]
        name=db[1]
        if mola >= int(size):
            tim=int(time.time())
            acc.un_mola(size,mola) #减少发出者的摩拉
            acc=acc_redbag(qq)
            acc.up_tim(tim)  #更新时间
            acc.send_red(size,num) #红包操作
            await send_re.send('【'+name+'】发送了'+str(num)+'个红包，总共 '+str(size)+' 摩拉\n(发送 抢红包@对方 以领取红包 红包180秒后消失)')
            await time_(180,qq,bot,event)
        else:
            await send_re.finish(name+' 你目前只有 '+str(mola)+' 摩拉，余额不足')
    except ValueError as aaa:
        await send_re.finish('请同时发送两个数字\n'+str(aaa))
# send_red(qq=1,size=10000,num=10)


rob_re=on_command('抢红包',priority=1)
@rob_re.handle()
async def rob_(bot:Bot,event:Event):
    try:
        qq_add=event.get_user_id()
        qq=re.findall("qq=[0-9]*",str(event.get_session_id))
        qq=qq[0].replace("qq=",'')
        acc=acc_redbag(qq)
        end=acc.select()
        size=end[1] #剩余大小
        num1=end[2] #剩余数量
        qqed=end[3] #已领QQ
        num2=end[4] #总数
        if num1 > 0:  #如果数量足够
            if str(qq_add) in qqed :
                await rob_re.finish('你已经领取过这个红包了')
            else:
                num_lst=num2-num1
                file1 =open("shuju\\redbag.json", 'r')
                file1=file1.read()
                file1=json.loads(file1)
                mola1=file1[num_lst]  #领取的摩拉
                
                acc.up_size(size-mola1) #更新大小
                acc.un_num(num1)  #更新剩余
                acc.up_qq(qqed,qq_add) #更新已领qq

                acc=acc_mola(qq_add)
                db=acc.select()
                mola2=db[2]
                name=db[1]
                acc.up_mola(mola1,mola2)  #给领取人增加
                await rob_re.finish(name+' 你领取了 '+str(mola1)+' 摩拉,原有 '+str(mola2))
        else:
            await rob_re.finish('红包不见了')
    except IndexError as bb:
        await rob_re.finish('请正确@\n'+str(bb))    

