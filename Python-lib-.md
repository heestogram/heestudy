💡 
파이썬에서 자주 쓰이는 라이브러리, 통계, 데이터 분석에 유용한 라이브러리들을 학습하고 정리한 페이지입니다. 
관심분야인 야구에 관한 응용문제를 직접 만들어 풀어보며 학습했습니다.

<br>


## 01. 텍스트 처리 서비스

### 01-01. textwrap

`textwrap.shorten` 함수는 문자열을 특정길이에 맞게 말줄임을 할 때 사용하는 함수이다.

`width` 매개변수를 15로 설정하면, 15글자만이 출력이 된다. 이 때 축약을 의미하는 [...]도 15에 포함된다. 또한 중간에 문자가 끊기지 않고 출력되게 하기 위해 15로 설정하더라도 그보다 짧거나 길 수가 있다.

```python
import textwrap
print(textwrap.shorten("군생활은 길고, 말년은 더 길다", width=15))

군생활은 길고, [...] 
#길이가 15이면 '군생활은 길고, 말[...]'이 될 텐데 이렇게 문자가 끊기는 것을 방지하기 위해 14글자만 출력됐다.
```

`placeholder` 매개변수를 무엇으로 설정하느냐에 따라 축약표시가 달라진다.

```python
print(textwrap.shorten("군생활은 길고, 말년은 더 길다", width=15, placeholder='~~~'))

군생활은 길고, 말년은~~~
```

`textwrap.fill` 함수는 문자열을 특정길이에 맞게 줄바꿈을 할 때 사용한다. `width` 매개변수에 입력한 바이트수를 기준으로 줄바꿈을 한다.

```python
text = "유구한 역사와 전통에 빛나는 우리 대한국민은 3·1운동으로 건립된 대한민국임시정부의 법통과 불의에 항거한 4·19민주이념을 계승하고, 조국의 민주개혁과 평화적 통일의 사명에 입각하여 정의·인도와 동포애로써 민족의 단결을 공고히 하고, 모든 사회적 폐습과 불의를 타파하며, 자율과 조화를 바탕으로 자유민주적 기본질서를 더욱 확고히 하여 정치·경제·사회·문화의 모든 영역에 있어서 각인의 기회를 균등히 하고, 능력을 최고도로 발휘하게 하며, 자유와 권리에 따르는 책임과 의무를 완수하게 하여, 안으로는 국민생활의 균등한 향상을 기하고 밖으로는 항구적인 세계평화와 인류공영에 이바지함으로써 우리들과 우리들의 자손의 안전과 자유와 행복을 영원히 확보할 것을 다짐하면서 1948년 7월 12일에 제정되고 8차에 걸쳐 개정된 헌법을 이제 국회의 의결을 거쳐 국민투표에 의하여 개정한다."
import textwrap
slicing = textwrap.fill(text,width=30)
print(slicing)

유구한 역사와 전통에 빛나는 우리 대한국민은
3·1운동으로 건립된 대한민국임시정부의 법통과 불의에
항거한 4·19민주이념을 계승하고, 조국의 민주개혁과
평화적 통일의 사명에 입각하여 정의·인도와 동포애로써
민족의 단결을 공고히 하고, 모든 사회적 폐습과 불의를
타파하며, 자율과 조화를 바탕으로 자유민주적 기본질서를
더욱 확고히 하여 정치·경제·사회·문화의 모든 영역에
있어서 각인의 기회를 균등히 하고, 능력을 최고도로
발휘하게 하며, 자유와 권리에 따르는 책임과 의무를
완수하게 하여, 안으로는 국민생활의 균등한 향상을
기하고 밖으로는 항구적인 세계평화와 인류공영에
이바지함으로써 우리들과 우리들의 자손의 안전과 자유와
행복을 영원히 확보할 것을 다짐하면서 1948년 7월
12일에 제정되고 8차에 걸쳐 개정된 헌법을 이제
국회의 의결을 거쳐 국민투표에 의하여 개정한다.
```

---

### 01-02. re - 정규표현식

아래와 같은 텍스트에 포함된 주민번호 뒷자리를 *문자로 변경하려 한다. 만약 평범하게 이 문제를 해결하려면 텍스트를 `split`하고, `for` 반복문을 사용하여 조건문을 걸어 복잡한 코드를 작성해야 한다.

하지만 `re` 모듈을 사용하면 보다 간단하게 해결할 수 있다.

```python
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
```

```python
import re
data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

#결과
홍길동의 주민번호는 800905-******* 입니다. 
그리고 고길동의 주민번호는 700905-******* 입니다.
그렇다면 누가 형님일까요?
```

`compile` 뒤에 작성한 문자열을 **정규표현식**이라고 한다. `compile`로 만든 객체(pat)에 `sub`함수를 사용하면 이 정규표현식의 문자열 일부분을 *로 바꿀 수 있다. 

`sub`함수의 `\g<1>` 은 정규표현식과 매치된 문자열 중 첫번째 그룹을 의미한다. 이렇게 그룹을 지정하기 위해 정규표현식에서 `(\d{6})`처럼 괄호를 묶어 그룹을 나타내줬다.

❓ **문제.** 
```
아래 텍스트에서 군번의 뒷 4자리를 &#42; 표시로 처리하라. 
”김희준 상병의 군번은 21-70003973입니다. 
홍길동 일병의 군번은 21-72004846입니다.”
```
💡 **정답.**


```python
import re
data = """
김희준 상병의 군번은 21-70003973입니다.
홍길동 일병의 군번은 21-72004846입니다.
"""
num = re.compile("(\d{2}[-]\d{4})\d{4}")
print(num.sub("\g<1>****", data))

#결과
김희준 상병의 군번은 21-7000****입니다.
홍길동 일병의 군번은 21-7200****입니다.
```

---

## 03. 데이터형

### 03-01. datetime

[`datetime.date`](http://datetime.date) 모듈은 년, 월, 일로 날짜를 표현할 때 사용하는 모듈이다. 2022년 12월 14일에서 2000년 12월 23일까지의 날짜 차이를 알아보자.

```python
import datetime
day1 = datetime.date(2022,12,14)
day2 = datetime.date(2000,12,23)

diff= day1-day2
print(diff)
print(diff.days)

#결과
8026 days, 0:00:00 #datetime.timedelta 객체
8026
```

두 날짜를 빼면 `datetime.timedelta` 객체가 리턴된다. 이 객체에서 days 함수를 적용하면 날짜만 출력해주는 것을 알 수 있다.

더 나아가 `datetime.datetime` 모듈을 사용하면 년, 월, 일, 시, 분, 초까지 표현할 수 있다.

`combine`함수를 사용하여 `datetime.date`와 `detetime.time`을 합칠 수도 있다.

```python
day3 = datetime.datetime(2022, 12, 14, 14, 10, 55)
print(day3)
print(day3.minute)

#결과
2022-12-14 14:10:55
10
```

요일은 [`datetime.date`](http://datetime.date) 객체의 `weekday` 함수를 사용하여 구할 수 있다. 0부터 월요일이고 6이 일요일이다. 만약 월요일을1, 일요일을 7로 리턴하게 하려면 `isoweekday()`를 사용할 수 있다.

```python
print(day1.weekday())
print(day1.isoweekday())

#결과
2 #수요일
3 #수요일
```

❓ **문제**. 
오늘 날짜에서 김희준 상병의 전역일(2022년 12월 14일)까지 남은 날짜를 구하시오. 
그리고 김희준이 태어난지 1000일째 되는 날과 요일을 언제인지 구하시오.


💡 **정답**.

```python
import datetime
today = datetime.date.today()
end_date = datetime.date(2022,12,14)
diff = end_date - today
print('전역까지 {}일 남았다!'.format(diff.days))
diff_days = datetime.timedelta(days=1000)
birthday = datetime.date(2000,12,23)
result = birthday + diff_days
print(result, result.weekday())

#결과
전역까지 277일 남았다!
2003-09-19 4

```

---

### 03-02. calendar.isleap -  윤년확인

윤년을 확인하는 함수는 조건문을 3개 중첩해서 만드는 번거로움이 있다.

하지만 `calendar` 모듈에는 간편한 `isleap` 함수가 있다.

```python
import calendar
print(calendar.isleap(2020))
print(calendar.isleap(2021))

#결과
True
False
```

---

### 03-03. collections.deque - 데크

`deque`는 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형이다.

```python
a = [1,2,3,4,5]
#위 리스트를 2만큼 오른쪽으로 회전하여 다음과 같은 리스트를 만들어보자.
a = [4,5,1,2,3]

from collections import deque
a = [1,2,3,4,5]
q = deque(a)
q.rotate(2)
print(q)
print(list(q))

#결과
deque([4, 5, 1, 2, 3])
[4, 5, 1, 2, 3]
```

`deque(a)`로 `deque` 객체를 만들어주고 여기에 `rotate` 함수를 적용하여 우측으로 회전시킬 수 있다. 좌측으로 회전시키려면 음수를 입력해주면 된다.

또한 `deque`는 리스트와 흡사하여 `append`, `pop`등의 함수를 동일하게 사용할 수 있다.

```python
d = deque([1,2,3,4])
d.append(5) #append는 마지막 index부터 채움
print(d)
d.appendleft(6) #appendleft는 가장 왼쪽 index부터 채움
print(d)
d.pop() #pop은 마지막 index를 삭제
print(d)
d.popleft() #popleft는 가장 왼쪽 index를 삭제
print(d)

#결과
deque([1, 2, 3, 4, 5])
deque([6, 1, 2, 3, 4, 5])
deque([6, 1, 2, 3, 4])
deque([1, 2, 3, 4])
```

---

### 03-04. collections.namedtuple

`tuple`은 인덱스를 통해서만 데이터에 접근이 가능하지만, `namedtuple`은 인덱스뿐만 아니라 key값으로도 데이터 접근이 가능한 자료형이다.

아래와 같은 튜플들을 key값으로 접근해보자.

```python
data = [
        ('양현종', 54, 'starting pitcher'),
        ('최형우', 34, 'designated hitter'),
        ('김선빈', 3, 'shortstop')
]
```

첫번째 매개변수는 객체로 만들어주는 것과 같은 이름을 입력한다. 뒤에 따라오는 콤마로 연결된 것들은 `player`의 속성이 된다.

```python
from collections import namedtuple
player = namedtuple('player', 'name, number, position')
```

그리고 아래처럼 `namedtuple`의 객체로 데이터를 변환해준다. 두 가지 방식 모두 같은 결과를 만든다. 아래의 `_make`함수는 튜플의 요소가 여러개일 때 특히 유용하다.

```python
data = [player(pla[0], pla[1], pla[2]) for pla in data]
data = [player._make(pla) for pla in data]
```

```python
pla = data[0]
print(pla.name) #이제 name이란 key로 데이터에 접근이 가능해졌다.
print(pla.position)
print(pla)

#결과
양현종
starting pitcher
player(name='양현종', number=54, position='starting pitcher')
```

그리고 네임드튜플도 튜플처럼 값을 변경할 수 없는 immutable 특성을 갖고 있다. 때문에 값을 그냥 변경할 수는 없고, `_replace`함수를 사용해줘야만 가능하다.

---

### 03-05. collections.Counter - 동일한 요소의 개수

`collections.Counter`클래스는 리스트나 문자열에서 동일한 값의 요소가 몇개 있는지 세주는 기능을 한다.

아래 고려대 사회학과 학과장 인사말에서 빈도수가 가장 높은 단어를 출력해보자.

```python
data = """
반갑습니다. 저희 고려대 사회학과는 국내 최대 규모의 학생 수를 자랑하며, 다양한 세부
분야의 뛰어난 교수진을 보유하고 있습니다. 1963년 창설된 이래 저희 사회학과는 5천여
명에 달하는 졸업생을 배출하였으며, 이들은 정부와 기업을 비롯하여 정치, 언론, 방송,
문화, 학술, 예술 등의 분야에서 빼어난 능력을 발휘하고 있습니다.  세계화와 정보화의
급변하는 세계를 이해하고 대처하는 데 있어 사회학은 중요한 역할을 할 수 있습니다. 또한
한국사회는 압축적 고도성장의 시대가 저물어가면서 그동안 누적되어온 부작용과 새로운
사회문제의 등장으로 복합적 위기국면에 들어서고 있습니다. 저출산-고령화, 고용불안정에 따른
사회적 불안의 심화, 삶의 질과 환경에 대한 관심의 증대와 같은 전환기의 당면과제들은 다른
어떤 학문분야보다 사회학의 적극적 역할을 필요로 하고 있습니다.  사회학은 개인의 문제를
공적 이슈로 전환시키는 비판적 관점과 상상력을 제공하고, 다원적 민주사회에 필요한 성숙한
시민의식을 배양시키며, 다양한 자료를 과학적으로 분석할 수 있는 방법론을 습득케 하며,
단편적 현실을 체계적이고 깊이 있게 이해할 수 있도록 하는 다양한 이론을 제공합니다.
2014년 저희 사회학과는 학부제에서 학과제로 전환하여 학부생들의 결속력을 높이고, 학부
커리큘럼 개편을 통해 정치, 경제, 사회, 문화의 4개 영역과 관련된 다양한 수업을
제공함으로써 체계적이고 포괄적인 교육과정을 수립하였습니다. 또한 거의 모든 대학원생들이
장학금을 받고 있을 정도로, 최고의 교육환경을 제공하고자 노력하고 있습니다. 고려대
사회학과에 대한 계속적인 성원과 관심 부탁드립니다. 감사합니다.
"""
```

우선 문장을 단어별로 나누기 위해 `re`의 `findall`함수를 사용했다.

정규식에서 `\w+`은 단어를 의미하므로 `refindall`에 의해 data에서 모든 단어가 `words`로 반환된다. 

그리고 `words`를 활용하여 `Counter` 객체를 만들고, `most_common` 함수를 이용해 매개변수를 1로 지정하여 가장 빈도수가 높은 한 단어를 출력한다.

```python
from collections import Counter
import re
words = re.findall(r'\w+', data)
Counter =  Counter(words)
print(Counter.most_common(1))

#결과
[('있습니다', 6)]
```

빈도수가 가장 높은 5개를 출력하려면 아래와 같이 한다.

```python
print(Counter.most_common(5))

#결과
[('있습니다', 6), ('다양한', 4), ('저희', 3), ('사회학과는', 3), ('수', 3)]
```

---

### 03-06. collections.defaultdict

다음과 같은 문자열이 있을 때 문자열의 각 단어의 개수를 value로 갖는 딕셔너리를 만들려고 한다.

```python
Life is too short, You need python.
{'L': 1, 'i': 2, 'f': 1, 'e': 3, ' ': 6, 's': 2, 't': 3, 'o': 5, 'h': 2, 'r': 1, ',': 1, 'Y': 1, 'u': 1, 'n': 2, 'd': 1, 'p': 1, 'y': 1, '.': 1}
```

클래식한 방법은 아래와 같은 반복문이다.

```python
d = dict()
for c in text:
    if c not in d:
        d[c] = 0
    d[c] += 1
```

여기서 `d[c] = 0` 부분은 초깃값을 설정해줌으로써 반복문이 오류가 없도록 한다.

하지만 이렇게 초깃값을 설정하지 않더라도 딕셔너리를 `defaultdict()`로 생성하면 자동으로 이 과정을 생략하고 오류도 발생하지 않는다.

```python
from collections import defaultdict
d = defaultdict(int) #초깃값을 정수로 설정해주기 위해 int 입력
for c in text:
  d[c] +=1
print(d)
```

---

### 03-07. pprint - 예쁘게 출력하기

아래와 같은 딕셔너리는 길이가 너무 길어 가독성이 떨어진다.

```python
result = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
```

`pprint`를 사용하면 이를 정돈되게 출력할 수 있다.

```python
import pprint
pprint.pprint(result)

#결과
{'body': 'quia et suscipit\n'
         'suscipit recusandae consequuntur expedita et cum\n'
         'reprehenderit molestiae ut ut quas totam\n'
         'nostrum rerum est autem sunt rem eveniet architecto',
 'id': 1,
 'title': 'sunt aut facere repellat provident occaecati excepturi optio '
          'reprehenderit',
 'userId': 1}
```

---

### 03-08. bisect - 이진 탐색

한 학급 학생들의 점수가 [33, 99, 77, 70, 89, 90, 100]라고 할 때, 등급의 기준이 아래와 같다고 하자.

- 90점 이상 : A
- 80점 이상 : B
- 70점 이상 : C
- 60점 이상 : D
- 0~59점 : F

이 문제를 해결하기 위해선 `if`를 사용한 분기문을 작성하는 방법도 있지만, `bisect`를 사용하면 훨씬 간편하고 우아하게 코드를 짤 수 있다.

`bisect` 함수의 첫번째 매개변수에는 등급의 기준을 리스트로 입력하고, 두번째 매개변수엔 점수 데이터를 입력한다.

그리고 등급명을 `grade` 객체에 담아주기 위해 아래처럼 코드를 작성한다.

```python
import bisect
result = []
for score in [33, 99, 77, 70, 89, 90, 100]: 
  pos = bisect.bisect([60,70,80,90], score) 
  grade = 'FDCBA'[pos]
  result.append(grade)
print(result)
```

만약 ‘이상’이 아니라 ‘초과’라면 `bisect`함수가 아니라  `bisect_left`함수를 사용하면 된다.

❓ **문제.** 
```
MLB API를 기반으로 보스턴 레드삭스 현역 투수들의 통산 볼넷삼진비율을 A~F등급으로 나눠보자. (4.0 이상 S / 3.5 이상 A / 2.5 이상 B / 2.0 이상 C / 1.5 이상 D / 1.5 미만 F) 최종결과값은 선수이름을 key로 하고 등급을 value로 하는 딕셔너리로 만들어라.
```
💡 **정답.**


```python

d=dict()
#2021 정규시즌 출전 선수중에
for n in statsapi.get('sports_players',{'season':2021, 'gameType':'R'})['people']:
  #보스턴 선수이고 투수인 선수를 뽑아서
  if n['currentTeam']['id'] == 111 and n['primaryPosition']['code'] =='1':
    #이 선수의 fullname을 key로 하고 strikeoutwalkratio를 value로 하는 딕셔너리를 만든다
    d[n['fullName']] = float(statsapi.player_stat_data(n['id'],'pitching','career')['stats'][0]['stats']['strikeoutWalkRatio'])

import bisect
swr = d.values() #value(볼넷삼진비율)만 리스트로 만든다
result = []
for score in swr:
  pos = bisect.bisect([1.5, 2.0, 2.5, 3.5, 4.0], score)
  grade = 'FDCBAS'[pos]
  result.append(grade)
print(result)

i=0
result_ = dict() #최종결과를 출력할 딕셔너리를 만든다
for n in d.keys():
  result_[n] = result[i] #앞서 만든 등급 리스트의 인덱스 순대로 선수 이름을 매칭시킨다
  i+=1

import pprint
pprint.pprint(result_) #예쁘게 출력한다

#결과
{'Adam Ottavino': 'B',
 'Austin Brice': 'C',
 'Austin Davis': 'C',
 'Brad Peacock': 'C',
 'Brandon Brennan': 'D',
 'Brandon Workman': 'C',
 'Chris Sale': 'S',
 'Colten Brewer': 'D',
 'Connor Seabold': 'F',
 'Darwinzon Hernandez': 'D',
 'Eduard Bazardo': 'D',
 'Eduardo Rodriguez': 'B',
 'Garrett Richards': 'C',
 'Garrett Whitlock': 'S',
...중략...
 'Yacksel Rios': 'D'}
```

---

### 03-09. enum - 상수 집합

`enum`은 서로 관련이 있는 여러 개의 상수 집합을 정의할 때 사용하는 모듈이다.

날짜를 입력하면 그 날짜의 요일에 해당되는 메뉴를 리턴하는 함수를 아래와 같이 정의해보자.

```python
from datetime import date
def get_menu(input_date):
    weekday = input_date.isoweekday()  # 1:월요일, 2:화요일, ... , 7: 일요일
    if weekday == 1:
        menu = "김치찌개"
    elif weekday == 2:
        menu = "비빔밥"
    elif weekday == 3:
        menu = "된장찌개"
    elif weekday == 4:
        menu = "불고기"
    elif weekday == 5:
        menu = "갈비탕"
    elif weekday == 6:
        menu = "라면"
    elif weekday == 7:
        menu = "건빵"
    return menu
print(get_menu(date(2020, 12, 6)))
print(get_menu(date(2020, 12, 18)))

#결과
건빵
갈비탕
```

위 코드는 요일을 나타내는 숫자 1~7이라는 매직넘버(상수로 선언하지 않은 숫자)를 사용하고 있다. 그러나 이러한 매직넘버를 코드의 가독성을 떨어뜨리기에 지양해야 한다.

```python
from enum import IntEnum
class week(IntEnum):
  MONDAY=1
  TUESDAY=2
  WEDNESDAY=3
  THURSDAY=4
  FRIDAY=5
  SATURDAY=6
  SUNDAY=7

def get_menu(input_date):
  menu = {
      week.MONDAY: "김치찌개",
      week.TUESDAY: "비빔밥",
      week.WEDNESDAY: "된장찌개",
      week.THURSDAY: "불고기",
      week.FRIDAY: "갈비탕",
      week.SATURDAY: "라면",
      week.SUNDAY: "건빵"
  }
  return menu[input_date.isoweekday()]
print(get_menu(date(2021,3,15)))
print(get_menu(date(2022,3,15)))

#결과
김치찌개
비빔밥
```

위와 같이 `enum.IntEnum`을 상속받아 `week`클래스를 만들면 유지보수에 유리하며 가독성도 좋아진다.

---

### 03-10. graphlib.TopologicalSorter - 위상정렬

![Untitled](https://user-images.githubusercontent.com/115082062/201685939-c2370ace-250d-4dca-a442-478c57da705a.png)


- 규칙1: 주황색 화살표
- 규칙2: 초록색 화살표
- 규칙3: 파란색 화살표

영어 수업의 선수강 규칙이 위와 같다고 할 때, 5개의 수업을 어떤 순서로 수강해야 하는지를 알려고 한다.

이는 `graphlib`의 `TopologicalSorter`를 이용하여 위상정렬을 쓰면 쉽게 해결할 수 있다.

`add(노드, 선행노드)` 함수는 어떤 노드의 선행노드를 추가할 때 사용하는 함수이다. 선행노드는 여러개를 입력할 수도 있다.

```python
from graphlib import TopologicalSorter
ts = TopologicalSorter()

#규칙1
ts.add('영어중급', '영어초급') #영어중급의 선수과목은 영어초급
ts.add('영어고급', '영어중급')

#규칙2
ts.add('영어문법', '영어중급')
ts.add('영어회화', '영어문법')

#규칙3
ts.add('영어회화', '영어문법')
print(list(ts.static_order()))

#결과
['영어초급', '영어중급', '영어문법', '영어고급', '영어회화']
```

---

## 04. 숫자와 수학모듈

### 04-01 math.gcd - 최대공약수

`math.gcd` 함수는 최대공약수를 구하는 함수이다. 인수에 숫자를 입력하면 그 숫자들의 최대공약수를 출력해준다.

사탕 60개와 초콜릿 100개 그리고 젤리 80개를 각각 나누어 똑같이 봉지에 나누어 담으려고 한다. 최대한으로 만들수 있는 봉지의 개수를 구해보자.

```python
import math
math.gcd(60,100,80)

#결과
20
```

---

### 04-02. math.icm - 최소공배수

`math.icm` 함수는 최소공배수를 구하는 함수이다. 인수에 숫자를 입력하면 그 숫자들의 최소공배수를 출력해준다.

```python
import math
math.icm(15,25) #15와 25의 최소공배수

#결과
75

```

---

### 04-03. decimal.Decimal -  정확한 소수점 연산

`decimal.Decimal` 모듈은 숫자를 10진수로 처리하여 정확한 소수점 자릿수를 표현할 때 사용하는 모듈이다.

이진수 기반의 파이썬 float 연산은 미세한 오차가 발생한다. 아래 결과가 이상한 것을 보자.

```python
print(0.1*3)
print(1.2-0.1)
#결과
0.30000000000000004
1.0999999999999999
```

이를 해결하기 위해 `decimal.Decimal` 모듈을 사용하자. 

인수를 넣을 땐 반드시 **문자열**로 써줘야 한다!

```python
from decimal import Decimal
print(Decimal('0.1')*3)
print(Decimal('1.2')-Decimal('0.1'))

#결과
0.3
1.1
```

결과가 잘 출력됐다. Decimal 자료형은 다시 float형으로 변환할 수 있다.

```python
print(float(Decimal('0.1')*3))
print(float(Decimal('1.2')-Decimal('0.1')))
```

Decimal은 정확성을 향상시키기 위해 고정소수점을 사용하여 메모리를 많이 사용하기 때문에 모든 float연산을 Decimal로 바꾸는 것은 좋은 방법이 아니다. 

Decimal은 보통 한치의 오차도 허용하지 않는 금융권 또는 재무/회계 관련 프로그램을 작성할 때 사용하는 것이 유리하다.

---

### 04-04. fractions - 유리수

파이썬에서 유리수를 그냥 더하면 미세한 오차가 생긴다. 때문에 `fractions.Fraction`을 사용해줘야 한다.

```python
from fractions import Fraction
a = Fraction(1,5)
b = Fraction(2,5)
print(a.numerator) #분자의 값
print(a.denominator) #분모의 값
print(a+b)
print(float(a+b))

#결과
1
5
3/5
0.6
```

---

### 04-05. random - 난수 생성

`random` 모듈은 난수를 생성할 때 사용하는 모듈이다. 

6개의 숫자로 이루어진 로또 번호를 무작위로 생성해 주는 프로그램을 작성해보자. 이 때 숫자는 중복될 수 없다.

`random.randint` 함수는 임의의 숫자를 생성해준다.

```python
import random
result = []
while len(result) <6:
  num = random.randint(1,45)
  if num not in result:
    result.append(num)
print(result)
```

리스트의 순서를 무작위로 섞고 싶을 땐 `shuffle`함수를 사용하고, 랜덤으로 하나를 선택하려면 `choice`함수를 사용한다.

```python
a = [1,2,3,4,5]
random.shuffle(a)
print(a)
print(random.choice(a))

#결과
[3, 5, 4, 1, 2]
4
```

---

### 04-06. statistics - 평균값과 중앙값

평균값은 `statistics.mean`을 이용하여 구할 수 있고, 중앙값은 `statistics.median`을 이용하여 구할 수 있다.

❓ **문제**
```
2021 보스턴 레드삭스의 투수들의 통산 whip를 나열하고, 이 값의 평균과 중앙값을 출력하라.
```
💡 **정답**.


```python
whip = []
for n in statsapi.get('sports_players',{'season':2021, 'gameType':'R'})['people']:
  #보스턴 선수이고 투수인 선수를 뽑아서
  if n['currentTeam']['id'] == 111 and n['primaryPosition']['code'] =='1':
    #스탯 값은 문자열로 출력되니 float을 이용하여 실수로 만든다.
    whip.append(float(statsapi.player_stat_data(n['id'], 'pitching', 'career')['stats'][0]['stats']['whip'])) 
print(whip)

import statistics
print(statistics.mean(whip))
print(statistics.median(whip))

#결과
1.6066666666666667
1.3599999999999999
```

---

## 05. 함수형 프로그래밍 모듈

### 05-01. itertools.cycle

`itertools.cycle(iterable)`함수는 `iterable`을 순서대로 무한히 반복시키는 이터레이터를 생성하는 함수이다.

```python
import itertools
pool = itertools.cycle(['양현종', '놀린', '로니', '이의리','윤중현'])
next(pool) #출력할 때마다 순서대로 바뀜.
```

위 코드의 `next`함수는 파이썬 자체 내장 함수로, 이터레이터의 다음 요소를 리턴하는 함수이다.

---

❓ **문제.**
```
기아 타이거즈의 선발 로테이션은 ['양현종', '놀린', '로니', '이의리','윤중현']이다. 
프로야구 개막일(2022년 4월 2일)부터 6월 2일까지 로테이션이 예외없이 돌아간다고 가정할 때, 
각 날짜에 맞는 선발투수를 나열하라. 
이 때 `itertools`와 `datetime` 모듈을 사용하고, 월요일은 야구가 없는 날이니 로테이션을 건너뛴다.
예시) 
2022-04-04 야구가 없는 월요일입니다.
2022-04-05 선발투수는 로니.
```

💡 **정답.**


```python
import itertools
pool = itertools.cycle(['양현종', '놀린', '로니', '이의리','윤중현'])

import datetime
open = datetime.date(2022,4,2)
close = datetime.date(2022,6,2)
days = close - open

for n in range(days.days):
  matchday = open+datetime.timedelta(days=n)
  if matchday.weekday()==0:
    print(matchday,"야구가 없는 월요일입니다.")
  else:
    print(matchday, "선발투수는 {}".format(next(pool)))

#결과
2022-04-02 선발투수는 양현종
2022-04-03 선발투수는 놀린
2022-04-04 야구가 없는 월요일입니다.
2022-04-05 선발투수는 로니
2022-04-06 선발투수는 이의리
2022-04-07 선발투수는 윤중현
2022-04-08 선발투수는 양현종
...중략...
2022-05-27 선발투수는 로니
2022-05-28 선발투수는 이의리
2022-05-29 선발투수는 윤중현
2022-05-30 야구가 없는 월요일입니다.
2022-05-31 선발투수는 양현종
2022-06-01 선발투수는 놀린

```

---

### 05-02. itertools.accumulate - 누적합 계산

`itertools.accumulate(iterable)` 함수는 `iterable`의 누적합을 계산하여 이터레이터로 리턴하는 함수이다.

한 회사의 월별 매출이 다음과 같다고 하자. 이 때 월별 누적합을 계산하려면 `itertools.accumulate()`함수를 사용하면 된다.

```python
monthly_income = [1161,1814,1270,2256,1413,1842,2221,2207,2450,2823,2540,2134]

import itertools
result = list(itertools.accumulate(monthly_income))
print(result)
```

---

❓ **문제**. 
```
KIA 최원준의 2021시즌 월별 안타개수는 다음 딕셔너리와 같다
`choi_hit = {'4월':29, '5월':35, '6월':23, '7월':5, '8월':12, '9월':35, '10월':35}`
이 때 최원준의 월별 누적안타를 딕셔너리 형태로 출력하라.
```

💡 **정답.**

```python
choi_hit = {'4월':29, '5월':35, '6월':23, '7월':5, '8월':12, '9월':35, '10월':35}
hit_list = choi_hit.values()
result = list(itertools.accumulate(hit_list))
choi_hit_acc = dict()
i=0
for n in range(4,11):
  choi_hit_acc["{}월까지 누적 안타".format(n)]=result[i]
  i+=1
print(choi_hit_acc)

#결과
{'4월까지 누적 안타': 29, '5월까지 누적 안타': 64, '6월까지 누적 안타': 87, '7월까지 누적 안타': 92, '8월까지 누적 안타': 104, '9월까지 누적 안타': 139, '10월까지 누적 안타': 174}
```

---

### 05-03. itertools.groupby - 키값으로 분류

`itertools.groupby(iterable, key=None)` 함수는 `iterable`을 `key`값으로 분류한 결과를 리턴하는 함수이다.

다음과 같이 선수이름과 포지션이 key로 주어진 딕셔너리의 묶음을 생각해보자. 이 때 포지션별로 분류해보자.

```python
data = [
        {'name':'양현종', 'pos': 'p'},
        {'name':'김선빈', 'pos': '2b'},
        {'name':'김도영', 'pos': 'ss'},
        {'name':'박찬호', 'pos': 'ss'},
        {'name':'이승재', 'pos': 'p'},
        {'name':'나성범', 'pos': 'of'},
        {'name':'소크라테스', 'pos': 'of'},
        {'name':'윤중현', 'pos': 'p'},
]
```

우선 data를 포지션별로 sort해야 한다.

```python
import operator
data = sorted(data, key=operator.itemgetter('pos'))
```

이제 `itertools.groupby`로 포지션별 그룹을 나눈다. (분류기준, 분류기준으로 묶인 데이터) 튜플을 반환하기 때문에 아래 반복문으로 딕셔너리를 만들어줄 수 있다.

```python
grouped_data = itertools.groupby(data, key=operator.itemgetter('pos'))

result = {}
for key, group_data in grouped_data:
  result[key] = list(group_data)
import pprint
pprint.pprint(result)

#결과
{'2b': [{'name': '김선빈', 'pos': '2b'}],
 'of': [{'name': '나성범', 'pos': 'of'}, {'name': '소크라테스', 'pos': 'of'}],
 'p': [{'name': '양현종', 'pos': 'p'},
       {'name': '이승재', 'pos': 'p'},
       {'name': '윤중현', 'pos': 'p'}],
 'ss': [{'name': '김도영', 'pos': 'ss'}, {'name': '박찬호', 'pos': 'ss'}]}
```

---

❓ **문제.** 
```
2021시즌 LAA의 선수들을 포지션별로 그룹화하여 나타내려고 한다. 
데이터는 MLB API를 이용하고, itertools 모듈을 활용하여 그룹화하라
```
💡 **정답.**


```python
#데이터 가져오기
import pprint
player={}
for n in statsapi.get('sports_players',{'season':2021, 'gameType':'R'})['people']:
  if n['currentTeam']['id'] == 108: #팀id가 108(LAA)인 팀일 경우
    player['name'] = n['fullName'] #'name' 키에 선수 이름을 value로
    player['pos'] = n['primaryPosition']['abbreviation'] #'pos' 키에 선수 포지션 약어를 value로
    pprint.pprint(player)

#그룹화
import operator
import itertools
data = sorted(data, key=operator.itemgetter('pos'))
grouped_data = itertools.groupby(data, key=operator.itemgetter('pos'))

result = {}
for key, group_data in grouped_data:
  result[key] = list(group_data)
pprint.pprint(result)

#결과
{'1B': [{'name': 'Jared Walsh', 'pos': '1B'}],
 '2B': [{'name': 'David Fletcher', 'pos': '2B'},
        {'name': 'Kean Wong', 'pos': '2B'}],
 '3B': [{'name': 'Phil Gosselin', 'pos': '3B'},
        {'name': 'Anthony Rendon', 'pos': '3B'},
        {'name': 'Jose Rojas', 'pos': '3B'}],
 'C': [{'name': 'Anthony Bemboom', 'pos': 'C'},
       {'name': 'Drew Butera', 'pos': 'C'},
       {'name': 'Jack Kruger', 'pos': 'C'},
       {'name': 'Max Stassi', 'pos': 'C'},
       {'name': 'Kurt Suzuki', 'pos': 'C'},
       {'name': 'Matt Thaiss', 'pos': 'C'}],
 'CF': [{'name': 'Juan Lagares', 'pos': 'CF'},
        {'name': 'Brandon Marsh', 'pos': 'CF'},
        {'name': 'Mike Trout', 'pos': 'CF'}],
 'LF': [{'name': 'Jo Adell', 'pos': 'LF'},
        {'name': 'Justin Upton', 'pos': 'LF'}],
 'OF': [{'name': 'Jon Jay', 'pos': 'OF'},
        {'name': 'Scott Schebler', 'pos': 'OF'}],
 'P': [{'name': 'Jaime Barria', 'pos': 'P'},
       {'name': 'Dylan Bundy', 'pos': 'P'},
       {'name': 'Griffin Canning', 'pos': 'P'},
       {'name': 'Steve Cishek', 'pos': 'P'},
       {'name': 'Alex Claudio', 'pos': 'P'},
       {'name': 'Alex Cobb', 'pos': 'P'},
...생략...
```

---

### 05-04. itertools.zip_longest - 사이즈가 큰 것을 기준으로 묶기

만약 다음에 주어진 두 리스트를 zip한다면 아래처럼 ‘이광수’, ‘김승민’은 짝을 찾지 못한다.

```python
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
rewards = ['사탕', '초컬릿', '젤리']
result = zip(students, rewards)
print(list(result))
#결과
[('한민서', '사탕'), ('황지민', '초컬릿'), ('이영철', '젤리')]
```

이런 경우 `itertools.zip_longest(iterables, fillvalue)`함수를 사용하면 짝을 찾지 못한 것을 `fillvalue`에 입력한 값으로 채워준다.

```python
import itertools
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
rewards = ['사탕', '초컬릿', '젤리']
result = itertools.zip_longest(students, rewards, fillvalue='새우깡')
print(list(result))

#결과
[('한민서', '사탕'), ('황지민', '초컬릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]
```

---

### 05-05. itertools.permutations - 순열

[’1’, ‘2’, ‘3’]이라는 세 장의 카드 중 두 장을 뽑아 만들 수 있는 두 자리 수를 구해보자. 이는 순열 3P2와 같다.

순열을 구하는 함수는 `itertools.permutations()`이다.

```python
import itertools
for a,b in list(itertools.permutations(['1','2','3'],2)):
  print(a+b)

#결과
12
13
21
23
31
32
```

순열이 아닌 **조합**을 알고 싶으면 `itertools.combinations()`를 사용하면 된다.

중복을 허용하는 중복조합은 `itertools.combinations_with_replacement`를 사용하면 된다.

---

### 05-06. functools.partial - 인수를 지정하여 함수 재정의

`functools.partial`함수는 하나 이상의 인수가 이미 채워진 함수의 새 버전을 만들 때 사용하는 함수이다.

다음 코드는 `choice` 매개변수에 따라 `*args` 인수를 합하거나 곱하는 함수이다.

```python
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5))

#결과
15
120
```

만약 여기서 `choice` 매개변수를 미리 지정해놓고 add(1,2,3,4,5)만으로 15를 출력하는 함수를 만들려면 `partial`을 사용하면 된다.

```python
add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')

print(add(1,2,3,4,5))  # 15 출력
print(mul(1,2,3,4,5))  # 120 출력
```

---

### 05-10. funtools.reduce

`functools.reduce(function, iterable)`함수는 function을 iterable의 요소에 차례로(왼쪽에서 오른쪽으로) 누적 적용하여 iterable을 단일 값으로 줄여나가는 함수이다.

다음 함수는 data의 모든 요소를 더하는 함수이다.

```python
def add(data):
    result = 0
    for i in data:
        result += i
    return result
```

`functools.reduce`를 사용하면 이와 동일한 기능을 하는 함수를 만들 수 있다.

`reduce`는 `lambda`함수를 `data`의 가장왼쪽부터 차례로 수행하는 기능을한다. 아래 예시에선 ((((1+2)+3)+4)+5)처럼 기능한다.

```python
import functools
data = [1,2,3,4,5]
result = functools.reduce(lambda x, y: x+y, data)
print(result)
```

같은 원리로 아래 코드는 최댓값을 구한다.

```python
num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)
```

---

### 05-11. operator.itemgetter - 다중 수준 정렬

선수 명단이 다음과 같이 튜플로 주어질 때 등번호순으로 정렬을 해보자.

```python
player = [
          ("양현종", 54, 'P'),
          ("김도영", 5, 'SS'),
          ("최형우", 34, 'DH'),
          ("소크라테스", 30, "CF")
]
```

이 문제는 `sorted` 함수의 key 매개변수에 `itemgetter(1)`을 지정하면 된다. 여기서 1은 튜플의 두번째 요소를 의미한다.

```python
from operator import item
sorted_player = sorted(player, key=itemgetter(1))
print(sorted_player)

#결과
[('김도영', 5, 'SS'), ('소크라테스', 30, 'CF'), ('최형우', 34, 'DH'), ('양현종', 54, 'P')]
```

만약에 정렬대상이 튜플이 아니라 딕셔너리라면 `itemgetter()`의 인수에 인덱싱 번호가 아니라 key 이름을 입력해야 한다.

```python
from operator import itemgetter
player = [
          {"name":"양현종", "num":54, "pos":'P'},
          {"name":"김도영", "num":5, "pos":'SS'},
          {"name":"최형우", "num":34, "pos":'DH'},
          {"name":"소크라테스", "num":30, "pos":"CF"}
]

sorted_player = sorted(player, key=itemgetter('num'))
print(sorted_player)
```

## 부록

### 01. 클로저와 데코레이터

어떤 수에 항상 3을 곱해서 리턴하는 함수, 항상 5를 곱해서 리턴하는 함수를 만들려면 일일이 함수를 만들기보다 아래처럼  클래스를 형성하는 것이 효율적이다.

```python
class Mul:
    def __init__(self, m):
        self.m = m

    def mul(self, n):
        return self.m * n

if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3.mul(10))  # 30 출력
    print(mul5.mul(10))  # 50 출력
```

하지만 **클로저**를 활용하면 더 간편하게 동일한 함수를 만들 수 있다.

**클로저**는 간단히 말해 함수 내에 내부 함수(inner function)를 구현하고 그 내부 함수를 리턴하는 함수를 말한다.

```python
def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

if __name__ == "__main__":
    mul3 = mul(3) #3은 m에 저장하는 인수
    mul5 = mul(5) #5는 m에 저장하는 인수

    print(mul3(10))  #10은 n
    print(mul5(10))  #10은 n

#결과
30
50
```

여기서 `mul()`이 외부함수, `wrapper()`이 내부함수이다. `mul()`함수에서 호출한 m은 `wrapper()`함수에 그대로 내장되어 활용된다.

```python
import time
def elapsed(original_func):
  def wrapper():
    start = time.time()
    result = original_func()
    end = time.time()
    print("함수 수행시간: %f 초"%(end-start))
    return result
  return wrapper

def myfunc():
  print("함수가 실행됩니다.")

decorated_myfunc = elapsed(myfunc)
decorated_myfunc()

#결과
함수가 실행됩니다.
함수 수행시간: 0.000120 초
```

위 코드는 `elapsed` 함수로 만든 클로저이다. 외부함수인 `elapsed()`는 함수를 인수로 받는다. 내부함수인 `wrapper()`는 함수의 수행시간을 알려주면서 외부함수의 인수 함수도 리턴해준다.

클로저를 이용하면 기존 함수에 뭔가 추가적인 부가 기능을 덧붙이기가 아주 편리하다. 이렇게 기존 함수의 변경 없이 추가적인 기능을 덧붙일 수 있도록 해 주는 `elapsed` 함수와 같은 클로저를 **데코레이터(Decorator)**라고 한다.

아래 코드는 위 코드에서 `@elapsed`라는 어노테이션을 추가한 것이다. 이처럼 함수명 바로 위에 어노테이션을 넣으면 이를 데코레이터 함수로 인식한다. 따라서 `myfunc()`함수는 `elapsed()`함수의 호출 없이도 데코레이터로 기능한다.

```python
import time
def elapsed(original_func):
  def wrapper():
    start = time.time()
    result = original_func()
    end = time.time()
    print("함수 수행시간: %f 초"%(end-start))
    return result
  return wrapper

@elapsed
def myfunc():
  print("함수가 실행됩니다.")
myfunc()

#결과
함수가 실행됩니다.
함수 수행시간: 0.000120 초
```

만약 `myfunc()`에 인수를 입력하고 싶다면 아래와 같이 `*args`, `**kwargs`를 사용해야 한다. `*args`는 모든 입력 인수를 튜플로 변환해 주는 매개변수이고 `**kwargs`는 모든 key=value 형태의 입력 인수를 딕셔너리로 변환해 주는 매개변수이다.

```python
import time
def elapsed(original_func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = original_func(*args, **kwargs)
    end = time.time()
    print("함수 수행시간: %f 초"%(end-start))
    return result
  return wrapper

@elapsed
def myfunc(text):
  print("'%s'을 출력합니다."%text)
myfunc("I love you")

#결과
'I love you'을 출력합니다.
함수 수행시간: 0.000135 초
```

---

### 02. 이터레이터와 제너레이터

반복구문으로 돌릴 수 있는 리스트와 같은 객체를 `iterable`이라 한다.

**이터레이터(iterator)**란 next함수 호출 시 그 다음 값을 리턴해주는 객체이다.

리스트는 iterable하지만, 이터레이터는 아니다. 따라서 리스트를 이터레이터로 만들려면 `iter()`함수로 감싸야 한다.

```python
a = [1,2,3]
ia = iter(a)
print(next(ia))
print(next(ia))
print(next(ia))

#결과
1
2
3
```

이터레이터는 한번 값을 읽어오면 다시는 그 값을 읽어올 수 없다는 특징이 있다. 따라서 이터레이터에 대해 for 반복문을 한 번 작동시킨 후에 다시금 반복문을 작동하면 값을 읽어올 수 없다.

보통 함수는 하나의 값을 리턴한다. 그 값은 정수, 리스트, 딕셔너리등이 될 수 있을 것이다. 그런데 만약 함수가 하나의 값을 리턴하는 것이 아니라 연속된 값을 순차적으로 리턴할 수 있다면 어떨까?

이러한 개념에서 만들어진 것이 바로 **제너레이터(generator)**이다.

```python
def mygen():
  yield 'a'
  yield 'b'
  yield 'c'

g = mygen()

print(g) #'a'
print(g) #'b'
print(g) #'c'
print(g) #오류
```

`yield` 구문은 여러 값을 리턴해주는 기능을 하고, `yield`가 포함된 함수를 제너레이터라고 한다.

이터레이터처럼 순서대로 출력이되고, 한번 읽어온 요소는 다시 불러올 수가 없어서 오류가 발생한다.

