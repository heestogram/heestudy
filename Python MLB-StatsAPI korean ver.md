# Python MLB-StatsAPI


๐ก 
```
ํ์ด์ฌ ํ๊ฒฝ์์ ์ฌ์ฉํ  ์ ์๋ MLB ๋ฐ์ดํฐ API์๋๋ค. 
์ ์ฉํ API์์๋ ๋ถ๊ตฌํ๊ณ , ์ฐ๋ฆฌ๋ง๋ก ๋ฒ์ญ๋ ๋ง๋ํ ์นํ์ด์ง๊ฐ ์์ด์ 
์ง์  ๋ฒ์ญํ์ฌ ํด๋น API๋ฅผ ์๊ฐํ๋ ํ์ด์ง๋ฅผ ๋ง๋ค์์ต๋๋ค.
```

[Home ยท toddrob99/MLB-StatsAPI Wiki](https://github.com/toddrob99/MLB-StatsAPI/wiki)


`pip`๋ ํ์ด์ฌ ํจํค์ง๋ฅผ ์ค์นํ๊ฑฐ๋ ๊ด๋ฆฌํ๋ ์์คํ์ด๋ค. MLB-StatsAPI ํจํค์ง๋ฅผ ์ค์นํด๋ณด์.

```python
#์ค์นํ๋ ค๋ ํจํค์ง ์ด๋ฆ์ ๋ฃ๊ณ  ์ค์น.
pip install MLB-StatsAPI

#ํจํค์ง ์๊ทธ๋ ์ด๋
pip install --upgrade MLB-StatsAPI

#ํจํค์ง์ ๋ํ ์ธ๋ถ ์ฌํญ์ ํ์ธํ  ์ ์๋ค.
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

#ํจํค์ง๋ฅผ importํ๋ค.
import statsapi
```

## 1. Function

### 1-1. `boxscore`

ํน์  ๊ฒ์์ ๋ฐ์ค์ค์ฝ์ด๋ฅผ ๊ฐ์ ธ์ค๋ ํจ์. ํ๋ผ๋ฏธํฐ๋ค์ ๊ธฐ๋ณธ๊ฐ์ ๋ชจ๋ True์ด๋ค.  

`gamePk` ๊ฐ์ ๋ฃ์ผ๋ฉด ํด๋น ๊ฒฝ๊ธฐ์ ๋ฐ์ค์ค์ฝ์ด๊ฐ ์ ๊ณต๋๋ค. `gamePk`๋ ํด๋น ๊ฒฝ๊ธฐ์ ์๋ฆฌ์ผ ๋๋ฒ์ด๋ค. 

์ด ๋ `timecode` ํ๋ผ๋ฏธํฐ์ ํน์  ํ์์คํฌํ๋ฅผ ๊ธฐ์ํด์ฃผ๋ฉด ๊ทธ ๋น์์ ๋ฐ์ค์ค์ฝ์ด๋ฅผ ์ถ๋ ฅํ  ์ ์๋ค. ๊ฒฝ๊ธฐ์ ๋งค ์๊ฐ๋ง๋ค ํ์์คํฌํ๊ฐ ์ ์ฅ๋๋๋ฐ, `statsapi.get(โgame_timestampsโ,{โgamePkโ= })`ํจ์๋ฅผ ์ฌ์ฉํ์ฌ ํน์  ๊ฒฝ๊ธฐ์ ํ์์คํฌํ๋ค์ ๋ฌด์์ด ์๋์ง ํ์ธํด๋ณผ ์ ์๋ค.

```python

statsapi.boxscore(gamePk, battingBox=True, battingInfo=True, fieldingInfo=True, pitchingBox=True, gameInfo=True, timecode=None)

#์์. gamePk๊ฐ 565997์ธ ๊ฒฝ๊ธฐ(ํ๋ฆฌ์ค์ 2019๋ 4์ 24์ผ ๋ฉ์ธ ์  1์๊ฐ 24๋ถ 40์ด ๊ฒฝ ๋ฐ์ค์ค์ฝ์ด
statsapi.boxscore(565997, timecode=20190425_012240)
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
Phillies Batters                         AB   R   H  RBI BB   K  LOB AVG   OPS  | Mets Batters                             AB   R   H  RBI BB   K  LOB AVG   OPS
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
1 McCutchen  LF                           5   0   1   0   0   1   3  .250 .830  | 1 McNeil  LF                              4   0   1   0   0   0   1  .363 .928
2 Realmuto  C                             3   1   1   0   1   1   2  .282 .786  | 2 Conforto  RF                            3   0   0   0   1   1   1  .292 .986
3 Harper  RF                              4   1   1   1   1   3   4  .261 .909  | 3 Canรณ  2B                                3   0   3   0   1   0   0  .272 .758
4 Hoskins  1B                             4   2   2   2   1   1   3  .273 .982  | 4 Ramos, W  C                             4   0   0   0   0   3   6  .278 .687
5 Franco  3B                              5   1   1   1   0   0   3  .271 .905  | 5 Smith, Do  1B                           2   0   0   0   1   1   2  .400 .996
6 Hernรกndez, C  2B                        5   1   1   0   0   1   2  .267 .730  |     c-Alonso, P  1B                       1   0   0   0   0   1   1  .306 1.086
7 Rodrรญguez, S  SS                        4   0   1   0   0   1   1  .250 .750  | 6 Frazier, T  3B                          3   0   0   0   0   0   4  .182 .705
8 Velasquez  P                            1   0   0   0   0   0   0  .167 .453  | 7 Rosario, A  SS                          4   0   1   0   0   0   1  .261 .676
    a-Williams, N  PH                     1   0   0   0   0   0   1  .150 .427  | 8 Lagares  CF                             2   0   0   0   0   1   1  .244 .653
    Neshek  P                             0   0   0   0   0   0   0  .000 .000  |     a-Nimmo  CF                           2   0   0   0   0   0   1  .203 .714
    Domรญnguez  P                          0   0   0   0   0   0   0  .000 .000  | 9 Vargas  P                               2   0   0   0   0   1   1  .000 .000
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
b-Singled for Domรญnguez in the 8th.                                             | b-Singled for Zamora in the 7th.
c-Struck out for Morgan in the 9th.                                             | c-Struck out for Smith, Do in the 8th.
1-Ran for Quinn in the 8th.                                                     | d-Struck out for Rhame in the 9th.
                                                                                |
BATTING                                                                         | BATTING
2B: Harper (7, Vargas); Rodrรญguez, S (1, Rhame); Realmuto (4, Vargas).          | TB: Canรณ 3; Guillorme; McNeil; Rosario, A.
3B: Hoskins (1, Gsellman).                                                      | Runners left in scoring position, 2 out: Frazier, T 2; Vargas; Smith, Do 2.
HR: Hoskins (7, 9th inning off Rhame, 1 on, 0 out).                             | GIDP: McNeil.
TB: Franco; Gosselin; Harper 2; Hernรกndez, C; Hoskins 7; McCutchen; Quinn;      | Team RISP: 0-for-6.
    Realmuto 2; Rodrรญguez, S 2.                                                 | Team LOB: 9.
RBI: Franco (19); Gosselin (4); Harper (15); Hoskins 2 (20); Quinn (1).         |
Runners left in scoring position, 2 out: Hoskins; Hernรกndez, C; Knapp; Realmuto | FIELDING
    2; McCutchen.                                                               | E: Canรณ (3, fielding); Rosario, A 2 (7, throw, throw).
SAC: Rodrรญguez, S; Velasquez.                                                   |
Team RISP: 4-for-13.                                                            |
Team LOB: 11.                                                                   |
                                                                                |
FIELDING                                                                        |
DP: (Hernรกndez, C-Rodrรญguez, S-Hoskins).                                        |
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
Phillies Pitchers                            IP   H   R  ER  BB   K  HR   ERA   | Mets Pitchers                                IP   H   R  ER  BB   K  HR   ERA
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
Velasquez  (W, 1-0)                         5.0   3   0   0   3   6   0   1.99  | Vargas  (L, 1-1)                            4.2   3   1   1   2   4   0   7.20
Neshek  (H, 2)                              1.0   1   0   0   0   0   0   2.70  | Lugo, S                                     2.0   0   0   0   0   2   0   4.60
Domรญnguez  (H, 3)                           1.0   1   0   0   0   0   0   4.32  | Zamora                                      0.1   0   0   0   0   1   0   0.00
Morgan                                      1.0   1   0   0   0   2   0   0.00  | Gsellman                                    1.0   5   3   3   0   1   0   4.20
Nicasio                                     1.0   0   0   0   0   1   0   5.84  | Rhame                                       1.0   2   2   2   1   2   1   8.10
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
Totals                                      9.0   6   0   0   3   9   0         | Totals                                      9.0  10   6   6   3  10   1
------------------------------------------------------------------------------- | -------------------------------------------------------------------------------
WP: Velasquez; Gsellman.
HBP: Realmuto (by Vargas); Frazier, T (by Velasquez).
Pitches-strikes: Velasquez 97-53; Neshek 13-8; Domรญnguez 9-6; Morgan 14-10; Nicasio 15-10; Vargas 89-53; Lugo, S 32-23; Zamora 5-3; Gsellman 25-17; Rhame 19-12.
Groundouts-flyouts: Velasquez 6-3; Neshek 1-2; Domรญnguez 1-1; Morgan 1-0; Nicasio 2-0; Vargas 8-3; Lugo, S 3-2; Zamora 0-0; Gsellman 1-1; Rhame 0-0.
Batters faced: Velasquez 22; Neshek 4; Domรญnguez 3; Morgan 4; Nicasio 3; Vargas 21; Lugo, S 8; Zamora; Gsellman 8; Rhame 6.
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

ํ๋ผ๋ฏธํฐ๋ค์ ๊ธฐ๋ณธ๊ฐ์ ๋ชจ๋ True์ด๋ค.  gamePk ๊ฐ์ ๋ฃ์ผ๋ฉด ํด๋น ๊ฒฝ๊ธฐ์ ๋ฐ์ค์ค์ฝ์ด๊ฐ ์ ๊ณต๋๋ค.

### 1-2. `boxscore_data`

boxscore ํจ์์ ๊ฐ์ ๋์๋๋ฆฌ๋ก ์ถ๋ ฅํ๋ค. `boxscore`ํจ์์ ํ๋ผ๋ฏธํฐ๋ ๋์ผํ๋ค.

```python
#์์. gamePk๊ฐ 565997์ธ ๊ฒฝ๊ธฐ(ํ๋ฆฌ์ค์ 2019๋ 4์ 24์ผ ๋ฉ์ธ ์  1์๊ฐ 24๋ถ 40์ด ๊ฒฝ ๋ฐ์ค์ค์ฝ์ด
statsapi.boxscore_data(565997, timecode=20190425_012240)
```

### 1-3. `last_game`

ํน์  ํ์ ๊ฐ์ฅ ์ต๊ทผ ๊ฒ์์ ์ถ๋ ฅ

```python
statsapi.last_game(teamId)
```

### 1-4. `game_highlights`

ํน์  ๊ฒ์์ ํ์ด๋ผ์ดํธ ์์ ๋งํฌ๋ฅผ ์ ๊ณตํด์ฃผ๋ ํจ์.

```python
statsapi.game_highlights(gamePk)
```

### 1-5. `game_pace`

ํน์ฑ ์์ฆ์ ์์์ ๊ฐ๋ตํํด์ฃผ๋ ํจ์. season ํ๋ผ๋ฏธํฐ ๊ธฐ๋ณธ๊ฐ์ด ํ์ฌ ์ฐ๋์ด๋ค.

```python
statsapi.game_pace(season=datetime.now().year, sportId=1)
```

### 1-6. `game_pace_data`

`game_pace`๋ฅผ ๋์๋๋ฆฌ ํํ๋ก ์ถ๋ ฅํ๋ ํจ์.

```python
statsapi.game_pace_data(season=datetime.now().year, sportId=1)
```

โ **๋ฌธ์ .** 
```
2008๋๋ถํฐ 2021๋๊น์ง ๊ฐ ์์ฆ์ 9์ด๋๋น ์ํ ๊ฐ์ ํ๊ท ์ ์๊ณ์ด ๊ทธ๋ํ๋ก ํํํ๋ผ.
```

๐ก **์ ๋ต.**

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

ํด๋ฅผ ๊ฑฐ๋ญํ ์๋ก ํฌ๊ณ ํ์  ํ์์ด ์ฌํด์ง๊ณ  ์๋ค.

### 1-7. `game_scoring_play`

ํน์  ๊ฒฝ๊ธฐ์ ์ค์ฝ์ด๊ฐ ๋ฐ์ํ ์ํฉ๋ค์ ์ค๋ชํด์ฃผ๋ ํจ์์ด๋ค.

```python
print(statsapi.game_scoring_plays(567074))

#์ ๊ฒฝ๊ธฐ์์ ๋ฐ์ํ ๊ฐ ๋์ ์ํฉ์ด ์ด๋ค ์์ผ๋ก ๋ฌ์ฌ๋๋์ง ํ์ธํด๋ณด์

Rhys Hoskins doubles (6) on a sharp line drive to left fielder Isaac Galloway.   
Bryce Harper scores.
Bottom 1 - Miami Marlins: 0, Philadelphia Phillies: 1
#1ํ๋ง, Hoskins๊ฐ ์ข์ต์ Galloway์ชฝ์ผ๋ก ๊ฐ๋ ๋ผ์ธ๋๋ผ์ด๋ธ์ฑ 2๋ฃจํ๋ฅผ ์ณค๊ณ , Harper๊ฐ ๋์ ํ๋ค.

Bryce Harper grounds out, shortstop Miguel Rojas to first baseman Martin Prado.   
Jean Segura scores.
Bottom 3 - Miami Marlins: 0, Philadelphia Phillies: 3
#3ํ๋ง, Harper๊ฐ ์ ๊ฒฉ์๋๋ณผ(6-3)๋ก ์์๋๊ณ  Segura๊ฐ ๋์ ํ๋ค.

Rhys Hoskins walks.   
Andrew McCutchen scores.    
Jean Segura to 3rd.  
Wild pitch by pitcher Tayron Guerrero.
Bottom 8 - Miami Marlins: 1, Philadelphia Phillies: 5
#8ํ๋ง, ํฌ์ Guerrero์ ์์ผ๋ํผ์น๋ก Hoskins๋ ๋ณผ๋ท ์ถ๋ฃจํ๊ณ  McCutchen์ด ๋์ , Segura๋ 3๋ฃจ๋ก ์ง๋ฃจํ๋ค.
```

### 1-8. `game_scoring_play_data`

`game_scoring_play`๋ฅผ ๋์๋๋ฆฌ ํํ๋ก ์ถ๋ ฅํ๋ ํจ์์ด๋ค. 

๋์๋๋ฆฌ์ `home`, `away`, `plays` ์ธ ๊ฐ์ง key๊ฐ ์๋๋ฐ ์ฌ๊ธฐ์ ์ฃผ๋ชฉํ  ๊ฒ์ด ์ธ๋ถ์ํฉ์ ๋ฌ์ฌํด์ฃผ๋ `plays`์ด๋ค. 

`plays`์ key๋ ๊ฐ ๋์  ์ํฉ์ `result`, `about`, `atBatIndex`๋ผ๋ key๋ก ์ธ๋ถํํ๋ค. ๊ฐ๊ฐ์ด ๊ฐ์ง ์ ๋ณด๋ฅผ ๋ฐ ์ฝ๋์์ ํ์ธํด๋ณด๊ธธ ๋ฐ๋๋ค.

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

MLB-StatsAPI ๋ฐ์ดํฐ๋ฅผ JSON ํฌ๋งท์ผ๋ก ์ถ๋ ฅํด์ฃผ๋ ํจ์์ด๋ค. `endpoint`์๋ ๋ถ๋ฌ์ฌ ๋์๋๋ฆฌ๋ฅผ ์๋ ฅํ๊ณ , `params`์๋ ๊ทธ ๋์๋๋ฆฌ์์ ๊ฐ์ ธ์ฌ ํ๋ผ๋ฏธํฐ๋ฅผ ์๋ ฅํด์ค๋ค.

```python
statsapi.get(endpoint, params, force=False)

#์๋ฅผ ๋ค์ด team์ด๋ผ๋ ๋์๋๋ฆฌ์์ teamID=143(ํ๋ผ๋ธํผ์)์ ๋ํ ์ ๋ณด๋ฅผ ๊ฐ์ ธ์ค๋ ค๋ฉด
statsapi.get('team', {'teamId':143})
```

### 1-10. `league_leaders`

```python
statsapi.league_leaders(leaderCategories, season=None, limit=10, 
	statGroup=None, leagueId=None, gameTypes=None, playerPool=None, 
	sportId=1, statType=None)
```

`leaderCategories`์๋ ๊ธฐ์ค์ด ๋  ์คํฏ์ ์๋ ฅํด์ผ ํ๋ค. ์๋ ฅ ๊ฐ๋ฅํ ์คํฏ๋ค์ `statsapi.meta(โleagueLeaderTypes')`์ผ๋ก ํ์ธ๊ฐ๋ฅํ๋ค. `leagueLeaderTypes`์๋ ๋ฌด์์ด ์๋์ง ์ถ์ถํด๋ณด์

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

์ ํจ์๋ ์์ผ๋ก `meta`ํจ์์์ ๊ฐ์ ธ์ฌ ์ ์๋ value๋ค์ด ๋ฌด์์ธ์ง ํ์ธํ๊ณ  ์ถ์ ๋ ์ ์ฉํ๊ฒ ์ฌ์ฉํ  ์ ์๋ค.

`limit`์๋ ์์๋ฅผ ๋ช์๊น์ง ์ถ๋ ฅํ ์ง ์ ํด์ค๋ค. `statGroup`์๋ ํด๋น ์คํฏ์ด ์ด๋ค ๊ทธ๋ฃน์ธ์ง๋ฅผ ์ ์ด์ค์ผ ํ๋ค. ํ์  ์คํฏ์ ์ถ๋ ฅํ๋๋ฐ pitching์ ์ ์ด๋ฒ๋ฆฌ๋ฉด ๋น์ฐํ ์ด์ํ ๊ฐ์ด ๋์ฌ ๊ฒ์ด๋ค.

`gameTypes`์๋ ์ด leaderboard๊ฐ ์ ๊ท์์ฆ ๊ฒ์ธ์ง, ํฌ์คํธ์์ฆ์ธ์ง ์ฌํ ์ด๋ค ์๋ฆฌ์ฆ์ธ์ง๋ฅผ ์๋ ฅํด์ค์ผ ํ๋ค.

`statTypes`์๋ ์คํฏํ์์ ์ ์ด์ค๋ค. `career`๋ฅผ ์๋ ฅํ๋ฉด ํต์ฐ์ปค๋ฆฌ์ด ๊ธฐ์ค์ด ๋๋ค.

`playerPool`์๋ ์์์ ๋ค์ด๊ฐ ๋์ ์ ์ ํ์ ์ ํด์ค๋ค. ๋ชจ๋  ์ ์๊ฐ ๋์์ด๋ผ๋ฉด `all`, ๊ท์ ์ด๋(ํ์) ์ ์๊ฐ ๋์์ด๋ผ๋ฉด `qualified`, ์ ์ธ์ด ๋์์ด๋ผ๋ฉด `rookies`๋ฅผ ์ ์ด์ค๋ค.

`leagueId`์๋ AL(103), NL(104)๋ฅผ ์ ์ด์ค๋ค.

โ **๋ฌธ์ 1.** 
```
1) 2021์์ฆ ์ด๋๋น ํฌ๊ตฌ์๊ฐ ๊ฐ์ฅ ๋ฎ์ 10์ธ์ ์ถ๋ ฅํ๋ผ.
2)๋ฉ์ด์ ๋ฆฌ๊ทธ ์ปค๋ฆฌ์ด ํต์ฐ ์ต๋คํ๋ฐ 1~10์๋ฅผ ์ถ๋ ฅํ๋ผ.
```
๐ก **์ ๋ต.**

```python
#๋ฌธ์ 1)
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

#๋ฌธ์ 2)
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

`league_leaders` ํจ์์ ๊ฐ์ ์ ๋ณด๋ฅผ ๋ถ๋ฌ์ค๊ณ , ์ด๋ฅผ ๋ฆฌ์คํธ ํ์์ผ๋ก ๋ฐํํด์ฃผ๋ ํจ์์ด๋ค. ํ๋ผ๋ฏธํฐ๊ฐ `league_leaders`ํจ์์ ๋ชจ๋ ๋์ผํ๋ค.

```python
statsapi.league_leader_data(leaderCategories, season=None, limit=10, 
	statGroup=None, leagueId=None, gameTypes=None, playerPool=None, 
	sportId=1, statType=None)

#์ ๋ฌธ์ 1์ ํจ์๋ฅผ league_leader_data ํจ์๋ก ์ถ๋ ฅํ๋ฉด ์๋์ ๊ฐ์ ๋ฆฌ์คํธ๋ฅผ ๋ฐํํ๋ค.
[[1, 'Adam Wainwright', 'St. Louis Cardinals', '14.87'], [2, 'Julio Urias', 'Los Angeles Dodgers', '15.01'], [3, 'Zack Wheeler', 'Philadelphia Phillies', '15.02'], [4, 'Cole Irvin', 'Oakland Athletics', '15.04'], [5, 'Sandy Alcantara', 'Miami Marlins', '15.05'], [6, 'Zack Greinke', 'Houston Astros', '15.07'], [7, 'Walker Buehler', 'Los Angeles Dodgers', '15.18'], [8, 'Anthony DeSclafani', 'San Francisco Giants', '15.26'], [9, 'Marcus Stroman', 'New York Mets', '15.31'], [10, 'Max Fried', 'Atlanta Braves', '15.44']]
```

### 1-12. `linescore`

ํน์  ๊ฒฝ๊ธฐ์ ๋ผ์ธ์ค์ฝ์ด๋ฅผ ์ถ๋ ฅํด์ฃผ๋ ํจ์

```python
print(statsapi.linescore(gamePk, timecode=None))

#์์. 2019๋ 4์ 25์ผ ํ๋ฆฌ์คvs๋ฉ์ธ ์ ๊ฒฝ๊ธฐ(565997)์ ๋ผ์ธ์ค์ฝ์ด๋ฅผ ์ถ๋ ฅํด๋ณด์
print(statsapi.linescore(565997))

Final    1 2 3 4 5 6 7 8 9  R   H   E  
Phillies 1 0 0 0 0 0 0 3 2  6   10  0  
Mets     0 0 0 0 0 0 0 0 0  0   6   3
```

### 1-13. `lookup_player`

`lookup_value`์ ๊ฒ์ํ๊ณ ์ ํ๋ ์ ์ ์ด๋ฆ์ ์๋ ฅํ๋ฉด, ๊ทธ ์ ์์ ์ด๋ฆ์ ๋ํ ์ ๋ณด๋ฅผ ์ถ๋ ฅํ๋ค.

๋ง์ฝ nola๋ผ๋ ์ ์๋ฅผ ๋ถ๋ฌ์ค๊ธฐ ์ํด nola๋ฅผ ์๋ ฅํ๋ค๋ฉด, nolan์ฒ๋ผ nola๋ฅผ ํฌํจํ๋ ๋ชจ๋  ์ด๋ฆ์ด ์ถ๋ ฅ๋์ด๋ฒ๋ฆฐ๋ค. ์ด๊ฒ์ ๋ฐฉ์งํ๊ธฐ ์ํด nola, ์ฒ๋ผ ๋ค์ ์ฝค๋ง๋ฅผ ๋ถ์ฌ์ฃผ๋ฉด nola๋ผ๋ ์ด๋ฆ๋ง ์ธ์ํ๋ค.

```python
statsapi.lookup_player(lookup_value, gameType="R", season=datetime.now().year, sportId=1)

#์์. ๋ฅํ์ง์ ๊ฒ์ํด๋ณด์.
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
  'nickName': 'Monster', #๋๋ค์๊น์ง๋ ์ถ๋ ฅ๋๋ค. ์ฆ, lookup_value์ Monster๋ฅผ ์๋ ฅํด๋ ๋ฅํ์ง์ ์ ๋ณด๊ฐ ์ถ๋ ฅ๋๋ค.
  'primaryNumber': '99',
  'primaryPosition': {'abbreviation': 'P', 'code': '1'},
  'useName': 'Hyun Jin'}]
```

โ **๋ฌธ์ .**  
```
๋ณ์๋ฅผ ์๋ ฅํ๋ฉด, ์ด๋ฆ์ ๊ทธ ๋ณ์๋ฅผ ํฌํจํ ์ ์๋ค๋ง ์ถ๋ ฅํ๋ ํจ์๋ฅผ ๋ง๋ค์ด๋ณด์ ์ด ๋  ์ถ๋ ฅํ์์ `Full name: ์ ์์ด๋ฆ, Position: ํฌ์ง์, Team: ํ ๊ณ ์  ๋ฒํธ` ๋ก ํ๋ค.
```
๐ก **์ ๋ต.**

```python
def player_npt(a):
  for player in statsapi.lookup_player(a):
    print('Full name: {} / Position: {} / Team: {}'.format(player['fullName'], player['primaryPosition']['abbreviation'], player['currentTeam']['id']))

#์์
player_npt('cole')

Full name: Gerrit Cole / Position: P / Team: 147
Full name: Dylan Coleman / Position: P / Team: 118
Full name: Cole Irvin / Position: P / Team: 133
Full name: Jared Oliva / Position: CF / Team: 134 #๋ฏธ๋ค๋ค์์ cole ๋ค์ด๊ฐ ๊ฒฝ์ฐ
Full name: Josh Rogers / Position: P / Team: 120 #๋ฏธ๋ค๋ค์์ cole ๋ค์ด๊ฐ ๊ฒฝ์ฐ
Full name: Cole Sands / Position: P / Team: 142
Full name: Cole Sulser / Position: P / Team: 110
Full name: Keegan Thompson / Position: P / Team: 112 #๋ฏธ๋ค๋ค์์ cole ๋ค์ด๊ฐ ๊ฒฝ์ฐ
Full name: Cole Tucker / Position: SS / Team: 134
```

### 1-14. `lookup_team`

`lookup_player` ํจ์์ ํก์ฌํ๋ค. `lookup value`์ ๊ฒ์ํ๊ณ ์ ํ๋ ํ ์ด๋ฆ์ ์๋ ฅํ๋ฉด, ๊ทธ ํ์ ๋ํ ์ ๋ณด๋ฅผ ์ถ๋ ฅํด์ค๋ค.

```python
statsapi.lookup_team(lookup_value, activeStatus="Y", season=datetime.now().year, sportIds=1)

#์์. new๊ฐ ํ ์ด๋ฆ์ ๋ค์ด๊ฐ๋ ํ๋ค ์ถ๋ ฅ
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

StatsAPI์์ ์ฌ์ฉํ๋ ์ฌ๋ฌ type๋ค์ด ๋ฌด์จ ๊ฐ์ ๊ฐ๊ณ  ์๋์ง ๋ณด์ฌ์ฃผ๋ ํจ์์ด๋ค. ๊ฐ๋ น StatsAPI์๋ `awards`(์ ์ข๋ฅ), `baseballStats`(์ผ๊ตฌ ์คํฏ ์ด๋ง๋ผํ ๊ฒ), `eventTypes`(๊ฒฝ๊ธฐ์์ ๋ฐ์ํ  ์ ์๋ ์ฌ๊ฑด์ ์ข๋ฅ) ๋ฑ์ ์ฌ๋ฌ ๊ฐ์ง type์ด ์๋ค. ์ด ๊ฐ๊ฐ ํ์์ด ๊ฐ๊ณ  ์๋ ๊ฐ๋ณ ๊ฐ๋ค์ ์ถ๋ ฅํด์ค๋ค. 

์์ธํ ์ ๋ณด๋ [2.meta](https://www.notion.so/Python-MLB-StatsAPI-56edea75bc664ba8a06407ef0b3a2655)์์ ํ์ธํ  ์ ์๋ค.

```python
statsapi.meta(type, fields=None)

#์์1. eventTypes์๋ ์ด๋ค ๊ฒ๋ค์ด ์๋์ง ํ์ธํด๋ณด์.
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
... ์๋ต ...

#์์2.pitchTypes(ํฌ๊ตฌ๊ฒฐ๊ณผ์ ํ)์๋ ์ด๋ค ๊ฒ๋ค์ด ์๋์ง ํ์ธํด๋ณด์
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
...์๋ต...
```

### 1-16. `next_game`

์ฃผ์ด์ง ํ์ ๋ค์ ๊ฒฝ๊ธฐ `gamePK`๊ฐ์ ์ถ๋ ฅํด์ฃผ๋ ํจ์์ด๋ค.

```python
statsapi.next_game(teamId)
```

### 1-17.  `notes`

๊ฐ endpoint๊ฐ ํ์๋ก ๊ฐ์ ธ์ผ ํ๋ ํ๋ผ๋ฏธํฐ(required parameters), ๊ฐ์ง ์ ์๋ ํ๋ผ๋ฏธํฐ(all parameters)๋ฅผ ํฌํจํ ์ ์ฉํ ์ ๋ณด๋ฅผ ๊ธฐ์ ํด์ฃผ๋ ํจ์์ด๋ค.

```python
statsapi.notes(endpoint)

#์์. attendance๋ผ๋ endpoint์ ๋ํ ์ ๋ณด๋ฅผ ์ถ๋ ฅํด๋ณด์. 
statsapi.notes('attendance')

Endpoint: attendance 
All path parameters: ['ver']. 
Required path parameters (note: ver will be included by default): ['ver']. 
All query parameters: ['teamId', 'leagueId', 'season', 'date', 'leagueListId', 'gameType', 'fields']. 
Required query parameters: [['teamId'], ['leagueId'], ['leagueListid']].

https://statsapi.mlb.com/api/v1/teams/143
```

### 1-18 `player_stats`

ํน์  ์ ์์ ์์ฆ์ฑ์  ํน์ ์ปค๋ฆฌ์ด ์ ์ฒด ์ฑ์ ์ ์ถ๋ ฅํด์ฃผ๋ ํจ์์ด๋ค.  `personId`์ ์ํ๋ ์ ์์ id๋ฅผ ์๋ ฅํด์ฃผ๊ณ , ์๊ณ ์ ํ๋ `statGroup`๊ณผ `season`์ ์๋ ฅํด์ค๋ค.

```python
statsapi.player_stats(personId, group="[hitting,pitching,fielding]", type="season")

#์์. ๋ง์ดํฌ ํธ๋ผ์์ ํต์ฐ hitting stat์ ์ถ๋ ฅํด๋ณด์. 
#personId๋ฅผ ๊ฐ์ ธ์ค๊ธฐ ์ํด getํจ์๋ก sports_players ์๋ํฌ์ธํธ๋ฅผ ์ฌ์ฉํ๋ค.
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

`player_stats`์ ์ถ๋ ฅ๊ฐ์ ๋์๋๋ฆฌ ํ์์ผ๋ก ๋ฐํํด์ค๋ค.

โ **๋ฌธ์ .** 
```
๋ณด์คํด๋ ๋์ญ์ค์ 2021์์ฆ ํ์ญ ์ ์๋ค์ ํ์จ์ ์ถ๋ ฅํ๋ผ. ๋จ, โfullName, ํ์จโ ํ์์ผ๋ก ์ถ๋ ฅํ๋ผ.
```

๐ก **์ ๋ต.**

```python
for n in statsapi.get('sports_players',{'season':2021, 'gameType':'R'})['people']:
  if n['currentTeam']['id'] == 111: #๋ณด์คํด ๋ ๋์ญ์ค์ id๊ฐ 111
    if statsapi.player_stat_data(n['id'],'hitting','career')['stats']: #hitting stat์ด true์ฌ์ผ ์ถ๋ ฅ
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
...์๋ต...
```

### 1-20 `roster`

ํน์  ํ์ ๋ก์คํฐ๋ฅผ ์ถ๋ ฅํด์ฃผ๋ ํจ์์ด๋ค. `date`๋ mm/dd/yyyy ํ์์ผ๋ก ์๋ ฅํด์ค๋ค.

```python
statsapi.roster(teamId, rosterType=None, season=datetime.now().year, date=None)

#์์. ํ๋ผ๋ธํผ์์ ์ฌ ์์ฆ ๋ก์คํฐ๋ฅผ ์ถ๋ ฅํด๋ณด์.
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
...์๋ต...
```

### 1-21 `schedule`

์ฃผ์ด์ง ๊ธฐ๊ฐ๋์ ํน์  ํ์ ๊ฒฝ๊ธฐ ๋ชฉ๋ก์ ์ถ๋ ฅํด์ฃผ๋ ํจ์์ด๋ค. 

```python
statsapi.schedule(date=None, start_date=None, end_date=None, team="", opponent="", sportId=1, game_id=None)

#์์. 7์ 9์ผ ํ๋ฆฌ์ค์ ๋ฉ์ธ ์ ๊ฒฝ๊ธฐ๋ฅผ ์ถ๋ ฅํด๋ณด์.
print(statsapi.schedule(date='07/09/2018',team=143,opponent=121))

{'game_id': 530769, #gamePk
'game_datetime': '2018-07-09T20:10:00Z', #๊ฒฝ๊ธฐ ๋ ์ง์ ์๊ฐ
'game_date': '2018-07-09', #๊ฒฝ๊ธฐ ๋ ์ง
'game_type': 'R', #๊ฒฝ๊ธฐ ์ ํ. R์ Regular season(์ ๊ท์์ฆ)์ ์๋ฏธ
'status': 'Final', #๊ฒฝ๊ธฐ ์ํ. Scheduled(์์ ), Warmup(๊ฒฝ๊ธฐ ์ง์  ๋ชธํธ๋ ๋), In progress(์งํ์ค), Final(์ข๋ฃ)๋ฅผ ์๋ฏธ.
'away_name': 'Philadelphia Phillies', #์์ ํ
'home_name': 'New York Mets', #ํํ
'away_id': 143, #์์ ํ id
'home_id': 121, #ํํ id
'doubleheader': 'Y', #๋๋ธํค๋ ์ฌ๋ถ. Y์ด๋ฏ๋ก ์ด ๊ฒฝ๊ธฐ๋ ๋๋ธํค๋.
'game_num': 1, #๋๋ธํค๋์ 1๋ฒ์งธ ๊ฒฝ๊ธฐ๋ผ๋ฉด 1, 2๋ฒ์งธ ๊ฒฝ๊ธฐ๋ผ๋ฉด 2. ๋๋ธํค๋๊ฐ ์๋๋ผ๋ฉด 1
'home_probable_pitcher': 'Zack Wheeler', #ํํ ์ ๋ฐํฌ์
'away_probable_pitcher': 'Zach Eflin', #์์ ํ ์ ๋ฐ
'home_pitcher_note': 'Another victim of a low-scoring offense, Wheeler is 0-4 over his last 11 starts, despite a 3.76 ERA and 67 strikeouts in those 66 innings. The Mets will push Wheeler back a day in the rotation, hoping he can provide length in a doubleheader.', 
#ํํ ํฌ์ ์ต๊ทผ ๊ฒฝ๊ธฐ ๋ฆฌํฌํธ
'away_pitcher_note': 'Following three consecutive starts of fewer than five innings to finish May, Eflin has been arguably the teamโs best pitcher since. He is 6-0 with a 1.91 ERA in his past six starts, striking out 34 and walking six in 37 2/3 innings.', 
#์์ ํ ํฌ์ ์ต๊ทผ ๊ฒฝ๊ธฐ ๋ฆฌํฌํธ
'away_score': 3, #์์ ํ ์ ์. in progress ์ํ์์๋ ์ค์๊ฐ ๋ฐ์
'home_score': 4, #ํํ ์ ์. in progress ์ํ์์๋ ์ค์๊ฐ ๋ฐ์
'current_inning': 10, #ํ์ฌ ์ด๋. in progress ์ํ์์ ์ ์ฉ.
'inning_state': 'Bottom', #์ด(Top)์ธ์ง ๋ง(Bottom)์ธ์ง
'venue_id': 3289, #๊ตฌ์ฅ id
'venue_name': 'Citi Field', #๊ตฌ์ฅ ์ด๋ฆ
'winning_team': 'New York Mets', #์น๋ฆฌํ
'losing_team': 'Philadelphia Phillies', #ํจ๋ฐฐํ
'winning_pitcher': 'Tim Peterson', #์น๋ฆฌํฌ์
'losing_pitcher': 'Victor Arano', #ํจ์ ํฌ์
'save_pitcher': None, #์ธ์ด๋ธํฌ์
'summary': '2018-07-09 - Philadelphia Phillies (3) @ New York Mets (4) (Final)'} #๊ฒฝ๊ธฐ ํ์ค ์์ฝ. @๊ฐ ๋ถ์ ๊ฒ ํํ.
```

โ **๋ฌธ์ **.
```
4์~7์ ์ค ์ด๋ฆฐ ํ๋๋ฆฌ์ค์ ๋ฉ์ธ ์ ๊ฒฝ๊ธฐ ๊ฒฐ๊ณผ ์์ฝ์ ์ถ๋ ฅํ๋ผ. ์ด ๋ ์น๋ฆฌ,ํจ์ ,์ธ์ด๋ธ ํฌ์๋ ํจ๊ป ์ถ๋ ฅํ๋ผ.
```
๐ก **์ ๋ต**.

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

์ฃผ์ด์ง ๋ฆฌ๊ทธ, ์ง๊ตฌ ์์ํ๋ฅผ ์ถ๋ ฅํด์ฃผ๋ ํจ์์ด๋ค. `include_wildcard`์ ๊ธฐ๋ณธ๊ฐ์ True์ด๋ค

```python
statsapi.standings(leagueId="103,104", division="all", include_wildcard=True, season=None, standingsTypes=None, date=None)

#์์. 2021๋ 9์ 27์ผ์ ๋ด์๋๋ฆฌ๊ทธ ์์ํ๋ฅผ ์ถ๋ ฅํ๋ผ.
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

`standing` ํจ์์ ์ถ๋ ฅ๊ฐ์ ๋์๋๋ฆฌ๋ก ๋ฐํํด์ฃผ๋ ํจ์์ด๋ค. ํ๋ผ๋ฏธํฐ๋ `standings` ํจ์์ ๋์ผํ๋ค.

### 1-24 `team_leaders`

ํน์  ํ์ ํน์  ์คํฏ ์์๋ฅผ ์ถ๋ ฅํด์ฃผ๋ ํจ์์ด๋ค. `leaderCategories`์ ๊ธฐ์ค ์คํฏ์ ์๋ ฅํด์ฃผ๊ณ , `limit`์ ์ถ๋ ฅํ  ์์๋ฅผ, `season`์ ์์๋ณผ ์์ฆ์ ์๋ ฅํด์ค๋ค.

```python
statsapi.team_leaders(teamId, leaderCategories, season=datetime.now().year, leaderGameTypes="R", limit=10)

#์์. ํ๋ฆฌ์ค์ 2021๋ ํ๋ ์์ 7์ธ์ ์ถ๋ ฅํ๋ผ.
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

team_leaders ํจ์์ ์ถ๋ ฅ๊ฐ์ ๋ฆฌ์คํธ๋ก ๋ณํํด์ฃผ๋ ํจ์์ด๋ค.

```python
#์์์ ์ถ๋ ฅํ ๊ฐ์ team_leader_data๋ก ์ถ๋ ฅํด๋ณด์. ๊ฐ๋์ฑ์ ๋์ด๊ธฐ ์ํด reshapeํด์คฌ๋ค.
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

API์์ ์ทจ๊ธํ๋ ๋ชจ๋  ์คํฏ๋ค์ ๋ชจ์๋์ ๊ฒ์ด๋ค. ์๋ ์์๋ฅผ ๋ณด์.

```python
{'highLowTypes': [],
  'isCounting': False, #์ ์ ์๋ ์คํฏ์ธ๊ฐ? false. ops๋ ๋น์จ์คํฏ.
  'lookupParam': 'ops', #์คํฏ์ ํ๋ผ๋ฏธํฐ์ด๋ฆ
  'name': 'onBasePlusSlugging', #์คํฏ์ ์ ์ ๋ช์นญ
  'orgTypes': [],
  'statGroups': [{'displayName': 'hitting'}, {'displayName': 'pitching'}], #๋ถ๋ฅ๋๋ ๊ทธ๋ฃน. hitting์์  ops, pitching์์  ํผops.
  'streakLevels': []},

{'highLowTypes': [],
  'isCounting': True, #์ ์ ์๋ ์คํฏ์ธ๊ฐ? true. ์น ์๋ ๋์ ์คํฏ.
  'lookupParam': 'w', #์คํฏ์ ํ๋ผ๋ฏธํฐ์ด๋ฆ
  'name': 'wins', #์คํฏ์ ์ ์ ๋ช์นญ
  'orgTypes': [],
  'statGroups': [{'displayName': 'pitching'}], #๋ถ๋ฅ๋๋ ๊ทธ๋ฃน
  'streakLevels': []},
```

- `baseballStats`์ ๋ด์ฅ๋ ์คํฏ ๋ชฉ๋ก
    
    ```python
    # ๊ฐ ์คํฏ์ ์ด๋ฆ๊ณผ lookupParam๋ง ์ถ์ถํ๊ธฐ ์ํ ๋ฐ๋ณต๋ฌธ
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
    # ์ํ๋ ์คํฏ๋ช์ ์๋ ฅํ๋ฉด ๊ทธ ์คํฏ์ ์์ธ ์ ๋ณด๋ฅผ ์ถ๋ ฅํด์ฃผ๋ ํจ์
    def search_stat(a):
      index=-1
      for stat in statsapi.meta('baseballStats'):
        index+=1
        if stat['name'] == a:
          print(statsapi.meta('baseballStats')[index])
    ```
    

### 2-3. `eventTypes`

๊ฒฝ๊ธฐ์์ ๋ฐ์ํ๋ ๋ชจ๋  ๊ฒฐ๊ณผ ์ ํ์ ์ด๋ง๋ผํ ๊ฒ. ์๋ ์์๋ฅผ ๋ณด์.

```python
{'baseRunningEvent': True, #์ฃผ์๊ฐ ๋ฒ ์ด์ค๋ฅผ ๋ฐ๋ ์ฌ๊ฑด์ธ๊ฐ? true.
  'code': 'stolen_base_3b', #3๋ฃจ ๋๋ฃจ
  'description': 'Stolen Base 3B',
  'hit': False, #์ํ๋ฅผ ์ณค๋๊ฐ? false.
  'plateAppearance': False} #ํ ํ์์ผ๋ก ์นด์ดํธ ๋๋๊ฐ? false.

{'baseRunningEvent': False, #์ฃผ์๊ฐ ๋ฒ ์ด์ค๋ฅผ ๋ฐ๋ ์ฌ๊ฑด์ธ๊ฐ? false.
  'code': 'triple', #3๋ฃจํ
  'description': 'Triple',
  'hit': True, #์ํ๋ฅผ ์ณค๋๊ฐ? true.
  'plateAppearance': True} #ํ ํ์์ผ๋ก ์นด์ดํธ ๋๋๊ฐ? true.

{'baseRunningEvent': False, #์ฃผ์๊ฐ ๋ฒ ์ด์ค๋ฅผ ๋ฐ๋ ์ฌ๊ฑด์ธ๊ฐ? false.
  'code': 'hit_by_pitch', #๋ชธ์ ๋ง๋ ๋ณผ
  'description': 'Hit By Pitch',
  'hit': False, #์ํ๋ฅผ ์ณค๋๊ฐ? false.
  'plateAppearance': True}, #ํ ํ์์ผ๋ก ์นด์ดํธ ๋๋๊ฐ? true.

```

- `eventTypes` ์ ํ

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

๊ฒฝ๊ธฐ์์ ๋ฐ์๋๋ ์์ธ์ ์ธ ์ํฉ(ํญ์, ์ค๋จ, ์ง์ฐ, ํ์  ๋ฆฌ๋ทฐ)๋ค์ ์ค๋ชํด์ค๋ค. ์๋ ์์๋ฅผ ๋ณด์.

```python
{'abstractGameCode': 'L', 
  'abstractGameState': 'Live', #๊ฒฝ๊ธฐ ์งํ ์ค
  'codedGameState': 'M',
  'detailedState': 'Manager challenge: Tag-up play', #ํ๊ทธ์ ํ๋ ์ด์ ๋ํ ๊ฐ๋์ ํญ์
  'reason': 'Tag-up play',
  'statusCode': 'MU'},

{'abstractGameCode': 'L',
  'abstractGameState': 'Live', #๊ฒฝ๊ธฐ ์งํ ์ค
  'codedGameState': 'N',
  'detailedState': 'Umpire review: Catch/drop in outfield', #์ธ์ผ์์ ๊ณต์ ๋์ณค๋์ง ์ฌ๋ถ์ ๋ํ ์ฌํ์ ๋ฆฌ๋ทฐ
  'reason': 'Catch/drop in outfield',
  'statusCode': 'ND'},

{'abstractGameCode': 'P',
  'abstractGameState': 'Preview', #๊ฒฝ๊ธฐ ์์ ์ 
  'codedGameState': 'P',
  'detailedState': 'Delayed Start: Rain', #๊ฒฝ๊ธฐ ์์์ด ์ง์ฐ๋๊ณ  ์๊ณ , ์ฌ์ ๋ ๋น
  'reason': 'Rain',
  'statusCode': 'PR'},

{'abstractGameCode': 'F',
  'abstractGameState': 'Final', #๊ฒฝ๊ธฐ ๋
  'codedGameState': 'C',
  'detailedState': 'Cancelled: Fog', #๊ฒฝ๊ธฐ๊ฐ ์ทจ์๋์๊ณ , ์ฌ์ ๋ ์๊ฐ
  'reason': 'Fog',
  'statusCode': 'CF'},
```

### 2-5. `gameTypes`

๊ฒฝ๊ธฐ์ ์ ํ์ด ์ ๊ท์์ฆ์ธ์ง, ์คํ๋ง์บ ํ์ธ์ง, ์์ผ๋์นด๋์ ์ธ์ง, ์๋์๋ฆฌ์ฆ์ธ์ง ๋ฑ์ ์๋ ค์ค๋ค.

- `gameTypes`์ ๋ด์ฅ๋ ๊ฒฝ๊ธฐ ์ ํ ๋ชฉ๋ก
    
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

ํ๊ตฌ์ ์ ํ์ด๋ค.

- `hitTrajectories` ๋ชฉ๋ก
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

์ผ๊ตฌ์ ๊ด๋ จ๋ ์ง์(์ ์, ์ฌํ, ์ฝ์น, ๋ถ์์ ๋ฑ)์ ์ด๋ง๋ผํ ๋ชฉ๋ก์ด๋ค.

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

์คํฏ ์์ํ์ ๊ธฐ์ค์ด ๋๋ ์คํฏ๋ค์ ๋ด์ฅํ๊ณ  ์๋ค. 

- `leagueLeaderTypes` ๋ชฉ๋ก
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

๊ฒฝ๊ธฐ์์ ๋ฐ์ํ๋ ์ํฉ๋ค ์ค ๋ค์ ์ํฉ์ผ๋ก ์ฐ๊ณ๊ฐ๋๋ ๋ผ๋ฆฌ ์ํฉ๋ค์ ๋ชจ์๋์ ๋ชฉ๋ก์ด๋ค.

- `logicalEvents` ๋ชฉ๋ก
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

์ผ๊ตฌ์์ ์ธก์ ๋๋ ๋ค์ํ ๋ฌผ๋ฆฌ์  ์์น๋ค์ ๋ชฉ๋ก. ์๋ ์์๋ฅผ ๋ณด์.

```python
{'group': 'hitting, pitching', #์คํฏ์ด ์ํ๋ ๊ทธ๋ฃน
  'metricId': 1005,
  'name': 'launchAngle', #๋ฐ์ฌ๊ฐ
  'unit': 'DEG'}, #๋จ์๋ degree(๊ฐ๋)

{'group': 'pitching', #์คํฏ์ด ์ํ๋ ๊ทธ๋ฃน
  'metricId': 1161,
  'name': 'deliveryTime', #ํฌ๊ตฌ ์๋
  'unit': 'SEC'}, #๋จ์๋ ์ด

{'group': 'pitching', #์คํฏ์ด ์ํ๋ ๊ทธ๋ฃน
  'metricId': 1002,
  'name': 'releaseSpeed', #ํฌ๊ตฌ ๊ตฌ์
  'unit': 'MPH'}, #๋จ์๋ ์์
```

- `metrics` ๋ชฉ๋ก

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

ํฌ์์ ๊ตฌ์ข ๋ชฉ๋ก์ด๋ค.

- `pitchTypes`์ ๋ด์ฅ๋ ๊ตฌ์ข ๋ชฉ๋ก
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

ํฌ์๊ฐ ๋์ง๋ ๋ชจ๋  ๊ณต์ ๊ฐ๊ฐ์ ๊ฒฐ๊ณผ๊ฐ ์๋ค. ๋จ์ํ ์คํธ๋ผ์ดํฌ, ๋ณผ, ์ํ, ๋ฒํ๋ง์ ๊ฒฐ๊ณผ๋ก ๋๋๋ ๊ฒ์ด ์๋๋ค. ๋ ์ธ๋ถ์ ์ผ๋ก, ์ด๋ฅผํ๋ฉด ์คํธ๋ผ์ดํฌ๊ฐ ํ์ค์ ์คํธ๋ผ์ดํฌ, ํ์ธ ์คํธ๋ผ์ดํฌ, ๋ฒํธ ํ์ค์ ์คํธ๋ผ์ดํฌ ๋ฑ์ผ๋ก ๋๋๋ค.

- `pitchCodes`์ ๋ด์ฅ๋ ํฌ๊ตฌ๊ฒฐ๊ณผ ์ ํ ๋ชฉ๋ก

```    
    {'code': 'R', 'description': 'Strike - Foul on Pitchout'} : ํผ์น์์ํ ๊ณต์ ํ๊ฒฉํ์ฌ ํ์ธ(์คํธ๋ผ์ดํฌ)
    {'code': 'Y', 'description': 'Pitchout Hit Into Play - Out(s)'} : ํผ์น์์์ ํ๊ฒฉํ์ฌ ์์
    {'code': 'M', 'description': 'Strike - Missed Bunt'} : ๋ฒํธ ํ์ค์์ผ๋ก ์คํธ๋ผ์ดํฌ
    {'code': 'X', 'description': 'Hit Into Play - Out(s)'} : ํ๊ฒฉํ์ฌ ์์
    {'code': 'O', 'description': 'Strike - Bunt Foul Tip'} : ๋ฒํธ ํ์ธํ(๋ฐฐํธ์ ์ค์น ๊ณต์ด ํฌ์ ๋ฏธํธ๋ก)์ผ๋ก ์คํธ๋ผ์ดํฌ
    {'code': 'E', 'description': 'Hit Into Play - Run(s)'} : ํ๊ฒฉํ์ฌ ๋์ ์ผ๋ก ์ฐ๊ฒฐ
    {'code': 'D', 'description': 'Hit Into Play - No Out(s)'} : ํ๊ฒฉํ์ฌ ์์๋นํ์ง ์์
    {'code': 'Q', 'description': 'Strike - Swinging on Pitchout'} : ํผ์น์์ํ ๊ณต์ ํ์ค์ํ์ฌ ์คํธ๋ผ์ดํฌ
    {'code': 'Z', 'description': 'Pitchout Hit Into Play - Run(s)'} : ํผ์น์์ํ ๊ณต์ ํ๊ฒฉํ์ฌ ๋์ ์ผ๋ก ์ฐ๊ฒฐ
    {'code': 'F', 'description': 'Strike - Foul'} : ํ์ธ(์คํธ๋ผ์ดํฌ)
    {'code': 'W', 'description': 'Strike - Swinging Blocked'} : ๋ฐ์ด๋๋์ด ํฌ์๊ฐ ๋ธ๋กํนํ ๊ณต์ ํ์ค์ ์คํธ๋ผ์ดํฌ
    {'code': 'T', 'description': 'Strike - Foul Tip'} : ํ์ธํ(๋ฐฐํธ์ ์ค์น ๊ณต์ด ํฌ์ ๋ฏธํธ๋ก) ์คํธ๋ผ์ดํฌ
    {'code': 'L', 'description': 'Strike - Foul Bunt'} : ๋ฒํธํ ๊ณต์ด ํ์ธ(์คํธ๋ผ์ดํฌ)
    {'code': 'C', 'description': 'Strike - Called'} : ํ์ค์์ด ์๋ ์ฌํ ์ฝ๋ก ์ฃผ์ด์ง ์คํธ๋ผ์ดํฌ
    {'code': 'K', 'description': 'Strike - Unknown'} : ?
    {'code': 'J', 'description': 'Pitchout Hit Into Play - No Out(s)'} : ํผ์น์์ํ ๊ณต์ ํ๊ฒฉํ์ฌ ์์๋นํ์ง ์์
    {'code': 'S', 'description': 'Strike - Swinging'} : ํ์ค์ ์คํธ๋ผ์ดํฌ
    {'code': 'B', 'description': 'Ball - Called'} : ์ฌํ ์ฝ๋ก ์ฃผ์ด์ง ๋ณผ
    {'code': 'P', 'description': 'Ball - Pitchout'} : ํผ์น์์์ผ๋ก ์ฃผ์ด์ง ๋ณผ
    {'code': 'H', 'description': 'Ball - Hit by Pitch'} : ๋ชธ์๋ง๋ ๋ณผ
    {'code': '*B', 'description': 'Ball - Ball In Dirt'} : ๋ฐ์ด๋ ๋ ๋ณผ
    {'code': '3', 'description': 'Pickoff Throw 3rd - Pitcher'} : ํฌ์์ 3๋ฃจ ๊ฒฌ์ 
    {'code': '1', 'description': 'Pickoff Throw 1st - Pitcher'} : ํฌ์์ 1๋ฃจ ๊ฒฌ์ 
    {'code': '+3', 'description': 'Pickoff Throw 3rd - Catcher'} : ํฌ์์ 3๋ฃจ ๊ฒฌ์ 
    {'code': '2', 'description': 'Pickoff Throw 2nd - Pitcher'} : ํฌ์์ 2๋ฃจ ๊ฒฌ์ 
    {'code': '+2', 'description': 'Pickoff Throw 2nd - Catcher'} : ํฌ์์ 2๋ฃจ ๊ฒฌ์ 
    {'code': '+1', 'description': 'Pickoff Throw 1st - Catcher'} : ํฌ์์ 1๋ฃจ ๊ฒฌ์ 
    {'code': 'A', 'description': 'Strike - Automatic'} : ?
    {'code': '.', 'description': 'Non Pitch'},
    {'code': 'N', 'description': 'No Pitch'} : ํฌ์๊ฐ ๋์ง ๊ณต์ด ๋ณผ๋, ์คํธ๋ผ์ดํฌ๋ ์๋ ๊ฒฝ์ฐ. ๋ณดํต ์ฃผ์ฌ์ ํ์์์ ์ดํ ๋์ง ๊ณต์ ๋ํด ๋ฌดํจ์ฒ๋ฆฌ ๋๋ ๊ฒ์ ๋งํ๋ค. ๊ทธ ๋ฐ์ ์์ธ์ ์ธ ์ฌ์ ๋ก ๋ฌดํจ์ฒ๋ฆฌ ๋๋ ๊ฒฝ์ฐ.
    {'code': 'I', 'description': 'Ball - Intentional'} : ๊ณ ์๋ก ํฌ๊ตฌํ ๋ณผ
    {'code': 'V', 'description': 'Ball - Automatic'} : ?
```
    

### 2-14. `platforms`

- `platforms` ๋ชฉ๋ก
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

ํฌ์ง์๋ค์ ๋ชฉ๋ก์ด๋ค. ๋น๋จ 10๊ฐ์ ํฌ์ง์๋ง์ด ์๋๋ผ, ๋ ์ธ๋ถํํ์ฌ ์ฌ๋ฌ ํฌ์ง์์ ๋ด์ฅํ๊ณ  ์๋ค. ์๋ ์์๋ฅผ ๋ณด์

```python
{'abbrev': '1B', #์ค๋ง
  'code': '3', #ํฌ์ง์ ๋๋ฒ
  'displayName': 'First Base', #1๋ฃจ์
  'fielder': True, #์ผ์ ์ฌ๋ถ. pitcher๋ False
  'formalName': 'First Baseman',
  'fullName': 'First Base',
  'gamePosition': True, #๊ฒฝ๊ธฐ์์ ๋ถ๋ฆฌ๋ ํฌ์ง์์ธ์ง ์ฌ๋ถ
  'outfield': False, #์ธ์ผ์ ์ฌ๋ถ
  'pitcher': False, #ํฌ์ ์ฌ๋ถ
  'shortName': '1st Base',
  'type': 'Infielder'}, #ํฌ์ง์ ์ ํ. ๋ด์ผ์

{'abbrev': 'PR', #์ค๋ง
  'code': '12', #ํฌ์ง์ ๋๋ฒ
  'displayName': 'Pinch Runner', #๋์ฃผ์
  'fielder': False, #์ผ์ ์ฌ๋ถ.
  'formalName': 'Pinch Runner',
  'fullName': 'Pinch Runner',
  'gamePosition': True, #๊ฒฝ๊ธฐ์์ ์ฐ์ด๋ ํฌ์ง์์ธ์ง ์ฌ๋ถ
  'outfield': False, #์ธ์ผ์ ์ฌ๋ถ
  'pitcher': False, #ํฌ์ ์ฌ๋ถ
  'shortName': 'Pinch Runner',
  'type': 'Runner'}, #ํฌ์ง์ ์ ํ. ์ฃผ์

{'abbrev': 'CP',#์ค๋ง
  'code': 'C', #ํฌ์ง์ ์ฝ๋
  'displayName': 'Closer', #๋ง๋ฌด๋ฆฌ ํฌ์
  'fielder': False, #์ผ์ ์ฌ๋ถ
  'formalName': 'Closer',
  'fullName': 'Closer',
  'gamePosition': False, #๊ฒฝ๊ธฐ์์ ์ฐ์ด๋ ํฌ์ง์์ธ์ง ์ฌ๋ถ. ๊ฒฝ๊ธฐ์์  ๊ทธ๋ฅ pitcher
  'outfield': False, #์ธ์ผ์ ์ฌ๋ถ
  'pitcher': True, #ํฌ์ ์ฌ๋ถ
  'shortName': 'Closer',
  'type': 'Pitcher'}, #ํฌ์ง์ ์ ํ. ํฌ์
```

- `positions` ๋ชฉ๋ก
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

์ฌํ์ review(๋น๋์คํ๋?)์ด ์ด๋ฃจ์ด์ง ๋ ๊ทธ ์ฌ์ ๋ค์ ๋ชจ์๋์ ๋ชฉ๋ก.

- `reviewReasons` ๋ชฉ๋ก
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

์ผ๊ตฌ์ ๋ก์คํฐ์๋ ์ฌ๋ฌ ๋ฐฉ์์ด ์๋ค. ํ์ 40์ธ ๋ก์คํฐ๋ ์๊ณ , ํ ๊ฒฝ๊ธฐ์ ๋ก์คํฐ๋ ์๊ณ , ์ฝ์น์ง ๋ก์คํฐ๋ ์๋ค. ๊ทธ ๋ก์คํฐ ์ ํ๋ค์ ๋ชจ์๋์ ๋ชฉ๋ก์ด๋ค.

- `rosterTypes` ๋ชฉ๋ก
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

์ผ๊ตฌ ๊ฒฝ๊ธฐ์ ๊ด๋ จ๋ ๊ฐ์ข ํ์ฌ๋ค์ ์ ํ ๋ชฉ๋ก์ด๋ค.

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

์ผ๊ตฌ์ ํฌ๊ณ ์๊ณ  ์ค์ํ๊ณ  ์ก๋คํ ๋ชจ๋  ์ํฉ๋ค์ ๋ชจ์๋์ ๋ชฉ๋ก.

```python
{'batting': True,
  'code': 'd', 
  'description': 'Day Games', #๋ฎ๊ฒฝ๊ธฐ
  'fielding': True,
  'navigationMenu': 'Game', #๊ทธ๋ฃน. game
  'pitching': True,
  'sortOrder': 3, #์ํฉ ์๋ฒ
  'team': True},
```

- `situationCodes` ๋ชฉ๋ก
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

๊ฒฝ๊ธฐ์ ๋ ์จ ์ ํ ๋ชฉ๋ก์ด๋ค.

- `sky` ๋ชฉ๋ก
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

์์ํ์ ๊ธฐ์ค๋ค์ ๋ชจ์๋์ ์ ํ. ์ ๋ฐ๊ธฐ ์์ํ์ ํ๋ฐ๊ธฐ ์์ํ๊ฐ ๋ค๋ฅด๋ฏ, ๊ธฐ์ค์ด ๋ญ๋์ ๋ฐ๋ผ ์์ํ๋ ๋ค๋ฅด๊ธฐ ๋ง๋ จ์ด๋ค.

- `standingsTypes` ๋ชฉ๋ก
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

๊ฐ ์คํฏ์ด ์ํ๋ ๊ทธ๋ฃน์ ๋งํ๋ค. ์๋ฅผ ๋ค์ด `assist`(๋ณด์ด)์ `fileding`๊ณผ `catching` ๊ทธ๋ฃน์ ์ํ๊ณ , `qualityStarts`๋ `pitching` ๊ทธ๋ฃน์ ์ํ๋ค.

- `statGroups` ๋ชฉ๋ก
    
    `['hitting']
    ['pitching']
    ['fielding']
    ['catching']
    ['running']
    ['game']
    ['team']
    ['streak']`
    

### 2-23. `statTypes`

- `statTypes`์ ๋ด์ฅ๋ ๋ชฉ๋ก
    
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

๋ฐ๋์ ๋ฐฉํฅ ์ ํ ๋ชฉ๋ก์ด๋ค.

- `windDirection` ๋ชฉ๋ก
    
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
