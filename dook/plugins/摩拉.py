import random
import re

from importlib_metadata import os
from .mola_def import *
from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Event,Bot,Message,MessageSegment

up = on_command("充值摩拉",priority=2)

@up.handle()
async def handle_first_receive(bot: Bot, event: Event):
    global qq
    qq=re.findall("qq=[0-9]*",str(event.get_session_id))
    qq=qq[0].replace("qq=",'')
    if event.get_user_id() != '123': #管理员qq
        await up.finish('你没有权限修改数据库！')

@up.got("coin",prompt="请输入数量")
async def handle_first_receive(bot: Bot, event: Event):    
    mola=acc_mola(qq)
    mola_2=(mola.select())[2]
    zhi=str(event.get_message())
    mola.up_mola(int(zhi),mola_2)
    db=mola.select()
    await up.finish('已为 '+db[1]+' 充值 '+zhi+' 摩拉')

mola=on_command('我的摩拉',priority=1)
@mola.handle()
async def mola_(event:Event,bot:Bot):
    qq=event.get_user_id()
    db=acc_mola(qq).select()
    if db[2] == 0 :
        await mola.finish(db[1]+'的口袋空空，签到了再来罢')
    else:
        await mola.finish(db[1]+'你有 '+str(db[3])+' 摩拉')


mola_1=on_command('他的摩拉',priority=1)
@mola_1.handle()
async def mola_1(event:Event,bot:Bot):
    qq=re.findall("qq=[0-9]*",str(event.get_session_id))
    qq=qq[0].replace("qq=",'')
    db=acc_mola(qq).select()
    if db[2] == None :
        await mola.finish('这个 '+db[1]+' 囊中羞涩呢！')
    else:
        await mola.finish('【'+db[1]+'】有 '+str(db[2])+' 摩拉')

pk=on_command('打劫',priority=2)
@pk.handle()
async def pk1(bot:Bot,event:Event):
    try:
        qq=re.findall("qq=[0-9]*",str(event.get_session_id)) 
        qq_1=qq[0].replace("qq=",'') #对方（被打劫）
        qq_2=event.get_user_id()
        if qq_1==qq_2:
            await pk.finish('自己打劫自己？')
        else:
            acc_1=acc_mola(qq_1)
            acc_2=acc_mola(qq_2)
            db_1=acc_1.select() #对方数据
            molaret=random.randint(1,10)
            mola_2=int(db_1[2]*molaret/100)
            if db_1[2]>mola_2: #如果对方禁得起扣
                ret_=random.randint(0,100)
                if ret_ <=50 :
                    shi=random.randint(10,100)/1000 #凭空损失的千分比                
                    mola_1=mola_2-int(mola_2*shi) #自己得到的
                    db_2=acc_2.select() #自己数据
                    acc_1.un_mola(mola_2,db_1[2]) #对方扣
                    acc_2.up_mola(mola_1,db_2[2]) #自己加
                    await pk.send(db_2[1]+'，你打劫了【'+db_1[1]+'】\n[在战斗过程中，对方失去 '+str(mola_2)+' 摩拉，你获得了 '+str(mola_1)+' 对方('+str(molaret)+'%)的摩拉]')
                else :
                    db_2=acc_2.select() #自己数据
                    mola_21=int(db_2[3]*molaret/100)
                    acc_1.up_mola(mola_21,db_1[3]) #对方加
                    acc_2.un_mola(mola_21,db_2[3]) #自己扣
                    await pk.send(db_2[1]+'，你打劫了【'+db_1[1]+'】\n[打劫失败，你被反抢了 '+str(mola_21)+' 摩拉]') 
            else:
                await pk.finish(db_1[1]+'已经快揭不开锅了..')
    except IndexError as bb:
        strr=str(event.get_message())
        strr=strr.split('劫')
        qq1=int(strr[1])
        qq2=event.get_user_id()
        if qq1==qq2:
            await pk.finish('自己打劫自己？')
        else:
            # try:
                acc1=acc_mola(qq1)
                acc2=acc_mola(qq2)
                db_1=acc1.select() #对方数据
                molaret=random.randint(1,10)
                mola_2=int(db_1[2]*molaret/100)
                if db_1[2]>mola_2: #如果对方禁得起扣
                    ret_=random.randint(0,100)
                    if ret_ <=50 : #成功概率50
                        shi=random.randint(10,100)/1000 #凭空损失的千分比                
                        mola_1=mola_2-int(mola_2*shi) #自己得到的
                        db_2=acc2.select() #自己数据
                        acc1.un_mola(mola_2,db_1[2]) #对方扣
                        acc2.up_mola(mola_1,db_2[2]) #自己加
                        await pk.finish(db_2[1]+'，你打劫了【'+db_1[1]+'】\n[在战斗过程中，对方失去 '+str(mola_2)+' 摩拉，你获得了 '+str(mola_1)+' 对方('+str(molaret)+'%)的摩拉]')
                    else :
                        db_2=acc2.select() #自己数据
                        mola_21=int(db_2[2]*molaret/100)
                        acc1.up_mola(mola_21,db_1[2]) #对方加
                        acc2.un_mola(mola_21,db_2[2]) #自己扣
                        await pk.finish(db_2[1]+'，你打劫了【'+db_1[1]+'】\n[打劫失败，你被反抢了 '+str(mola_21)+' 摩拉]') 
            # except:
            #     await pk.finish('打劫谁？')

bang=on_command('摩拉榜',priority=1)
@bang.handle()
async def bang(event:Event,bot:Bot):
    a=mopaihang(21)
    msg=""
    nsg=""
    nu=1
    for i in a:
        msg+=str(nu)+'.昵称：'+str(i[1])+'\n-—————————————————\n'
        nsg+='摩拉:'+str(i[2])+'\n—————————-\n'
        nu+=1
    molapaihang(msg,nsg)
    img = MessageSegment.image(file='file:///'+os.getcwd()+'\image\mola.png')
    await bot.send(event=event,message=Message(img))

zhuan = on_command("转账",priority=2)

@zhuan.handle()
async def handle_first_receive(bot: Bot, event: Event):
    global qq_Z
    qq_Z=re.findall("qq=[0-9]*",str(event.get_session_id))
    qq_Z=qq_Z[0].replace("qq=",'') #对方qq

@zhuan.got("数量",prompt="请输入转账数量")
async def handle_first_receive(bot: Bot, event: Event):    
    global zhuan_1,mola_11,mola_a
    zhuan_1=str(event.get_message())
    qq_1=event.get_user_id()
    mola_11=acc_mola(qq_1)
    mola_a=(mola_11.select())[2] #自己的摩拉
    if qq_1==qq_Z:        
        await zhuan.finish(mola_11[1]+'，不能自己给自己转账！')
    else:
        try:
            float(zhuan_1) #是不是数字
            if '.' in zhuan_1 : #判断是不是整数
                await zhuan.finish('你确定是整数吗？？？')
            elif '-' in zhuan_1:
                await zhuan.finish('负数？？？')
            else:
                if mola_a > int(zhuan_1) : #如果摩拉足够
                    return
                else :
                    await zhuan.finish('你没有这么多摩拉啦！真是的~')
        except ValueError :
            await zhuan.finish('你确定你输的是数字吗？？？')

@zhuan.got("是否",prompt="是否转账(是/否)")
async def handle_first_receive(bot: Bot, event: Event): 
    pan=str(event.get_message())
    if pan == '是':
        mola_2=acc_mola(qq_Z)
        mola_b=(mola_2.select()) #查对方的
        name=mola_b[1]
        mola_2.up_mola(int(zhuan_1),mola_b[2]) #给对方加
        mola_11.un_mola(int(zhuan_1),mola_a) #给自己减
        await zhuan.finish(' 已给 '+name+' 转账 '+zhuan_1+' 摩拉')
    elif pan == '否' :
        await zhuan.finish('已退出转账')
    else :
        await zhuan.finish('已退出转账')

chabang = on_command("查榜摩拉",priority=2)
@chabang.handle()
async def handle_first_receive(bot: Bot, event: Event):
    return

@chabang.got("摩拉榜",prompt="摩拉榜几？")
async def handle_first_receive(bot: Bot, event: Event): 
    pan=str(event.get_message())
    num=int(pan)
    a=mopaihang(num)[num-1]
    str_1='qq:'+str(a[0])+'\n昵称:'+a[1]+'\n摩拉:'+str(a[2])
    await chabang.finish(str_1)