import openai as oi # gpt를 사용하기 위한 외부모듈 import

oi.api_key = "" # api_key 입력

def create_completion(messages): # 매개변수 messages를 받는 메서드 생성
    try:
        return oi.ChatCompletion.create( # 채팅 응답 생성, 생성시 반환함
            model="gpt-3.5-turbo", # 사용 모델
            messages=messages # 매개변수
        )
    except oi.OpenAIError as e: # API호출시 에러발생
        print("GPT ERROR: ", str(e))
        return None

class basic_condition: # 클래스 정의
    condition_text = ( # gpt로 부터 URL 제공시 조건 설정
        "If the user asks for a URL, provide the URL in this format: **URL**. "
        "If the user asks to open a URL, provide the URL in this format: **URL**. "
        "Here's an example: **www.openai.com**. "
        "URL is website adress. "
        "If the user asks to open a URL in Chrome, provide a direct URL."
    )