from tkinter import Tk, Label, Entry, Button, Text
from gpt_setting import create_completion, basic_condition
from chrome_setting import open_url_in_chrome

def link_from_response(response):
    if '**' in response: # 매개변수인 response에서 **이 있는지 찾음
        start_of_link = response.find('**') + 2 # **부터 시작하도록 즉 **은 포함시키지 않게 하도록 하기 위해 **의 길이를 더함.
        end_of_link = response.find('**', start_of_link) # start_of_link 이후의 **을 찾아 변수에 저장
        return response[start_of_link:end_of_link].strip() # strip은 불필요한 공백을 제거하기 위해 사용
    return None

def submit_query(entry, text_widget):
    user_input = entry.get() # Entry위젯에서 사용자의 input을 가져옴

    condition_text = basic_condition.condition_text # class에서 선언한 값을 가져옴

    messages = [ # GPT에게 보낼 list생성
        {"role": "user", "content": condition_text},
        {"role": "user", "content": user_input}
    ]

    completion = create_completion(messages)

    if completion:
        response_text = completion.choices[0].get("message", {}).get("content", "").strip()
        # Text 위젯에 응답을 설정
        text_widget.delete(1.0, 'end') #첫번째지점부터 끝지점 까지 내용 삭제
        text_widget.insert('end', response_text) # 끝지점에서부터 response_text까지 내용 삽입
        url = link_from_response(response_text)
        if url:
            open_url_in_chrome(url)

def on_enter(event, entry, text_widget): # 엔터키 입력시 submit_query메서드 호출
    submit_query(entry, text_widget)

def start_gui():
    root = Tk()
    root.title("Chat with GPT")
    root.geometry("600x400")  # 화면 설정
    root.resizable(True, True)  # 크기 조절 가능

    Label(root, text="User:").pack()
    entry = Entry(root, width=50)
    entry.pack()
    entry.bind("<Return>", lambda event: on_enter(event, entry, response_label))  # Enter 키로도 입력

    response_label = Text(root, height=15, wrap='word')
    response_label.pack()

    Button(root, text="Submit", command=lambda: submit_query(entry, response_label)).pack()
    root.mainloop() # 이벤트 루프 시작. 생성된 GUI로 user가 상호작용가능
