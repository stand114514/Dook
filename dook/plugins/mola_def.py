import re
import sqlite3
from PIL import Image,ImageDraw,ImageFont
import requests

dbfile='shuju\\data.db'
biao="mola表"#表的名字

def upnike(qq):  #获取QQ头像
    url='https://r.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?g_tk=1518561325&uins='+str(qq)
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
    nikename = requests.get(url,headers=headers)
            # nikename=nikename.text
    nikename=nikename.content
    nikename=nikename.decode('gbk')
            # print(nikename)
    nikename=re.findall(',".*",',str(nikename))
    nikename=nikename[0].replace(',','')
    return nikename

class acc_mola():
    def __init__(self, qq):
        self.qq=qq
        self.db=self.select()
        self.name=self.db[1]
        self.mola=self.db[2]
        self.day=self.db[3]
    def select(self):
        '''
        返回dblist
        '''
        select=sqlite3.connect(dbfile)
        cursor=select.cursor()
        db=cursor.execute(f"SELECT *from '{biao}' where qq={self.qq};").fetchone()#向数据库查询用户表数据
        select.commit()
        select.close()
        qq=self.qq
        if db==None:
            nikename=upnike(qq)
            sign=sqlite3.connect(dbfile)
            cursor=sign.cursor()
            cursor.execute(f"INSERT INTO '{biao}' (qq,name,mola,day) \
                  VALUES ({self.qq},{nikename}, 0, 0)")#创建记录
            sign.commit()
            sign.close()
            return self.qq,{nikename},0,0
        else:
            return db

    def info_account(self):
        '''
        返回用户信息
        db[0]:qq
        db[1]:coin
        db[2]:name
        '''
        return self.db
    def up_name(self,name):#更新name
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE '{biao}' set name={name}  where qq={self.qq}")#更新表单数据
        update.commit()
        update.close()

    def up_day(self,day):#更新day
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE '{biao}' set day={day} where qq={self.qq}")#更新表单数据
        update.commit()
        update.close()

    def up_mola(self,mola_1,mola_2):#充值mola
        if mola_2 == None:
            mola=0+mola_1
        if mola_2=='':
            mola=0+mola_1
        else:
            mola=mola_1+mola_2
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE '{biao}' set mola={mola} where qq={self.qq}")#更新表单数据
        update.commit()
        update.close()

    def un_mola(self,mola_1,mola_2):#减少mola
        '''
        mola1是要减少的摩拉
        mola2是现有的摩拉
        '''
        mola=mola_2-mola_1
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE '{biao}' set mola={mola} where qq={self.qq}")#更新表单数据
        update.commit()
        update.close()

def mopaihang(number):
        '''
    number是获取前多少位人
    返回的db是个嵌套的
    例如number=2
    那么db[0]=[榜一qq,coin,name]
        db[1]=[榜二qq,coin,name]
     '''
        select=sqlite3.connect(dbfile)
        cursor=select.cursor()
        db=cursor.execute(f"select * from '{biao}'  order by mola desc limit 0,{number};").fetchall()  #向数据库查询用户表数据
        select.commit()
        select.close()
        return db

def molapaihang(msg,nsg):
    image = Image.new(mode="RGB",size=(580,980),color="white") #色彩通道，大小，颜色
    draw = ImageDraw.Draw(image)  #绘制
    arial_1 = ImageFont.truetype('fonts\\方正像素14.ttf',20) #字体路径
    draw.text((15,15),'-----------------------摩拉榜(1~21)--------------------',font =arial_1, fill='black')
    draw.text((15,45),msg,font =arial_1, fill='black') #fill为字体颜色
    draw.text((375,45),nsg,font =arial_1, fill='black') #fill为字体颜色
    image.save('./image/mola.png')