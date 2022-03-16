import json
import requests
from nonebot.plugin import on_message,on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from .mola_def import acc_mola

#网址：https://api.ownthink.com/
# userid='pP0ZhBEs'
# appid = '109b652219dcf142df3eb12e9e5f650c'
url = 'https://api.ownthink.com/bot?appid=109b652219dcf142df3eb12e9e5f650c&userid=pP0ZhBEs&spoken='

async def get_n(text):
    try:
        r = requests.post(url=url+text)
        r=r.text
        r = json.loads(r)
        message = r['data']['info']['text']
        return message
    except KeyError:
        return '这个问题好头疼呀，问点别的叭'

tuling = on_message(priority=4) # permission= PRIVATE
@tuling.handle()
async def cheatt_(bot:Bot,event:Event):
    qq_1=event.get_user_id()
    name=acc_mola(qq_1)
    db=name.select()
    if ('dook' or 'Dook') in str(event.get_message()):    
        mysay = event.get_message()
        mysay = await get_n(str(mysay))
        await tuling.finish(message=db[1]+'，'+mysay)

    elif event.is_tome():
        mysay = event.get_message()
        mysay = await get_n(str(mysay))   
        await tuling.finish(db[1]+'，'+mysay)
            #at_sender=True

gongneng=on_command('功能',priority=1)
@gongneng.handle()
async def gongneng_(bot:Bot,event:Event):
    await gongneng.finish('当前功能有：\n—\n-图片搜索\n-昵称操作\n-摩拉操作\n-戳一戳\n-语音包\n-二次元\n-图片制作\n-同归于尽@对方(需要管理员权限)')

mola=on_command('摩拉操作',priority=1)
@mola.handle()
async def mola_(bot:Bot,event:Event):
    await mola.finish('摩拉操作支持：\n—\n-我的摩拉\n-他的摩拉@对方\n-转账@对方\n-打劫@对方或打劫QQ号\n-签到\n-摩拉榜\n-发红包\n-充值摩拉@对方（管理员）')

name=on_command('昵称操作',priority=1)
@name.handle()
async def name_(bot:Bot,event:Event):
    await name.finish('昵称操作支持：\n—\n-我是谁\n-他是谁@对方\n-以后叫我xxx\n-更新名字@对方（管理员）')

chuo=on_command('戳一戳',priority=1)
@chuo.handle()
async def chuo_(bot:Bot,event:Event):
    await chuo.finish('关于戳一戳：\n—\n-戳我\n-戳@对方\n-自己戳自己\n-特殊效果（管理员戳机器人，管理员自戳）')

soutu=on_command('图片搜索',priority=1)
@soutu.handle()
async def soutu_(bot:Bot,event:Event):
    await soutu.finish('图片搜索：\n—\n-搜图 关键词\n-bing搜图 关键词\n(搜图是百度搜图，bing搜图是微软必应搜图)')

yuying=on_command('语音包',priority=1)
@yuying.handle()
async def yuying_(bot:Bot,event:Event):
    await yuying.finish('当前语音包：\n—\n-鸡汤来咯\n-哥谭噩梦(发送 焯)\n-奥力给')

acg=on_command('二次元',priority=1)
@acg.handle()
async def acg_(bot:Bot,event:Event):
    await acg.finish('二次元图片：\n—\n-随机图(发送 acg)\n-头像(发送 acghead)\n-cos图(发送 cos)')    

ttu=on_command('图片制作',priority=1)
@ttu.handle()
async def ttu_(bot:Bot,event:Event):
    await ttu.finish('图片制作：\n—\n-ph风格图(发送ph 文字 文字)\n-恶搞新闻')    