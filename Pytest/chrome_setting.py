import subprocess as sp
import winreg as wr

def get_chrome_path():
    try:
        reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
        with wr.OpenKey(wr.HKEY_LOCAL_MACHINE, reg_path) as key:
            return wr.QueryValue(key, None)
    except Exception as e:
        print(f"Error finding Chrome path: {e}")
        return None

def open_url_in_chrome(url):
    chrome_path = get_chrome_path()
    if not chrome_path:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    sp.Popen([chrome_path, url], shell=True)