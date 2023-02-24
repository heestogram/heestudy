# Diffense Stat

## Standard Stats

- Intentional Walk(IBB)
    
    고의사구
    
- Passed Ball(PB)
    
    wild pitch는 투수 귀책, passed ball은 포수 귀책. passed ball은 error로 보지 않음. 또한 passed ball로 점수를 내주는 경우에도 투수 방어율에 영향을 주지 않음.
    
- put out(자살)-assist(보살)
    
    태그아웃, 포스아웃, 삼진 시 포구⇒put out
    
- total chance(TC)
    
    아웃을 기록할 수 있었던 찬스. put out+assist+error. 그러나 맹점이 있음. 다이빙 캐치를 하여 어렵게 타구를 잡아내면 그건 total chance에 산입되지만, 그 타구를 놓치면 안타로 기록되어 total chance에 산입되지 않음.
    
- pickoff attempt
    
    견제 시도. pickoff는 견제사
    

---

## Advanced Stats

- Defensive Efficiency Ratio(DER)
    
    인플레이 타구를 아웃으로 만들 확률
    
    formula = 1 - ((안타+에러-홈런) / (타석-볼넷-삼진-몸에맞는볼-홈런))
    
- Defensive Runs Saved(DRS)
    
    한 선수가 그 포지션의 다른 선수보다 얼마나 더 많은 Runs(득점)을 막아냈는지를 측정한 지표. 즉, 한 선수의 상대적 수비 가치를 의미한다.
    
    DRS는 계산이 어렵지만, 한 눈에 들어온다는 장점이 있다. 예를 들어 한 선수의 DRS가 +5라면, 평균적인 선수의 수비력보다 5만큼 뛰어나다는 뜻이다.
    
    하지만 포지션별로도 수비 난이도가 상이하기 때문에, 서로 다른 포지션의 선수를 비교하기 위해선 포지션 조정을 가한 DEF를 사용한다.
    
    | Defensive Ability | DRS |
    | --- | --- |
    | Gold Glove Caliber | +15 |
    | Great | +10 |
    | Above Average | +5 |
    | Average | 0 |
    | Below Average | -5 |
    | Poor | -10 |
    | Awful | -15 |
    
    DRS는 9가지 요소로 구성되어있다.
    
    - Range&Positioning Runs Saved(rPM, 포수 제외 모두)
    - Catcher Adjusted Earned Runs Saved (포수)
    - Strike Zone Runs Saved (포수)
    - Catcher Stolen Base Runs Saved (rSB, 포수)
    - Pitcher Stolen Base Runs Saved (rSB, 투수): 도루 저지(혹은 예방)가 흔히 포수의 몫이라고 생각하지만, 실은 투수의 몫이 65%에 달한다고 봐도 무방하다.
    - Outfielder Arm Runs Saved (rARM, 외야수): 주자가 extra-base situation에서 진루했는지의 비율을 갖고 외야수 어깨의 정확도와 강도를 평가한다. extra-base situation이란 1)주자가 무사히 다음 베이스로 간 경우 2)진루하려다 아웃당한 경우 3)진루하지 않고 원래 베이스에 묶인 경우로 볼 수 있다. 물론 모든 상황이 동일한 조건은 아니므로 약간의 조정을 거친 후에 계산한다.
    - Bunt Runs Saved (rBU, 1,3루수, 투수, 포수)
    - Double Play Runs Saved (rGDP, 1,2,3루수, 유격수)
    - Good Plays/Misplays Runs Saved (모두)
    
    [Fielding Bible](http://fieldingbible.com/Fielding-Bible-FAQ.asp)
    
- Range Factor(RF)
    
    한 선수의 9이닝당 put outs+assists. 만약 ground-ball pitcher가 마운드에 오른 경우엔 내야수들의 RF를 높일 기회가 더 늘어나게 된다. 즉, 선수의 실력보다는 경기 상황이 주는 영향이 더 크다.
    
    그러나 한 선수가 얼마나 많은 영역을 커버했는지를 알아보기에는 중요한 지표이다.
    
- Ultimate Zone Rating(UZR)
    
    한 선수가 그 포지션의 다른 선수보다 얼마나 더 많은 Runs(득점)을 막아냈는지를 측정한 지표. 즉, 한 선수의 상대적 수비 가치를 의미한다. 따라서 DRS와 상당히 흡사하지만, 세부적인 공식에서 차이가 있다.
    
    한 외야수가 플라이볼을 처리한 상황에서 그 플라이볼이 아웃될 확률이 60%였다면, 그 외야수는 0.4point를 획득한다. 만약 그 외야수가 플라이볼을 처리하지 못했다면 0.6point를 잃게 된다.
    

---

## Statcast

- Arms Strength(ARM)
    
    the maximum velocity of any throw made by a fielder(야수가 던진 공의 최고 시속.)
    
- Distance Covered(DCOV)
    
    공을 친 시점부터 공이 필드에 떨어지기까지 야수가 이동한 거리. 이 거리는 야수가 실제로 이동한 거리로, 야수의 첫 위치부터 공까지의 직선 거리가 아니다. 만약 직선거리를 DCOV로 나누면 **Route Efficiency**라는 새로운 지표를 얻는다.
    
- Catch Probability
    
    타구가 외야수에게 잡힐 확률. 이 확률은 네 가지 요인에 의해 계산된다.
    
    1) 야수가 타구를 잡기 위해 이동하는 최소거리(실제 이동 거리가 아님)
    
    2) 야수가 타구를 잡기 위해 걸리는 시간(투수가 공 던진 시점부터 잰다)
    
    3) 야수가 타구를 잡기 위해 가야 하는 방향(머리 뒤로 가는 타구는 잡기가 어려우므로 가중치 부여함)
    
    4) 낙구 지점이 벽과 가까운지
    
    Catch Probability는 OAA를 계산하는 데 쓰인다.
    
- Jump
    
    외야수가 얼마나 신속하게 타구에 반응하고, 얼마나 올바른 경로로 공을 따라가는지를 보여주는 지표. 이 때 catch probability가 90%이하인 타구만 측정된다. 이 지표는 세 가지 요인에 의해 결정된다.
    
    1) reaction: 외야수가 투구 시점부터 1.5초까지 커버한 걸음(반응속도, 판단력)
    
    2) burst: 외야수가 reaction 이후 1.5초동안 커버한 걸음(가속도)
    
    3) route: 최단거리에 비해 걸은 실제 걸음 수
    
- Outs Above Average(OAA)
    
    수비 성공 확률을 기반으로 평균 대비 얼마나 많은 아웃을 잡아냈는지를 보여줌. 수비 성공 확률이 0.75인 타구를 처리하면 +0.25를 얻고 반대로 실패하면 0.75를 잃는다. 수비 성공 확률을 구하기 위해서는 포구 지점까지의 이동거리, 이동시간, 송구 거리, 타자의 주력 등을 고려해야 한다.
    
    expected catch percentage는 특정 야수에게 가는 타구의 수비 성공 확률을 나타낸다.
    
    actual catch percentage는 말 그대로 특정 야수가 타구를 아웃으로 만든 확률을 나타낸다.
    
    catch percentage added는 앞선 두 수치 간의 차이를 의미한다.
    
    baseball savant 제공 OAA 순위표.
    
    [Statcast Catch Probability](https://baseballsavant.mlb.com/leaderboard/catch_probability)
    
- Pop Time
    
    투구한 공이 포수 미트에 포구된 시점부터 포수가 주자를 잡기 위해 그 공을 던져 베이스에 안착하기까지 걸린 시간.
    
    아래는 2018시즌 pop time 베스트6인이다.(보통 주자가 도루 시 2루까지 걸리는 시간이 2.01초)
    
    1.90 seconds — J.T. Realmuto
    
    1.93 seconds -- Yan Gomes
    
    1.94 seconds -- Jorge Alfaro
    
    1.94 seconds -- Austin Hedges
    
    1.94 seconds -- Manny Pina
    
    1.94 seconds -- Gary Sanchez
    
- Shifts
    
    타자 성향에 맞춘 수비 조정. 2017MLB 기준 좌타자는 22.1%의 쉬프트가, 우타자는 5.2%의 쉬프트가 걸렸다.
    
    쉬프트의 여러가지 종류는 아래 링크 참조
    
    [Shifts | Glossary | MLB.com](https://www.mlb.com/glossary/statcast/shifts)