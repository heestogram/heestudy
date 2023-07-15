# 제 4회 빅스타 경진대회(KOGAS 한국가스공사 주관)
## Task2 생산기지 BOG 최적가동 예측 모델 개발

### intro
- LNG 저장 탱크에서 자연적으로 발생하는 BOG의 발생 시점을 파악하여 최적의 BOG 처리 솔루션을 제안
- 학습데이터: LNG 및 BOG 공정에 필요한 각종 장비의 10분 단위 측정값
- 평가데이터: 1시간 전 측정값 및 기타 변수를 활용해 10분 후 탱크의 최소/최대 압력을 예측

### Data
- 기상청 데이터 수집
- 결측치 원인 파악 및 보간

### Feature Engineering
- 시간 파생변수(cos 변환), 과거 압력값 lag 파생변수 등 추가
- 다중공선성, metric 등 활용하여 25개 변수 select

### Modeling
- RF, XGB, LGBM Stacking한 모델 vs XGB 단일 모델 사용 -> XGB 최종 모델 확정
- 랜덤서치 하이퍼파라미터 튜닝

### Conclusion
- LTD 데이터, BOG 자동 조절 등 사업화 IDEATION 진행
- 리더보드 10위
- 우수상 수상
  
