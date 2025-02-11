## 프로젝트명 : 그 시절 개성 
프로젝트 개요 : OOTD를 기록하고, 옷을 등록해 한 눈에 보고 매치해 볼 수 있는 옷장을 제공


#### playList 기능 사용하기
- 터미널에 입력해서 모듈을 설치해야 합니다
  
`pip install python-vlc`
`pip install pafy`
`pip install youtube-dl==2020.12.2`

- vlc 플레이어 다운 받기 (다운이 안되어있으면 오류 나옴)
- playList 페이지의 경우 영상을 youtube url을 입력하는 식으로 작동함 -> EX)https://www.youtube.com/watch?v=5sfABTrQnpY
  
#### 옷장 기능 사용하기 

- closet_top , closet_bot folder에 등록하고자하는 사진을 미리 넣어놓고  해당 사진 file 이름으로 등록하기 
- 선택을 누르고 사진을 누르면 사진이 다이얼로그에 들어가는 방식 

#### OOTD 기능 사용하기

- 계절 별 folder에 사진을 미리 넣어놓고 해당 사진 file 이름으로 등록하기
  




식의 유튜브 주소를 넣어야함 

-변수명 쉽게 짓지 말것 
-pafy는 어쩔 수 없이 속도 오류가 생김 (크롤링 속도 느리므로)
-스케쥴 페이지는 차후 구현 일정에 관한 부분 필요성 못느낌 + 시간 부족 
