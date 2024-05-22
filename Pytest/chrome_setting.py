import subprocess as sp # 새로운 프로세스 실행 및 관리를 위한 내부 모듈
import winreg as wr # 윈도우 레지스트리 편집 및 엑세스를 위한 내부 모듈

def get_chrome_path():
    try:
        reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe" # 크롬실행파일의 레지스트리 경로 저장
        with wr.OpenKey(wr.HKEY_LOCAL_MACHINE, reg_path) as key: # SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe 경로를 사용하여 Chrome의 실행 파일 경로를 찾음
            return wr.QueryValue(key, None) # 레지스트리 기본값 반환 즉 크롬의 실행파일을 반환
    except Exception as e:
        print(f"Error finding Chrome path: {e}") # 크롬실행파일의 위치를 못 찾을경우의 예외처리
        return None

def open_url_in_chrome(url):
    chrome_path = get_chrome_path()
    if not chrome_path:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" # 만약 에러가 나서 return값이 None일경우 크롬 실행 파일의 위치 지정
    sp.Popen([chrome_path, url], shell=True) # Chrome 실행 파일과 URL을 포함한 새로운 프로세스를 시작
                                             # shell = True옵션을 사용해 쉘을 통해 명령 실행