import requests
import json
import time
class node:
    flower=0 #1234
    num=0  # 234567891011121314, A14
    def __init__(self,f,n):
        self.flower=f
        self.num=n

poker_1,poker_2,poker_3=[],[],[]    # 扑克牌分堆
ans_1,ans_2,ans_3=[],[],[]  #暂时寄存排列答案
temp_1,temp_2,temp_3=[],[],[]   #存放完整排列答案
end_1,end_2,end_3=[],[],[]   #最终答案
s1,s2,s3=[],[],[]   #标记
tempp1,tempp2,tempp3=[],[],[]
pddun=[]
hua,number={},{}
submit_ans=[]
for i in range(0, 20):
    poker_1.append(node(0, 0))
    poker_2.append(node(0, 0))
    poker_3.append(node(0, 0))
    ans_1.append(node(0, 0))
    ans_2.append(node(0, 0))
    ans_3.append(node(0, 0))
    temp_1.append(node(0, 0))
    temp_2.append(node(0, 0))
    temp_3.append(node(0, 0))
    end_1.append(node(0, 0))
    end_2.append(node(0, 0))
    end_3.append(node(0, 0))
    s1.append(0)
    s2.append(0)
    s3.append(0)
    submit_ans.append("")
    pddun.append(node(0,0))

for i in range(0, 2 + 1):
    tempp1.append(node(0, 0))
    submit_ans.append("")
for i in range(0, 4 + 1):
    tempp2.append(node(0, 0))
for i in range(0, 4 + 1):
    tempp3.append(node(0, 0))

for i in range(0, 15 + 1):
    hua[i] = 0
    number[i] = 0  # 桶排初始化

global end_ans ,score
end_ans,score=0.0,0.0
global token,id,use



def init_cnt():
    for i in range(0, 15+1):
        hua[i] = 0
        number[i] = 0  # 桶排初始化

def takenum(x):
    return x.num

def shunzi3(start) :
    for i in range(start,start+2+1):
        if number[i] < 1:
            return 0
    return 1

def shunzi5(start):
    for i in range(start,start+4+1):
        if number[i] < 1:
            return 0
    return 1

def standof() :
    for i in range(1,3+1):# 前墩
        end_3[i] = ans_3[i]
    for i in range(1,5+1):#中墩
        end_2[i] = ans_2[i]
    for i in range(1,5+1): #后墩
        end_1[i] = ans_1[i]

def tempof() :
    for i in range(1,3+1):  #前墩
        ans_3[i] = temp_3[i]
    for i in range(1, 5 + 1):  # 中墩
        ans_2[i] = temp_2[i]
    for i in range(1, 5 + 1):  # 后墩
        ans_1[i] = temp_1[i]


def first():#前墩
    global score
    init_cnt()
    x = 1

    for i in range(0,2+1):
        tempp1[i]=ans_3[i+1]
    tempp1.sort(key=takenum) #  前墩牌组有序化

    for i in range(1,3+1):
        ans_3[i]=tempp1[i-1]


    for i in range(1,3+1):
        hua[ans_3[i].flower] +=1
        number[ans_3[i].num]+=1
    x = 1
    for i in range(1,4+1):
        if hua[i] == 3:
            if shunzi3(ans_3[1].num) == 1:
                k=(120.0+1.0 / 11.0 * (ans_3[1].num - 1))
                score += k
                return k # 3张同花顺
    x = 1
    for i in range(1,4+1):
        if hua[i] == 3:
            k=(70.0 +1.0/(1300+130+13)*((ans_3[3].num-1)*100+(ans_3[2].num-1)*10+(ans_3[1].num-1))*1.0 )
            score += k
            return k #3张同花
    x = 1
    if shunzi3(ans_3[1].num) == 1:
        k=(60.0  + 1.0/11.0*(ans_3[1].num-1)*1.0)
        score += k
        return k #3张顺子
    x = 1
    for i in range(3,0,-1):
        if number[ans_3[i].num] == 3:
            k=(50.0+1.0/13.0*(ans_3[1].num - 1)*1.0)
            score += k
            return k#三条
    x = 1
    for i in range(3,0,-1):
        if number[ans_3[i].num] == 1:
            x = ans_3[i].num
        if number[ans_3[i].num] == 2:
            k=(20.0+ 1.0/(130+13)*((ans_3[i].num - 1)*10+x-1)*1.0)
            score += k
            return k#单对
    x = 1
    k=10.0+1.0 / (1300.0 + 130.0 + 13.0)*((ans_3[3].num - 1) * 100 + (ans_3[2].num - 1) * 10 + (ans_3[1].num - 1))
    score += k
    return k #散牌

def second():
    global score
    init_cnt()

    for i in range(0, 4 + 1):
        tempp2[i] = ans_2[i + 1]

    tempp2.sort(key=takenum)  # 中墩牌组有序化
    for i in range(1, 5 + 1):
        ans_2[i] = tempp2[i - 1]

    x = 1
    for i in range(1,5+1):
        hua[ans_2[i].flower] +=1
        number[ans_2[i].num]+=1

    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            if shunzi5(ans_2[1].num) == 1:
                k= (150.0 + 1.0 / 9 * (ans_2[1].num - 1)) * 1.0
                score += k# 14 13 12 11 10
                return k # 同花顺

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 4:
            k=(120.0+ 1.0/(130+13)*((ans_2[i].num - 1)*10))*1.0
            score += k
            return k#炸弹

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5,0,-1):
                if number[ans_2[j].num] == 2:
                    k=(90.0 + 1.0 / (130 + 13)*((x - 1) * 10 + ans_2[j].num - 1))*1.0
                    score += k
                    return k#葫芦
    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            k=(70.0 + 1.0 / (130000 + 13000 + 1300+130+13)*((ans_2[5].num-1)*10000+(ans_2[4].num - 1)*1000 + (ans_2[3].num - 1) * 100 + (ans_2[2].num - 1) * 10 + (ans_2[1].num - 1)))*1.0
            score +=k
            return k#同花

    x = 1
    if shunzi5(ans_2[1].num) == 1 :
        k=(60.0 + 1.0/9*(ans_2[1].num - 1)*1.0)
        score += k
        return k#5张顺子

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5,0,-1):
                if number[ans_2[j].num] == 1:
                    k=(50.0 + 1.0 / (1300+130+13) * ((x-1) * 100))
                    score += k
                    return k# 三条

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 and abs(ans_2[i].num - ans_2[j].num) == 1 :
                    k=(40.0+ 1.0 / 10 * (ans_2[j].num-1-1)) * 1.0
                    score += k
                    return k# 连对2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 :
                    k=(30.0 +1.0 / (130+13) * ((ans_2[i].num - 1) * 10+ans_2[j].num-1)) * 1.0
                    score += k
                    return k # 普通2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 2:
            k=(20.0+1.0/(130+13)*((ans_2[i].num-1)*10+x-1))*1.0
            score += k
            return k #单对+3张散

    k= (10.0+1.0 / (130000 + 13000 + 1300 + 130 + 13)*((ans_2[5].num - 1) * 10000 + (ans_2[4].num - 1) * 1000 + (ans_2[3].num - 1) * 100 + (ans_2[2].num - 1) * 10 + ans_2[1].num - 1))*1.0
    score +=k
    return k

def third():
    global score
    init_cnt()

    for i in range(0, 4 + 1):
        tempp3[i] = ans_1[i + 1]

    tempp3.sort(key=takenum)  # 后墩牌组有序化
    for i in range(1, 5 + 1):
        ans_1[i] = tempp3[i - 1]

    x = 1
    for i in range(1,5+1):
        hua[ans_1[i].flower] +=1
        number[ans_1[i].num]+=1

    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            if shunzi5(ans_1[1].num) == 1:
                k=(150.0 + 1.0 / 9 * (ans_1[1].num - 1)) * 1.0 # 14 13 12 11 10
                score += k
                return k # 同花顺

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 4:
            k=(120.0+ 1.0/(130+13)*((ans_1[i].num - 1)*10))*1.0
            score += k
            return k#炸弹

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5,0,-1):
                if number[ans_1[j].num] == 2:
                    k=(90.0 + 1.0 / (130 + 13)*((x - 1) * 10 + ans_1[j].num - 1))*1.0
                    score += k
                    return k#葫芦
    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            k=(70.0 + 1.0 / (130000 + 13000 + 1300+130+13)*((ans_1[5].num-1)*10000+(ans_1[4].num - 1)*1000 + (ans_1[3].num - 1) * 100 + (ans_1[2].num - 1) * 10 + (ans_1[1].num - 1)))*1.0
            score +=k
            return k #同花

    x = 1
    if shunzi5(ans_1[1].num) == 1 :
        k=(60.0 + 1.0/9*(ans_1[1].num - 1)*1.0)
        score += k
        return k#5张顺子

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5,0,-1):
                if number[ans_1[j].num] == 1:
                    k=(50.0 + 1.0 / (1300+130+13) * ((x-1) * 100))
                    score += k
                    return k# 三条

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2 and abs(ans_1[i].num - ans_1[j].num) == 1 :
                    k= (40.0+ 1.0 / 10 * (ans_1[j].num-1-1)) * 1.0
                    score +=k
                    return k # 连对2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2 :
                    k=(30.0 +1.0 / (130+13) * ((ans_1[i].num - 1) * 10+ans_1[j].num-1)) * 1.0
                    score += k
                    return k # 普通2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 2:
            k=(20.0+1.0/(130+13)*((ans_1[i].num-1)*10+x-1))*1.0
            score += k
            return k #单对+3张散

    k=(10+1.0 / (130000 + 13000 + 1300 + 130 + 13)*((ans_1[5].num - 1) * 10000 + (ans_1[4].num - 1) * 1000 + (ans_1[3].num - 1) * 100 + (ans_1[2].num - 1) * 10 + ans_1[1].num - 1))*1.0
    score += k
    return  k




def contrast_ans() :
    global score,end_ans
    tempof()
    score = 0.0
    k1 = first()
    k2 = second()
    k3 = third()
    score=k1*3.0+k2*2.0+k3*1.0
    if k1 > k2 or k2 > k3 or k1 > k3 :
        score = 0
    if score>end_ans :
        end_ans = score
        standof()


def init_2():
    index = 0
    for i in range(1,8+1):
        if s2[i] == 0 :
            index+=1
            temp_3[index] = poker_2[i]

def dfs_2(d,index_2) :#/*枚举组合*/
    for i in range(d,9):
        temp_2[index_2] = poker_2[i]
        s2[i] = 1
        if index_2 == 5 :
            init_2()
            contrast_ans()
        else :
            dfs_2(i + 1, index_2 + 1)
        s2[i] = 0

def init_1() :
    index = 0
    for i in range(1,14):
        if s1[i] == 0:
            index+=1
            poker_2[index] = poker_1[i]

def pddi():

    init_cnt()
    for i in range(0, 4 + 1):
        tempp2[i] = temp_1[i + 1]

    tempp2.sort(key=takenum)  # 中墩牌组有序化
    for i in range(1, 5 + 1):
        pddun[i] = tempp2[i - 1]

    x = 1
    for i in range(1, 5 + 1):
        hua[pddun[i].flower] += 1
        number[pddun[i].num] += 1

    x = 1
    for i in range(1, 4 + 1):
        if hua[i] == 5:
            if shunzi5(pddun[1].num) == 1:
                k = (150.0 + 1.0 / 9 * (pddun[1].num - 1)) * 1.0
                # score += k  # 14 13 12 11 10
                return k  # 同花顺

    x = 1
    for i in range(5, 0, -1):
        if number[pddun[i].num] == 1:
            x = pddun[i].num
        if number[pddun[i].num] == 4:
            k = (120.0 + 1.0 / (130 + 13) * ((pddun[i].num - 1) * 10)) * 1.0
            return k  # 炸弹

    x = 1
    for i in range(5, 0, -1):
        if number[pddun[i].num] == 3:
            x = pddun[i].num
            for j in range(5, 0, -1):
                if number[pddun[j].num] == 2:
                    k = (90.0 + 1.0 / (130 + 13) * ((x - 1) * 10 + pddun[j].num - 1)) * 1.0
                    return k  # 葫芦
    x = 1
    for i in range(1, 4 + 1):
        if hua[i] == 5:
            k = (70.0 + 1.0 / (130000 + 13000 + 1300 + 130 + 13) * ((pddun[5].num - 1) * 10000 + (pddun[4].num - 1) * 1000 + (pddun[3].num - 1) * 100 + (pddun[2].num - 1) * 10 + (pddun[1].num - 1))) * 1.0
            return k  # 同花

    x = 1
    if shunzi5(pddun[1].num) == 1:
        k = (60.0 + 1.0 / 9 * (pddun[1].num - 1) * 1.0)
        return k  # 5张顺子

    x = 1
    for i in range(5, 0, -1):
        if number[pddun[i].num] == 3:
            x = pddun[i].num
            for j in range(5, 0, -1):
                if number[pddun[j].num] == 1:
                    k = (50.0 + 1.0 / (1300 + 130 + 13) * ((x - 1) * 100))
                    return k  # 三条

    x = 1
    for i in range(5, 0, -1):
        if number[pddun[i].num] == 2:
            for j in range(5, 0, -1):
                if (pddun[i].num != pddun[j].num) and number[pddun[j].num] == 2 and abs(
                        pddun[i].num - pddun[j].num) == 1:
                    k = (40.0 + 1.0 / 10 * (pddun[j].num - 1 - 1)) * 1.0
                    return k  # 连对2对

    x = 1
    for i in range(5, 0, -1):
        if number[pddun[i].num] == 2:
            for j in range(5, 0, -1):
                if (pddun[i].num != pddun[j].num) and number[pddun[j].num] == 2:
                    k = (30.0 + 1.0 / (130 + 13) * ((pddun[i].num - 1) * 10 + pddun[j].num - 1)) * 1.0
                    return k  # 普通2对

    x = 1
    for i in range(5, 0, -1):
        if number[pddun[i].num] == 1:
            x = pddun[i].num
        if number[pddun[i].num] == 2:
            k = (20.0 + 1.0 / (130 + 13) * ((pddun[i].num - 1) * 10 + x - 1)) * 1.0
            return k  # 单对+3张散

    k = 10.0+(1.0 / (130000 + 13000 + 1300 + 130 + 13) * ((pddun[5].num - 1) * 10000 + (pddun[4].num - 1) * 1000 + (pddun[3].num - 1) * 100 + (pddun[2].num - 1) * 10 + pddun[1].num - 1)) * 1.0
    return k

def dfs_1(d, index_1): #/ * 枚举组合 * /
    for i in range(d,13+1):
        s1[i] = 1
        temp_1[index_1] = poker_1[i]
        if index_1 == 5 :
            if pddi()>=30.0:
                init_1()
                dfs_2(1, 1)
        else:
            dfs_1(i + 1, index_1 + 1)
        s1[i] = 0


def number_to_hua(x):
    if x == 1:
        return "&"
    if x == 2:
        return "$"
    if x == 3:
        return "#"
    if x == 4:
        return "*"

def hua_to_number(x):
    if x == "&":
        return 1
    if x == "$":
        return 2
    if x == "#":
        return 3
    if x == "*":
        return 4

def change(x):
    if x==10:
        return "10"
    if x==11:
        return "J"
    if x==12:
        return "Q"
    if x==13:
        return "K"
    if x==14:
        return "A"
    return str(x)



def rank():
    url = "https://api.shisanshui.rtxux.xyz/rank"
    response = requests.get(url)
    print(response.text)

def history(limit,page):
    global use
    url = 'https://api.shisanshui.rtxux.xyz/history'
    headers = {"X-Auth-Token":token}
    params={
        "player_id":use,
        "limit":limit,
        "page":page
    }

    response=requests.get(url,params=params,headers=headers)
    message=response.json()
    print(response.text)
    return response

def history_detail():
    global id
    url = "https://api.shisanshui.rtxux.xyz/history/{id}"
    params = {"id": id}
    headers = {"X-Auth-Token": token}
    response = requests.get(url,params=params,headers=headers)
    print(response)


def opengame():
    global token
    global id
    url = "https://api.shisanshui.rtxux.xyz/game/open"
    headers = {"X-Auth-Token": token}
    response = requests.post(url, headers=headers)
    try:
        message=response.json()
        id=message["data"]["id"]
        card=message["data"]["card"]
        print(response.text)
        return card
    except:
        time().sleep(5)

def submitgame(submit_ans):
    global token, id
    url = "https://api.shisanshui.rtxux.xyz/game/submit"
    headers = {"content-type": "application/json"}
    headers["X-Auth-Token"] = token
    data={"id":id}
    data["card"]=submit_ans
    response=requests.post(url,data=json.dumps(data),headers=headers)
    print(response.text)


def logout():
    global token
    url = "https://api.shisanshui.rtxux.xyz/auth/logout"
    headers = {"X-Auth-Token":token}
    response = requests.post(url,headers=headers)
    print(response.text)

def login_check():
    global token
    url = "https://api.shisanshui.rtxux.xyz/auth/validate"
    headers = {"X-Auth-Token": token}
    response = requests.get(url,headers=headers)
    print(response.text)


def login(usename,password):
    global token,use
    url = "https://api.shisanshui.rtxux.xyz/auth/login"
    payload = "{\"username\":"+"\""+usename+"\""+","+"\"password\":"+"\""+password+"\""+"}"
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=payload, headers=headers)
    try:
        message = response.json()  # 登录
        token = message["data"]["token"]
        use=message["data"]["user_id"]
        print (response.text)
        return message
    except :
        time().sleep(5)
#139 dzy001 dzy001
#143 dzy002 dzy002

def registered(usename,password):
    url = "https://api.shisanshui.rtxux.xyz/auth/register"
    payload = "{\"username\":"+"\""+usename+"\""+","+"\"password\":"+"\""+password+"\""+"}"
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)


def read_opengame():#读入

    str0 = opengame()#开始牌局
    # print(str0)

    str1 = str0.replace("10", "T")
    dex = 0
    for i in range(0, 39, 3):
        if str1[i + 1] == "T":
            x = node(hua_to_number(str1[i]), 10)
        elif str1[i + 1] == "J":
            x = node(hua_to_number(str1[i]), 11)
        elif str1[i + 1] == "Q":
            x = node(hua_to_number(str1[i]), 12)
        elif str1[i + 1] == "K":
            x = node(hua_to_number(str1[i]), 13)
        elif str1[i + 1] == "A":
            x = node(hua_to_number(str1[i]), 14)
        else:
            x = node(hua_to_number(str1[i]), int(str1[i + 1]))
        dex += 1
        poker_1[dex] = x

def printf_ans():#输出
    submit_ans.clear()
    s=""
    for i in range(1, 3 + 1):  # 前墩
        if i!=3:
            s+=number_to_hua(end_3[i].flower)+change(end_3[i].num)+" "
        else:
            s+=number_to_hua(end_3[i].flower)+change(end_3[i].num)

    submit_ans.append(s)
    print(s)
    s=""
    for i in range(1, 5 + 1):  # 中墩
        if i != 5:
            s += number_to_hua(end_2[i].flower) + change(end_2[i].num) + " "
        else:
            s += number_to_hua(end_2[i].flower) + change(end_2[i].num)
    submit_ans.append(s)
    print(s)
    s = ""
    for i in range(1, 5 + 1):
        if i != 5:
            s += number_to_hua(end_1[i].flower) + change(end_1[i].num) + " "
        else:
            s += number_to_hua(end_1[i].flower) + change(end_1[i].num)
    submit_ans.append(s)
    print(s)
    return submit_ans

def init_end():
    print("end!")
def init_start():
    print("start!")
    global end_ans,score
    end_ans,score=0.0,0.0
    poker_1.clear()
    poker_2.clear()
    poker_3.clear()
    ans_1.clear()
    ans_2.clear()
    ans_3.clear()
    temp_1.clear()
    temp_2.clear()
    temp_3.clear()
    end_1.clear()
    end_2.clear()
    end_3.clear()
    s1.clear()
    s2.clear()
    s3.clear()
    tempp1.clear()
    tempp2.clear()
    tempp3.clear()
    submit_ans.clear()
    pddun.clear()
    for i in range(0, 20):
        poker_1.append(node(0, 0))
        poker_2.append(node(0, 0))
        poker_3.append(node(0, 0))
        ans_1.append(node(0, 0))
        ans_2.append(node(0, 0))
        ans_3.append(node(0, 0))
        temp_1.append(node(0, 0))
        temp_2.append(node(0, 0))
        temp_3.append(node(0, 0))
        end_1.append(node(0, 0))
        end_2.append(node(0, 0))
        end_3.append(node(0, 0))
        s1.append(0)
        s2.append(0)
        s3.append(0)
        submit_ans.append("")
        pddun.append(node(0,0))

    for i in range(0, 2 + 1):
        tempp1.append(node(0, 0))
        submit_ans.append("")
    for i in range(0, 4 + 1):
        tempp2.append(node(0, 0))
    for i in range(0, 4 + 1):
        tempp3.append(node(0, 0))

    for i in range(0, 15 + 1):
        hua[i] = 0
        number[i] = 0  # 桶排初始化


#主函数


# usename=input()
# password=input()
# registered(usename,password)#注册
# login(usename,password)#登录
# login_check()#验证
#
# read_opengame()#开启牌局，读入
# dfs_1(1, 1)#解决问题，深搜
# submit_ans=printf_ans()
# print(submit_ans)
# submitgame(submit_ans)#提交牌局
#
# rank()
# history(3,1)#历史记录
# history_detail()#记录详情
# logout()  # 注销
#print("权值:",end_ans)





