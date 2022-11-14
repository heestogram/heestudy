# Do it! 쉽게 배우는 R 데이터 분석  

```
💡 R을 처음 배우기 위해 공부한 책입니다. 
책에서 공부한 내용을 정리하고, 이를 기반으로 직접 문제를 만들어 풀이해보는 식으로 학습했습니다. 
KBO, MLB 야구 기록들을 csv 파일로 크롤링하여 문제에 사용했고, 
야구 데이터 패키지인 `Lahman`을 토대로 문제를 만들기도 했습니다.  
```  
  
  
> **책 소개**
> 

[Do it! 쉽게 배우는 R 데이터 분석](https://book.naver.com/bookdb/book_detail.nhn?bid=12256508)

> **목차**
* [00.팁](#00.-팁)
* [03.변수, 함수, 패키지 이해하기](#03.-변수,-함수,-패키지-이해하기)
* 04.데이터 프레임 이해하기
* 05.데이터 파악 및 수정 기초
* 06.데이터 전처리 및 가공
* 07.결측치 이상치 정제
* 08.그래프 만들기
* 09.데이터 분석 프로젝트 -Lahman패키지로 MLB 분석
* 10.텍스트마이닝
* 11.지도 시각화
* 12.인터랙티브 그래프
* 13.통계 분석 기법을 이용한 가설 검정
* 14.R Markdown으로 데이터 분석 보고서 만들기

01, 02 챕터에서는 R에 대한 개괄적 설명, R설치 및 세팅에 대해 다루고 있습니다. 해당 챕터는 건너 뛰고, 본격적인 시작인 03 챕터부터 내용을 정리했습니다. 

---

### 00. 팁

tip1. `invalid graphics state` 오류가 뜬다면? `dev.off()`를 입력하면 해결된다.

tip2. Lahman 패키지(MLB 데이터베이스) 사용법 [https://cinema4dr12.tistory.com/1098](https://cinema4dr12.tistory.com/1098)

```r
install.packages("Lahman")
library(Lahman)
```

tip3. 간혹 어떤 패키지는 다른 패키지를 활용하는 의존성(dependency)이 있어서 함께 설치해야만 정상적으로 작동한다. 그럴 경우 다음과 같이 코드를 작성하자.

```r
install.packages("ggplot2", dependencies=T)
```

---

### 03. 변수, 함수, 패키지 이해하기

**03-1. 변수 이해하기**

변수(Variable)는 다양한 값을 지니고 있는 하나의 속성이다. 데이터는 변수들의 덩어리라고 할 수 있다. 반면에 상수(Constant)는 고정된 값을 지니고 있다. 변수와 달리 분석 대상이 아니다.

R에서 변수를 만들 때에는 `<-`를 사용한다. `=`를 사용해도 되긴 하지만, `=`가 다른 기능도 하기 때문에 헷갈리지 않게 그냥 화살표를 쓰는 편이 낫다.

```r
a <- 2 #변수 지정
b <- 2.5

a #2
b #2.5
a*b #5
a+b #4.5
```

변수에는 여러 값을 넣을 수도 있다. `c()`함수가 그러한 기능을 한다. `seq()`함수로도 연속 값을 출력할 수 있다. `by`파라미터는 간격을 설정한다.

```r
#콤마로 구분하기
var1 <- c(1, 2, 5, 7, 8) 
var1
# [1] 1 2 5 7 8

#콜론으로 연속값 만들기
var2 <- c(1:7) 
var2
# [1] 1 2 3 4 5 6 7

#seq()함수 이용
var3 <- seq(1, 9, by=2)
var3
# [1] 1 3 5 7 9

```

변수끼리 연산할 수도 있다. 이 때 연속값을 서로 연산하려면 길이가 같아야 한다.

```r
var1+2
#[1]  3  4  7  9 10

var1+var3
#[1]  2  5 10 14 17
```

문자로 된 변수 역시도 만들 수 있다. 마찬가지로 `c()`함수를 이용하면 여러 개의 문자로 구성된 변수를 만들 수 있다. 하지만 문자 변수는 연산할 수 없다!

```r
str1 <- c("a", "b", "c")
str1
#[1] "a" "b" "c"
```

---

**03-2. 함수 이해하기**

데이터 분석은 함수를 이용해서 변수를 조작하는 일이라고 할 수 있다. 이 때 괄호안에 파라미터(parameter)를 조정해서 다양한 결과값을 얻을 수 있다. 다양한 함수를 실행해보자.

```r
x <- c(1,2,3,4,5)
mean(x) #평균
max(x) #최댓값
min(x) #최솟값

str2 <- c("hello", "I", "am", "heejun")
paste(str2, collapse=" ") #문자를 합치는 함수. collapse 파라미터의 구분자로 여러 문자를 합친다.
# [1] "hello I am heejun"
```

함수의 결과물로 새 변수를 만들 수도 있다.

```r
str2_paste <- paste(str2, collapse=" ")
str2_paste
#[1] "hello i am heejun"
```

---

**03-3. 패키지 이해하기**

하나의 패키지 안에는 다양한 함수가 들어 있다. 일례로 `ggplot2`에는 `ggplot()`, `qplot()`, `geom_histogram()` 등 수십 가지 그래프 관련 함수가 들어있다.

`ggplot2` 패키지를 설치해보자.

```r
install.packages("ggplot2") #패키지 설치
library(ggplot2) #패키지 로드

#qplot()함수로 빈도 막대 그래프를 그려보자.
x <- c("pitcher", "pitcher", "catcher", "outfielder")
qplot(x)
```

![Untitled](https://user-images.githubusercontent.com/115082062/200174989-a487e552-bbd8-4c07-8a98-b1b7173795b8.png)


또한 패키지는 여러 예제 데이터를 제공한다. mpg(Mile Per Gallon) 데이터는 미국 환경 보호국에서 공개한 자료로, 1999년~2008년 사이 미국에서 출시된 자동차 234종의 연비 정보를 담고 있다.

이제 mpg 데이터로 그래프를 그려보자. `data` 파라미터에 mpg를 지정하고, x 파라미터에 다양한 변수들을 지정ㅎ자.

```r
qplot(data=mpg, x=hwy)
qplot(data = mpg, x=cty)
qplot(data = mpg, x=drv, y=hwy)

#geom파라미터로 그래프 모양 변경 가능.
qplot(data = mpg, x= hwy, y= drv, geom = "line") #선 그래프
qplot(data= mpg, x= drv, y= hwy, geom = "boxplot", colour = drv)#drv별 색 표현, 상자 그래프
```

![1](https://user-images.githubusercontent.com/115082062/200175070-af16c551-6168-4a08-bbaa-7935c805e5e0.jpg)

drv 변수 별로 색이 다른 상자 그래프.

---


❓ **문제.**
```
한 야구팀의 선발투수 다섯 명의 승 수와 패 수는 다음과 같다. 
1)각 선수의 승 수를 담는 변수와 패 수를 담는 변수를 만들어라. 
2)각 선수의 승률을 나타내는 변수를 만들어라. 
3)모든 선수의 승률 전체 평균을 나타내는 변수를 만들어라. 
4)각 선수의 승률을 막대그래프로 나타내라.
```


```r
#1선발: 15승 4패
#2선발: 17승 9패
#3선발: 8승 9패
#4선발: 7승 4패
#5선발: 6승 8패
```

💡 **답**.

```r
#1)
win<- c(15,17,8,7,6)
lose<- c(4,9,9,4,8)

#2)
win_pro <- win/(win+lose)

#3)
win_pro_mean <- mean(win_pro)

#4)
qplot(y=win_pro) + geom_col()
```

![2](https://user-images.githubusercontent.com/115082062/200175543-02271cf5-77ec-46f6-b4d0-ff7183fee0fc.jpg)


---

### 04. 데이터 프레임 이해하기

**04-1. 데이터 프레임이란**

데이터프레임은 가장 많이 사용하는 데이터 형태로, 행과 열로 구성된 사각형 표처럼 생겼다. 이를테면 다음과 같다.

| 성병 | 연령 | 학점 | 연봉 |
| --- | --- | --- | --- |
| 남자 | 26 | 3.8 | 2,700만 원 |
| 여자 | 42 | 4.2 | 4,000만 원 |
| 남자 | 35 | 2.6 | 3,500만 원 |

이 때 각 열은 **속성**을 나타내는데, **컬럼(column)** 이나 **변수(variable)** 라 부른다. 각 행은 row 또는 case라고 부른다.

---

**04-2. 데이터 프레임 만들기**

네 명의 학생이 영어 시험과 수학 시험을 봤다고 가정하고 아래와 같은 데이터 프레임을 만들어보자.

| 영어 점수 | 수학 점수 |
| --- | --- |
| 90 | 50 |
| 80 | 60 |
| 60 | 100 |
| 70 | 20 |

```r
eng <- c(90, 80, 60, 70)
math <- c(50,60,100,20)
df_midterm <- data.frame(eng, math)
df_midterm

##  eng math
##1  90   50
##2  80   60
##3  60  100
##4  70   20
```

이번에는 학생의 반에 대한 정보가 추가된 데이터 프레임을 만들어보자.

```r
class <- c(1,1,2,2)
df_midterm <- data.frame(eng, math, class)
df_midterm

#변수와 값을 나열하여 한번에 만드는 방법도 있다.
df_midterm <- data.frame(eng = c(90,80,60,70), math = c(50,60,100,20), clasee = c(1,1,2,2)
```

이제 이 데이터를 분석해보자. 기호 `$`는 데이터 프레임 안의 변수를 지정할 때 사용한다.

```r
mean(df_midterm$eng) ##75
mean(df_midterm$math) ##57.5
```

---

**04-3. 엑셀 데이터 불러오기**

외부에서 생성된 엑셀 파일이나 csv 파일을 불러와 데이터 프레임을 만드는 방법을 익혀보자.

우선 사용하려는 엑셀 파일을 프로젝트 폴더에 넣어둔다. 그리고 `readxl` 패키지를 설치하고 로드한다. 그 후 `readxl` 패키지에서 제공하는 `read_excel()`함수를 이용해 엑셀 파일을 불러온다. 프로젝트 폴더가 아닌 다른 폴더에 있는 엑셀 파일을 불러오려면 파일 경로를 지정하면 된다.

```r
install.packages("readxl")
library(readxl)
df_exam <- read_excel("excel_exam.xlsx")
df_exam
```

데이터를 불러왔으니 분석을 해보자.

```r
mean(df_exam$english) #84.9
max(df_exam$english) #98
min(df_exam$english) #56
median(df_exam$english) #86.5
```

만약 엑셀의 첫 행이 변수명이 아니라 바로 데이터가 시작된다면 문제가 발생한다. 이런 경우엔 `col_names = F` 파라미터를 설정해주면 첫번째 행을 변수명이 아니라 데이터로 인식하고, 변수명은 숫자로 자동 지정된다. 이 때 F는 논리형 벡터의 FALSE를 의미한다. 즉, 열 이름을 가져올 것인가?라는 질문에 False(아니요)로 답한 셈이다.

```r
df_exam_novar <- read_excel("excel_exam_novar.xlsx", col_names = F)
```

엑셀 파일에 시트가 여러개라면 sheet 파라미터를 이용해 몇번째 시트를 불러올지 지정할 수 있다.

```r
df_exam_sheet <- read_excel("excel_exam_sheet.xlsx", sheet=3)
#세번째 시트의 데이터 불러오기
```

---

**04-4. csv 파일 불러오기**

csv파일은 다양한 프로그램에서 지원하고 엑셀에 비해 용량이 작기에 더 자주 이용된다.

엑셀 파일과 마찬가지로 프로젝트 폴더에 csv 파일을 넣어둔다. 별도의 패키지를 이용하지 않고 R에 기본적으로 내장된 `read.csv()`를 이용하면 파일을 불러올 수 있다. 첫번째 행에 변수명이 없는 파일의 경우 `header=F` 파라미터를 지정해주면 된다.

```r
df_csv_exam <- read.csv("csv_exam.csv")
df_csv_exam
```

또한 역으로 데이터 프레임을 csv 파일로 저장할 수도 있다. R내장함수인 write.csv()를 이용하면 된다. 괄호 안에 저장할 데이터 프레임명을 지정하고, `file` 파라미터에 파일명을 저장하면 된다. 저장한 파일은 프로젝트 폴더에 생성된다.

```r
write.csv(df_midterm, file = "df_midterm.csv")
```

---

**04-5. RDS 파일 활용하기**

RDS 파일은 R 전용 데이터 파일이다.  R 전용 파일이므로 다른 파일에 비해 속도가 빠르고 용량이 작다는 장점이 있다.

`saveRDS()`를 이용하면 데이터프레임을 .rds 파일로 저장할 수 있다. 괄호 안에 데이터 프레임명과 저장할 파일명을 지정한다.

`readRDS()`를 이용하면 RDS 파일을 불러올 수 있다.

```r
saveRDS(df_midterm, file="df_midterm.rds")
df_midterm_rds <- readRDS("df_midterm.rds")
df_midterm_rds
```

---


❓ **문제.**
```
스탯티즈 사이트에서 2017년 기아타이거즈 타자들의 기록을 불러와 엑셀파일로 작성하고, 
1) 이를 데이터프레임으로 가져오자. 
2) 기록 중 최다도루가 몇개인지, 최다 삼진이 몇개인지, 최고 장타율은 얼마인지를 구하라.
```


💡 **답.**
```r
#1)
df_kia <- read_excel("17kia_record.xlsx")
df_kia

#2)
max(df_kia$도루) #32
max(df_kia$삼진) #112
max(df_kia$장타) #0.576
```

[17kia_record.xlsx](Do%20it!%20%E1%84%89%E1%85%B1%E1%86%B8%E1%84%80%E1%85%A6%20%E1%84%87%E1%85%A2%E1%84%8B%E1%85%AE%E1%84%82%E1%85%B3%E1%86%AB%20R%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%200283c0e38f9246a7932d7b5110ac8cdf/17kia_record.xlsx)

---

### 05. 데이터 파악 및 수정 기초

**05-1. 데이터를 파악할 때 사용하는 함수들**

`head()`: 데이터 앞부분 확인하기

데이터 전부를 출력하면 너무 많은 양이 출력되어 알아보기 어렵다. 이럴 땐 `head()`함수로 데이터의 앞부분만 출력할 수 있다.

```r
exam <- read.csv("csv_exam.csv")
head(exam) #기본값으로 앞에서부터 6행 출력
head(exam, 10) #앞에서 10행 출력
```

`tail()`: 데이터 뒷부분 확인하기

```r
tail(exam) #head와 마찬가지로 기본값은 뒤에서부터 6행이다.
tail(exam, 10)
```

`View()`: 뷰어 창에서 데이터 확인하기

`View()`는 엑셀과 유사한 뷰어 창에 원자료를 보여주는 기능을 한다. 이때 View의 V는 반드시 대문자로 써주자.

```r
View(exam)
```


`dim()`: 데이터가 몇 행 몇 열인지 알아보기

`dim()`함수로 출력된 2개의 숫자 중 앞은 행의 개수, 뒤는 열의 개수를 나타낸다.

```r
dim(exam)
#[1] 20  5
```

`str()`: 속성 파악하기

```r
str(exam)

'data.frame':	20 obs. of  5 variables:
 $ id     : int  1 2 3 4 5 6 7 8 9 10 ...
 $ class  : int  1 1 1 1 2 2 2 2 3 3 ...
 $ math   : int  50 60 45 30 25 50 80 90 20 50 ...
 $ english: int  98 97 86 98 80 89 90 78 98 98 ...
 $ science: int  50 60 78 58 65 98 45 25 15 45 ...
```

`summary()`: 요약 통계량 산출하기

```r
summary(exam)

id            class        math      
 Min.   : 1.00   Min.   :1   Min.   :20.00  #최솟값
 1st Qu.: 5.75   1st Qu.:2   1st Qu.:45.75  #하위25%의 값
 Median :10.50   Median :3   Median :54.00  #중앙값
 Mean   :10.50   Mean   :3   Mean   :57.45  #평균
 3rd Qu.:15.25   3rd Qu.:4   3rd Qu.:75.75  #하위75%의 값
 Max.   :20.00   Max.   :5   Max.   :90.00  #최댓값
    english        science     
 Min.   :56.0   Min.   :12.00  
 1st Qu.:78.0   1st Qu.:45.00  
 Median :86.5   Median :62.50  
 Mean   :84.9   Mean   :59.45  
 3rd Qu.:98.0   3rd Qu.:78.00  
 Max.   :98.0   Max.   :98.00
```

---

**05-2. mpg 데이터 파악하기**

`ggplot2` 패키지에 내장된 `mpg` 데이터를 불러와 특성을 파악해보자. `as.data.frame()`은 데이터 속성을 데이터 프레임 형태로 바꾸는 함수이다. 더블 콜론(`::`)을 사용하면 특정 패키지에 들어있는 함수나 데이터를 지정한다.

```r
install.packages("ggplot2")
mpg <- as.data.frame(ggplot2::mpg)

head(mpg)
#manufacturer model displ year cyl      trans drv cty hwy fl   class
#1         audi    a4   1.8 1999   4   auto(l5)   f  18  29  p compact
#2         audi    a4   1.8 1999   4 manual(m5)   f  21  29  p compact
#3         audi    a4   2.0 2008   4 manual(m6)   f  20  31  p compact
#4         audi    a4   2.0 2008   4   auto(av)   f  21  30  p compact
#5         audi    a4   2.8 1999   6   auto(l5)   f  16  26  p compact
#6         audi    a4   2.8 1999   6 manual(m5)   f  18  26  p compact

dim(mpg)
#[1] 234  11
#234행, 11열로 이루어져 있다. 즉 자동차 234종에 대한 11개 변수로 구성되어있다.

str(mpg)
'data.frame':	234 obs. of  11 variables:
 $ manufacturer: chr  "audi" "audi" "audi" "audi" ...
 $ model       : chr  "a4" "a4" "a4" "a4" ...
 $ displ       : num  1.8 1.8 2 2 2.8 2.8 3.1 1.8 1.8 2 ...
 $ year        : int  1999 1999 2008 2008 1999 1999 2008 1999 1999 2008 ...
 $ cyl         : int  4 4 4 4 6 6 6 4 4 4 ...
 $ trans       : chr  "auto(l5)" "manual(m5)" "manual(m6)" "auto(av)" ...
 $ drv         : chr  "f" "f" "f" "f" ...
 $ cty         : int  18 21 20 21 16 18 18 18 16 20 ...
 $ hwy         : int  29 29 31 30 26 26 27 26 25 28 ...
 $ fl          : chr  "p" "p" "p" "p" ...
 $ class       : chr  "compact" "compact" "compact" "compact" ...

#각 변수명 옆에 적힌 것은 chr(문자), num(소수점이 있는 실수), int(소수점이 없는 정수)이다.

summary(mpg)
#출력값 중 일부만 가져왔다.
cty             hwy       
 Min.   : 9.00   Min.   :12.00  
 1st Qu.:14.00   1st Qu.:18.00  
 Median :17.00   Median :24.00  
 Mean   :16.86   Mean   :23.44  
 3rd Qu.:19.00   3rd Qu.:27.00  
 Max.   :35.00   Max.   :44.00  
      fl               class          
 Length:234         Length:234        
 Class :character   Class :character  
 Mode  :character   Mode  :character
#숫자로 된 변수는 여섯 가지 요약 통계량을 보여주고
#문자로 된 변수는 값의 개수(length)와 속성(class, mode)을 보여준다.
```

---

**05-3. 변수명 바꾸기**

변수명이 기억하기 어려운 문자로 되어 있으면 분석에 용이하게 쉬운 단어로 변경해주는 게 좋다. `dplyr`패키지의 `rename()`으로 변수명을 바꿀 수 있다.

우선 실습에 활용하기 위해 데이터 프레임을 생성하고, `dplyr` 패키지를 설치/로드한다.

```r
df_raw <- data.frame(var1=c(1,2,1), var2=c(2,3,2))
df_raw

install.packages("dplyr") #설치
library(dplyr) #로드
```

변수명을 바꾸기 전에 원본을 유지하기 위해 `df_new`라는 복사본을 만든다. 그리고 이제 `rename()`을 이용해 var2를 v2로 바꿔보자. 괄호 안에 (데이터 프레임명, 새 변수명 = 기존 변수명)을 입력하면 된다. 이 때 두 변수명의 순서는 바뀌면 안 된다.

```r
df_new <- df_raw

df_new <- rename(df_new, v2=var2)
df_new
```

---


❓ **문제**. 
```
df_kia 데이터프레임의 변수 중 wOBA, wRC+, WPA는 생소한 스탯이므로 이를 풀어써줄 필요가 있다. 
`rename()`을 이용해 변수명을 변경해주자.
```

💡 **답**.
```r
df_kia_easy <- rename(df_kia, '가중출루율'='wOBA', '득점창출력'='wRC+', '승리기여도'='WPA')
View(df_kia_easy)
```

![2 1](https://user-images.githubusercontent.com/115082062/200175677-894a0def-019c-4a20-ad93-d62b4a18cd4e.jpg)

변수명이 잘 바뀐 것을 볼 수 있다.

---

**05-4. 파생변수 만들기**

기존의 변수를 변형하거나 함수를 적용해 만든 새 변수를 **파생변수(derived variable)** 라고 한다. 데이터 프레임을 만들고 파생변수를 직접 만들어보자. 파생변수를 만들 때엔 데이터 프레임명에 `$`를 붙여 새로 만들 변수명을 입력하고 계산공식을 할당하면 된다.

```r
df <- data.frame(var1=c(4,3,8), var2=c(2,6,1))
df
   var1 var2
1    4    2
2    3    6
3    8    1

df$var_sum <- df$var1+df$var2 #합을 나타내는 파생변수
df
    var1 var2 var_sum
1    4    2       6
2    3    6       9
3    8    1       9

df$var_mean <- df$var_sum/2 #평균을 나타내는 파생변수
df
    var1 var2 var_sum var_mean
1    4    2       6      3.0
2    3    6       9      4.5
3    8    1       9      4.5
```

mpg 데이터에서 파생변수를 만들어보자. 도시연비를 나타내는 cty, 고속도로 연비를 나타내는 hwy를 통합하는 연비 변수를 만들어볼 것이다.

```r
install.packages("ggplot2") #패키지 설치
mpg <- as.data.frame(ggplot2::mpg) #mpg데이터를 데이터 프레임으로 불러오기

mpg$total <- (mpg$cty+mpg$hwy)/2 #통합 연비 변수 만들기

#생성한 파생변수를 분석
mean(mpg$total) #20.14957
median(mpg$total) #20.5
max(mpg$total) #39.5

```

---

**05-5. 조건문을 이용해 파생변수 만들기**

이번에는 조건에 따라 서로 다른 값을 반환하는 조건문 함수로 파생변수를 만들어보자. mpg 데이터에서 일정 연비 기준을 넘는 자동차가 몇 대인지 알아보자.

먼저 연비 기준점을 설정해야 한다. summary()를 이용해 아까 만든 total의 통계량을 확인해보고, 히스토그램을 그려 분포를 확인해보자.  `hist()`를 이용하면 히스토그램을 그릴 수 있다.

```r
summary(mpg$total)
Min.  1st Qu.   Median   Mean  3rd Qu.   Max. 
10.50   15.50   20.50   20.15   23.50   39.50

hist(mpg$total)
```

![1](https://user-images.githubusercontent.com/115082062/200175825-76542424-ed13-4979-978f-0cb47cd5fee9.png)

이를 확인하면 total연비가 20~25인 자동차가 제일 많고, 대부분 25이하라는 것을 알 수 있다. 연비가 23을 넘기면 합격, 못 넘기면 불합격으로 분류된 변수를 만들어보자.

`ifelse()`는 가장 많이 사용하는 **조건문 함수**이다. 지정한 조건에 맞을 때와 맞지 않을 때 서로 다른 값을 반환하는 기능을 한다.

```r
mpg$test <- ifelse(mpg$total>23, "pass", "fail")
head(mpg,8)
manufacturer      model displ year cyl      trans drv cty hwy fl   class total test
1         audi         a4   1.8 1999   4   auto(l5)   f  18  29  p compact  23.5 pass
2         audi         a4   1.8 1999   4 manual(m5)   f  21  29  p compact  25.0 pass
3         audi         a4   2.0 2008   4 manual(m6)   f  20  31  p compact  25.5 pass
4         audi         a4   2.0 2008   4   auto(av)   f  21  30  p compact  25.5 pass
5         audi         a4   2.8 1999   6   auto(l5)   f  16  26  p compact  21.0 fail
6         audi         a4   2.8 1999   6 manual(m5)   f  18  26  p compact  22.0 fail
7         audi         a4   3.1 2008   6   auto(av)   f  18  27  p compact  22.5 fail
8         audi a4 quattro   1.8 1999   4 manual(m5)   4  18  26  p compact  22.0 fail

```

`table()`을 이용하면 빈도표를 만들어 변수의 값이 몇개씩 존재하는지를 확인할 수 있다. 그리고 `qplot()`을 이용해 막대 그래프로 빈도를 표현해보자.

```r
table(mpg$test)
fail pass 
 173   61

library(ggplot2)
```

이번엔 total이 30이상이면 A, 20~29면 B, 20미만이면 C등급으로 분류해보자. 이런 **중첩 조건문**은 `ifelse()` 안에 다시 `ifelse()`를 넣는 방식으로 만든다.

```r
mpg$grade <- ifelse(mpg$total>=30, "A", ifelse(mpg$total>=20, "B", "C"))
head(mpg)

```

---


❓ **문제**. 
```
17kia_record.xlsx 파일을 데이터 프레임으로 불러오고, 
0) ‘안타...9’의 변수명을 ‘안타’로 수정해주고, WAR*의 변수명을 WAR로 수정해준다.
1) BABIP 파생변수를 만든다.
`BABIP = (안타-홈런)/(타수-삼진-홈런+희생플라이)`
2) ISO(순수장타력) 파생변수를 만든다.
`ISO = (1*2루타 + 2*3루타 + 3*홈런) / 타수`
3) 아래 표를 참고해 선수의 WAR 등급을 매기는 파생변수를 만든다.
4) WAR 등급의 빈도 막대 그래프를 그려본다.
```



| WAR | 등급 |
| --- | --- |
| 0-1 | 보결 선수(Scrub)[9] |
| 1-2 | 보조 선수(Role Player)[10] |
| 2-3 | 주전 선수(Solid Starter) |
| 3-4 | 좋은 선수(Good Player) |
| 4-5 | 올스타(All Star) |
| 5-6 | 슈퍼 스타(Super Star) |
| 6+ | MVP |

💡 **답.**
```r
install.packages("readxl")
library(readxl)
df_kia <- read_excel("17kia_record.xlsx")

#0)
df_kia <- rename(df_kia, '안타'='안타...9', 'WAR'='WAR*')

#1)
df_kia$BABIP <- (df_kia$안타-df_kia$홈런)/(df_kia$타수-df_kia$삼진-df_kia$홈런+df_kia$희비)

#2)
df_kia$ISO <- (df_kia$'2타' + 2*df_kia$'3타' + 3*df_kia$홈런)/(df_kia$타수)

#3)
df_kia$WAR_grade <- ifelse(df_kia$WAR>=6, 'MVP', ifelse(df_kia$WAR>=5, "Super Star", ifelse(df_kia$WAR>=4, "All Star", ifelse(df_kia$WAR>=3, "Good Player", ifelse(df_kia$WAR>=2, "Solid Player", ifelse(df_kia$WAR>=1, "Role Player", "Scrub"))))))

View(df_kia)
```
![4](https://user-images.githubusercontent.com/115082062/200175904-cf1d968f-603e-4067-afd5-6e83024244e4.png)
세 가지 파생변수가 잘 만들어졌다.

![3](https://user-images.githubusercontent.com/115082062/200175928-1fa7f6c7-8d27-44f5-9cc6-ef12d7160da5.png)
빈도 막대 그래프가 잘 그려졌다.

---

### 06. 데이터 전처리 및 가공

**06-1. 조건에 맞는 데이터만 추출**

분석에 적합하게 데이터를 가공하는 작업을 데이터 전처리(data Preprocessing)라고 한다. `dplyr`은 데이터 전처리 작업에 가장 많이 사용되는 패키지이다. 우선 패키지와 데이터를 준비한다.

```r
install.packages("dplyr")
library(dplyr) #패키지 로드
exam <- read.csv("csv_exam.csv") #변수에 저장
```

`dplyr` 패키지는 `%>%` 기호를 이용해 함수들을 나열하는 방식으로 코드를 작성한다. `filter()`함수에 조건을 입력하면 조건에 해당되는 행만 출력된다. 1반인 학생들만 추출해보자. 파이썬처럼 등호 두개는 ‘같다’를 의미한다. 그리고 =! 기호를 이용하여 3반이 아닌 경우를 출력해보자. 비슷한 방식으로 여러 조건을 걸어보자.

```r
exam %>% filter(class==1)
exam %>% filter(class!=3)

exam$avg <- (exam$math+exam$english+exam$science)/3 #3과목 평균 점수 파생변수
options(digits=4) #소수점 2째자리까지만
exam %>% filter(avg>=70) #평균 70점 이상만 추출
```

기호 `&`를 사용하면 여러 조건을 모두 충족하는 데이터를 추출할 수 있다. 

기호 `|`를 사용하면 여러 조건 중 하나라도 충족하는 데이터를 추출할 수 있다. 

`%in%` 기호와 `c()`함수를 이용하면 코드가 더 간편해진다. `%in%`는 지정한 조건 목록에 해당하는지 확인한다.

```r
exam %>% filter(class==2 & avg>=65) #2반이면서 평균이 65 이상인 경우
exam %>% filter(math>=85 | english>=85) #수학 점수가 85점 이상이거나 영어 점수가 85점 이상인 경우
exam %>% filter(class %in% c(1,5)) #1반이나 5반인 경우
```

추출한 행으로 새 변수를 만들 수도 있다. 1반 데이터만 추출해서 1반의 평균 점수를 구해보자.

```r
class1 <- exam %>% filter(class==1)
mean(class1$math) #46.25
mean(class1$english) #94.75
mean(class1$science) #61.5
mean(class1$avg) #67.5
```

---


❓ **문제**. 
```
자동차 배기량에 따라 도시 연비가 다른지 알아보려고 한다. 
`displ`(배기량)이 4이하인 자동차와 5이상인 자동차 중 어떤 자동차의 `cty`(도시 연비)가 더 높은지 알아보자.
```

💡 **답**.


```r
mpg <- as.data.frame(ggplot2::mpg) #데이터프레임으로 만들기

displ4 <- mpg %>% filter(displ<=4) #배기량이 4이하인 행만 추출해서 변수로 만들기
displ5 <- mpg %>% filter(displ>=5) #배기량이 5이상인 행만 추출해서 변수로 만들기
mean(displ4$cty) #18.7
mean(displ5$cty) #12.63

#배기량이 4이하인 자동차가 도시연비가 더 높다.
```

---


❓ **문제.** 
```
17kia_record.xlsx 파일을 데이터 프레임으로 불러오고, 
**1)** 규정타석수 변수(`RMAB`)를 정의하라. (규정타석은 소속 팀 경기 수의 3.1배이다.)
**2)** 규정타석수를 충족한 선수들만 추출하여 `df_RMAB` 변수로 만들어라.
**3)** 규정타석수를 충족한 선수들의 평균 타율을 구하라.
```


💡 **답.**

```r
#1)
RMAB <- 144*3.1

#2)
df_RMAB <- df_kia %>% filter(RMAB<=df_kia$타석)

#3)
mean(df_RMAB$타율) #0.3203
```

---


❓ **문제.** 
```
Baseball Reference에서 2021 batting record를 크롤링하여 “MLB batting record.xlsx”로 저장하고, 이를 데이터 프레임으로 불러오고, 
1) 20-20 클럽을 달성한 선수들만 추출하여 `club20_20` 변수로 만들어라.
2) `select()`를 이용하여 club20_20 선수들의 이름, 홈런, 도루 컬럼을 추출하라.
3) 토론토 블루제이스 팀 선수들 중 규정타석을 채운 선수들만 추출하여 `tor` 변수로 만들고 이 선수들의 평균 타율을 구하라.
```

💡 **답.**

![df_mlb](https://user-images.githubusercontent.com/115082062/201664769-840e40bc-c4dc-4098-bb3f-b89c96f5ee51.png)

크롤링해온 데이터를 View한 모습이다.

```r
#1)
club20_20 <- df_mlb %>% filter(df_mlb$SB>=20 & df_mlb$HR>=20)

#2)
club20_20 %>% select(Name, HR, SB)

                 Name HR SB
1         Bo Bichette 29 25
2       Ozzie Albies# 30 20
3     Cedric Mullins* 30 30
4         Trea Turner 28 32
5    Robbie Grossman# 23 20
6       Jose Ramirez# 36 27
7      Shohei Ohtani* 46 26
8     Randy Arozarena 20 20
9        Trevor Story 24 20
10 Fernando Tatis Jr. 42 25

#3)
tor <- df_mlb %>% filter(df_mlb$Tm=='TOR', PA>=162*3.1)
mean(tor$BA) #0.2812

```

[mlb batting record.csv](Do%20it!%20%E1%84%89%E1%85%B1%E1%86%B8%E1%84%80%E1%85%A6%20%E1%84%87%E1%85%A2%E1%84%8B%E1%85%AE%E1%84%82%E1%85%B3%E1%86%AB%20R%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%200283c0e38f9246a7932d7b5110ac8cdf/mlb_batting_record.csv)

---

**06-2. 필요한 변수만 추출**

필요한 행이 아니라 컬럼을 추출하기 위해선 `select()`함수를 사용한다. 

특정 변수만 제외하고 추출하는 방법도 있다. 제외할 변수명 앞에 `-`기호만 붙이면 된다.

```r
exam %>% select(math) #math변수(열)만 추출
exam %>% select(english) #english(열)만 추출
exam %>% select(english, science) #english, science열 추출
```

`dplyr` 함수들은 `%>%`를 이용해 조합할 수 있다는 장점이 있다. `filter()`와 `select()`를 조합해보자. 이 때 `%>%`를 기준으로 줄바꿈을 해주는 것이 좋다.

```r
exam %>%
  filter(class==1) %>%
  select(math, english)
```

**06-3. 순서대로 정렬하기**

`arrange()`를 이용하면 데이터를 원하는 순서로 정렬할 수 있다. 괄호 안에 정렬 기준으로 삼을 변수명을 입력하면 된다. 기본값은 오름차순이고, 내림차순을 원하면 `desc()`로 변수를 감싸준다.

```r
exam %>% arrange(math) #math 기준으로 오름차순 정렬
exam %>% arrange(desc(math)) #math 기준으로 내림차순 정렬
```

---

**06-4. 파생변수 추가하기**

앞서 파생변수 추가하는 법을 이미 배웠다. 이번엔 `mutate()`함수로 파생변수를 추가하는 방법이다. 이 방법의 장점은 아까와는 달리 데이터프레임명을 반복해서 입력할 필요가 없다는 것이다. 때문에 훨씬 간결하게 코드를 작성할 수 있다.

`ifelse()`를 적용하면 조건문으로 변수를 추가할 수 있다.

```r
exam %>% mutate(avg = (math+english+science)/3) #평균점수를 나타내는 avg파생변수 추가
exam %>% mutate(test=ifelse(avg>=65, "pass", "fail")) #평균이 65를 넘으면 pass 못 넘으면 fail
```

---

❓ **문제.** 
```
mlb batting record를 불러오고, dplyr함수를 이용해 전처리를 하라
1) wOBA(가중출루율) 파생변수를 추가하라.
`가중 출루율 =  (0.691×(볼넷-고의4구) + 0.722×몸에 맞는 볼 + 0.884×1루타 + 1.257×2루타 + 1.593×3루타 + 2.058×홈런) / (타수 + 볼넷 - 고의4구 + 희생플라이 + 몸에 맞는 볼)`
2) wOBA를 기준으로 정렬하여 상위 10명의 선수 데이터를 `df_mlb_wOBA_top`변수에 담자. 이 때 출력할 컬럼은 Name, Tm, OBP, wOBA이고, 규정타석을 채운 선수만 출력하도록 한다.
```

💡 **답.**


```r
#1)
df_mlb <- df_mlb %>% mutate(wOBA = (0.691*(BB-IBB) + 0.722*HBP + 0.884*(H-X2B-X3B-HR) + 1.257*X2B + 1.593*X3B + 2.058*HR)/(AB+BB-IBB+SF+HBP))

#2)
df_mlb %>%
  filter(df_mlb$PA >= 162*3.1)%>%
  select(Name, Tm, OBP, wOBA) %>%
  arrange(desc(wOBA))%>%
  head(10)

                   Name  Tm   OBP   wOBA
1          Bryce Harper* PHI 0.429 0.4357
2  Vladimir Guerrero Jr. TOR 0.401 0.4240
3             Juan Soto* WSN 0.465 0.4239
4     Fernando Tatis Jr. SDP 0.364 0.4081
5         Shohei Ohtani* LAA 0.372 0.3987
6       Nick Castellanos CIN 0.362 0.3960
7            Joey Votto* CIN 0.375 0.3960
8            Aaron Judge NYY 0.373 0.3915
9            Trea Turner TOT 0.375 0.3903
10       Bryan Reynolds# PIT 0.390 0.3888
```

---

**06-5. 집단별로 요약하기**

각 집단을 요약한 값을 구할 때는 `group_by()`와 `summarise()`를 사용한다. `summary()`와 헷갈리지 말자. 보통 `summarise()`는 `group_by()`와 조합해 집단별 요약표를 만들 때 사용한다.

```r
exam %>%
  group_by(class) %>% #먼저 반별로 그룹화를 해주고
  summarise(mean_math=mean(math)) #각 반의 수 평균을 집계

# A tibble: 5 x 2
class    mean_math
  <int>     <dbl>
1     1      46.2
2     2      61.2
3     3      45  
4     4      56.8
5     5      78

exam %>%
  group_by(class) %>%
  summarise(mean_math = mean(math),
            median_math = median(math),
            n=n())
```

`tibble: 5 X 2`라는 것은 이 데이터가 5행 2열의 **tibble** 형태라는 걸 의미한다. `group_by()`는 출력 결과를 데이터 프레임의 업그레이드 버전인 tibble로 출력한다. 변수명 아래 `<int>`는 정수, `<dbl>`은 소수점이 있는 숫자를 의미한다.

`n()`은 데이터가 몇 행인지를 구한다. 여기선 반별로 집단을 나눴으니, 반별 학생수를 의미한다.

각 집단별로 다시 하위 집단을 나눌 수도 있다. `group_by(기준변수1, 기준변수2)` 식으로 작성하면 된다. mpg데이터에서 회사별로 집단을 나누고, 구동 방식별로 하위집단을 나눠보자.

```r
mpg %>%
  group_by(manufacturer, drv) %>% #manufacturer 변수를 기준으로 집단 나누고, drv 변수를 기준으로 하위 집단
  summarise(mean_cty = mean(cty)) %>%
  head(10)

manufacturer    drv   mean_cty
   <chr>        <chr>    <dbl>
 1 audi         4         16.8
 2 audi         f         18.9
 3 chevrolet    4         12.5
 4 chevrolet    f         18.8
 5 chevrolet    r         14.1
 6 dodge        4         12  
 7 dodge        f         15.8
 8 ford         4         13.3
 9 ford         r         14.8
10 honda        f         24.4
```

---


❓ **문제**. 
```
회사별로 “midsize” 자동차의 도시 및 고속도로 통합 연비 평균을 구해 내림차순으로 정렬하고, 하위 5위를 출력하기
```

💡 **답.**


```r
mpg %>%
  group_by(manufacturer) %>% #회사별로 그룹화
  filter(class == 'midsize') %>% #midsize 차종류 행만 추출
  mutate(total = (hwy+cty)/2) %>% #도시 및 고속도로 통합 연비 변수 추가
  summarise(total_mean = mean(total)) %>% #연비 평균 집계
  arrange(desc(total_mean)) %>% #내림차순 정렬
  tail(5) #하위 5개 회사 출력
```

---

❓ **문제**. 
```
mlb batting record에서 팀별로  26세 이하 선수들의 삼진대비볼넷 비율 평균을 구해 내림차순으로 정렬하라.
```

💡 **답.**


```r
#만약 앞서 배운 방식대로 코드를 작성하면
df_mlb %>%
  group_by(Tm) %>%
  filter(Age<=26) %>%
  mutate(SBP = BB/SO) %>%
  summarise(sbp_mean = mean(SBP)) %>%
  arrange(sbp_mean)

Tm    sbp_mean
   <chr>    <dbl>
 1 CHC      0.164
 2 OAK      0.209
 3 TBR    Inf    
 4 ARI    NaN    
 5 ATL    NaN    
 6 BAL    NaN    
 7 BOS    NaN    
 8 CHW    NaN    
 9 CIN    NaN    
10 CLE    NaN
#이 같은 결과가 나온다.
#NaN은 분모, 분자가 모두 0이 되어 발생하는 에러고
#Inf는 분모가 0이 되어 infinite가 되는 에러다.
#이는 삼진과 볼넷이 0인 데이터가 포함되어서 발생한 문제다.

#이 문제를 해결하기 위해 적절한 전처리를 해주자
df_mlb_nona <- df_mlb %>%
  filter(BB!=0 & SO!=0) #볼넷과 삼진이 모두 0이 아닌 행만 추출

df_mlb_nona %>%
  group_by(Tm) %>% #팀 기준으로 그룹화
  filter(Age<=26) %>% #26세 이하 행만 추출
  mutate(SBP = BB/SO) %>% #삼진대비볼넷 변수 추가
  summarise(sbp_mean = mean(SBP),
            BB_sum = sum(BB),
            SO_sum = sum(SO))%>%
  arrange(desc(sbp_mean)) #삼진대비볼넷 평균 기준 내림차순
librar
Tm    sbp_mean BB_sum SO_sum
   <chr>    <dbl>  <int>  <int>
 1 CIN      0.583    145    308
 2 WSN      0.567    227    309
 3 NYY      0.505    112    264
 4 TOR      0.491    242    487
 5 CHW      0.485    224    530
 6 LAA      0.476    137    369
 7 TBR      0.459    284    664
 8 NYM      0.454    116    279
 9 DET      0.408    155    528
10 STL      0.405    208    609

#신시내티가 가장 준수한 기록을 보유하고 있다

```

---

**06-6. 데이터 합치기**

여러 데이터를 하나의 데이터로 합치는 것도 가능하다. 먼저 데이터를 가로로 합치는 방법을 알아보자. 학생 다섯 명이 중간고사와 기말고사를 봤다고 가정하고 2개의 데이터 프레임을 만들어보자. `left_join()`함수를 쓰면 데이터를 **가로**로 합칠 수 있다. 괄호 안에 데이터 프레임명을 나열하고, 기준으로 삼을 변수명을 by파라미터에 지정하면 된다.

```r
term1 <- data.frame(id=c(1,2,3,4,5),
                      midterm=c(60,80,70,90,85))
term2 <- data.frame(id=c(1,2,3,4,5),
                    final=c(70,83,65,95,80))

total <- left_join(term1,term2,by="id") #id를 기준으로 두 데이터를 가로로 합치기
total
```

`left_join()`을 응용하면 특정 변수를 기준으로 다른 데이터를 불러올 수도 있다. 예를 들어 각 반 학생의 시험 점수인 exam데이터를 분석하는데, 반별 담임교사 명단 데이터프레임에서 교사명을 exam에 합치려는 경우를 생각해보자.

```r
t_list <- data.frame(class=c(1,2,3,4,5),
                     teacher=c("kim", "lee","park","choi","jung")) #반별 담임교사 명단

exam_new <- left_join(exam, t_list, by="class")
exam_new

     id class math english science teacher
1   1     1   50      98      50     kim
2   2     1   60      97      60     kim
3   3     1   NA      86      78     kim
4   4     1   30      98      58     kim
5   5     2   25      80      65     lee
6   6     2   50      89      98     lee
```

이번에는 데이터를 세로로 합치는 방법을 알아보자. 학생 5명이 시험을 먼저 보고 5명이 나중에 보았을 때 이들을 세로로 합치는 상황이다. `bind_rows()`를 이용하면 데이터를 세로로 합치게 된다.

```r
group1 <- data.frame(id=c(1,2,3,4,5),
                     test=c(60,80,70,90,85))
group2 <- data.frame(id=c(6,7,8,9,10),
                     test=c(70,83,65,95,80))
groupall <- bind_rows(group1,group2)
groupall
```

---


❓ **문제**. 
```
Lahman패키지의 Batting 데이터와 Fielding 데이터를 가로로 합치려고 한다. 이 때 2020년 LA에인절스의 데이터만을 합쳐서 가져온다.
```

💡 **답.**


```r
df_bat <- Batting %>%
  filter(yearID==2020 & teamID=="LAA") #2020년 LAA팀 데이터만을 추출한다

df_bat_new <- left_join(df_bat, Fielding, by="playerID") #두 데이터를 선수 이름 기준으로 합친다
View(df_bat_new)
```

---

### 07. 결측치, 이상치 정제

**07-1. 결측치 제거하기**

**결측치(missing value)**는 누락된 값을 의미한다. 결측치가 있으면 에러가 뜨는 경우가 빈번하여 이를 꼭 정제해주어야 한다.

결측치는 `NA`로 표기된다. 만약 이를 따옴표로 감싸 “NA”가 된다면 결측치가 아니라 문자열”NA”를 의미하게 된다. 결측치를 확인하기 위해 간단한 데이터 프레임을 만들어보자.

```r
df <- data.frame(sex=c("M","F",NA,"M","F"),
                 score=c(5,4,3,4,NA))
df
    sex score
1    M     5
2    F     4
3 <NA>     3
4    M     4
5    F    NA
```

이 때 문자로 구성된 변수는 그냥 `NA`로 나오지 않고 `<NA>`로 출력된다.

`is.na()`함수를 사용하면 결측치를 확인할 수 있다. 결측치라면 `TRUE`, 결측치가 아니라면 `FALSE`를 반환한다. 

```r
is.na(df)
      sex score
[1,] FALSE FALSE
[2,] FALSE FALSE
[3,]  TRUE FALSE
[4,] FALSE FALSE
[5,] FALSE  TRUE
```

만약 결측치가 있는 데이터를 함수에 적용하면 `NA` 에러라 뜬다.

이제 결측치를 제거해보자. `filter()`함수를 이용해 결측치가 아닌 값만 추출하면 될 것이다. 즉 `filter(!is.na(변수명))`로 작성하면 된다. 그리고 이것을 새로운 변수로 만들어주면 함수를 적용해도 에러 없이 작동할 것이다.

```r
df %>%
  filter(!is.na(score) & !is.na(sex)) #score의 결측치와 sex의 결측치 모두 제거

sum(df_new$score) #13
```

`filter()`에 일일이 변수를 지정하여 제거하는 방법보단, `na.omit()`를 이용하여 변수를 지정하지 않고도 한 번에 결측치를 없애는 것이 낫다. 

`na.omit()`은 결측치가 하나라도 있으면 모조리 제거한다는 편리함이 있지만, 분석에 필요한 행까지도 모두 삭제해버릴 수 있다는 단점이 있다. 따라서 경우에 따라 `na.omit()`과 `filter()`를 잘 구분하여 사용하여야 한다.

```r
df_new2 <- na.omit(df)
df_new2
```

수치 연산 함수들은 결측치를 제외하고 연산하게끔 하는 `na.rm` 파라미터를 지원한다. `na.rm`을 `TRUE`로 설정하면 결측치를 제외하고 함수를 적용한다.

```r
mean(df$score, na.rm=T) #4

#summarise도 na.rm 지원
exam[c(3,8,15),"math"] <- NA #[행위치, 열위치]. 3,8,15행의 math열에 NA 부여
exam
exam %>%
  summarise(mean_math = mean(math, na.rm=T),
            median_math = median(math, na.rm=T))
```

---

**07-2. 결측치 대체하기**

데이터가 작고 결측치가 많은 경우엔 결측치를 제거하면 많은 데이터가 손실되어 결과가 왜곡될 수도 있다. 이런 경우엔 결측치를 대체(imputation)해주는 편이 현명하다.

일반적인 경우에 결측치는 평균으로 대체한다.

```r
mean(exam$math, na.rm=T) #55.23529
exam$math <- ifelse(is.na(exam$math),55,exam$math) #결측치라면 55(평균), 결측치가 아니라면 원래값
table(is.na(exam$math)) #FALSE 20.
```

---


❓ **문제.** 
```
Lahman Batting 데이터에서 팀별 통산 BABIP을 내림차순으로 출력하려 한다. 
이 때 결측치를 적절히 제거하여 에러 없이 값을 출력하라.
```

💡 **답.**

```r
batting_nona <- Batting %>%
  filter(!is.na(SF)&(AB-SO-HR+SF)!=0) #20세기 초반까지는 SF데이터가 집계되지 않았다.
#때문에 SF가 결측치인 데이터들을 제거해줘야 한다.
#BABIP의 분모가 0이 되는 데이터들도 제거해준다.

team_BABIP <- batting_nona %>%
  group_by(teamID) %>% #팀별로 그룹화한다
  mutate(BABIP=(H-HR)/(AB-SO-HR+SF)) %>% #BABIP 파생변수를 만든다
  summarise(mean_BABIP=mean(BABIP)) %>% #팀별로 BABIP평균을 집계한다
  arrange(desc(mean_BABIP)) #BABIP의 내림차순으로 정렬한다
head(team_BABIP)

  teamID    mean_BABIP
  <fct>       <dbl>
1 TEX         0.278
2 COL         0.275
3 ANA         0.274
4 KCA         0.271
5 TBA         0.269
6 BOS         0.268
#텍사스의 통산 babip이 가장 우수한 것을 알 수 있다.
```

**07-3. 이상치 제거하기**

이상치는 크게 두 가지로 나눠볼 수 있다. 논리적으로 존재할 수 없는 값(EX: 남,여가 아닌 제3의 성)과 극단적인 값이다.

논리적으로 존재할 수 없는 값들은 결측값으로 대체를 해주어야 한다. 1은 남자, 2는 여자를 나타내는 데이터를 만들자. 이 때 3이라는 이상치를 삽입한다. score도 1~5의 값을 가져야 한다고 가정하자. 이 때 6이라는 이상치를 삽입한다.

```r
outlier <- data.frame(sex=c(1,2,1,3,2,1),
                      score=c(5,4,3,4,2,6))

table(outlier$sex)
1 2 3 
3 2 1 #이상치 3이 하나 껴있다.

#성별이 3이라면 NA로 바꾼다.
outlier$sex <- ifelse(outlier$sex==3,NA,outlier$sex)
#score가 6이라면 NA로 바꾼다.
outlier$score <- ifelse(outlier$score==6,NA,outlier$score)

#이제 결측치를 제거해주고 성별에 따른 score 평균을 구해보자
outlier %>%
  filter(!is.na(sex) & !is.na(score)) %>%
  group_by(sex) %>%
  summarise(mean_score=mean(score))
```

극단적으로 크거나 작은 값을 제거하기 위해선 정상 범주의 기준을 정해야 한다. `Boxplot`을 이용해 중심에서 크게 벗어난 값을 극단치로 간주해보자.

```r
boxplot(mpg$hwy)
boxplot(mpg$hwy)$stats #Boxplot 통계치 출력
      [,1]
[1,]   12 #아래쪽 극단치 경계
[2,]   18 #1사분위수
[3,]   24 #2사분위수
[4,]   27 #3사분위수
[5,]   37 #위쪽 극단치 경계_
```

![프레젠테이션_1](https://user-images.githubusercontent.com/115082062/201664381-cfc2d4af-9bd1-4cf7-aa27-a62c821559f6.jpg)


극단치 경계가 위로는 37, 아래로는 12에 위치해있으므로 12~37을 벗어나면 극단치로 분류하여 결측값으로 만들면 된다.

```r
mpg$hwy <- ifelse(mpg$hwy<12 | mpg$hwy>37, NA, mpg$hwy) #12미만, 27초과인 경우 NA
mpg %>%
  group_by(drv) %>% #구동방식별로 그룹화
  summarise(mean_hwy=mean(hwy, na.rm=T)) #결측치는 제거한 채 평균 계산

   drv   mean_hwy
  <chr>    <dbl>
1 4         19.2
2 f         27.7
3 r         21
```

---

### 08. 그래프 만들기

`ggplot2` 문법은 레이어 구조로 되어 있다. 먼저 배경(축)을 만들고, 그 위에 그래프(점, 막대, 선)을 그리고, 마지막으로 축 범위, 색, 표식 등을 설정하는 순서로 나뉜다.

---

**08-1. 산점도(scatter plot)**

1) 우선 배경을 만들어준다. `data`에 사용할 데이터를 지정하고 `aes`에 x축과 y축에 사용할 변수를 지정한다. 2) 그리고 그래프를 그려준다. `+`기호를 이용해 그래프 유형을 지정하면 된다. 산점도는 `geom_point()`이다. 3) `xlim()`와 `ylim()`으로 축 범위를 설정할 수도 있다. 축 시작값과 종료값을 쉼표로 나열하면 된다.

```r
#1)
ggplot(data= mpg, aes(x=displ, y=hwy))
#2)
ggplot(data= mpg, aes(x=displ, y=hwy)) + geom_point()
#3)
ggplot(data= mpg, aes(x=displ, y=hwy)) +
  geom_point() + 
	ylim(10, 30)

# +로 층층이 이어붙인다는 점에서 레이어 구조라는 것!
```

![Untitled 1](https://user-images.githubusercontent.com/115082062/201665016-c598c3dc-51db-4f32-ac7c-3587a3969e85.png)

---


❓ **문제**. 
```
Lahman 패키지에서 whip와 ERA의 관계를 산점도로 나타내고자 한다. 샘플은 2010년 이후 기록으로, 30이닝 이상을 투구한 선수이다. 그래프 축을 적절히 설정하여 한 눈에 들어오도록 하자.
```

💡 **답.**

```r
new_pitching <- Pitching %>%
  mutate(whip = (BB+H)/(IPouts/3)) %>% #whip 변수가 없으므로 새로 만들어준다
  filter(yearID>=2010 & (IPouts/3)>=30) #2010년 이후 자료, 30이닝 이상 선수만 추출

ggplot(data=new_pitching, aes(x=ERA, y=whip))+
  geom_point()+ #산점도
  xlim(0,10)+
  ylim(0,3)
```

![Untitled 2](https://user-images.githubusercontent.com/115082062/201665177-e08feef8-a022-4090-ad92-f4711b5ddd86.png)

나름의 선형관계를 보이고 있다.

---

**08-2. 막대 그래프**

mpg 데이터를 이용해 drv(구동방식)별 평균 hwy 막대 그래프를 만들어보자. **평균 막대 그래프**를 만들려면 우선 1)집단별 평균표로 구성된 데이터 프레임이 필요하다. 2)그리고 아까의 과정처럼 그래프를 만들자. 막대 그래프는 `geom_col()`함수를 사용한다. 3)`reorer()`를 사용하면 막대를 크기 순으로 정렬할 수 있다. 괄호 안에 x축 변수와 기준 변수를 넣고 `-`기호를 붙이면 내림차순으로 정렬된다.

```r
#1)
df_mpg <- mpg %>%
  group_by(drv) %>%
  summarise(mean_hwy = mean(hwy))
df_mpg
#2)
ggplot(data=df_mpg, aes(x=drv, y=mean_hwy)) +
  geom_col()
#3)
ggplot(data=df_mpg, aes(x=reorder(drv,-mean_hwy), y=mean_hwy)) +
  geom_col()
```

![Untitled 3](https://user-images.githubusercontent.com/115082062/201665310-0f604107-42fd-4420-96aa-3c7709934aff.png)


geom_bar()를 이용하면 빈도 막대 그래프를 만들 수 있다. 이 때 y축 없이 x축만 지정하면 된다. 만약 x축에 연속(continuous) 변수를 지정하면 값의 분포를 확인할 수 있다.

```r
ggplot(data=mpg, aes(x=drv)) + geom_bar() #빈도 막대 그래프

ggplot(data=mpg, aes(x=hwy)) + geom_bar() #연속 변수
```

---


❓ **문제**. 
```
Lahman데이터로 2019년 MLB의 포지션별 빈도를 그래프로 그려보자.
```

💡 **답**.


```r
Fielding_2020 <- Fielding %>%
  filter(yearID == '2020') #2020년 자료만 추출
ggplot(data=Fielding_2020, aes(x=POS)) + geom_bar()
```

![Untitled 4](https://user-images.githubusercontent.com/115082062/201665373-afa8995c-f776-4966-b7ed-a5fdd99534fb.png)

---

**08-3. 선 그래프**

시계열 데이터를 주로 선 그래프로 나타낸다. 선 그래프를 그리기 위해 `ggplot2` 패키지의 `economics` 데이터를 이용해보자. 선 그래프는 `geom_line()`함수를 사용한다.

```r
ggplot(data=economics, aes(x=date, y=unemploy)) + geom_line()
```

---


❓ **문제.** 
```
세기말을 대표하는 홈런타자 배리본즈와 마크맥과이어, 이 둘의 통산 홈런 시계열 그래프를 Lahman데이터로 그려보자. 둘의 그래프를 색깔을 달리하여 동시에 나타내라.
```

💡 **답.**

```r
bonds <- Batting %>%
  filter(playerID=='bondsba01') #본즈의 데이터만 추출
mcgwire <- Batting %>%
  filter(playerID=='mcgwima01') #맥과이어의 데이터만 추출
bonds_mc <- bind_rows(bonds, mcgwire) #둘의 데이터를 세로로 결합

#group 매개변수로 그래프 나눌 기준 선정
#shape 매개변수로 모양 나눌 기준 선정
ggplot(data=bonds_mc, aes(x=yearID, y=HR, group=playerID, colour=playerID, shape=playerID)) +
  geom_line() +
  geom_point() #그래프 꼭짓점에 모양 추가
```

![Untitled 5](https://user-images.githubusercontent.com/115082062/201665560-fcc9237d-6573-44fc-9cf5-2c7e04aa9fae.png)

---

**08-4. 상자 그림(Box Plot)**


`mpg` 데이터의 `drv`별 `hwy`를 상자 그림으로 나타내보자.

```r
ggplot(data=mpg, aes(x=drv, y=hwy)) + geom_boxplot()
```

---


❓ **문제.** 
```
2020 아메리칸리그의 팀별 홈런을 상자 그림으로 나타내라. 이 때 50타수 이상의 타자만을 대상으로 하라.
```

💡 **답.**


```r
batting_2019 <- Batting %>%
  filter(yearID=='2019'& AB>=50 & lgID=='AL')

ggplot(data=batting_2019, aes(x=teamID, y=HR)) +
  geom_boxplot()
```

![Untitled 6](https://user-images.githubusercontent.com/115082062/201665725-a86bdee4-04cb-4a7f-9ef1-2fb89469b248.png)
캔자스시티 솔레르와 에인절스 트라웃의 홈런 기록(48개, 45개)이 극단치로 눈에 띈다.

---

### 09. 데이터 분석 프로젝트 - Lahman패키지로 MLB 분석

원래 해당 챕터에선 한국복지패널 데이터를 사용해야 하나, 데이터가 다운로드되지 않는 탓에 Lahman 패키지로 MLB 데이터를 분석하기로 하였음.

❓ **문제.** 
```
MLB타자들의 나이에 따른 연봉의 변화 추이를 선그래프로 나타내자. 이 때 1995년 이후 자료만을 사용하며, 40세 이하 선수만을 대상으로 한다.
```

💡 **답.**


```r
master_new <- Master %>%
  select(playerID, birthYear) #선수id와 출생년도 추출
salary_new <- Salaries %>%
  select(playerID, salary, yearID) #선수id와 당해년도와 연봉 추출
Batting_new <- left_join(Batting, master_new, by="playerID") #출생년도 데이터 합치기
Batting_new <- left_join(Batting_new, salary_new, by=c("playerID","yearID")) #연봉 데이터 합치기

batting_salary <- Batting_new %>%
  mutate(age=(yearID-birthYear+1)) %>% #나이 변수 추가
  filter(yearID>=1995 & !is.na(salary) & age<=40) %>% #1995년 이후 자료, salary 결측값 제거, 40세 이하만 추출
  group_by(age) %>% #나이로 그룹화
  summarise(mean_salary = mean(salary)/10000) #10,000달러 단위로 나이별 평균 연봉 집ㄱ
```

![Untitled 7](https://user-images.githubusercontent.com/115082062/201665847-f5b369af-c1a6-4de6-a831-126580374ae9.png)

35세 때 가장 절정의 연봉(약 450만 달러)을 받는 것으로 보인다. 확실히 30세 이후로 접어들며 FA신분을 취득하거나 커리어 하이를 찍는 선수들이 많다보니 연봉이 가파르게 상승하는 것으로 보인다. 40세에 가까운 선수들은 기량이 노쇠화하였음에도 베테랑/ 프랜차이즈 우예 등의 이유로 연봉이 높을 수도 있다.(애초에 40세까지 야구를 할 정도라면 기량이 워낙 출중한 것이니 높은 연봉은 자연스럽기도 하다.)


❓ **문제.** 
```
메이저리그의 시대를 4개로 나눠보자(dead볼 시대(1920년 이전), liveball 시대(1920년~1969), flyball혁명(1970~1999), shifte혁명(2000~2020). 
각 시대마다 어느 포지션이 몇 퍼센트의 아웃카운트를 책임졌는지 보여주는 비율 막대그래프를 만들어보자
```
💡 **답.**


```r
out_pos_era1 <- Fielding %>%
  #시대에 따라 era변수를 dead(~1919), live(1920~1969), flyball(1970~1999), shift(2000~)로 나눈다
  mutate(era=ifelse(yearID<1920,'dead',ifelse(yearID<1970,'live',ifelse(yearID<2000,'flyball','shift')))) %>%
  group_by(era) %>% #era로 그룹화하여
  summarise(era_po=(sum(PO))) #era별 아웃카운트 수를 변수로 만든다

out_pos_era2 <- Fielding %>%
  mutate(era=ifelse(yearID<1920,'dead',ifelse(yearID<1970,'live',ifelse(yearID<2000,'flyball','shift')))) %>%
  group_by(era,POS) %>% #era와 포지션으로 그룹화하여
  summarise(erapos_po=(sum(PO))) #시대별,포지션별 아웃카운트 수를 변수로 만든다

#앞서 만든 두 테이블을 합친다
out_pos_era3 <- left_join(out_pos_era1, out_pos_era2, by='era') %>%
  mutate(proportion=(erapos_po/era_po)) #포지션별 아웃카운트 비중을 시대에 따라 나타내도록 한다

ggplot(data=out_pos_era3, aes(x=era, y=proportion, fill=POS))+ #fill을 POS로 설정하여 포지션별로 색깔을 달리 한다
  geom_col()+
  coord_flip() #그래프를 90도 회전시킨다
```

![Untitled 8](https://user-images.githubusercontent.com/115082062/201666395-5e8db669-bcb5-4298-aceb-00974b145150.png)

데드볼시대는 역시 타구가 외야로 뻗는 법이 거의 없었다. OF(외야수)가 처리한 비율이 다른 시대에 비해 현저히 낮다. 대신에 타구가 내야에 갖혀 1루 포스아웃으로 연결되는 경우가 굉장히 많았던 것으로 보인다. 가장 현대인 shift 시대엔 포수가 잡아낸 아웃이 현저히 많다. 이는 탈삼진이 많아졌다는 것으로 해석할 수 있다.


❓ **문제.** 
```
명예의 전당 입성 선수들을 포지션별로 빈도 그래프로 나타내려고 한다.
```

💡 **답.** 아직 해결 못함


```r
position <- Fielding %>%
  group_by(playerID) %>%
  summarise(pos = max(POS)) #이 부분이 잘못됨.

fame <- left_join(HallOfFame, position, by="playerID") %>%
  filter(category=='Player' & !is.na(pos))
ggplot(data=fame, aes(x=pos,fill=inducted)) + 
  geom_bar(position='dodge')

View(Fielding)
```

---

### 10. 텍스트 마이닝

텍스트 마이닝을 할 때 가장 먼저 하는 작업은 문장을 구성하는 어절들이 어떤 품사인지 확인하는 ‘형태소 분석(Morphology Analysis)’이다. `KoNLP`(Korean Natural Language Processing) 패키지를 이용하면 한글 텍스트의 형태소를 분석할 수 있다.

책에 나온 설치 방식은 버전 호환이 안되는 관계로 해당 챕터는 건너뛰었다.

---

### 11. 지도 시각화

**11-1. 미국 주별 강력 범죄율 단계 구분도**

지역별 통계치를 색깔의 차이로 표현한 지도를 단계구분도(Choropleth Map)이라 한다. 미국 주별 강력 범죄율 데이터를 이용해 단계구분도를 만들어보자. 단계구분도는 `ggiraphExtra` 패키지로 만들 수 있는데, 그 전에 먼저 `mapproj` 패키지를 설치해야 한다.

`USArrests` 데이터는 1973년 미국 주별 강력 범죄율 정보를 담고 있다. 이 데이터는 지역명 변수가 따로 없기 때문에 `tibble` 패키지의 `rownames_to_column()`함수로 행 이름을 state 변수로 바꿔 새 데이터프레임으로 만들어야 한다.

뒤에 사용할 지도 데이터의 지역명 변수는 모두 소문자이기에 이에 맞춰주기 위해 `state` 값을 `tolower()`로 소문자로 만든다.

```r
install.packages("mapproj")
install.packages("ggiraphExtra")
library(ggiraphExtra)

str(USArrests)
library(tibble)
crime <- rownames_to_column(USArrests, var="state")
crime$state <- tolower(crime$state)
```

단계구분도를 만들려면 지역별 위도, 경도 정보가 있는 maps 패키지가 필요하다. 그리고  패키지의 `map_data()`를 이용해 이 데이터를 데이터 프레임으로 불러온다.

```r
install.packages("maps")
library(ggplot2)
states_map <- map_data("state")
```

이제 데이터가 모두 준비되었으니 `ggChoropleth()`함수로 단계 구분도를 만들어보자. 살인 범죄 건수를 색깔로 표현하기 위해 `fill` 매개변수를 `Murder`로 지정하고, `map_id`에 지역 구분 기준이 되는 `state`를 지정한다. `map` 매개변수에는 앞서 만든 지도 데이터프레임 `states_map`을 넣는다.

```r
ggChoropleth(data=crime, aes(fill=Murder, map_id=state), map=states_map)
```

![Untitled 9](https://user-images.githubusercontent.com/115082062/201666513-af8cbeba-0c43-4465-905d-082e19fa1733.png)

만약 `interactive` 파라미터를 TRUE로 설정하면, 마우스 움직임에 반응하는 **인터랙티브 단계 구분도**를 만들 수 있다.

```r
ggChoropleth(data=crime, aes(fill=Rape, map_id=state), map=states_map, interactive = T)
```

---

**11-2. 대한민국 시도별 인구, 결핵 환자 수 단계 구분도 만들기**

`kormaps2014` 패키지를 이용하면 대한민국의 지역 통계 데이터와 지도 데이터를 사용할 수 있다.

패키지가 설치되지 않는 관계로 생략한다.

---

### 12. 인터랙티브 그래프

인터랙티브 그래프(Interactive Graph)란 마우스 움직임에 반응하며 실시간으로 형태가 변하는 그래프이다. 그래프를 HTML 포맷으로 저장하면 일반 사용자들도 웹 브라우저에서 그래프를 조작할 수 있다.

`ggplot()`으로 만든 그래프에 `ggplotly()`를 적용하면 인터랙티브 그래프가 만들어진다.

```r
install.packages("plotly")
library(plotly)
install.packages("ggplot2")
library(ggplot2)
p <- ggplot(data=mpg, aes(x=displ, y=hwy, col=drv))+geom_point()
ggplotly(p)
```

![1 2](https://user-images.githubusercontent.com/115082062/201666618-b7a425fe-f12e-4b59-bcb7-db67f7b34b69.jpg)

점 위에 마우스 커서를 갖다대면 값이 나타나고, 특정 부분을 드래그하면 그 영역을 확대할 수 있다.

뷰어 창에서 Export → Save as Web Page를 클릭하면 그래프를 HTML 포맷으로 저장할 수 있다. 이 파일은 R을 사용하지 않아도 웹에서 열어볼 수 있다.

---

❓ **문제**. 
```
2019년 메이저리그 포지션별 홈런 수를 인터랙티브 그래프로 나타내보자.
```
💡 **정답.**


```r
batting_2019 <- Batting %>%
  filter(yearID==2019)
fielding_2019 <- Fielding %>%
  filter(yearID==2019)
POSHR <- ggplot(data=poshr, aes(x=POS, y=HR, fill=POS)) + geom_col()
ggplotly(POSHR)
```

![2 2](https://user-images.githubusercontent.com/115082062/201666686-32610c0f-7690-4d19-8138-45cdb45a17f1.jpg)

---

이번엔 `dygraphs`패키지로 인터랙티브 시계열 그래프를 만들어보자.

시계열 그래프를 만들려면 `xts()`를 이용해 데이터를 시간 순서 속성을 갖게 해야 한다.

```r
install.packages("dygraphs")
library(dygraphs)
library(xts)
economics <- ggplot2::economics
eco <- xts(economics$unemploy, order.by=economics$date)
dygraph(eco)
```

`dyRangeSelector()`를 추가하면 그래프 아래에 날짜 범위 선택 기능이 추가된다.

```r
dygraph(eco) %>% dyRangeSelector()
```

여러 값을 동시에 표현할 수도 있다. `economics`데이터의 `unemploy`와 `psavert`를 함께 표현해보자.

```r
ecoa <- xts(economics$psavert, order.by=economics$date)
ecob <- xts(economics$unemploy/1000, order.by=economics$date)
eco2 <- cbind(ecoa, ecob) #가로로 두 데이터 묶어주기
#xts타입은 rename()으로 변수명을 수정할 수 없으므로 colnames() 사용
colnames(eco2) <- c("psavert","unemploy") 
dygraph(eco2) %>% dyRangeSelector()
```

![4](https://user-images.githubusercontent.com/115082062/201666888-a609e9b9-8526-4bb2-819d-058a0808080e.jpg)


---

❓ **문제**. 
```
1901년부터 아메리칸리그와 내셔널리그 각각의 시즌 평균자책점을 시계열 인터랙티브 그래프로 나타내라. (Lahman 패키지 활용)
```
💡 **정답**.


```r
ALout <- Pitching %>%
  filter(yearID>=1901 & lgID=="AL")%>%
  group_by(yearID) %>%
  summarise(sum_out=sum(IPouts))

ALer <- Pitching %>%
  filter(yearID>=1901 & lgID=="AL")%>%
  group_by(yearID) %>%
  summarise(sum_er=sum(ER))

NLout <- Pitching %>%
  filter(yearID>=1901 & lgID=="NL")%>%
  group_by(yearID) %>%
  summarise(sum_out=sum(IPouts))

NLer <- Pitching %>%
  filter(yearID>=1901 & lgID=="NL")%>%
  group_by(yearID) %>%
  summarise(sum_er=sum(ER))

ALouter <- left_join(ALout, ALer, by="yearID")
ALouter <- ALouter %>%
  mutate(inn=sum_out/3) %>%
  mutate(era=(9*sum_er)/inn) %>%
  mutate(lgID="AL")

NLouter <- left_join(NLout, NLer, by="yearID")
NLouter <- NLouter %>%
  mutate(inn=sum_out/3) %>%
  mutate(era=(9*sum_er)/inn) %>%
  mutate(lgID="NL")

ALLERA <- bind_rows(ALouter, NLouter)

era <- ggplot(data=ALLERA, aes(x=yearID, y=era, group=lgID, colour=lgID))+geom_line()  
ggplotly(era)
```

![Untitled 5](https://user-images.githubusercontent.com/115082062/201667006-63f30109-fba7-48a1-b44b-02e2b5e31c77.png)

---

### 13. 통계 분석 기법을 이용한 가설 검정

**13-1. t검정**

t-test는 두 집단 평균에 통계적으로 유의한 차이가 있는지 알아볼 때 사용하는 통계 분석 기법이다. R에 내장된 `t.test()`를 이용하면 된다.

우선 `mpg` 데이터를 불러와 `class`, `cty` 변수만 남기고 `class`는 `compact`와 `suv`만 남긴다.

```python
mpg <- as.data.frame(ggplot2::mpg)
mpg_diff <- mpg %>%
  select(class, cty) %>%
  filter(class %in% c("compact", "suv"))
```

`t.test`는 `data` 매개변수에 분석할 데이터를 입력하고, 두번째 인수에 비교할 두 값을 ~기호로 연결해준다. 집단의 분산이 같다면 `var.equal`에 `T`를 지정한다.

```python
t.test(data=mpg_diff, cty~class, var.equal=T)

#결과
Two Sample t-test

data:  cty by class
t = 11.917, df = 107, p-value < 2.2e-16 
alternative hypothesis: true difference in means between group compact and group suv is not equal to 0
95 percent confidence interval:
 5.525180 7.730139
sample estimates:
mean in group compact     mean in group suv 
             20.12766              13.50000
```

`p-value`가 유의확률을 의미한다. 일반적으로 `**p-value`가 0.5 미만**이면 집단 간 차이가 통계적으로 유의하다고 해석한다.

---

❓ **문제.** 
```
2019년 MLB에서 포지션 별로 도루 개수가 유의미한 차이가 있는지 알아보려고 한다. 비교대상은 유격수와 포수이고, 40경기 이상 출전한 선수를 대상으로 한다.
```
💡 **정답.**


```python
bat_2019 <- Batting %>%
  filter(yearID==2019 & G>=40)
fie_2019 <- Fielding %>%
  filter(yearID==2019)
player_2019 <- left_join(bat_2019, fie_2019,by="playerID")

player_2019_SB <- player_2019 %>%
  select(playerID, POS, SB.x) %>%
  filter(POS %in% c("SS","C"))
head(player_2019_SB)

t.test(data = player_2019_SB, SB.x~POS, var.equal=T)

#결과
Two Sample t-test

data:  SB.x by POS
t = -5.5016, df = 173, p-value = 1.336e-07
alternative hypothesis: true difference in means between group C and group SS is not equal to 0
95 percent confidence interval:
 -7.625180 -3.598501
sample estimates:
 mean in group C mean in group SS 
        1.057971         6.669811
```

---

**13-2. 상관분석**

상관분석은 두 연속 변수가 서로 관련이 있는지 검증하는 기법이다. 상관계수(correlation coefficient)로 두 변수가 얼마나 관련되어 있는지 알 수 있다. 상관계수는 **-1에서 1**의 값을 지니고 절댓값이 1에 가까울수록 관련성이 큼을 의미한다. **양수면 정비례, 음수면 반비례** 관계이다.

R에 내장된 `cor.test()`를 이용하면 상관분석을 할 수 있다.

```python
economics <- as.data.frame(ggplot2::economics)
cor.test(economics$unemploy, economics$pce)

#결과
Pearson's product-moment correlation

data:  economics$unemploy and economics$pce
t = 18.63, df = 572, p-value < 2.2e-16
alternative hypothesis: true correlation is not equal to 0
95 percent confidence interval:
 0.5608868 0.6630124
sample estimates:
      cor 
0.6145176
```

여러 변수의 관련성을 한 눈에 알아보고자 할 경우, 상관행렬을 만들면 된다. R에 내장된 `mtcars`데이터를 이용해 상관행렬을 만들어보자. `cor()`을 이용하면 상관행렬을 만들 수 있다.

```python
			mpg   cyl  disp    hp  drat    wt  qsec    vs
mpg   1.00 -0.85 -0.85 -0.78  0.68 -0.87  0.42  0.66
cyl  -0.85  1.00  0.90  0.83 -0.70  0.78 -0.59 -0.81
disp -0.85  0.90  1.00  0.79 -0.71  0.89 -0.43 -0.71
hp   -0.78  0.83  0.79  1.00 -0.45  0.66 -0.71 -0.72
drat  0.68 -0.70 -0.71 -0.45  1.00 -0.71  0.09  0.44
wt   -0.87  0.78  0.89  0.66 -0.71  1.00 -0.17 -0.55
qsec  0.42 -0.59 -0.43 -0.71  0.09 -0.17  1.00  0.74
vs    0.66 -0.81 -0.71 -0.72  0.44 -0.55  0.74  1.00
```

`corrplot()`을 이용하면 상관행렬을 히트맵으로 시각화할 수 있다.

```python
install.packages("corrplot")
library(corrplot)
corrplot(car_cor)
```

![1 3](https://user-images.githubusercontent.com/115082062/201667102-81cee162-36ba-4705-8bb1-2b6fd94b2858.jpg)

```python
corrplot(car_cor, method="number")
```

![2 3](https://user-images.githubusercontent.com/115082062/201667152-e5ca4120-541e-4491-ad52-c9df117b3c3a.jpg)

```python
col <- colorRampPalette(c("#BB4444","#FFFFFF","#77AADD","#4477AA"))
corrplot(car_cor, 
         method='color', #색깔로 표현
         col = col(200), #색상 200개 선정
         type = 'lower', #대각성분 아래쪽 행렬만 표시
         order = 'hclust', #유사한 상관계수끼리 군집화
         addCoef.col = 'black', #상관계수 색깔
         tl.col = 'black', #변수명 색깔
         tl.srt = 45, #변수명 45도 기울임
         diag = F) #대각성분 제외
```

![3](https://user-images.githubusercontent.com/115082062/201667219-c4a9570a-0d98-4007-a1ff-31d62fa1f4da.jpg)

---

❓ **문제.** 
```
MLB의 타자 스탯들 간의 상관행렬을 만들고 이를 시각화하라. 단, 2018년부터의 데이터를 사용하고, 스탯은 가중출루율, 타율, 볼넷대비삼진, 순수장타율, 출루율, 도루성공률, 장타율, 병살타, 안타를 사용하라.
```
💡 **정답.**

```python
install.packages("corrplot")
library(corrplot)

Batting_cor <- Batting %>%
  filter(yearID>=2018) %>%
  mutate(wOBA = round((0.691*(BB-IBB) + 0.722*HBP + 0.884*(H-X2B-X3B-HR) + 1.257*X2B + 1.593*X3B + 2.058*HR)/(AB+BB-IBB+SF+HBP),3)) %>%
  mutate(avg = round(H/AB,3)) %>%
  mutate(spb = round(SO/BB,3)) %>%
  mutate(BABIP=round((H-HR)/(AB-SO-HR+SF),3)) %>%
  mutate(OBP = round((H+BB+HBP)/(AB+BB+HBP+SH),3)) %>%
  mutate(SBA = round(SB/(SB+CS),3)) %>%
  mutate(SLG = round(((H-X2B-X3B-HR)+X2B*2+X3B*3+HR*4)/AB,3)) %>%
  filter(AB>=100) %>%
  filter(!is.na(SBA)) %>%
  select(wOBA, avg, spb, BABIP, OBP, SBA, SLG, RBI, GIDP, H)
           

bat_cor <- cor(Batting_cor)
corrplot(bat_cor)
```

![1 4](https://user-images.githubusercontent.com/115082062/201667386-12d8dc08-d786-40b8-b5ef-961290000580.jpg)

---

### 14. R Markdown으로 데이터 분석 보고서 만들기

[File → New File → R Markdown]을 클릭하면 마크다운 문서 생성 창이 열린다.

라이브러리 문제로 Markdown 실행 불가

### 15.
