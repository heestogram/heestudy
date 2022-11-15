# 깃허브 블로그 만들기
<br>

## 1. 기본 정보 변경
<br>
가장 기본적인 초기 정보 setting이다. github.io 폴더 -> &#95;config.yml 파일로 들어간다.
<br/>

```yml
# Site Settings
locale                   : "ko-KR" #사용 언어
title                    : "Heestogram's Heestudy" #블로그 이름
title_separator          : "-"
subtitle                 : "Catch Jun If U Can" #블로그 이름 밑에 들어갈 부제목
name                     : "Hee Jun Kim"  #사용자 이름
description              : "study portfolio" #블로그에 대한 설명
url                      : "https://heestogram.github.io" #블로그 주소
baseurl                  : # the subpath of your site, e.g. "/blog"
repository               : "https://github.com/heestogram/heestogram.github.io" #해당 레퍼지터리 주소
teaser                   : # path of fallback teaser image, e.g. "/assets/images/500x300.png"
logo                     : # path of logo image to display in the masthead, e.g. "/assets/images/88x88.png"
masthead_title           : "Heestogram's Heestudy" #블로그 이름
# breadcrumbs            : false # true, false (default)
words_per_minute         : 200
```
<br>

스크롤을 조금 더 내리면 아래와 같은 내용이 있다. Author, 즉 블로그 사용자의 정보를 수정하는 곳이다.<br>
블로그 홈에 표시될 사용자 정보에 나타나는 내용이라고 이해하면 쉽다.
강조하고 싶은 부분은 &#42;&#42;로 감싸자.
<br><br>
또한 links 부분을 수정하여 블로그 좌단에 링크를 걸 수도 있다. 주석처리하면 그 링크는 표시되지 않는다.
<br>
email의 url을 설정할 때는 다른 것과 달리 앞에 mailto: 를 붙여줘야 한다.
<br>
```yml
# Site Author
author:
  name             : "Hee Jun Kim"
  avatar           : # path of avatar image, e.g. "/assets/images/bio-photo.jpg"
  bio              : "Wanna be a **Data Analyst**" #사용자 이름 밑에 들어가는 bio
  location         : "Seoul, Republic of Korea" #사용자 출신지
  email            :
  links:
    - label: "anthjoon11@naver.com" #블로그에 표시될 링크의 제목
      icon: "fas fa-fw fa-envelope-square" #설정된 아이콘값. 각각 고유의 값이 있음
      url: mailto:anthjoon11@naver.com #이 부분만 주석 처리하면 블로그에 표시 안 할 수 있음
    - label: "Website"
      icon: "fas fa-fw fa-website"
      # url: "https://github.com/heestogram"
    - label: "Twitter"
      icon: "fab fa-fw fa-twitter-square"
      # url: "https://twitter.com/"
    - label: "Facebook"
      icon: "fab fa-fw fa-facebook-square"
      # url: "https://facebook.com/"
    - label: "GitHub"
      icon: "fab fa-fw fa-github"
      url: "https://github.com/heestogram"
    - label: "Instagram"
      icon: "fab fa-fw fa-instagram"
      # url: "https://instagram.com/"
 ```
 <br>
 
