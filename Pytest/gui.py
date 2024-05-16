from tkinter import Tk, Label, Entry, Button, Text
from gpt_setting import create_completion, basic_condition
from chrome_setting import open_url_in_chrome

def link_from_response(response):
    if '**' in response:
        start_of_link = response.find('**') + 2
        end_of_link = response.find('**', start_of_link)
        return response[start_of_link:end_of_link].strip()
    return None

def submit_query(entry, text_widget):
    user_input = entry.get()

    condition_text = basic_condition.condition_text

    messages = [
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

def on_enter(event, entry, text_widget):
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
    root.mainloop()
