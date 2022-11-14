# Python MLB-StatsAPI


💡 
```
파이썬 환경에서 사용할 수 있는 MLB 데이터 API입니다. 
유용한 API임에도 불구하고, 우리말로 번역된 마땅한 웹페이지가 없어서 
직접 번역하여 해당 API를 소개하는 페이지를 만들었습니다.
```

[Home · toddrob99/MLB-StatsAPI Wiki](https://github.com/toddrob99/MLB-StatsAPI/wiki)

- Function

`pip`는 파이썬 패키지를 설치하거나 관리하는 시스템이다. MLB-StatsAPI 패키지를 설치해보자.

```python
#설치하려는 패키지 이름을 넣고 설치.
pip install MLB-StatsAPI

#패키지 업그레이드
pip install --upgrade MLB-StatsAPI

#패키지에 대한 세부 사항을 확인할 수 있다.
pip show MLB-StatsAPI

Name: MLB-StatsAPI
Version: 1.4.1
Summary: MLB Stats API Wrapper for Python
Home-page: https://github.com/toddrob99/MLB-StatsAPI
Author: Todd Roberts
Author-email: todd@toddrob.com
License: UNKNOWN
Location: /usr/local/lib/python3.7/dist-packages
Requires: requests
Required-by:

#패키지를 import한다.
import statsapi
```

## 1. Function

### 1-1. `boxscore`

특정 게임의 박스스코어를 가져오는 함수. 파라미터들의 기본값은 모두 True이다.  

`gamePk` 값을 넣으면 해당 경기의 박스스코어가 제공된다. `gamePk`란 해당 경기의 시리얼 넘버이다. 

이 때 `timecode` 파라미터에 특정 타임스탬프를 기입해주면 그 당시의 박스스코어를 출력할 수 있다. 경기의 매 순간마다 타임스탬프가 저장되는데, `statsapi.get(’game_timestamps’,{’gamePk’= })`함수를 사용하여 특정 경기의 타임스탬프들은 무엇이 있는지 확인해볼 수 있다.

```python

statsapi.boxscore(gamePk, battingBox=True, battingInfo=True, fieldingInfo=True, pitchingBox=True, gameInfo=True, timecode=None)

#예시. gamePk가 565997인 경기(필리스의 2019년 4월 24일 메츠전 1시간 24분 40초 경 박스스코어
statsapi.boxscore(565997, timecode=20190425_012240)
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
Phillies Batters                         AB   R   H  RBI BB   K  LOB AVG   OPS  | Mets Batters                             AB   R   H  RBI BB   K  LOB AVG   OPS
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
1 McCutchen  LF                           5   0   1   0   0   1   3  .250 .830  | 1 McNeil  LF                              4   0   1   0   0   0   1  .363 .928
2 Realmuto  C                             3   1   1   0   1   1   2  .282 .786  | 2 Conforto  RF                            3   0   0   0   1   1   1  .292 .986
3 Harper  RF                              4   1   1   1   1   3   4  .261 .909  | 3 Canó  2B                                3   0   3   0   1   0   0  .272 .758
4 Hoskins  1B                             4   2   2   2   1   1   3  .273 .982  | 4 Ramos, W  C                             4   0   0   0   0   3   6  .278 .687
5 Franco  3B                              5   1   1   1   0   0   3  .271 .905  | 5 Smith, Do  1B                           2   0   0   0   1   1   2  .400 .996
6 Hernández, C  2B                        5   1   1   0   0   1   2  .267 .730  |     c-Alonso, P  1B                       1   0   0   0   0   1   1  .306 1.086
7 Rodríguez, S  SS                        4   0   1   0   0   1   1  .250 .750  | 6 Frazier, T  3B                          3   0   0   0   0   0   4  .182 .705
8 Velasquez  P                            1   0   0   0   0   0   0  .167 .453  | 7 Rosario, A  SS                          4   0   1   0   0   0   1  .261 .676
    a-Williams, N  PH                     1   0   0   0   0   0   1  .150 .427  | 8 Lagares  CF                             2   0   0   0   0   1   1  .244 .653
    Neshek  P                             0   0   0   0   0   0   0  .000 .000  |     a-Nimmo  CF                           2   0   0   0   0   0   1  .203 .714
    Domínguez  P                          0   0   0   0   0   0   0  .000 .000  | 9 Vargas  P                               2   0   0   0   0   1   1  .000 .000
    b-Gosselin  PH                        1   0   1   1   0   0   0  .211 .474  |     Lugo, S  P                            0   0   0   0   0   0   0  .000 .000
    Morgan  P                             0   0   0   0   0   0   0  .000 .000  |     Zamora  P                             0   0   0   0   0   0   0  .000 .000
    c-Knapp  PH                           1   0   0   0   0   1   1  .222 .750  |     b-Guillorme  PH                       1   0   1   0   0   0   0  .167 .378
    Nicasio  P                            0   0   0   0   0   0   0  .000 .000  |     Gsellman  P                           0   0   0   0   0   0   0  .000 .000
9 Quinn  CF                               4   0   1   1   0   1   1  .120 .305  |     Rhame  P                              0   0   0   0   0   0   0  .000 .000
    1-Altherr  CF                         0   0   0   0   0   0   0  .042 .163  |     d-Davis, J  PH                        1   0   0   0   0   1   0  .276 .865
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
Totals                                   38   6  10   6   3  10  21             | Totals                                   32   0   6   0   3   9  19
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
a-Popped out for Velasquez in the 6th.                                          | a-Flied out for Lagares in the 6th.
b-Singled for Domínguez in the 8th.                                             | b-Singled for Zamora in the 7th.
c-Struck out for Morgan in the 9th.                                             | c-Struck out for Smith, Do in the 8th.
1-Ran for Quinn in the 8th.                                                     | d-Struck out for Rhame in the 9th.
                                                                                |
BATTING                                                                         | BATTING
2B: Harper (7, Vargas); Rodríguez, S (1, Rhame); Realmuto (4, Vargas).          | TB: Canó 3; Guillorme; McNeil; Rosario, A.
3B: Hoskins (1, Gsellman).                                                      | Runners left in scoring position, 2 out: Frazier, T 2; Vargas; Smith, Do 2.
HR: Hoskins (7, 9th inning off Rhame, 1 on, 0 out).                             | GIDP: McNeil.
TB: Franco; Gosselin; Harper 2; Hernández, C; Hoskins 7; McCutchen; Quinn;      | Team RISP: 0-for-6.
    Realmuto 2; Rodríguez, S 2.                                                 | Team LOB: 9.
RBI: Franco (19); Gosselin (4); Harper (15); Hoskins 2 (20); Quinn (1).         |
Runners left in scoring position, 2 out: Hoskins; Hernández, C; Knapp; Realmuto | FIELDING
    2; McCutchen.                                                               | E: Canó (3, fielding); Rosario, A 2 (7, throw, throw).
SAC: Rodríguez, S; Velasquez.                                                   |
Team RISP: 4-for-13.                                                            |
Team LOB: 11.                                                                   |
                                                                                |
FIELDING                                                                        |
DP: (Hernández, C-Rodríguez, S-Hoskins).                                        |
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
Phillies Pitchers                            IP   H   R  ER  BB   K  HR   ERA   | Mets Pitchers                                IP   H   R  ER  BB   K  HR   ERA
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
Velasquez  (W, 1-0)                         5.0   3   0   0   3   6   0   1.99  | Vargas  (L, 1-1)                            4.2   3   1   1   2   4   0   7.20
Neshek  (H, 2)                              1.0   1   0   0   0   0   0   2.70  | Lugo, S                                     2.0   0   0   0   0   2   0   4.60
Domínguez  (H, 3)                           1.0   1   0   0   0   0   0   4.32  | Zamora                                      0.1   0   0   0   0   1   0   0.00
Morgan                                      1.0   1   0   0   0   2   0   0.00  | Gsellman                                    1.0   5   3   3   0   1   0   4.20
Nicasio                                     1.0   0   0   0   0   1   0   5.84  | Rhame                                       1.0   2   2   2   1   2   1   8.10
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
Totals                                      9.0   6   0   0   3   9   0         | Totals                                      9.0  10   6   6   3  10   1
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
WP: Velasquez; Gsellman.
HBP: Realmuto (by Vargas); Frazier, T (by Velasquez).
Pitches-strikes: Velasquez 97-53; Neshek 13-8; Domínguez 9-6; Morgan 14-10; Nicasio 15-10; Vargas 89-53; Lugo, S 32-23; Zamora 5-3; Gsellman 25-17; Rhame 19-12.
Groundouts-flyouts: Velasquez 6-3; Neshek 1-2; Domínguez 1-1; Morgan 1-0; Nicasio 2-0; Vargas 8-3; Lugo, S 3-2; Zamora 0-0; Gsellman 1-1; Rhame 0-0.
Batters faced: Velasquez 22; Neshek 4; Domínguez 3; Morgan 4; Nicasio 3; Vargas 21; Lugo, S 8; Zamora; Gsellman 8; Rhame 6.
Inherited runners-scored: Lugo, S 2-0; Zamora 1-0.
Umpires: HP: Brian Gorman. 1B: Jansen Visconti. 2B: Mark Carlson. 3B: Scott Barry.
Weather: 66 degrees, Clear.
Wind: 12 mph, L To R.
First pitch: 7:11 PM.
T: 3:21.
Att: 27,685.
Venue: Citi Field.
April 24, 2019
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
```

파라미터들의 기본값은 모두 True이다.  gamePk 값을 넣으면 해당 경기의 박스스코어가 제공된다.

### 1-2. `boxscore_data`

boxscore 함수의 값을 딕셔너리로 출력한다. `boxscore`함수와 파라미터는 동일하다.

```python
#예시. gamePk가 565997인 경기(필리스의 2019년 4월 24일 메츠전 1시간 24분 40초 경 박스스코어
statsapi.boxscore_data(565997, timecode=20190425_012240)
```

### 1-3. `last_game`

특정 팀의 가장 최근 게임을 출력

```python
statsapi.last_game(teamId)
```

### 1-4. `game_highlights`

특정 게임의 하이라이트 영상 링크를 제공해주는 함수.

```python
statsapi.game_highlights(gamePk)
```

### 1-5. `game_pace`

특성 시즌의 양상을 간략화해주는 함수. season 파라미터 기본값이 현재 연도이다.

```python
statsapi.game_pace(season=datetime.now().year, sportId=1)
```

### 1-6. `game_pace_data`

`game_pace`를 딕셔너리 형태로 출력하는 함수.

```python
statsapi.game_pace_data(season=datetime.now().year, sportId=1)
```

❓ **문제.** 
```
2008년부터 2021년까지 각 시즌의 9이닝당 안타 개수 평균을 시계열 그래프로 표현하라.
```

💡 **정답.**

```python
y_list = []
x_list = []
for year in range(2008, 2022):
  y_list.append(statsapi.game_pace_data(year)['sports'][0]['hitsPer9Inn'])
  x_list.append(year)
plt.plot(x_list, y_list, marker='o')
plt.axis([2007,2022,16,19])
plt.xlabel('year')
plt.ylabel('hits per 9 innigs')
plt.show()
```

![Untitled](https://user-images.githubusercontent.com/115082062/200174629-2a2a6763-18b7-45cf-bdb2-fd6e2f73a480.png)

해를 거듭할수록 투고타저 현상이 심해지고 있다.

### 1-7. `game_scoring_play`

특정 경기의 스코어가 발생한 상황들을 설명해주는 함수이다.

```python
print(statsapi.game_scoring_plays(567074))

#위 경기에서 발생한 각 득점상황이 어떤 식으로 묘사되는지 확인해보자

Rhys Hoskins doubles (6) on a sharp line drive to left fielder Isaac Galloway.   
Bryce Harper scores.
Bottom 1 - Miami Marlins: 0, Philadelphia Phillies: 1
#1회말, Hoskins가 좌익수 Galloway쪽으로 가는 라인드라이브성 2루타를 쳤고, Harper가 득점했다.

Bryce Harper grounds out, shortstop Miguel Rojas to first baseman Martin Prado.   
Jean Segura scores.
Bottom 3 - Miami Marlins: 0, Philadelphia Phillies: 3
#3회말, Harper가 유격수땅볼(6-3)로 아웃되고 Segura가 득점했다.

Rhys Hoskins walks.   
Andrew McCutchen scores.    
Jean Segura to 3rd.  
Wild pitch by pitcher Tayron Guerrero.
Bottom 8 - Miami Marlins: 1, Philadelphia Phillies: 5
#8회말, 투수 Guerrero의 와일드피치로 Hoskins는 볼넷 출루하고 McCutchen이 득점, Segura는 3루로 진루했다.
```

### 1-8. `game_scoring_play_data`

`game_scoring_play`를 딕셔너리 형태로 출력하는 함수이다. 

딕셔너리엔 `home`, `away`, `plays` 세 가지 key가 있는데 여기서 주목할 것이 세부상황을 묘사해주는 `plays`이다. 

`plays`의 key는 각 득점 상황을 `result`, `about`, `atBatIndex`라는 key로 세분화한다. 각각이 가진 정보를 밑 코드에서 확인해보길 바란다.

```python
{'home': {'id': 143, 'name': 'Philadelphia Phillies', 'link': '/api/v1/teams/143', 'teamCode': 'phi', 'fileCode': 'phi', 'abbreviation': 'PHI', 'teamName': 'Phillies', 'locationName': 'Philadelphia', 'shortName': 'Philadelphia'}, 
'away': {'id': 146, 'name': 'Miami Marlins', 'link': '/api/v1/teams/146', 'teamCode': 'mia', 'fileCode': 'mia', 'abbreviation': 'MIA', 'teamName': 'Marlins', 'locationName': 'Miami', 'shortName': 'Miami'}, 
'plays': 
	[{'result': {'description': 'Rhys Hoskins doubles (6) on a sharp line drive to left fielder Isaac Galloway.   Bryce Harper scores.', 'awayScore': 0, 'homeScore': 1}, 
		'about': {'atBatIndex': 6, 'halfInning': 'bottom', 'inning': 1, 'endTime': '2019-04-28T17:25:19.458Z'}, 
		'atBatIndex': 6}, 
	{'result': {'description': 'Jean Segura triples (2) on a sharp ground ball to right fielder Brian Anderson.   Andrew McCutchen scores.', 'awayScore': 0, 'homeScore': 2}, 
		'about': {'atBatIndex': 20, 'halfInning': 'bottom', 'inning': 3, 'endTime': '2019-04-28T17:52:28.085Z'}, 
		'atBatIndex': 20}, 
	{'result': {'description': 'Bryce Harper grounds out, shortstop Miguel Rojas to first baseman Martin Prado.   Jean Segura scores.', 'awayScore': 0, 'homeScore': 3}, 
		'about': {'atBatIndex': 21, 'halfInning': 'bottom', 'inning': 3, 'endTime': '2019-04-28T17:53:53.570Z'}, 
		'atBatIndex': 21}, 
```

### 1-9. `get`

MLB-StatsAPI 데이터를 JSON 포맷으로 출력해주는 함수이다. `endpoint`에는 불러올 딕셔너리를 입력하고, `params`에는 그 딕셔너리에서 가져올 파라미터를 입력해준다.

```python
statsapi.get(endpoint, params, force=False)

#예를 들어 team이라는 딕셔너리에서 teamID=143(필라델피아)에 대한 정보를 가져오려면
statsapi.get('team', {'teamId':143})
```

### 1-10. `league_leaders`

```python
statsapi.league_leaders(leaderCategories, season=None, limit=10, 
	statGroup=None, leagueId=None, gameTypes=None, playerPool=None, 
	sportId=1, statType=None)
```

`leaderCategories`에는 기준이 될 스탯을 입력해야 한다. 입력 가능한 스탯들은 `statsapi.meta(’leagueLeaderTypes')`으로 확인가능하다. `leagueLeaderTypes`에는 무엇이 있는지 추출해보자

```python
def meta(a):
  
  length = len(statsapi.meta(a))
  categories = []
  b=statsapi.meta(a)[0].keys()

  keys_list=[]
  for n in b:
   keys_list.append(n)
  length2 = len(keys_list)
  for j in keys_list:
    for n in range(length):
      categories.append(statsapi.meta(a)[n][j])

  categories_arr = np.array(categories).reshape(length2,length).T
  return categories_arr
```

위 함수는 앞으로 `meta`함수에서 가져올 수 있는 value들이 무엇인지 확인하고 싶을 때 유용하게 사용할 수 있다.

`limit`에는 순위를 몇위까지 출력할지 정해준다. `statGroup`에는 해당 스탯이 어떤 그룹인지를 적어줘야 한다. 타점 스탯을 출력하는데 pitching을 적어버리면 당연히 이상한 값이 나올 것이다.

`gameTypes`에는 이 leaderboard가 정규시즌 것인지, 포스트시즌인지 여타 어떤 시리즈인지를 입력해줘야 한다.

`statTypes`에는 스탯타입을 적어준다. `career`를 입력하면 통산커리어 기준이 된다.

`playerPool`에는 순위에 들어갈 대상 선수 풀을 정해준다. 모든 선수가 대상이라면 `all`, 규정이닝(타석) 선수가 대상이라면 `qualified`, 신인이 대상이라면 `rookies`를 적어준다.

`leagueId`에는 AL(103), NL(104)를 적어준다.

❓ **문제1.** 
```
1) 2021시즌 이닝당 투구수가 가장 낮은 10인을 출력하라.
2)메이저리그 커리어 통산 최다홈런 1~10위를 출력하라.
```
💡 **정답.**

```python
#문제1)
print(statsapi.league_leaders('pitchesPerInning',statGroup='pitching', limit=10, season=2021))
Rank Name                 Team                    Value
 1   Adam Wainwright      St. Louis Cardinals     14.87
 2   Julio Urias          Los Angeles Dodgers     15.01
 3   Zack Wheeler         Philadelphia Phillies   15.02
 4   Cole Irvin           Oakland Athletics       15.04
 5   Sandy Alcantara      Miami Marlins           15.05
 6   Zack Greinke         Houston Astros          15.07
 7   Walker Buehler       Los Angeles Dodgers     15.18
 8   Anthony DeSclafani   San Francisco Giants    15.26
 9   Marcus Stroman       New York Mets           15.31
 10  Max Fried            Atlanta Braves          15.44

#문제2)
print(statsapi.league_leaders('homeRuns',statGroup='batting', limit=10, statType='career'))
Rank Name                 Team                    Value
 1   Barry Bonds          San Francisco Giants     762 
 2   Hank Aaron           Atlanta Braves           755 
 3   Babe Ruth            New York Yankees         714 
 4   Alex Rodriguez       New York Yankees         696 
 5   Albert Pujols        Los Angeles Dodgers      679 
 6   Willie Mays          San Francisco Giants     660 
 7   Ken Griffey Jr.      Seattle Mariners         630 
 8   Jim Thome            Philadelphia Phillies    612 
 9   Sammy Sosa           Chicago Cubs             609 
 10  Frank Robinson       Cincinnati Reds          586
```

### 1-11. `league_leader_data`

`league_leaders` 함수와 같은 정보를 불러오고, 이를 리스트 형식으로 반환해주는 함수이다. 파라미터가 `league_leaders`함수와 모두 동일하다.

```python
statsapi.league_leader_data(leaderCategories, season=None, limit=10, 
	statGroup=None, leagueId=None, gameTypes=None, playerPool=None, 
	sportId=1, statType=None)

#위 문제1의 함수를 league_leader_data 함수로 출력하면 아래와 같은 리스트를 반환한다.
[[1, 'Adam Wainwright', 'St. Louis Cardinals', '14.87'], [2, 'Julio Urias', 'Los Angeles Dodgers', '15.01'], [3, 'Zack Wheeler', 'Philadelphia Phillies', '15.02'], [4, 'Cole Irvin', 'Oakland Athletics', '15.04'], [5, 'Sandy Alcantara', 'Miami Marlins', '15.05'], [6, 'Zack Greinke', 'Houston Astros', '15.07'], [7, 'Walker Buehler', 'Los Angeles Dodgers', '15.18'], [8, 'Anthony DeSclafani', 'San Francisco Giants', '15.26'], [9, 'Marcus Stroman', 'New York Mets', '15.31'], [10, 'Max Fried', 'Atlanta Braves', '15.44']]
```

### 1-12. `linescore`

특정 경기의 라인스코어를 출력해주는 함수

```python
print(statsapi.linescore(gamePk, timecode=None))

#예시. 2019년 4월 25일 필리스vs메츠의 경기(565997)의 라인스코어를 출력해보자
print(statsapi.linescore(565997))

Final    1 2 3 4 5 6 7 8 9  R   H   E  
Phillies 1 0 0 0 0 0 0 3 2  6   10  0  
Mets     0 0 0 0 0 0 0 0 0  0   6   3
```

### 1-13. `lookup_player`

`lookup_value`에 검색하고자 하는 선수 이름을 입력하면, 그 선수의 이름에 대한 정보를 출력한다.

만약 nola라는 선수를 불러오기 위해 nola를 입력한다면, nolan처럼 nola를 포함하는 모든 이름이 출력되어버린다. 이것을 방지하기 위해 nola, 처럼 뒤에 콤마를 붙여주면 nola라는 이름만 인식한다.

```python
statsapi.lookup_player(lookup_value, gameType="R", season=datetime.now().year, sportId=1)

#예시. 류현진을 검색해보자.
statsapi.lookup_player('ryu')
[{'boxscoreName': 'Ryu',
  'currentTeam': {'id': 141},
  'firstLastName': 'Hyun Jin Ryu',
  'firstName': 'Hyun Jin',
  'fullFMLName': 'Hyun Jin Ryu',
  'fullLFMName': 'Ryu, Hyun Jin',
  'fullName': 'Hyun Jin Ryu',
  'id': 547943,
  'initLastName': 'H Ryu',
  'lastFirstName': 'Ryu, Hyun Jin',
  'lastInitName': 'Ryu, H',
  'lastName': 'Ryu',
  'mlbDebutDate': '2013-04-02',
  'nameFirstLast': 'Hyun Jin Ryu',
  'nickName': 'Monster', #닉네임까지도 출력된다. 즉, lookup_value에 Monster를 입력해도 류현진의 정보가 출력된다.
  'primaryNumber': '99',
  'primaryPosition': {'abbreviation': 'P', 'code': '1'},
  'useName': 'Hyun Jin'}]
```

❓ **문제.**  
```
변수를 입력하면, 이름에 그 변수를 포함한 선수들만 출력하는 함수를 만들어보자 이 때  출력형식은 `Full name: 선수이름, Position: 포지션, Team: 팀 고유 번호` 로 한다.
```
💡 **정답.**

```python
def player_npt(a):
  for player in statsapi.lookup_player(a):
    print('Full name: {} / Position: {} / Team: {}'.format(player['fullName'], player['primaryPosition']['abbreviation'], player['currentTeam']['id']))

#예시
player_npt('cole')

Full name: Gerrit Cole / Position: P / Team: 147
Full name: Dylan Coleman / Position: P / Team: 118
Full name: Cole Irvin / Position: P / Team: 133
Full name: Jared Oliva / Position: CF / Team: 134 #미들네임에 cole 들어간 경우
Full name: Josh Rogers / Position: P / Team: 120 #미들네임에 cole 들어간 경우
Full name: Cole Sands / Position: P / Team: 142
Full name: Cole Sulser / Position: P / Team: 110
Full name: Keegan Thompson / Position: P / Team: 112 #미들네임에 cole 들어간 경우
Full name: Cole Tucker / Position: SS / Team: 134
```

### 1-14. `lookup_team`

`lookup_player` 함수와 흡사하다. `lookup value`에 검색하고자 하는 팀 이름을 입력하면, 그 팀에 대한 정보를 출력해준다.

```python
statsapi.lookup_team(lookup_value, activeStatus="Y", season=datetime.now().year, sportIds=1)

#예시. new가 팀 이름에 들어가는 팀들 출력
statsapi.lookup_team('new')

[{'fileCode': 'nyy',
  'id': 147,
  'locationName': 'Bronx',
  'name': 'New York Yankees',
  'shortName': 'NY Yankees',
  'teamCode': 'nya',
  'teamName': 'Yankees'},
 {'fileCode': 'nym',
  'id': 121,
  'locationName': 'Flushing',
  'name': 'New York Mets',
  'shortName': 'NY Mets',
  'teamCode': 'nyn',
  'teamName': 'Mets'}]
```

### 1-15. `meta`

StatsAPI에서 사용하는 여러 type들이 무슨 값을 갖고 있는지 보여주는 함수이다. 가령 StatsAPI에는 `awards`(상 종류), `baseballStats`(야구 스탯 총망라한 것), `eventTypes`(경기에서 발생할 수 있는 사건의 종류) 등의 여러 가지 type이 있다. 이 각각 타입이 갖고 있는 개별 값들을 출력해준다. 

자세한 정보는 [2.meta](https://www.notion.so/Python-MLB-StatsAPI-56edea75bc664ba8a06407ef0b3a2655)에서 확인할 수 있다.

```python
statsapi.meta(type, fields=None)

#예시1. eventTypes에는 어떤 것들이 있는지 확인해보자.
statsapi.meta('eventTypes')

[{'baseRunningEvent': True,
  'code': 'pickoff_1b',
  'description': 'Pickoff 1B',
  'hit': False,
  'plateAppearance': False},
 {'baseRunningEvent': True,
  'code': 'pickoff_2b',
  'description': 'Pickoff 2B',
  'hit': False,
  'plateAppearance': False},
 {'baseRunningEvent': True,
  'code': 'pickoff_3b',
  'description': 'Pickoff 3B',
  'hit': False,
  'plateAppearance': False},
... 생략 ...

#예시2.pitchTypes(투구결과유형)에는 어떤 것들이 있는지 확인해보자
statsapi.meta('pitchCodes')

[{'code': 'R', 'description': 'Strike - Foul on Pitchout'},
 {'code': 'Y', 'description': 'Pitchout Hit Into Play - Out(s)'},
 {'code': 'M', 'description': 'Strike - Missed Bunt'},
 {'code': 'X', 'description': 'Hit Into Play - Out(s)'},
 {'code': 'O', 'description': 'Strike - Bunt Foul Tip'},
 {'code': 'E', 'description': 'Hit Into Play - Run(s)'},
 {'code': 'D', 'description': 'Hit Into Play - No Out(s)'},
 {'code': 'Q', 'description': 'Strike - Swinging on Pitchout'},
 {'code': 'Z', 'description': 'Pitchout Hit Into Play - Run(s)'},
 {'code': 'F', 'description': 'Strike - Foul'},
...생략...
```

### 1-16. `next_game`

주어진 팀의 다음 경기 `gamePK`값을 출력해주는 함수이다.

```python
statsapi.next_game(teamId)
```

### 1-17.  `notes`

각 endpoint가 필수로 가져야 하는 파라미터(required parameters), 가질 수 있는 파라미터(all parameters)를 포함한 유용한 정보를 기술해주는 함수이다.

```python
statsapi.notes(endpoint)

#예시. attendance라는 endpoint에 대한 정보를 출력해보자. 
statsapi.notes('attendance')

Endpoint: attendance 
All path parameters: ['ver']. 
Required path parameters (note: ver will be included by default): ['ver']. 
All query parameters: ['teamId', 'leagueId', 'season', 'date', 'leagueListId', 'gameType', 'fields']. 
Required query parameters: [['teamId'], ['leagueId'], ['leagueListid']].

https://statsapi.mlb.com/api/v1/teams/143
```

### 1-18 `player_stats`

특정 선수의 시즌성적 혹은 커리어 전체 성적을 출력해주는 함수이다.  `personId`에 원하는 선수의 id를 입력해주고, 알고자 하는 `statGroup`과 `season`을 입력해준다.

```python
statsapi.player_stats(personId, group="[hitting,pitching,fielding]", type="season")

#예시. 마이크 트라웃의 통산 hitting stat을 출력해보자. 
#personId를 가져오기 위해 get함수로 sports_players 엔드포인트를 사용했다.
print( statsapi.player_stats(
	next(x['id'] for x in statsapi.get('sports_players',{'season':2011,'gameType':'W'})['people'] 
	if x['fullName']=='Mike Trout'), 
'hitting', 'career') )

Mike "Kiiiiid" Trout, CF (2011-)

Career Hitting
gamesPlayed: 1288
groundOuts: 884
airOuts: 1190
runs: 967
doubles: 268
triples: 49
homeRuns: 310
strikeOuts: 1215
baseOnBalls: 865
intentionalWalks: 109
hits: 1419
hitByPitch: 86
avg: .305
atBats: 4656
obp: .419
slg: .583
ops: 1.002
caughtStealing: 37
stolenBases: 203
stolenBasePercentage: .846
groundIntoDoublePlay: 58
numberOfPitches: 24099
plateAppearances: 5660
totalBases: 2715
rbi: 816
leftOnBase: 1599
sacBunts: 0
sacFlies: 52
babip: .348
groundOutsToAirouts: 0.74
catchersInterference: 1
atBatsPerHomeRun: 15.02
```

### 1-19 `player_stat_data`

`player_stats`의 출력값을 딕셔너리 형식으로 반환해준다.

❓ **문제.** 
```
보스턴레드삭스의 2021시즌 현역 선수들의 타율을 출력하라. 단, ‘fullName, 타율’ 형식으로 출력하라.
```

💡 **정답.**

```python
for n in statsapi.get('sports_players',{'season':2021, 'gameType':'R'})['people']:
  if n['currentTeam']['id'] == 111: #보스턴 레드삭스의 id가 111
    if statsapi.player_stat_data(n['id'],'hitting','career')['stats']: #hitting stat이 true여야 출력
      print(n['fullName'],statsapi.player_stat_data(n['id'],'hitting','career')['stats'][0]['stats']['avg'])

Jonathan Arauz .219
Christian Arroyo .235
Matt Barnes .000
Xander Bogaerts .290
Ryan Brasier .000
Brandon Brennan .000
Colten Brewer .000
Austin Brice .000
Franchy Cordero .221
...생략...
```

### 1-20 `roster`

특정 팀의 로스터를 출력해주는 함수이다. `date`는 mm/dd/yyyy 형식으로 입력해준다.

```python
statsapi.roster(teamId, rosterType=None, season=datetime.now().year, date=None)

#예시. 필라델피아의 올 시즌 로스터를 출력해보자.
print(statsapi.roster(143))

#27  P   Aaron Nola
#40  CF  Adam Haseley
#28  3B  Alec Bohm
#70  P   Bailey Falter
#3   RF  Bryce Harper
#75  P   Connor Brogdon
#    P   Corey Knebel
#61  P   Cristopher Sanchez
#68  P   Damon Jones
#18  SS  Didi Gregorius
#    C   Donny Sands
#69  P   Francisco Morales
#    C   Garrett Stubbs
#51  P   Hans Crouse
#10  C   J.T. Realmuto
#    P   James McArthur
#2   2B  Jean Segura
...생략...
```

### 1-21 `schedule`

주어진 기간동안 특정 팀의 경기 목록을 출력해주는 함수이다. 

```python
statsapi.schedule(date=None, start_date=None, end_date=None, team="", opponent="", sportId=1, game_id=None)

#예시. 7월 9일 필리스와 메츠의 경기를 출력해보자.
print(statsapi.schedule(date='07/09/2018',team=143,opponent=121))

{'game_id': 530769, #gamePk
'game_datetime': '2018-07-09T20:10:00Z', #경기 날짜와 시간
'game_date': '2018-07-09', #경기 날짜
'game_type': 'R', #경기 유형. R은 Regular season(정규시즌)을 의미
'status': 'Final', #경기 상태. Scheduled(예정), Warmup(경기 직전 몸푸는 때), In progress(진행중), Final(종료)를 의미.
'away_name': 'Philadelphia Phillies', #원정팀
'home_name': 'New York Mets', #홈팀
'away_id': 143, #원정팀 id
'home_id': 121, #홈팀 id
'doubleheader': 'Y', #더블헤더 여부. Y이므로 이 경기는 더블헤더.
'game_num': 1, #더블헤더의 1번째 경기라면 1, 2번째 경기라면 2. 더블헤더가 아니라면 1
'home_probable_pitcher': 'Zack Wheeler', #홈팀 선발투수
'away_probable_pitcher': 'Zach Eflin', #원정팀 선발
'home_pitcher_note': 'Another victim of a low-scoring offense, Wheeler is 0-4 over his last 11 starts, despite a 3.76 ERA and 67 strikeouts in those 66 innings. The Mets will push Wheeler back a day in the rotation, hoping he can provide length in a doubleheader.', 
#홈팀 투수 최근 경기 리포트
'away_pitcher_note': 'Following three consecutive starts of fewer than five innings to finish May, Eflin has been arguably the team’s best pitcher since. He is 6-0 with a 1.91 ERA in his past six starts, striking out 34 and walking six in 37 2/3 innings.', 
#원정팀 투수 최근 경기 리포트
'away_score': 3, #원정팀 점수. in progress 상태에서도 실시간 반영
'home_score': 4, #홈팀 점수. in progress 상태에서도 실시간 반영
'current_inning': 10, #현재 이닝. in progress 상태에서 유용.
'inning_state': 'Bottom', #초(Top)인지 말(Bottom)인지
'venue_id': 3289, #구장 id
'venue_name': 'Citi Field', #구장 이름
'winning_team': 'New York Mets', #승리팀
'losing_team': 'Philadelphia Phillies', #패배팀
'winning_pitcher': 'Tim Peterson', #승리투수
'losing_pitcher': 'Victor Arano', #패전투수
'save_pitcher': None, #세이브투수
'summary': '2018-07-09 - Philadelphia Phillies (3) @ New York Mets (4) (Final)'} #경기 한줄 요약. @가 붙은 게 홈팀.
```

❓ **문제**.
```
4월~7월 중 열린 파드리스와 메츠의 경기 결과 요약을 출력하라. 이 때 승리,패전,세이브 투수도 함께 출력하라.
```
💡 **정답**.

```python
for n in statsapi.schedule(start_date='04/01/2021', end_date='06/30/2021', team=138, opponent=121):
  print(n['summary'])

2021-06-03 - New York Mets (3) @ San Diego Padres (4) (Final) win: Yu Darvish / lose: Taijuan Walker / save: Mark Melancon
2021-06-04 - New York Mets (0) @ San Diego Padres (2) (Final) win: Blake Snell / lose: Joey Lucchesi / save: Mark Melancon
2021-06-05 - New York Mets (4) @ San Diego Padres (0) (Final) win: Jacob deGrom / lose: Joe Musgrove / save: None
2021-06-06 - New York Mets (6) @ San Diego Padres (2) (Final) win: Marcus Stroman / lose: Chris Paddack / save: None
2021-06-11 - San Diego Padres (2) @ New York Mets (3) (Final) win: Jacob deGrom / lose: Blake Snell / save: Edwin Diaz
2021-06-12 - San Diego Padres (1) @ New York Mets (4) (Final) win: Marcus Stroman / lose: Joe Musgrove / save: Edwin Diaz
2021-06-13 - San Diego Padres (7) @ New York Mets (3) (Final) win: Chris Paddack / lose: Jeurys Familia / save: None
```

### 1-22 `standings`

주어진 리그, 지구 순위표를 출력해주는 함수이다. `include_wildcard`의 기본값은 True이다

```python
statsapi.standings(leagueId="103,104", division="all", include_wildcard=True, season=None, standingsTypes=None, date=None)

#예시. 2021년 9월 27일의 내셔널리그 순위표를 출력하라.
print( statsapi.standings(leagueId='104', date='09/27/2021') )

National League East
Rank Team                   W   L   GB  (E#) WC Rank WC GB (E#)
 1   Atlanta Braves        83  72   -    -      -      -    -  
 2   Philadelphia Phillies 81  75  2.5   5      4     6.0   1  
 3   New York Mets         73  82  10.0  E      6    13.5   E  
 4   Washington Nationals  65  92  19.0  E      9    22.5   E  
 5   Miami Marlins         64  91  19.0  E     10    22.5   E  

National League Central
Rank Team                   W   L   GB  (E#) WC Rank WC GB (E#)
 1   Milwaukee Brewers     94  62   -    -      -      -    -  
 2   St. Louis Cardinals   87  69  7.0   E      2      -    -  
 3   Cincinnati Reds       82  75  12.5  E      3     5.5   1  
 4   Chicago Cubs          67  89  27.0  E      8    20.0   E  
 5   Pittsburgh Pirates    58  98  36.0  E     11    29.0   E  

National League West
Rank Team                   W   L   GB  (E#) WC Rank WC GB (E#)
 1   San Francisco Giants  102 54   -    -      -      -    -  
 2   Los Angeles Dodgers   100 56  2.0   5      1    +13.0  -  
 3   San Diego Padres      78  78  24.0  E      5     9.0   E  
 4   Colorado Rockies      71  85  31.0  E      7    16.0   E  
 5   Arizona Diamondbacks  50  106 52.0  E     12    37.0   E
```

### 1-23 `standing_data`

`standing` 함수의 출력값을 딕셔너리로 반환해주는 함수이다. 파라미터는 `standings` 함수와 동일하다.

### 1-24 `team_leaders`

특정 팀의 특정 스탯 순위를 출력해주는 함수이다. `leaderCategories`에 기준 스탯을 입력해주고, `limit`에 출력할 순위를, `season`에 알아볼 시즌을 입력해준다.

```python
statsapi.team_leaders(teamId, leaderCategories, season=datetime.now().year, leaderGameTypes="R", limit=10)

#예시. 필리스의 2021년 홀드 상위 7인을 출력하라.
print(statsapi.team_leaders(143, 'holds', limit=7, season=2021))

Rank Name                 Value
 1   Jose Alvarado         16  
 2   Archie Bradley        13  
 3   Connor Brogdon        11  
 3   Hector Neris          11  
 5   Sam Coonrod            8  
 6   JoJo Romero            3  
 7   Bailey Falter          2  
 7   Brandon Kintzler       2
```

### 1-25 team_leader_data

team_leaders 함수의 출력값을 리스트로 변환해주는 함수이다.

```python
#위에서 출력한 값을 team_leader_data로 출력해보자. 가독성을 높이기 위해 reshape해줬다.
print(np.array(statsapi.team_leader_data(143, 'holds', limit=7, season=2021)).reshape(8,3))

[['1' 'Jose Alvarado' '16']
 ['2' 'Archie Bradley' '13']
 ['3' 'Connor Brogdon' '11']
 ['3' 'Hector Neris' '11']
 ['5' 'Sam Coonrod' '8']
 ['6' 'JoJo Romero' '3']
 ['7' 'Bailey Falter' '2']
 ['7' 'Brandon Kintzler' '2']]
```

## 2. meta

### 2-1. `awards`

### 2-2. `baseballStats`

API에서 취급하는 모든 스탯들을 모아놓은 것이다. 아래 예시를 보자.

```python
{'highLowTypes': [],
  'isCounting': False, #셀 수 있는 스탯인가? false. ops는 비율스탯.
  'lookupParam': 'ops', #스탯의 파라미터이름
  'name': 'onBasePlusSlugging', #스탯의 정식 명칭
  'orgTypes': [],
  'statGroups': [{'displayName': 'hitting'}, {'displayName': 'pitching'}], #분류되는 그룹. hitting에선 ops, pitching에선 피ops.
  'streakLevels': []},

{'highLowTypes': [],
  'isCounting': True, #셀 수 있는 스탯인가? true. 승 수는 누적스탯.
  'lookupParam': 'w', #스탯의 파라미터이름
  'name': 'wins', #스탯의 정식 명칭
  'orgTypes': [],
  'statGroups': [{'displayName': 'pitching'}], #분류되는 그룹
  'streakLevels': []},
```

- `baseballStats`에 내장된 스탯 목록
    
    ```python
    # 각 스탯의 이름과 lookupParam만 추출하기 위한 반복문
    count=0
    for stat in statsapi.meta('baseballStats'):
      count+=1
      if 'lookupParam' in stat:
        print(count,'name:{} / lookupParam:{}'.format(stat['name'], stat['lookupParam']))
      else:
        print(count,'name:{}'.format(stat['name']))
    ```
    ```
    1 name: airOuts  /  lookupParam: ao
    2 name: assists  /  lookupParam: a
    3 name: atBats  /  lookupParam: ab
    4 name: atBatsPerHomeRun
    5 name: balk  /  lookupParam: bk
    6 name: battingAverage  /  lookupParam: avg
    7 name: babip  /  lookupParam: babip
    8 name: qualityStarts  /  lookupParam: qs
    9 name: bequeathedRunners  /  lookupParam: bq
    10 name: bequeathedRunnersScored  /  lookupParam: bqs
    11 name: blownSaves  /  lookupParam: bs
    12 name: catcherEarnedRunAverage  /  lookupParam: cera
    13 name: catchersInterference  /  lookupParam: ci
    14 name: caughtStealing  /  lookupParam: cs
    15 name: chances  /  lookupParam: tc
    16 name: completeGames  /  lookupParam: cg
    17 name: doublePlays  /  lookupParam: dp
    18 name: doubles  /  lookupParam: d
    19 name: earnedRun  /  lookupParam: er
    20 name: earnedRunAverage  /  lookupParam: era
    21 name: errors  /  lookupParam: e
    22 name: exitVelocity  /  lookupParam: exitVelo
    23 name: extraBaseHits  /  lookupParam: xbh
    24 name: fieldingPercentage  /  lookupParam: fpct
    25 name: flyouts  /  lookupParam: ao
    26 name: gamesFinished  /  lookupParam: gf
    27 name: gamesPlayed  /  lookupParam: g
    28 name: gamesStarted  /  lookupParam: gs
    29 name: groundIntoDoublePlays  /  lookupParam: gidp
    30 name: groundIntoDoublePlayOpportunities  /  lookupParam: gidp_opp
    31 name: groundIntoTriplePlays  /  lookupParam: gitp
    32 name: groundOuts  /  lookupParam: go
    33 name: groundoutToFlyoutRatio  /  lookupParam: go_ao
    34 name: hits  /  lookupParam: h
    35 name: hitsRisp  /  lookupParam: hits_risp
    36 name: hitBatsman  /  lookupParam: hb
    37 name: hitByPitches  /  lookupParam: hbp
    38 name: hitsPer9Inn  /  lookupParam: h_9
    39 name: holds  /  lookupParam: hld
    40 name: homeRuns  /  lookupParam: hr
    41 name: homeRunsPerPlateAppearance
    42 name: inheritedRunner  /  lookupParam: ir
    43 name: inheritedRunnerScored  /  lookupParam: irs
    44 name: innings  /  lookupParam: inn
    45 name: outsPitched  /  lookupParam: p_out
    46 name: inningsPitched  /  lookupParam: ip
    47 name: intentionalWalks  /  lookupParam: ibb
    48 name: iso
    49 name: leftOnBase  /  lookupParam: lob
    50 name: leftOnBaseRisp  /  lookupParam: lob_risp
    51 name: losses  /  lookupParam: l
    52 name: numberOfStrikes  /  lookupParam: s
    53 name: numberOfBalls  /  lookupParam: b
    54 name: numberOfPitches  /  lookupParam: np
    55 name: onBasePercentage  /  lookupParam: obp
    56 name: onBasePlusSlugging  /  lookupParam: ops
    57 name: outfieldAssists  /  lookupParam: ofa
    58 name: passedBalls  /  lookupParam: pb
    59 name: pickoffs  /  lookupParam: po
    60 name: pitchesPerInning  /  lookupParam: p_ip
    61 name: pitchesPerPlateAppearance
    62 name: putOuts  /  lookupParam: po
    63 name: rangeFactorPerGame  /  lookupParam: rf
    64 name: rangeFactorPer9Inn  /  lookupParam: rf_9
    65 name: reachedOnError  /  lookupParam: roe
    66 name: runs  /  lookupParam: r
    67 name: runsBattedIn  /  lookupParam: rbi
    68 name: sacrificeBunts  /  lookupParam: sac
    69 name: sacrificeFlies  /  lookupParam: sf
    70 name: saves  /  lookupParam: sv
    71 name: saveOpportunities  /  lookupParam: svo
    72 name: shutouts  /  lookupParam: sho
    73 name: sluggingPercentage  /  lookupParam: slg
    74 name: stolenBases  /  lookupParam: sb
    75 name: stolenBasePercentage  /  lookupParam: sbpct
    76 name: strikeouts  /  lookupParam: so
    77 name: strikeoutsPer9Inn  /  lookupParam: k_9
    78 name: strikeoutsPerPlateAppearance
    79 name: strikeoutWalkRatio  /  lookupParam: k_bb
    80 name: throwingErrors  /  lookupParam: throwing_e
    81 name: totalBases  /  lookupParam: tb
    82 name: totalBattersFaced  /  lookupParam: tbf
    83 name: totalPlateAppearances  /  lookupParam: tpa
    84 name: triplePlays  /  lookupParam: tp
    85 name: triples  /  lookupParam: t
    86 name: walksPerStrikeout
    87 name: walksPerPlateAppearance
    88 name: walksAndHitsPerInningPitched  /  lookupParam: whip
    89 name: walks  /  lookupParam: bb
    90 name: walksPer9Inn  /  lookupParam: bb_9
    91 name: walkoffs  /  lookupParam: wo
    92 name: wildPitch  /  lookupParam: wp
    93 name: wins  /  lookupParam: w
    94 name: winPercentage  /  lookupParam: wpct
    95 name: attendance  /  lookupParam: attendance
    96 name: duration  /  lookupParam: duration
    97 name: winStreak  /  lookupParam: win_streak
    98 name: lossStreak  /  lookupParam: loss_streak
    99 name: woba
    100 name: xWoba
    101 name: xWobacon
    102 name: xAvg
    103 name: xSlg
    104 name: launchAngle  /  lookupParam: launchAngle
    105 name: homeRunDistance  /  lookupParam: homeRunDistance
    106 name: hitDistance  /  lookupParam: hitDistance
    107 name: hangTime  /  lookupParam: hangTime
    108 name: maxHeight  /  lookupParam: maxHeight
    109 name: hitProbability  /  lookupParam: hitProbability
    110 name: catchProbability  /  lookupParam: catchProbability
    111 name: barrels  /  lookupParam: barrels
    112 name: releaseSpeed  /  lookupParam: releaseSpeed
    113 name: releaseSpinRate  /  lookupParam: releaseSpinRate
    114 name: releaseExtension  /  lookupParam: releaseExtension
    115 name: horizontalBreak  /  lookupParam: horizontalBreak
    116 name: armStrength  /  lookupParam: armStrength
    117 name: distanceCovered  /  lookupParam: distanceCovered
    118 name: exchange  /  lookupParam: exchange
    119 name: fielderBurstDistance  /  lookupParam: fielderBurstDistance
    120 name: fielderJumpDistance  /  lookupParam: fielderJumpDistance
    121 name: fielderReactionDistance  /  lookupParam: fielderReactionDistance
    122 name: firstStep  /  lookupParam: firstStep
    123 name: firstStepEfficiency  /  lookupParam: firstStepEfficiency
    124 name: popTime1b  /  lookupParam: popTime1b
    125 name: popTime2b  /  lookupParam: popTime2b
    126 name: popTime3b  /  lookupParam: popTime3b
    127 name: routeEfficiency  /  lookupParam: routeEfficiency
    128 name: sprintSpeed  /  lookupParam: sprintSpeed
    129 name: throwingAccuracy  /  lookupParam: throwingAccuracy
    130 name: throwDistance  /  lookupParam: throwDistance
    131 name: throwDistanceWithBounces  /  lookupParam: throwDistanceWithBounces
    132 name: acceleration  /  lookupParam: acceleration
    133 name: burst  /  lookupParam: burst
    134 name: firstToHome  /  lookupParam: firstToHome
    135 name: firstToSecond  /  lookupParam: firstToSecond
    136 name: firstToThird  /  lookupParam: firstToThird
    137 name: homeToHome  /  lookupParam: homeToHome
    138 name: homeToFirst  /  lookupParam: homeToFirst
    139 name: homeToSecond  /  lookupParam: homeToSecond
    140 name: homeToThird  /  lookupParam: homeToThird
    141 name: primaryLead  /  lookupParam: primaryLead
    142 name: outOfBox  /  lookupParam: outOfBox
    143 name: secondToHome  /  lookupParam: secondToHome
    144 name: secondToThird  /  lookupParam: secondToThird
    145 name: secondaryLead  /  lookupParam: secondaryLead
    146 name: firstToSecondSteal  /  lookupParam: stealFirstToSecondSteal
    147 name: secondToThirdSteal  /  lookupParam: secondToThirdSteal
    148 name: thirdToHomeSteal  /  lookupParam: thirdToHomeSteal
    149 name: tagFirstStep  /  lookupParam: tagFirstStep
    150 name: firstToSecondTag  /  lookupParam: firstToSecondTag
    151 name: secondToThirdTag  /  lookupParam: secondToThirdTag
    152 name: thirdToHomeTag  /  lookupParam: thirdToHomeTag
    153 name: thirdToHome  /  lookupParam: thirdToHome
    154 name: outsAboveAverage
    155 name: fieldingRunsPrevented
    156 name: streak  /  lookupParam: streak
    157 name: war
    158 name: gameDate
    159 name: verticalBreak  /  lookupParam: verticalBreak
    ```
    
    ```python
    # 원하는 스탯명을 입력하면 그 스탯의 상세 정보를 출력해주는 함수
    def search_stat(a):
      index=-1
      for stat in statsapi.meta('baseballStats'):
        index+=1
        if stat['name'] == a:
          print(statsapi.meta('baseballStats')[index])
    ```
    

### 2-3. `eventTypes`

경기에서 발생하는 모든 결과 유형을 총망라한 것. 아래 예시를 보자.

```python
{'baseRunningEvent': True, #주자가 베이스를 뛰는 사건인가? true.
  'code': 'stolen_base_3b', #3루 도루
  'description': 'Stolen Base 3B',
  'hit': False, #안타를 쳤는가? false.
  'plateAppearance': False} #한 타석으로 카운트 되는가? false.

{'baseRunningEvent': False, #주자가 베이스를 뛰는 사건인가? false.
  'code': 'triple', #3루타
  'description': 'Triple',
  'hit': True, #안타를 쳤는가? true.
  'plateAppearance': True} #한 타석으로 카운트 되는가? true.

{'baseRunningEvent': False, #주자가 베이스를 뛰는 사건인가? false.
  'code': 'hit_by_pitch', #몸에 맞는 볼
  'description': 'Hit By Pitch',
  'hit': False, #안타를 쳤는가? false.
  'plateAppearance': True}, #한 타석으로 카운트 되는가? true.

```

- `eventTypes` 유형

```
    1 pickoff_1b
    2 pickoff_2b
    3 pickoff_3b
    4 pickoff_error_1b
    5 pickoff_error_2b
    6 pickoff_error_3b
    7 no_pitch
    8 single
    9 double
    10 triple
    11 home_run
    12 double_play
    13 field_error
    14 error
    15 field_out
    16 fielders_choice
    17 fielders_choice_out
    18 force_out
    19 grounded_into_double_play
    20 grounded_into_triple_play
    21 strikeout
    22 strike_out
    23 strikeout_double_play
    24 strikeout_triple_play
    25 triple_play
    26 sac_fly
    27 catcher_interf
    28 batter_interference
    29 fielder_interference
    30 runner_interference
    31 fan_interference
    32 batter_turn
    33 ejection
    34 cs_double_play
    35 defensive_indiff
    36 sac_fly_double_play
    37 sac_bunt
    38 sac_bunt_double_play
    39 walk
    40 intent_walk
    41 hit_by_pitch
    42 injury
    43 os_ruling_pending_prior
    44 os_ruling_pending_primary
    45 at_bat_start
    46 passed_ball
    47 other_advance
    48 runner_double_play
    49 runner_placed
    50 pitching_substitution
    51 offensive_substitution
    52 defensive_switch
    53 umpire_substitution
    54 pitcher_switch
    55 game_advisory
    56 stolen_base
    57 stolen_base_2b
    58 stolen_base_3b
    59 stolen_base_home
    60 caught_stealing
    61 caught_stealing_2b
    62 caught_stealing_3b
    63 caught_stealing_home
    64 defensive_substitution
    65 pickoff_caught_stealing_2b
    66 pickoff_caught_stealing_3b
    67 pickoff_caught_stealing_home
    68 balk
    69 wild_pitch
    70 other_out
```
    

### 2-4. `gameStatus`

경기에서 발생되는 예외적인 상황(항의, 중단, 지연, 판정 리뷰)들을 설명해준다. 아래 예시를 보자.

```python
{'abstractGameCode': 'L', 
  'abstractGameState': 'Live', #경기 진행 중
  'codedGameState': 'M',
  'detailedState': 'Manager challenge: Tag-up play', #태그업 플레이에 대한 감독의 항의
  'reason': 'Tag-up play',
  'statusCode': 'MU'},

{'abstractGameCode': 'L',
  'abstractGameState': 'Live', #경기 진행 중
  'codedGameState': 'N',
  'detailedState': 'Umpire review: Catch/drop in outfield', #외야에서 공을 놓쳤는지 여부에 대한 심판의 리뷰
  'reason': 'Catch/drop in outfield',
  'statusCode': 'ND'},

{'abstractGameCode': 'P',
  'abstractGameState': 'Preview', #경기 시작 전
  'codedGameState': 'P',
  'detailedState': 'Delayed Start: Rain', #경기 시작이 지연되고 있고, 사유는 비
  'reason': 'Rain',
  'statusCode': 'PR'},

{'abstractGameCode': 'F',
  'abstractGameState': 'Final', #경기 끝
  'codedGameState': 'C',
  'detailedState': 'Cancelled: Fog', #경기가 취소되었고, 사유는 안개
  'reason': 'Fog',
  'statusCode': 'CF'},
```

### 2-5. `gameTypes`

경기의 유형이 정규시즌인지, 스프링캠프인지, 와일드카드전인지, 월드시리즈인지 등을 알려준다.

- `gameTypes`에 내장된 경기 유형 목록
    
    `['S' 'Spring Training']
    ['R' 'Regular Season']
    ['F' 'Wild Card Game']
    ['D' 'Division Series']
    ['L' 'League Championship Series']
    ['W' 'World Series']
    ['C' 'Championship']
    ['N' 'Nineteenth Century Series']
    ['P' 'Playoffs']
    ['A' 'All-Star Game']
    ['I' 'Intrasquad']
    ['E' 'Exhibition']`
    

### 2-6. `hitTrajectories`

타구의 유형이다.

- `hitTrajectories` 목록
```
    
    [{'code': 'bunt_grounder', 'description': 'Bunt - Ground Ball'},
    {'code': 'bunt_line_drive', 'description': 'Bunt - Line Drive'},
    {'code': 'fly_ball', 'description': 'Fly Ball'},
    {'code': 'ground_ball', 'description': 'Ground Ball'},
    {'code': 'line_drive', 'description': 'Line Drive'},
    {'code': 'bunt_popup', 'description': 'Bunt - Popup'},
    {'code': 'popup', 'description': 'Popup'}]
```

### 2-7. `jobTypes`

야구와 관련된 직업(선수, 심판, 코치, 분석원 등)을 총망라한 목록이다.

- `jobTypes`
```
    Umpire
    Director of Instant Replay
    Replay Official
    Stringer
    BOSS Operator
    Field Timing Coordinator
    Video Room Monitor
    Tracking Operator
    Scrubber Operator
    Pitchcast Operator
    Official Scorer
    Supervisor
    Manager
    Bench Coach
    Interim Manager
    Associate Manager
    Hitting Coach
    Batting Coach
  .
  .
  .
    Team Operations Manager
```
    

### 2-8. `languages`

### 2-9. `leagueLeaderTypes`

스탯 순위표의 기준이 되는 스탯들을 내장하고 있다. 

- `leagueLeaderTypes` 목록
```    
    ['assists']
    ['shutouts']
    ['homeRuns']
    ['sacrificeBunts']
    ['sacrificeFlies']
    ['runs']
    ['groundoutToFlyoutRatio']
    ['stolenBases']
    ['battingAverage']
    ['groundOuts']
    ['numberOfPitches']
    ['onBasePercentage']
    ['caughtStealing']
    ['groundIntoDoublePlays']
    ['totalBases']
    ['earnedRunAverage']
    ['fieldingPercentage']
    ['walksAndHitsPerInningPitched']
    ['flyouts']
    ['hitByPitches']
    ['gamesPlayed']
    ['walks']
    ['sluggingPercentage']
    ['onBasePlusSlugging']
    ['runsBattedIn']
    ['triples']
    ['extraBaseHits']
    ['hits']
    ['atBats']
    ['strikeouts']
    ['doubles']
    ['totalPlateAppearances']
    ['intentionalWalks']
    ['wins']
    ['losses']
    ['saves']
    ['wildPitch']
    ['airOuts']
    ['balk']
    ['blownSaves']
    ['catcherEarnedRunAverage']
    ['catchersInterference']
    ['chances']
    ['completeGames']
    ['doublePlays']
    ['earnedRun']
    ['errors']
    ['gamesFinished']
    ['gamesStarted']
    ['hitBatsman']
    ['hitsPer9Inn']
    ['holds']
    ['innings']
    ['inningsPitched']
    ['outfieldAssists']
    ['passedBalls']
    ['pickoffs']
    ['pitchesPerInning']
    ['putOuts']
    ['rangeFactorPerGame']
    ['rangeFactorPer9Inn']
    ['saveOpportunities']
    ['stolenBasePercentage']
    ['strikeoutsPer9Inn']
    ['strikeoutWalkRatio']
    ['throwingErrors']
    ['totalBattersFaced']
    ['triplePlays']
    ['walksPer9Inn']
    ['winPercentage']]`
```

### 2-10. `logicalEvents`

경기에서 발생하는 상황들 중 다음 상황으로 연계가되는 논리 상황들을 모아놓은 목록이다.

- `logicalEvents` 목록
```
    {'code': 'sceneStateUpdate'},
    {'code': 'newBatter'},
    {'code': 'newLeftHandedBatter'},
    {'code': 'newLeftHandedBatterWithPitches'},
    {'code': 'newRightHandedBatter'},
    {'code': 'newRightHandedBatterWithPitches'},
    {'code': 'newRightHandedHit'},
    {'code': 'newLeftHandedHit'},
    {'code': 'batterSwitchedToLeftHanded'},
    {'code': 'batterSwitchedToRightHanded'},
    {'code': 'countChange'},
    {'code': 'count42'},
    {'code': 'count41'},
    {'code': 'count40'},
    {'code': 'count33'},
    {'code': 'count32'},
    {'code': 'count31'},
    {'code': 'count30'},
    {'code': 'count23'},
    {'code': 'count22'},
    {'code': 'count21'},
    {'code': 'count20'},
    {'code': 'count13'},
    {'code': 'count12'},
    {'code': 'count11'},
    {'code': 'count10'},
    {'code': 'count03'},
    {'code': 'count02'},
    {'code': 'count01'},
    {'code': 'count00'},
    {'code': 'basesEmpty'},
    {'code': 'runnerOnFirst'},
    {'code': 'runnerOnSecond'},
    {'code': 'runnerOnThird'},
    {'code': 'runnersOnFirstAndSecond'},
    {'code': 'runnersOnFirstAndThird'},
    {'code': 'runnersOnSecondAndThird'},
    {'code': 'basesLoaded'},
    {'code': 'runnersInScoringPosition'},
    {'code': 'gameStateChangeToInProgress'},
    {'code': 'gameStateChangeToWarmup'},
    {'code': 'gameStateChangeToPreview'},
    {'code': 'gameStateChangeToPreGame'},
    {'code': 'gameStateChangeToLineups'},
    {'code': 'gameStateChangeToDelayed'},
    {'code': 'gameStateChangeToDelayedStart'},
    {'code': 'gameStateChangeToFinal'},
    {'code': 'gameStateChangeToGameOver'},
    {'code': 'gameStateChangeToCompletedEarly'},
    {'code': 'gameStateChangeToSuspended'},
    {'code': 'gameStateChangeToCancelled'},
    {'code': 'gameStateChangeToPostponed'},
    {'code': 'gameStateChangeToForfeit'},
    {'code': 'gameStateChangeToInstantReplay'},
    {'code': 'gameStateChangeToExtraInnings'},
    {'code': 'abstractGameStateChangeToPregame'},
    {'code': 'abstractGameStateChangeToLive'},
    {'code': 'abstractGameStateChangeToDelayed'},
    {'code': 'abstractGameStateChangeToFinal'},
    {'code': 'abstractGameStateChangeToOther'},
    {'code': 'UIGameStateChangeToPregame'},
    {'code': 'UIGameStateChangeToLive'},
    {'code': 'UIGameStateChangeToFinal'},
    {'code': 'defensiveSubstitution'},
    {'code': 'offensiveSubstitution'},
    {'code': 'pitcherChange'},
    {'code': 'pitcherChangeComplete'},
    {'code': 'coachToMound'},
    {'code': 'midInning'},
    {'code': 'newHalfInning'},
    {'code': 'newVideoHighlights'},
    {'code': 'beginCommercialBreak'},
    {'code': 'endCommercialBreak'}
```  

### 2-11. `metrics`

야구에서 측정되는 다양한 물리적 수치들의 목록. 아래 예시를 보자.

```python
{'group': 'hitting, pitching', #스탯이 속하는 그룹
  'metricId': 1005,
  'name': 'launchAngle', #발사각
  'unit': 'DEG'}, #단위는 degree(각도)

{'group': 'pitching', #스탯이 속하는 그룹
  'metricId': 1161,
  'name': 'deliveryTime', #투구 속도
  'unit': 'SEC'}, #단위는 초

{'group': 'pitching', #스탯이 속하는 그룹
  'metricId': 1002,
  'name': 'releaseSpeed', #투구 구속
  'unit': 'MPH'}, #단위는 시속
```

- `metrics` 목록

``` 
    releaseSpinRate
    releaseExtension
    releaseSpeed
    effectiveSpeed
    launchSpeed
    launchAngle
    generatedSpeed
    maxHeight
    travelTime
    hangTime
    opportunityTimeGround
    distance
    travelDistance
    hrDistance
    hitTrajectory
    launchSpinRate
    barreledBall
    deliveryTime
    limbApexSkeletal
    distanceToCatchersMittSkeletal
```
    

### 2-12. `pitchTypes`

투수의 구종 목록이다.

- `pitchTypes`에 내장된 구종 목록
```    
    {'code': 'EP', 'description': 'Eephus Pitch'},
    {'code': 'PO', 'description': 'Pitchout'},
    {'code': 'AB', 'description': 'Automatic Ball'},
    {'code': 'AS', 'description': 'Automatic Strike'},
    {'code': 'CH', 'description': 'Changeup'},
    {'code': 'CU', 'description': 'Curveball'},
    {'code': 'FA', 'description': 'Fastball'},
    {'code': 'FT', 'description': 'Two-seam FB'},
    {'code': 'FF', 'description': 'Four-seam FB'},
    {'code': 'FC', 'description': 'Cutter'},
    {'code': 'FS', 'description': 'Splitter'},
    {'code': 'FO', 'description': 'Forkball'},
    {'code': 'GY', 'description': 'Gyroball'},
    {'code': 'IN', 'description': 'Intentional Ball'},
    {'code': 'KC', 'description': 'Knuckle Curve'},
    {'code': 'KN', 'description': 'Knuckleball'},
    {'code': 'NP', 'description': 'No Pitch'},
    {'code': 'SC', 'description': 'Screwball'},
    {'code': 'SI', 'description': 'Sinker'},
    {'code': 'SL', 'description': 'Slider'},
    {'code': 'UN', 'description': 'Unknown'},
    {'code': 'ST', 'description': 'Slutter'},
    {'code': 'SV', 'description': 'Slurve'},
    {'code': 'CS', 'description': 'Slow Curve'}]
```
    

### 2-13 `pitchCodes`

투수가 던지는 모든 공은 각각의 결과가 있다. 단순히 스트라이크, 볼, 안타, 범타만의 결과로 나뉘는 것이 아니다. 더 세부적으로, 이를테면 스트라이크가 헛스윙 스트라이크, 파울 스트라이크, 번트 헛스윙 스트라이크 등으로 나뉜다.

- `pitchCodes`에 내장된 투구결과 유형 목록

```    
    {'code': 'R', 'description': 'Strike - Foul on Pitchout'} : 피치아웃한 공을 타격하여 파울(스트라이크)
    {'code': 'Y', 'description': 'Pitchout Hit Into Play - Out(s)'} : 피치아웃을 타격하여 아웃
    {'code': 'M', 'description': 'Strike - Missed Bunt'} : 번트 헛스윙으로 스트라이크
    {'code': 'X', 'description': 'Hit Into Play - Out(s)'} : 타격하여 아웃
    {'code': 'O', 'description': 'Strike - Bunt Foul Tip'} : 번트 파울팁(배트에 스친 공이 포수 미트로)으로 스트라이크
    {'code': 'E', 'description': 'Hit Into Play - Run(s)'} : 타격하여 득점으로 연결
    {'code': 'D', 'description': 'Hit Into Play - No Out(s)'} : 타격하여 아웃당하지 않음
    {'code': 'Q', 'description': 'Strike - Swinging on Pitchout'} : 피치아웃한 공을 헛스윙하여 스트라이크
    {'code': 'Z', 'description': 'Pitchout Hit Into Play - Run(s)'} : 피치아웃한 공을 타격하여 득점으로 연결
    {'code': 'F', 'description': 'Strike - Foul'} : 파울(스트라이크)
    {'code': 'W', 'description': 'Strike - Swinging Blocked'} : 바운드되어 포수가 블로킹한 공을 헛스윙 스트라이크
    {'code': 'T', 'description': 'Strike - Foul Tip'} : 파울팁(배트에 스친 공이 포수 미트로) 스트라이크
    {'code': 'L', 'description': 'Strike - Foul Bunt'} : 번트한 공이 파울(스트라이크)
    {'code': 'C', 'description': 'Strike - Called'} : 헛스윙이 아닌 심판 콜로 주어진 스트라이크
    {'code': 'K', 'description': 'Strike - Unknown'} : ?
    {'code': 'J', 'description': 'Pitchout Hit Into Play - No Out(s)'} : 피치아웃한 공을 타격하여 아웃당하지 않음
    {'code': 'S', 'description': 'Strike - Swinging'} : 헛스윙 스트라이크
    {'code': 'B', 'description': 'Ball - Called'} : 심판 콜로 주어진 볼
    {'code': 'P', 'description': 'Ball - Pitchout'} : 피치아웃으로 주어진 볼
    {'code': 'H', 'description': 'Ball - Hit by Pitch'} : 몸에맞는 볼
    {'code': '*B', 'description': 'Ball - Ball In Dirt'} : 바운드 된 볼
    {'code': '3', 'description': 'Pickoff Throw 3rd - Pitcher'} : 투수의 3루 견제
    {'code': '1', 'description': 'Pickoff Throw 1st - Pitcher'} : 투수의 1루 견제
    {'code': '+3', 'description': 'Pickoff Throw 3rd - Catcher'} : 포수의 3루 견제
    {'code': '2', 'description': 'Pickoff Throw 2nd - Pitcher'} : 투수의 2루 견제
    {'code': '+2', 'description': 'Pickoff Throw 2nd - Catcher'} : 포수의 2루 견제
    {'code': '+1', 'description': 'Pickoff Throw 1st - Catcher'} : 포수의 1루 견제
    {'code': 'A', 'description': 'Strike - Automatic'} : ?
    {'code': '.', 'description': 'Non Pitch'},
    {'code': 'N', 'description': 'No Pitch'} : 투수가 던진 공이 볼도, 스트라이크도 아닌 경우. 보통 주심의 타임아웃 이후 던진 공에 대해 무효처리 되는 것을 말한다. 그 밖의 예외적인 사유로 무효처리 되는 경우.
    {'code': 'I', 'description': 'Ball - Intentional'} : 고의로 투구한 볼
    {'code': 'V', 'description': 'Ball - Automatic'} : ?
```
    

### 2-14. `platforms`

- `platforms` 목록
```
    Web
    Android Phone
    Android Tablet
    iOS Phone
    iOS Tablet
    Xbox One
    Xbox 360
    Roku
    PlayStation
    Chromecast
    Apple TV
    tvOS
```
    

### 2-15. `positions`

포지션들의 목록이다. 비단 10개의 포지션만이 아니라, 더 세분화하여 여러 포지션을 내장하고 있다. 아래 예시를 보자

```python
{'abbrev': '1B', #준말
  'code': '3', #포지션 넘버
  'displayName': 'First Base', #1루수
  'fielder': True, #야수 여부. pitcher는 False
  'formalName': 'First Baseman',
  'fullName': 'First Base',
  'gamePosition': True, #경기에서 불리는 포지션인지 여부
  'outfield': False, #외야수 여부
  'pitcher': False, #투수 여부
  'shortName': '1st Base',
  'type': 'Infielder'}, #포지션 유형. 내야수

{'abbrev': 'PR', #준말
  'code': '12', #포지션 넘버
  'displayName': 'Pinch Runner', #대주자
  'fielder': False, #야수 여부.
  'formalName': 'Pinch Runner',
  'fullName': 'Pinch Runner',
  'gamePosition': True, #경기에서 쓰이는 포지션인지 여부
  'outfield': False, #외야수 여부
  'pitcher': False, #투수 여부
  'shortName': 'Pinch Runner',
  'type': 'Runner'}, #포지션 유형. 주자

{'abbrev': 'CP',#준말
  'code': 'C', #포지션 코드
  'displayName': 'Closer', #마무리 투수
  'fielder': False, #야수 여부
  'formalName': 'Closer',
  'fullName': 'Closer',
  'gamePosition': False, #경기에서 쓰이는 포지션인지 여부. 경기에선 그냥 pitcher
  'outfield': False, #외야수 여부
  'pitcher': True, #투수 여부
  'shortName': 'Closer',
  'type': 'Pitcher'}, #포지션 유형. 투수
```

- `positions` 목록
``` 
    1 Pitcher
    2 Catcher
    3 First Baseman
    4 Second Baseman
    5 Third Baseman
    6 Shortstop
    7 Left Fielder
    8 Center Fielder
    9 Right Fielder
    10 Designated Hitter
    11 Pinch Hitter
    12 Pinch Runner
    13 Extra Hitter
    14 Base Runner
    15 Outfield
    16 Infield
    17 Starting Pitcher
    18 Relief Pitcher
    19 Closer
    20 Utility
    21 Utility Infielder
    22 Utility Outfielder
    23 Right-Handed Pitcher
    24 Left-Handed Pitcher
    25 Right-Handed Starter
    26 Left-Handed Starter
    27 Left-Handed Reliever
    28 Right-Handed Reliever
    29 Pitcher - Infielder
    30 Pitcher - Outfielder
    31 Pitcher - Utility
    32 Two-Way Player
    33 Batter
    34 Unknown
    35 Runner on First
    36 Runner on Second
    37 Runner on Third
```
    

### 2-16. `reviewReasons`

심판의 review(비디오판독?)이 이루어질 때 그 사유들을 모아놓은 목록.

- `reviewReasons` 목록
```
    Close play at 1st
    Timing Play
    Force play
    Home-plate collision
    Slide interference
    Home run
    Fair/foul in outfield
    Catch/drop in outfield
    Trap play in outfield
    Hit by pitch
    Touching a base
    Passing runners
    Fan interference
    Stadium boundary call
    Grounds rule
    Rules check
    Record keeping
    Multiple issues
    Other
    Tag-up play
    Tag play
    Pitch result
    Catcher interference
```
    

### 2-17. `rosterTypes`

야구의 로스터에는 여러 방식이 있다. 팀의 40인 로스터도 있고, 한 경기의 로스터도 있고, 코치진 로스터도 있다. 그 로스터 유형들을 모아놓은 목록이다.

- `rosterTypes` 목록
```
    40 man roster for a team
    Full roster including active and inactive players for a season
    Full roster including active and inactive players
    Non-Roster Invitees
    Active roster for a team
    All Time roster for a team
    Depth chart for a team
    Roster for day of game
    Coach roster for a team
```
    

### 2-18. `scheduleEventTypes`

야구 경기와 관련된 각종 행사들의 유형 목록이다.

- `scheduleEventTypes`
```    
    All-Star Weekend Event
    Team Event
    Exhibition
    Postseason Games
    Spring Training Games
    Pitchers & Catchers Report
    Full Squad Reports
    STH Events
    Ballpark Tours
    Important Dates
    Other
    Cultural Events
    Tracking Data Events
    Festival
    Kids & Family
    Music
    Promotion Logo - Background Image
    Promotion Logo - Single Date Image
    Studio Event
```

### 2-19. `situationCodes`

야구의 크고작고 중요하고 잡다한 모든 상황들을 모아놓은 목록.

```python
{'batting': True,
  'code': 'd', 
  'description': 'Day Games', #낮경기
  'fielding': True,
  'navigationMenu': 'Game', #그룹. game
  'pitching': True,
  'sortOrder': 3, #상황 순번
  'team': True},
```

- `situationCodes` 목록
```    
    Home Games
    Away Games
    Day Games
    Night Games
    On Grass
    On Turf
    February
    March
    April
    May
    June
    July
    August
    September
    October
    November
    December
    January
    Season To Date
   .
   .
   .
    vs Right Zone 14
```


### 2-20. `sky`

경기의 날씨 유형 목록이다.

- `sky` 목록
```
    Rain
    Roof Closed
    Overcast
    Snow
    Cloudy
    Dome
    Clear
    Sunny
    Partly Cloudy
    Drizzle
```
    

### 2-21. `standingsTypes`

순위표의 기준들을 모아놓은 유형. 전반기 순위표와 후반기 순위표가 다르듯, 기준이 뭐냐에 따라 순위표는 다르기 마련이다.

- `standingsTypes` 목록
```    
    Regular Season Standings
    Wild card standings
    Division Leader standings
    Wild card standings with Division Leaders
    First half standings.  Only valid for leagues with a split season.
    Second half standings. Only valid for leagues with a split season.
    Spring Training Standings
    Postseason Standings
    Standings by Division
    Standings by Conference
    Standings by League
    Standing by Organization
```
    

### 2-22. `statGroups`

각 스탯이 속하는 그룹을 말한다. 예를 들어 `assist`(보살)은 `fileding`과 `catching` 그룹에 속하고, `qualityStarts`는 `pitching` 그룹에 속한다.

- `statGroups` 목록
    
    `['hitting']
    ['pitching']
    ['fielding']
    ['catching']
    ['running']
    ['game']
    ['team']
    ['streak']`
    

### 2-23. `statTypes`

- `statTypes`에 내장된 목록
    
    `['projected']
    ['projectedRos']
    ['yearByYear']
    ['yearByYearAdvanced']
    ['yearByYearPlayoffs']
    ['season']
    ['standard']
    ['advanced']
    ['career']
    ['careerRegularSeason']
    ['careerAdvanced']
    ['seasonAdvanced']
    ['careerStatSplits']
    ['careerPlayoffs']
    ['gameLog']
    ['playLog']
    ['pitchLog']
    ['metricLog']
    ['metricAverages']
    ['pitchArsenal']
    ['outsAboveAverage']
    ['expectedStatistics']
    ['sabermetrics']
    ['sprayChart']
    ['tracking']
    ['vsPlayer']
    ['vsPlayerTotal']
    ['vsPlayer5Y']
    ['vsTeam']
    ['vsTeam5Y']
    ['vsTeamTotal']
    ['lastXGames']
    ['byDateRange']
    ['byDateRangeAdvanced']
    ['byMonth']
    ['byMonthPlayoffs']
    ['byDayOfWeek']
    ['byDayOfWeekPlayoffs']
    ['homeAndAway']
    ['homeAndAwayPlayoffs']
    ['winLoss']
    ['winLossPlayoffs']
    ['rankings']
    ['rankingsByYear']
    ['statsSingleSeason']
    ['statsSingleSeasonAdvanced']
    ['hotColdZones']
    ['availableStats']
    ['opponentsFaced']
    ['gameTypeStats']
    ['firstYearStats']
    ['lastYearStats']
    ['statSplits']
    ['statSplitsAdvanced']
    ['atGameStart']
    ['vsOpponents']`
    

### 2-24. `windDirection`

바람의 방향 유형 목록이다.

- `windDirection` 목록
    
    Calm
    None
    Varies
    In From RF
    In From LF
    In From CF
    R To L
    L To R
    Out To CF
    Out To RF
    Out To LF
