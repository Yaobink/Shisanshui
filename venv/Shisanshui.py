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

for i in range(0,20):
    poker_1.append(node(0,0))
    poker_2.append(node(0, 0))
    poker_3.append(node(0, 0))
    ans_1.append(node(0, 0))
    ans_2.append(node(0, 0))
    ans_3.append(node(0, 0))
    temp_1.append(node(0, 0))
    temp_2.append(node(0, 0))
    temp_3.append(node(0, 0))
    end_1.append(node(0,0))
    end_2.append(node(0, 0))
    end_3.append(node(0, 0))
    s1.append(0)
    s2.append(0)
    s3.append(0)

for i in range(0,2+1):
    tempp1.append(node(0,0))
for i in range(0,4+1):
    tempp2.append(node(0,0))
for i in range(0,4+1):
    tempp3.append(node(0,0))

global cnt,r1,r2,r3,end_ans,score # 计数器
cnt,r1,r2,r3=0,5,5,3
end_ans ,score= 0.0,0.0
global e1, e2, e3;
global a1, a2, a3;

hua,number={},{}
for i in range(0,15+1):
    hua[i]=0
    number[i]=0#桶排初始化

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
                score += (9.0+0.9 / 11.0 * (ans_3[1].num - 1))
                return 10 # 3张同花顺
    x = 1
    for i in range(1,4+1):
        if hua[i] == 3:
            score += (6.0 +0.9/(1300+130+13)*((ans_3[3].num-1)*100+(ans_3[2].num-1)*10+(ans_3[1].num-1))*1.0 )
            return 7 #3张同花
    x = 1
    if shunzi3(ans_3[1].num) == 1:
        score += (5.0  + 0.9/11.0*(ans_3[1].num-1)*1.0)
        return 6 #3张顺子
    x = 1
    for i in range(3,0,-1):
        if number[ans_3[i].num] == 3:
            score += (4.0+0.9/13.0*(ans_3[1].num - 1)*1.0)
            return 5#三条
    x = 1
    for i in range(3,0,-1):
        if number[ans_3[i].num] == 1:
            x = ans_3[i].num
        if number[ans_3[i].num] == 2:
            score += (1.0 + 0.9/(130+13)*((ans_3[i].num - 1)*10+x-1)*1.0)
            return 2#单对
    x = 1
    score += 0.9 / (1300.0 + 130.0 + 13.0)*((ans_3[3].num - 1) * 100 + (ans_3[2].num - 1) * 10 + (ans_3[1].num - 1))
    return 1 #散牌

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
                score += (9.0 + 0.9 / 9 * (ans_2[1].num - 1)) * 1.0 # 14 13 12 11 10
                return 10 # 同花顺

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 4:
            score += (8.0+ 0.9/(130+13)*((ans_2[i].num - 1)*10))*1.0
            return 9#炸弹

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5,0,-1):
                if number[ans_2[j].num] == 2:
                    score += (7.0 + 0.9 / (130 + 13)*((x - 1) * 10 + ans_2[j].num - 1))*1.0
                    return 8#葫芦
    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            score +=(6.0 + 0.9 / (130000 + 13000 + 1300+130+13)*((ans_2[5].num-1)*10000+(ans_2[4].num - 1)*1000 + (ans_2[3].num - 1) * 100 + (ans_2[2].num - 1) * 10 + (ans_2[1].num - 1)))*1.0
            return 7#同花

    x = 1
    if shunzi5(ans_2[1].num) == 1 :
        score += (5.0 + 0.9/9*(ans_2[1].num - 1)*1.0)
        return 6#5张顺子

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5,0,-1):
                if number[ans_2[j].num] == 1:
                    score += (4.0 + 0.9 / (1300+130+13) * ((x-1) * 100))
                    return 5# 三条

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 and abs(ans_2[i].num - ans_2[j].num) == 1 :
                    score += (3.0+ 0.9 / 10 * (ans_2[j].num-1-1)) * 1.0
                    return 4# 连对2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 :
                    score += (2.0 +0.9 / (130+13) * ((ans_2[i].num - 1) * 10+ans_2[j].num-1)) * 1.0
                    return 3 # 普通2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 2:
            score += (1.0+0.9/(130+13)*((ans_2[i].num-1)*10+x-1))*1.0
            return 2#单对+3张散
    score += (0.9 / (130000 + 13000 + 1300 + 130 + 13)*((ans_2[5].num - 1) * 10000 + (ans_2[4].num - 1) * 1000 + (ans_2[3].num - 1) * 100 + (ans_2[2].num - 1) * 10 + ans_2[1].num - 1))*1.0
    return 1

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
                score += (9.0 + 0.9 / 9 * (ans_1[1].num - 1)) * 1.0 # 14 13 12 11 10
                return 10 # 同花顺

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 4:
            score += (8.0+ 0.9/(130+13)*((ans_1[i].num - 1)*10))*1.0
            return 9#炸弹

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5,0,-1):
                if number[ans_1[j].num] == 2:
                    score += (7.0 + 0.9 / (130 + 13)*((x - 1) * 10 + ans_1[j].num - 1))*1.0
                    return 8#葫芦
    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            score +=(6.0 + 0.9 / (130000 + 13000 + 1300+130+13)*((ans_1[5].num-1)*10000+(ans_1[4].num - 1)*1000 + (ans_1[3].num - 1) * 100 + (ans_1[2].num - 1) * 10 + (ans_1[1].num - 1)))*1.0
            return 7#同花

    x = 1
    if shunzi5(ans_1[1].num) == 1 :
        score += (5.0 + 0.9/9*(ans_1[1].num - 1)*1.0)
        return 6#5张顺子

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5,0,-1):
                if number[ans_1[j].num] == 1:
                    score += (4.0 + 0.9 / (1300+130+13) * ((x-1) * 100))
                    return 5# 三条

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2 and abs(ans_1[i].num - ans_1[j].num) == 1 :
                    score += (3.0+ 0.9 / 10 * (ans_1[j].num-1-1)) * 1.0
                    return 4# 连对2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2 :
                    score += (2.0 +0.9 / (130+13) * ((ans_1[i].num - 1) * 10+ans_1[j].num-1)) * 1.0
                    return 3 # 普通2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 2:
            score += (1.0+0.9/(130+13)*((ans_1[i].num-1)*10+x-1))*1.0
            return 2#单对+3张散
    score += (0.9 / (130000 + 13000 + 1300 + 130 + 13)*((ans_1[5].num - 1) * 10000 + (ans_1[4].num - 1) * 1000 + (ans_1[3].num - 1) * 100 + (ans_1[2].num - 1) * 10 + ans_1[1].num - 1))*1.0
    return 1


def tempof() :
    for i in range(1,4): #前墩
        ans_3[i] = temp_3[i]
    for i in range(1,6): #中墩
        ans_2[i] = temp_2[i]
    for i in range(1,6): #后墩
        ans_1[i] = temp_1[i]

def contrast_ans() :


    global score,end_ans,cnt
    global e1, e2, e3
    global a1, a2, a3
    tempof()
    score = 0.0
    k1 = first()
    e1 = score
    k2 = second()
    e2 = score - e1
    k3 = third()
    e3 = score - (e1 + e2)
    if k1 > k2 or k2 > k3 or k1 > k3 :
        score = 0
    if score>end_ans :
        end_ans = score
        a1 = e1; a2 = e2; a3 = e3
        standof()
    cnt+=1


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
        if index_2 == r2 :
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

def dfs_1(d, index_1): #/ * 枚举组合 * /
    for i in range(d,13+1):
        s1[i] = 1
        temp_1[index_1] = poker_1[i]
        if index_1 == r1 :
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

#主函数

str0 = input()
str1=str0.replace("10","T")
dex=0
for i in range(0,39,3) :
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
    dex+=1
    poker_1[dex]=x

dfs_1(1, 1)
print(cnt)
print("答案:")
for i in range(1,3+1):#前墩
    print(end_3[i].num,end=" ")
print("\n")
for i in range(1,5+1):# 中墩
    print(end_2[i].num,end=" ")
print("\n")
for i in range(1,5+1):
    print(end_1[i].num,end=" ")
print("\n")

print("权值:",end_ans)

#cout << a1 << " " << a2 << " " << a3 << endl;78i




