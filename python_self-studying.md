# 파이썬 유튜브 독학

<aside>
💡 파이썬 기초 문법을 떼기 위해 유튜브 ‘나도코딩’ 채널에서 학습한 내용을 간추렸습니다.
몰입도를 높이기 위해 강의에 나오는 코드들을 야구 용어로 바꾸어 학습했습니다. 배운 개념을 기반으로 야구 문자중계를 시뮬레이션 해보았습니다.

</aside>

---

> **목차**
> 

### 1. 문자열

```python
print(abs(-6))
print(pow(4,5)) #4의 4제곱
print(max(5,10)) #최댓값
print(round(4.95)) #반올림

from math import *
print(floor(4.9)) #내림
print(floor(ceil(3.1))) #올림
print(sqrt(16)) #제곱근

from random import *
print(random()) #난수 뽑기 0.0~1.0 사이의 임의의 값 생성.
print(random()*10)
print(int(random()))

print(int(random())+1) 
print(randrange(1,46)) #1부터 46미만의 임의의 값 생성.
print(randint(1,45)) #1부터 45이하의 임의의 값 생성.
```

```python
from random import *

date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " +str(date)+ "일로 선정되었습니다")
sentence1="나는 소년입니다"
sentence2='파이썬은 즐거워요'
print(sentence1)
sentence3= """나는 희준이고
파이썬은 
재밌지
"""
print(sentence3)
```

```python
#슬라이싱
jumin = "001223-3173611"
print("성별 : " +jumin[7]) #jumin[7] => jumin에서 7번째 자리의 문자 추출
print("연 : " + jumin[0:2]) #jumin[0:2] => jumin에서 0번째부터 2번째 직전자리까지의 문자 추출
print("월 : " +jumin[2:4])
print("일 : " +jumin[4:6])
#jumin[:7] = jumin[0:7]
print("뒤 7자리(뒤에부터) : " +jumin[-3:])

python= "Python IS amazing"
print(python.lower()) #모든 문자 소문자로 출력
print(python.upper()) #모든 문자 대문자로 출력
print(python[0].isupper()) #python의 첫번째 문자가 대문자인가?
print(len(python)) #python의 문자 길이
print(python.replace("Python","java")) #문자를 다른 문자로 대체

print(python.index("I")) #python에서 문자 "I"의 자릿수 출력
index= python.index("n")
index=python.index("n", index+1) #python에서 두번째 "n"의 자릿수 출력
print(python.find("k")) #find함수는 index함수와 다르게 없는 문자는 -1로 출력. index함수는 오류.
print(python.count("n")) #python에서 "n"의 개수 출력
```

```python
print("나는 %d살입니다" %21) # %자리에 21을 출력. d는 정수값만 입력 가능
print("나는 %s를 좋아해요" %"기아타이거즈") # %자리에 "기아타이거즈"를 출력. s는 문자열, 정수 입력 가능
print("나는 %c을 좋아해요" %"a") # %자리에 "a"를 출력. c는 한 글자만 입력 가능
print("나는 %s과 %s를 좋아해요" %("양현종", "루니"))
print("나는 {}살입니다." .format(21)) # {}자리에 21 출력
print("좋아하는 숫자는 {}이고 좋아하는 선수는 {}입니다".format(27, "루니"))
print("좋아하는 캐릭터는 {1}과 {0}입니다".format("스누피", "그로밋")) #출력순서 지정
print("나는 {age}살이고 {color}색을 좋아해요".format(age=21, color="파란"))

position="유격수"
strenth="도루"
print(f"나는 {position}이고 {strenth}를 잘해요")
```

```python
print("비내리는 호남선 \n남행 열차에") # \n은 줄바꿈
print("나는 '김희준' 입니다")
print('나는 "김희준" 입니다')
print("나는 \"김희준\"입니다.") # \"는 "를 그대로 출력
print("출전 가능한 선수는 김선빈\\박찬호\\최형우이다") # \\는 \를 그대로 출력
print("기아 베어스\r두산") # \r은 "두산"을 처음커서로 당겨서 덮어씌움
print("두산 베라\b어스") # \b는 마지막 글자 삭제하고 "두산"을 이어붙임
print("manchester\tunited") # \t는 띄어쓰기

#퀴즈
url= "http://naver.com"
url= "http://google.com"
myurl=url.replace("http://","")
print(myurl)
myurl=myurl[:myurl.find(".")]
print(myurl)
print(str(myurl[:3]+str(len(myurl))+str(myurl.count("e"))+"!"))
```

---

### 2. 리스트

```python
# 리스트 만들기, 대괄호[ ]
subway = [10,20,30]
print(subway)
starting_pitcher=["브룩스", "가뇽", "양현종", "임기영"]
print(starting_pitcher)
pitcher="양현종"
print(pitcher+"은 기아의 "+str(starting_pitcher.index(pitcher)+1)+"선발입니다.")
starting_pitcher.append("이민우") #리스트 맨 끝에 "이민우" 추가
print(starting_pitcher)
starting_pitcher.insert(4,"김기훈") #리스트 4 자리에 "김기훈" 추가
print(starting_pitcher)
starting_pitcher.pop() #리스트 뒤에서부터 한 개 제거
print(starting_pitcher)
starting_pitcher.pop()
print(starting_pitcher)
```

---

### 3. 딕셔너리

```python
#사전, 중괄호{ }
hitter={1:"최원준",2:"터커",3:"최형우",4:"나지완", 5:"유민상"}  # 사전에선 중괄호 사용
print(hitter[2]) #hitter사전에서 key2를 가진 value터커를 출력
print(hitter.get(2)) #hitter사전에서 key2를 가진 value터커를 출력, key가 없는 경우에 오류 발생 안 시키고 none을 출력!
print(hitter.get(6,"김민식")) #없는 key6을 입력하면 오류 안 내고 새로운 value "김민식" 출력 
hn=3
print("기아 타이거즈의 "+str(hn)+"번타자는 "+hitter[hn]+"입니다.")
sp={"1브룩스":2.68, "2양현종":4.82, "3가뇽":4.42, "4이민우":5.22}
name="1브룩스"
print("기아의 "+name[:1]+ "선발투수는 "+name[1:]+"이고, "+name[1:]+"의 ERA는 "+str(sp[name])+"입니다.")
print(3 in hitter) #3이라는 key가 hitter에 있는지 여부
hitter[6]="김민식" #key6을 새롭게 생성
hitter[7]="홍종표"
hitter[1]="김선빈" #기존의 key1을 새로운 key1으로 업데이트
del hitter[3] #key3 삭제
print(hitter)
print(sp.keys()) #key만 출력
print(sp.values()) #value만 출력
print(sp.items()) #key와 value를 쌍으로 출력
hitter.clear() #사전 내용 전부 삭제
print(hitter)
```

---

### 4. 튜플과 집합

```python
#tuple(튜플) (리스트와는 다르게 내용 수정 불가), 소괄호 ( )
coach=("윌리엄스","최희섭", "서재응")
front=("조계현", "정민철")
print(coach[0])
name="김민식"
position="cathcer"
strenth="blocking"
print(name, position, strenth)
(name, position, strenth) = ("김민식", "catcher", "blocking")
print(name, position, strenth)
```

```python
#set(집합) 중복이 안 되고 순서가 없는!, 중괄호 { }
my_set={1,2,3,3,3} #중복된 3은 한 개만 출력 
print(my_set)
infielder={"최원준","유민상","박찬호","김주찬"}
outfielder= set(["최원준", "터커","김주찬","나지완"])
print(infielder & outfielder) # 교집합 출력
print(infielder.intersection(outfielder)) # 교집합 출력
print(infielder|outfielder) #합집합
print(infielder.union(outfielder)) #합집합
print(outfielder-infielder) #차집합
print(outfielder.difference(infielder)) #차집합
print("외야만 볼 수 있는 선수는 "+str(outfielder-infielder)+"이고, 내외야 멀티플레이어는 " +str(infielder&outfielder)+"입니다.")
infielder.add("김선빈") #집합에 값 추가
print(infielder)
outfielder.remove("김주찬") #집합에서 값 삭제
print(outfielder)
```

```python
#자료구조의 변경
stats={"출루율", "장타율", "홈런", "안타", "타율"} #set(집합)
print(type(stats)) #stats의 자료구조
stats= list(stats) #stats의 자료구조를 list로 변경
print(stats, type(stats))
stats= tuple(stats) #stats의 자료구조를 tuple로 변경
print(stats, type(stats))
```

```python
#퀴즈
from random import *
users= range(1,21) #1부터 20까지 숫자 생성
users=list(users)
shuffle(users)
winners= sample(users,4)
print(winners)
print("당첨자 발표")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("축하합니다!")
```

---

### 5. 반복문

```python
#for: 여러번 반복해야 하는 출력을 한번에 출력
for back_no in range(2,8):
    print("등번호: {0}".format(back_no)) #range(2,8)의 수를 순차적으로 출력
sp=["브룩스", "양현종", "가뇽", "임기영"]
for todaysp in sp:
    print("오늘의 선발투수는 {0}입니다.".format(todaysp))

#while: 특정 조건이 만족될 때까지 반복
pitcher="정해영"
index=4
while index>=1:
    print("{0}이 상대할 타자는 {1}명 남았습니다.".format(pitcher, index))
    index -=1
    if index==0:
        print("{0}을 교체합니다.".format(pitcher))
```

```python
#continue와 break
no_hit = [2,5,9]
game_set=[8]
for hitter in range(1,10):
    if hitter in no_hit:
        continue #해당 문장을 출력하지 않고 그 다음 문장을 출력
    if hitter in game_set:
        print("{0}번 타자가 아웃되며 경기가 종료되었다.".format(hitter))
        break #해당 문장에서 컨티뉴를 종료!
    print("{0}번 타자가 안타를 기록했다.".format(hitter))
```

```python
#한줄 for
#출석번호가 1,2,3,4이고, 앞에 100을 붙이기로 함.
students=[1,2,3,4]
students=[i+100 for i in students]
print(students)
#선수 이름을 길이로 변환
player=["Rooney", "Son", "Messi"]
player=[len(i) for i in player]
print(player)
#선수 이름을 대문자로 변환
player=["Rooney", "Son", "Messi"]
player=[i.upper() for i in player]
print(player)
```

```python
#퀴즈
from random import *
count=0
for i in range(1,51):
    time=randrange(5,51)
    if 15>=time>=5:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        count+=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
print("총 탑승 승객 : {0} 분".format(count))
```

---

### 6. 함수

```python
#함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance>=money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance=0
balance= deposit(balance,2000)
balance= deposit(balance,3000)
balance=withdraw(balance,1000)
balance=withdraw(balance,100)
print(balance)
```

### 7. 야구 문자중계 시뮬레이션

배운 개념들을 종합하여 야구 문자중계를 약식으로 시뮬레이션 해보았습니다. 27개의 아웃카운트가 잡히면 반복문이 종료되고, 결과는 삼진, 볼넷, 1땅, 2땅, 3땅, 유땅으로 나뉘었습니다.

```python

sp={"1브룩스":2.68, "2양현종":4.82, "3가뇽":4.42, "4이민우":5.22}
name="1브룩스" #딕셔너리에서 선발 투수 지정
pitcher=name[1:]
p_no=name[:1]
#오프닝 코멘트
print("오늘 기아의 선발투수는 "+p_no+"선발 "+pitcher+"이고, "+pitcher+"의 ERA는 "+str(sp[name])+"입니다.")

from random import *

#스트라이크, 볼 수 count하기 위한 기본 설정
s_total=0
b_total=0
s_count=0
b_count=0
pb_count=0
k_count=0

b4_count=0
game_set=[18]

for pc in range(1,200):
    top=int(randrange(1,8)) #구종을 랜덤으로 지정
    if k_count+pb_count in game_set:
        print("브룩스의 오늘 투구는 여기까지였습니다.")
        print("오늘경기 {0}의 투구수는 {1}개이고 스트라이크 {2}개, 볼 {3}개였습니다. 삼진은 {4}개를 기록하고, 볼넷은{5}개 허용했습니다.".format(pitcher, pc-1,s_total,b_total,k_count,b4_count))
        break
    if s_count>=3: #3스트라이크일 시 삼진
        print("삼진!\n")
        s_count=0  
        b_count=0
        k_count+=1 #토탈 삼진 수 1 추가
    elif b_count>=4: #볼 4개일 경우 포볼
        print("볼넷\n")
        s_count=0
        b_count=0
        b4_count+=1 #토탈 볼넷 수 1추가

#포심:투심:슬라이더:체인지업:커브 비율을 2:3:2:2:2로 잡기 위한 설정
    if 1<=top<=2:
        speed=randrange(147,153) #구속 역시 지정된 range에서 랜덤으로 출력
        top_name="포심"
    elif 2<top<=4:
        speed=randrange(147,151)
        top_name="투심"
    elif 4<top<=5:
        speed=randrange(136,143)
        top_name="슬라이더"
    elif 5<top<=6:
        speed=randrange(131,136)
        top_name="체인지업"
    elif 6<top<=7:
        speed=randrange(123,130)
        top_name="커브"

#스트라이크 볼 여부를 판단하는 if문
    sb=int(randrange(9,12))
    if 9<=sb<10:
        sb_name="스트라이크"
        s_total+=1 #경기 마무리 시 집계를 위한 총 스트라이크 개수 저장
        s_count+=1
    elif 10<=sb<11:
        sb_name="볼"
        b_total+=1 #경기 마무리 시 집계를 위한 총 볼 개수 저장
        b_count+=1
    elif 11<=sb<12:
        sb_name="스윙"
        s_total+=1
        swing=int(randrange(18,23))
        if 18<=swing<20:
            sw="파울이군요"
            if s_count<2:
                s_count+=1
            else:
                s_count+=0
        elif 20<=swing<21:
            sw="헛스윙이군요"
            s_count+=1
        elif 21<=swing<=22:
            hitting=int(randrange(23,27))
            if 23<=hitting<24:
                sw="3루수 앞 땅볼"
                s_count=0
                b_count=0
                pb_count+=1
            elif 24<=hitting<25:
                sw="유격수 앞 땅볼"
                s_count=0
                b_count=0
                pb_count+=1
            elif 25<=hitting<26:
                sw="2루수 앞 땅볼"
                s_count=0
                b_count=0
                pb_count+=1
            elif 26<=hitting<27:
                sw="1루수 앞 땅볼"
                s_count=0
                b_count=0
                pb_count+=1
    
#투구 location 지정
    loc=int(randrange(14,17))
    if loc==14:
        location="몸쪽"
    elif loc==15 and sb_name!="볼":
        location="한가운데"
    elif loc==15 and sb_name=="볼":
        location="크게 벗어난 곳"
    elif loc==16:
        location="바깥쪽"
    

    if s_count==3 or b_count==4:
        if 11<=sb<12 and 18<=swing<21:
            print(pitcher+"의 제{0}구, {3}에 날아오는 {1}km의 {2}, {4}입니다. {5}.".format(pc,speed,top_name,location,sb_name,sw))
        else:
             print(pitcher+"의 제{0}구, {3}에 날아오는 {1}km의 {2}, {4}입니다.".format(pc,speed,top_name,location,sb_name))

    elif 11<=sb<12 and 18<=swing<21:
        print(pitcher+"의 제{0}구, {3}에 날아오는 {1}km의 {2}, {4}입니다. {7}. 카운트는 {5}-{6}".format(pc,speed,top_name,location,sb_name,b_count,s_count,sw))
    elif 11<=sb<12 and 21<=swing<=22:
        print(pitcher+"의 제{0}구, {3}에 날아오는 {1}km의 {2}, {4}입니다. {5}\n".format(pc,speed,top_name,location,sb_name,sw))
    else:
        print(pitcher+"의 제{0}구, {3}에 날아오는 {1}km의 {2}, {4}입니다. 카운트는 {5}-{6}".format(pc,speed,top_name,location,sb_name,b_count,s_count))
```

출력값은 다음과 같고, random함수를 이용했기에 매번 다른 결과를 출력.

```python
오늘 기아의 선발투수는 1선발 브룩스이고, 브룩스의 ERA는 2.68입니다.

브룩스의 제1구, 몸쪽에 날아오는 127km의 커브, 스트라이크입니다. 카운트는 0-1
브룩스의 제2구, 크게 벗어난 곳에 날아오는 128km의 커브, 볼입니다. 카운트는 1-1
브룩스의 제3구, 몸쪽에 날아오는 151km의 포심, 스트라이크입니다. 카운트는 1-2
브룩스의 제4구, 바깥쪽에 날아오는 152km의 포심, 볼입니다. 카운트는 2-2
브룩스의 제5구, 한가운데에 날아오는 148km의 투심, 스트라이크입니다.
삼진!

브룩스의 제6구, 바깥쪽에 날아오는 150km의 투심, 스트라이크입니다. 카운트는 0-1
브룩스의 제7구, 한가운데에 날아오는 132km의 체인지업, 스트라이크입니다. 카운트는 0-2
브룩스의 제8구, 몸쪽에 날아오는 150km의 투심, 볼입니다. 카운트는 1-2
브룩스의 제9구, 몸쪽에 날아오는 148km의 투심, 볼입니다. 카운트는 2-2
브룩스의 제10구, 크게 벗어난 곳에 날아오는 149km의 투심, 볼입니다. 카운트는 3-2
브룩스의 제11구, 몸쪽에 날아오는 147km의 포심, 볼입니다.
볼넷

브룩스의 제12구, 바깥쪽에 날아오는 148km의 포심, 스트라이크입니다. 카운트는 0-1
브룩스의 제13구, 몸쪽에 날아오는 147km의 투심, 스트라이크입니다. 카운트는 0-2
브룩스의 제14구, 바깥쪽에 날아오는 139km의 슬라이더, 스윙입니다. 파울이군요. 카운트는 0-2
브룩스의 제15구, 바깥쪽에 날아오는 141km의 슬라이더, 스트라이크입니다.
삼진!

브룩스의 제16구, 바깥쪽에 날아오는 150km의 투심, 볼입니다. 카운트는 1-0
브룩스의 제17구, 몸쪽에 날아오는 129km의 커브, 볼입니다. 카운트는 2-0
브룩스의 제18구, 바깥쪽에 날아오는 150km의 포심, 스트라이크입니다. 카운트는 2-1
브룩스의 제19구, 몸쪽에 날아오는 133km의 체인지업, 볼입니다. 카운트는 3-1
브룩스의 제20구, 한가운데에 날아오는 138km의 슬라이더, 스윙입니다. 헛스윙이군요. 카운트는 3-2
브룩스의 제21구, 한가운데에 날아오는 147km의 포심, 스트라이크입니다.
삼진!

브룩스의 제22구, 한가운데에 날아오는 129km의 커브, 스트라이크입니다. 카운트는 0-1
브룩스의 제23구, 몸쪽에 날아오는 149km의 투심, 스윙입니다. 1루수 앞 땅볼

브룩스의 제24구, 크게 벗어난 곳에 날아오는 147km의 투심, 볼입니다. 카운트는 1-0
브룩스의 제25구, 몸쪽에 날아오는 147km의 투심, 스트라이크입니다. 카운트는 1-1
브룩스의 제26구, 한가운데에 날아오는 147km의 포심, 스윙입니다. 파울이군요. 카운트는 1-2
브룩스의 제27구, 몸쪽에 날아오는 149km의 포심, 스윙입니다. 파울이군요. 카운트는 1-2
브룩스의 제28구, 바깥쪽에 날아오는 149km의 포심, 스윙입니다. 1루수 앞 땅볼

브룩스의 제29구, 몸쪽에 날아오는 129km의 커브, 스윙입니다. 유격수 앞 땅볼

브룩스의 제30구, 바깥쪽에 날아오는 150km의 투심, 볼입니다. 카운트는 1-0
브룩스의 제31구, 바깥쪽에 날아오는 129km의 커브, 스윙입니다. 파울이군요. 카운트는 1-1
브룩스의 제32구, 바깥쪽에 날아오는 123km의 커브, 볼입니다. 카운트는 2-1
브룩스의 제33구, 바깥쪽에 날아오는 149km의 투심, 스윙입니다. 헛스윙이군요. 카운트는 2-2
브룩스의 제34구, 바깥쪽에 날아오는 136km의 슬라이더, 볼입니다. 카운트는 3-2
브룩스의 제35구, 크게 벗어난 곳에 날아오는 135km의 체인지업, 볼입니다.
볼넷

브룩스의 제36구, 한가운데에 날아오는 147km의 포심, 스윙입니다. 파울이군요. 카운트는 0-1
브룩스의 제37구, 크게 벗어난 곳에 날아오는 151km의 포심, 볼입니다. 카운트는 1-1
브룩스의 제38구, 한가운데에 날아오는 148km의 포심, 스트라이크입니다. 카운트는 1-2
브룩스의 제39구, 바깥쪽에 날아오는 149km의 포심, 스트라이크입니다.
삼진!

브룩스의 제40구, 바깥쪽에 날아오는 149km의 투심, 볼입니다. 카운트는 1-0
브룩스의 제41구, 바깥쪽에 날아오는 135km의 체인지업, 스트라이크입니다. 카운트는 1-1
브룩스의 제42구, 한가운데에 날아오는 131km의 체인지업, 스윙입니다. 3루수 앞 땅볼

브룩스의 제43구, 한가운데에 날아오는 142km의 슬라이더, 스트라이크입니다. 카운트는 0-1
브룩스의 제44구, 몸쪽에 날아오는 152km의 포심, 볼입니다. 카운트는 1-1
브룩스의 제45구, 바깥쪽에 날아오는 150km의 포심, 볼입니다. 카운트는 2-1
브룩스의 제46구, 한가운데에 날아오는 126km의 커브, 스트라이크입니다. 카운트는 2-2
브룩스의 제47구, 크게 벗어난 곳에 날아오는 137km의 슬라이더, 볼입니다. 카운트는 3-2
브룩스의 제48구, 바깥쪽에 날아오는 151km의 포심, 스윙입니다. 파울이군요. 카운트는 3-2
브룩스의 제49구, 한가운데에 날아오는 149km의 포심, 스윙입니다. 파울이군요. 카운트는 3-2
브룩스의 제50구, 바깥쪽에 날아오는 137km의 슬라이더, 볼입니다.
볼넷

브룩스의 제51구, 몸쪽에 날아오는 151km의 포심, 스윙입니다. 유격수 앞 땅볼

브룩스의 제52구, 바깥쪽에 날아오는 127km의 커브, 스트라이크입니다. 카운트는 0-1
브룩스의 제53구, 바깥쪽에 날아오는 123km의 커브, 스윙입니다. 2루수 앞 땅볼

브룩스의 제54구, 바깥쪽에 날아오는 132km의 체인지업, 스트라이크입니다. 카운트는 0-1
브룩스의 제55구, 바깥쪽에 날아오는 151km의 포심, 스트라이크입니다. 카운트는 0-2
브룩스의 제56구, 몸쪽에 날아오는 129km의 커브, 스윙입니다. 1루수 앞 땅볼

브룩스의 제57구, 바깥쪽에 날아오는 132km의 체인지업, 스트라이크입니다. 카운트는 0-1
브룩스의 제58구, 몸쪽에 날아오는 132km의 체인지업, 스트라이크입니다. 카운트는 0-2
브룩스의 제59구, 바깥쪽에 날아오는 147km의 투심, 스윙입니다. 파울이군요. 카운트는 0-2
브룩스의 제60구, 크게 벗어난 곳에 날아오는 148km의 투심, 볼입니다. 카운트는 1-2
브룩스의 제61구, 크게 벗어난 곳에 날아오는 152km의 포심, 볼입니다. 카운트는 2-2
브룩스의 제62구, 바깥쪽에 날아오는 134km의 체인지업, 볼입니다. 카운트는 3-2
브룩스의 제63구, 바깥쪽에 날아오는 135km의 체인지업, 스윙입니다. 2루수 앞 땅볼

브룩스의 제64구, 몸쪽에 날아오는 136km의 슬라이더, 볼입니다. 카운트는 1-0
브룩스의 제65구, 크게 벗어난 곳에 날아오는 151km의 포심, 볼입니다. 카운트는 2-0
브룩스의 제66구, 한가운데에 날아오는 147km의 투심, 스트라이크입니다. 카운트는 2-1
브룩스의 제67구, 바깥쪽에 날아오는 142km의 슬라이더, 볼입니다. 카운트는 3-1
브룩스의 제68구, 몸쪽에 날아오는 148km의 포심, 스윙입니다. 파울이군요. 카운트는 3-2
브룩스의 제69구, 바깥쪽에 날아오는 136km의 슬라이더, 스트라이크입니다.
삼진!

브룩스의 제70구, 한가운데에 날아오는 135km의 체인지업, 스윙입니다. 파울이군요. 카운트는 0-1
브룩스의 제71구, 크게 벗어난 곳에 날아오는 128km의 커브, 볼입니다. 카운트는 1-1
브룩스의 제72구, 크게 벗어난 곳에 날아오는 131km의 체인지업, 볼입니다. 카운트는 2-1
브룩스의 제73구, 바깥쪽에 날아오는 135km의 체인지업, 볼입니다. 카운트는 3-1
브룩스의 제74구, 몸쪽에 날아오는 135km의 체인지업, 볼입니다.
볼넷

브룩스의 제75구, 바깥쪽에 날아오는 136km의 슬라이더, 스윙입니다. 1루수 앞 땅볼

브룩스의 제76구, 몸쪽에 날아오는 147km의 투심, 스트라이크입니다. 카운트는 0-1
브룩스의 제77구, 한가운데에 날아오는 151km의 포심, 스트라이크입니다. 카운트는 0-2
브룩스의 제78구, 몸쪽에 날아오는 128km의 커브, 볼입니다. 카운트는 1-2
브룩스의 제79구, 바깥쪽에 날아오는 147km의 투심, 볼입니다. 카운트는 2-2
브룩스의 제80구, 바깥쪽에 날아오는 147km의 투심, 스윙입니다. 파울이군요. 카운트는 2-2
브룩스의 제81구, 크게 벗어난 곳에 날아오는 124km의 커브, 볼입니다. 카운트는 3-2
브룩스의 제82구, 몸쪽에 날아오는 149km의 투심, 볼입니다.
볼넷

브룩스의 제83구, 몸쪽에 날아오는 147km의 투심, 스트라이크입니다. 카운트는 0-1
브룩스의 제84구, 크게 벗어난 곳에 날아오는 151km의 포심, 볼입니다. 카운트는 1-1
브룩스의 제85구, 몸쪽에 날아오는 149km의 투심, 스윙입니다. 2루수 앞 땅볼

브룩스의 제86구, 몸쪽에 날아오는 131km의 체인지업, 스트라이크입니다. 카운트는 0-1
브룩스의 제87구, 바깥쪽에 날아오는 150km의 포심, 볼입니다. 카운트는 1-1
브룩스의 제88구, 바깥쪽에 날아오는 152km의 포심, 볼입니다. 카운트는 2-1
브룩스의 제89구, 크게 벗어난 곳에 날아오는 151km의 포심, 볼입니다. 카운트는 3-1
브룩스의 제90구, 몸쪽에 날아오는 135km의 체인지업, 스윙입니다. 파울이군요. 카운트는 3-2
브룩스의 제91구, 크게 벗어난 곳에 날아오는 142km의 슬라이더, 볼입니다.
볼넷

브룩스의 제92구, 몸쪽에 날아오는 151km의 포심, 스트라이크입니다. 카운트는 0-1
브룩스의 제93구, 바깥쪽에 날아오는 125km의 커브, 스트라이크입니다. 카운트는 0-2
브룩스의 제94구, 바깥쪽에 날아오는 124km의 커브, 스윙입니다. 헛스윙이군요.
삼진!

브룩스의 제95구, 바깥쪽에 날아오는 151km의 포심, 볼입니다. 카운트는 1-0
브룩스의 제96구, 바깥쪽에 날아오는 147km의 투심, 스윙입니다. 파울이군요. 카운트는 1-1
브룩스의 제97구, 한가운데에 날아오는 139km의 슬라이더, 스윙입니다. 파울이군요. 카운트는 1-2
브룩스의 제98구, 바깥쪽에 날아오는 140km의 슬라이더, 스윙입니다. 파울이군요. 카운트는 1-2
브룩스의 제99구, 바깥쪽에 날아오는 148km의 포심, 스윙입니다. 파울이군요. 카운트는 1-2
브룩스의 제100구, 바깥쪽에 날아오는 147km의 투심, 스트라이크입니다.
삼진!

브룩스의 제101구, 몸쪽에 날아오는 150km의 투심, 스트라이크입니다. 카운트는 0-1
브룩스의 제102구, 바깥쪽에 날아오는 148km의 투심, 스윙입니다. 3루수 앞 땅볼

브룩스의 오늘 투구는 여기까지였습니다.
오늘경기 브룩스의 투구수는 102개이고 스트라이크 62개, 볼 40개였습니다. 삼진은 7개를 기록하고, 볼넷은6개 허용했습니다.
```

[https://www.youtube.com/watch?v=kWiCuklohdY&t=9349s](https://www.youtube.com/watch?v=kWiCuklohdY&t=9349s)