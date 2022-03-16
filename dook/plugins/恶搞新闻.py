import os
import random
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event,Bot,Message,MessageSegment
from PIL import Image,ImageDraw,ImageFont
import urllib.request
import datetime
import json

lst=['江苏一男子和情人同居两年卷走15万，全部上交给自己老婆。',
'山东医疗队英雄父亲支援黄冈，儿子要求带特产回来，于是父亲带回黄冈密卷。',
'浙江一男子偷40多个奔驰车标想打一副银手镯，4s店这边回应说，车标是不锈钢的。',
'安徽男子出狱之后，再次盗窃被抓，希望法院重判，只为在监狱里学缝纫技术。',
'江苏一女子偷走30根香肠抱怨太硬，老板说他偷的是模型。',
'江西男子无证驾驶撞车之后，找人顶包，因为忘记自己是光头而露馅。',
'安徽六个人在宾馆赌博，设暗语:天王盖地虎，警察答:宝塔镇河妖。门竟然开了。',
'浙江一男子出狱之后，纹身:东山再起，听天由命。结果又犯事，警察说你纹身有错别字。',
'浙江一位妈妈接到女儿遭绑架诈骗电话被索要50万赎金，妈妈砍价砍到3万。',
'一南方人特意到东北体验“澡堂子文化”，被辽宁搓澡师傅搓到报警。',
'扬州两小伙自制催情药水并以身试药，暍完后药性发作',
'美国男子沉迷中国网络小说，成功戒掉可卡因',
'错把猴屁股当红灯，贵州女司机分神致两车追尾',
'男子点1只鸡吃出10个鸡爪，进厨房发现鸡还活着',
'杭州男子溜进派出所内偷马桶，称最危险的地方也最安全',
'泰国毒贩逼两只鸡吞1400粒冰毒，警方令其向鸡道歉',
'男子网恋“美女”转账40万，得知对方是男性后又转百万',
'小猪幸运从火场获救，半年后被做成香肠送给消防员',
'男子抢劫1元硬币买大白兔奶糖，获刑4年被罚1000元',
'只因不愿和熟人打招呼，西班牙一女子装瞎28年',
'为让儿子学会独立生活，父亲主动盗窃去坐牢',
'高三女孩不来例假去医院检查，检查发现自己是男的',
'毒贩老大被判死刑，五个小弟混进庭审现场送行齐被抓',
'女子不吃晚饭天天锻炼一斤没瘦，借酒消愁醉倒路边',
'东北小伙骑车回家过年，一个月后发现骑反了方向',
'煽扇除霾"专利初审通过：1500万人同时持雾霾扇就能把雾霾吹出北京',
'湖南女子发布谣言"政府发老婆"被拘 民警：真有人去领',
' 阿塞拜疆总统阿利耶夫任命自己的妻子阿利耶娃为副总统',
'粗心丈夫将妻子忘在服务区，妻子不知丈夫手机号',
'河南男子半年被骗10余次 骗子:实在想不出理由骗他了',
'男子围观居民楼火灾还吐槽，结果发现烧的是自己家',
'湖北男子误入传销窝点，因饭量过大遭强制遣返',
'中年男子为混入高校盗窃常敷面膜，落网后教育民警不懂保养',
'扬州阿姨网恋被骗60万，事后发现对方是女婿',
'英国野外生存节目收视不佳停播，参赛者不知情继续野外生活一年多',
'安徽男子撞伤老人逃逸，不料撞的是自己亲妈',
'泰国男子自夸有神力可刀枪不入，自刺一剑后再也没醒来',
'男子去年在高速停车摘李子被罚，今年徒步来摘再被逮',
'六名逃犯 KTV 中高唱“不要怕”：结果被警察一锅端',
'浙江民警帮助寻回宠物狗，派出所获赠"救我狗命"锦旗',
'湖南一小愉专愉学生用品，偷完试卷自己还做一遍',
'广东女子跳河轻生，身体太胖漂在水面沉不下去',
'广州破获跨国毒品大案，黑人毒贩凭肤色躲暗处警察狂找',
'男子跳江自杀发现江中有一条蛇，被吓得游回岸边',
'网恋少年少女遭家长反对，俩人用502将手粘一起',
'江苏一小偷蹭饭蹭到警察婚宴，周围坐的都是民警',
'朋友酒驾被查男子开车去帮忙，忘了自己也酒驾还没驾照',
'珠海女子走路玩手机被撞骨折，司机竟是自己老公',
'男子酒后步行见交警主动要吹酒精测试仪，被拒绝后开车来测',
'美国一男子欲自杀，拒绝交出手枪被警察击毙',
'女子实拉杆箱却收到登机牌，原是快递员嫌乱花钱替她退货',
'深圳警方询问嫌犯为何制假币 嫌犯：因为真币做不出来',
'毒贩视力不好交易毒品收到冥币，一怒之下报警',
'美发店营业员哭穷，杭州女子透支信用卡充值十三万',
'重庆陌生男女打麻将大打出手，民警调解后两人成为恋人',
]

def newss(qq):
    image_1=Image.open('image\新闻.png').convert('RGBA') 
    image_1=image_1.resize((800,500))  #改变大小尺寸
    draw = ImageDraw.Draw(image_1)  #绘制
    tim=(datetime.datetime.now()).strftime("%H:%M")  #当前时间

    arial_1 = ImageFont.truetype('fonts\SourceHanSansCNBold.otf',25) #字体路径
    draw.text((43,470),tim,font =arial_1, fill='white') #fill为字体颜色
    
    l = len(lst)
    k = random.randint(0,l-1)
    event=lst[k]

    arial_3 = ImageFont.truetype('fonts\SourceHanSansCN-Regular.otf',16) #字体路径
    draw.text((160,473),event,font =arial_3, fill='white')

    file1 =open("shuju\\news.json", 'r')
    js=file1.read()  #读取json数据
    js=json.loads(js)
    txt=js[qq+'txt']
    title=js[qq+'title']
    
    arial_1 = ImageFont.truetype('fonts\SourceHanSansCNBold.otf',25) 
    draw.text((167,383),txt,font =arial_1, fill='#F5F5F5') 

    arial_2 = ImageFont.truetype('fonts\SourceHanSansCNBold.otf',30)
    draw.text((167,423),title,font =arial_2, fill='yellow')


    image_2=Image.open('image\\qq.jpg').convert('RGBA')
    
    size=image_2.size
    s1=size[0]
    s2=size[1]
    a=size[0]/800  #宽
    # b=int(size[1]/500)  #高
    size=(s1/2-a*400,
          s2/2-a*250,
          s1/2+a*400,
          s2/2+a*250,)  #从中心取
    image_2=image_2.crop(size)  #裁剪尺寸
    
    size=(800,500)
    image_2=image_2.resize(size)#改变大小尺寸
    
    final = Image.alpha_composite(image_2, image_1)
    final = final.convert('RGB')
    final.save('.\\image\\news.jpg')

news = on_command("恶搞新闻",priority=2)

@news.handle()
async def handle_first_receive(bot: Bot, event: Event):
    return

@news.got("title",prompt="请输入标题文字")
async def handle_first_receive(bot: Bot, event: Event):    
    title=str(event.get_message())
    len_=len(title.encode('utf-8'))
    if len_ >= 51 :
        await news.finish('文字太长了')
    else:
        js={}
        qq=str(event.get_user_id())
        file1 =open("shuju\\news.json", 'w')
        js[qq+'title']=title
        file1.write(json.dumps(js))
        file1.close()

@news.got("txt",prompt="请输入内容")
async def handle_first_receive(bot: Bot, event: Event):  
    txt=str(event.get_message())
    len_=len(txt.encode('utf-8'))
    if len_ >= 51 :
        await news.finish('文字太长了')
    else:
        qq=str(event.get_user_id())
        file1 =open("shuju\\news.json", 'r')
        js=file1.read()  #读取json数据
        js=json.loads(js)  #将json转化为字典
        file1 =open("shuju\\news.json", 'w')
        js[qq+'txt']=txt  #字典的添加
        file1.write(json.dumps(js))
        file1.close()

@news.got("img",prompt="请发送要制作的图片")
async def handle_first_receive(bot: Bot, event: Event):  
    qq=str(event.get_user_id())
    url=str(event.get_message())
    url=(url.split(','))[2]
    url=url.replace('url=','')
    if ']' in url :
        url=url.replace(']','')
    print(url)
    urllib.request.urlretrieve(url, filename='image\\qq.jpg')
    newss(qq)
    tu=MessageSegment.image(file="file:///"+os.getcwd()+"\\image\\news.jpg")
    await news.finish(message=Message(tu))