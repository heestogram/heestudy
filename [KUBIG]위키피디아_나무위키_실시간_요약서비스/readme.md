# [KUBIG CONTEST] 위키피디아, 나무위키 실시간 요약 서비스
## TEAM 세줄요약좀
### 15기 반민정, 16기 엄기영 17기 김희준

### Intro
- 방대한 양의 위키 문서를 읽기조차 버거운 현대인을 위해, 이를 실시간으로 요약해주는 시스템 개발
- 위키피디아 API를 활용하여 원하는 문서를 입력하면 그에 대한 문서 요약
- 나무위키를 크롤링하여 원하는 문서를 입력하면 그에 대한 문서 요약

### Data Collect/Preprocessing
- selenium 이용한 웹 크롤링
- 위키피디아 API 이용
- 태그 제거, 토큰화 등 전처리 수행

### Modeling
- KOBART summarization 모델 digit82, gogamza, ainize 사용
