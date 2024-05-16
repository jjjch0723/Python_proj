# Python_proj

## 사용 라이브러리 및 모듈
1.  OPENAI 0.28.0ver(GPT와의 connection을 위해 사용)
2.  tkinter(파이썬의 내부 모듈)
3.  winreg(파이썬의 내부 모듈)
4.  subprocess(파이썬의 내부 모듈)
***
## 파일 및 메서드 설명
### chrome_setting.py
1.  gee_chrome_path()
  chrome.exe의 파일 위치를 찾는 메서드 입니다.
  조사해본 결과 chrome는 기본적으로 정해진 루트에 설치 되기때문에 상대경로를 사용하지않고 절대경로를 사용했습니다.
  
2.  opne_url_in_chrome()
  위 메서드로 크롬의 절대경로를 찾고, subprocess모듈을 사용하여 chrome을 실행 시킵니다.
***
### get_setting.py
1.  oi.api_key에 자신의 api_key를 입력하시면 됩니다.
2.  create_completion()
  try문에서 gpt와의 연결 및 gpt의 모델을 선택하고, gpt와의 통신에서 유저의 request는 json형태로 받기때문에 key값이 user의 value값에 request를     넣어줍니다.
  except문에서 에러 메세지를 나타내고 예외처리를 강화하기 위하여 return은 None 즉 null값을 반환하도록 합니다.
3. class basic_condition
   condition_text에 gpt에게 response를 줄 경우 response의 형태를 명확히 하기 위해 넣었습니다.
