# 깃허브 블로그 만들기
<br>

## 1. 기본 정보 변경
<br>
github.io 폴더 -> &#95;config.yml

<br>
가장 기본적인 초기 정보 setting이다.
<br>

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
 초기설정이 끝났다면 아래와 같은 화면이 생성된다. 좌단에는 프로필 소개가 잘 들어가 있고, 하단에는 footer에서 기입한 내용(github icon)이 보일 것이다.
 <br>
 캡쳐 화면에 보이는 최근 포스트 업로드 방법과 우측상단 카테고리들 만드는 법은 다음 단계에서 차차 확인할 수 있다.
 <br><br>
 <img src= "https://user-images.githubusercontent.com/115082062/201826923-2a2482e8-c8a6-4955-868a-651f4d48e3d7.JPG">

 ## 2. 카테고리 만들기
 <br>
 github.io 폴더 -> &#95;data 폴더 -> navigation.yaml 파일
 <br>
 무척이나 간단하다. 생성하고 싶은 카테고리의 title을 적어주고 url을 설정해주면 된다. 이 때 주석처리는 당연히 풀어줘야 한다.<br>
 
 <br>
```yml
# main links
main:
  - title: "About Me"
    url: /me/
  # - title: "About"
  #   url: https://mmistakes.github.io/minimal-mistakes/about/
  - title: "Sample Posts"
  #   url: /year-archive/  #안 보이게 하고 싶은 부분은 주석처리
  # - title: "Sample Collections"
  #   url: /collection-archive/
  # - title: "Sitemap"
  #   url: /sitemap/
```
 

