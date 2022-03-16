import json
import random
import sqlite3
import time
dbfile='shuju\\data.db'#db绝对路径
biao="redbag"#表的名字

class acc_redbag():
    def __init__(self, qq):
        self.qq=qq
        self.db=self.select()
        self.size=self.db[1]  #大小
        self.num=self.db[2]   #个数
        self.qqed=self.db[3]  #已领QQ
        self.nums=self.db[4]  #总数
        self.time=self.db[5]  #时间戳
    def select(self):
        '''
        返回dblist
        '''
        times=int(time.time())
        select=sqlite3.connect(dbfile)
        cursor=select.cursor()
        db=cursor.execute(f"SELECT *from '{biao}' where qq={self.qq};").fetchone()#向数据库查询用户表数据
        select.commit()
        select.close()
        if db==None:
            sign=sqlite3.connect(dbfile)
            cursor=sign.cursor()
            cursor.execute(f"INSERT INTO '{biao}' (qq,size,num,qqed,nums,time) \
                  VALUES ({self.qq},  0, 0, 0, 0, {times})")#创建记录
            sign.commit()   
            sign.close()
            return self.qq,0,0,0,0,times
        else:  
            return db
    
    def info_account(self):
        '''
        返回用户信息
        db[0]:qq
        db[1]:大小
        db[2]:数量
        '''
        return self.db
        
    def up_size(self,size): 
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE '{biao}' set size={size} where qq={self.qq}")#更新大小
        update.commit()
        update.close()
    
    def up_tim(self,tim): 
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE '{biao}' set time={tim} where qq={self.qq}")#更新大小
        update.commit()
        update.close()

    def un_num(self,num1):#更新剩余个数
        '''
        num1是现存个数
        '''
        num=num1-1
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE '{biao}' set num={num} where qq={self.qq}")
        update.commit()
        update.close()

    def up_qq(self,qq1,qq2):#更新已领QQ
        '''
        qq1是数据库的
        qq2是领取人的
        '''
        qqed='"'+qq1+str(qq2)+'"'
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE '{biao}' set qqed={qqed} where qq={self.qq}")
        update.commit()
        update.close()
    
    def send_red(self,size,num): #发红包函数
        '''
    size 是包的大小
    num 是包的数量
    '''
        sui=[]  #用于存储随机数
        nu=0
        for i in range(num):
           numm=random.randint(1,10)
           sui.append(numm)
           nu=nu+numm
        
        mo=[]  #存储每个包的大小
        for res in range(num):
            mola=int(sui[res]/nu*size)  #计算大小
            file1 =open("shuju\\redbag.json", 'w')
    # mo[res]=mola
            mo.append(mola)
            file1.write(json.dumps(mo)) #列表写入json
            file1.close()
            res+=1

        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE '{biao}' set size={size} where qq={self.qq}")#更新大小
        cursor.execute(f"UPDATE '{biao}' set num={num} where qq={self.qq}")#更新个数
        cursor.execute(f"UPDATE '{biao}' set qqed='' where qq={self.qq}")#更新qq
        cursor.execute(f"UPDATE '{biao}' set nums={num} where qq={self.qq}")#更新总个数
        update.commit()
        update.close()
