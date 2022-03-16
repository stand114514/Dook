from sre_parse import State
import requests 
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment

def get_acg():
    url='https://api.sunweihu.com/api/sjbz/api.php?method=mobile&lx=dongman'
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c

def get_acghead():
    url='https://api.yimian.xyz/img?type=head'
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    d = res.url
    return d

acg = on_keyword({'acg'}, priority=3,block=False)
@acg.handle()
async def acg_(bot: Bot, event: Event):
    await acg.finish(message=MessageSegment.image(get_acg()))


acghead = on_keyword({'acghead'}, priority=2)
@acghead.handle()
async def acghead_(bot: Bot, event: Event): 
    await acghead.finish(message=MessageSegment.image(get_acghead())
    )


def get_setu():
    url='https://api.iyk0.com/cos'
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c

cos = on_keyword({'cos'}, priority=2)
@cos.handle()
async def cos_(bot: Bot, event: Event):         
    await cos.finish(message=MessageSegment.image(get_setu()))


    
    