import openai as oi

oi.api_key = ""

def create_completion(messages):
    try:
        return oi.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    except oi.OpenAIError as e:
        print("GPT ERROR: ", str(e))
        return None

class basic_condition:
    condition_text = (
        "If the user asks for a URL, provide the URL in this format: **URL**. "
        "If the user asks to open a URL, provide the URL in this format: **URL**. "
        "Here's an example: **www.openai.com**. "
        "URL is website adress. "
        "If the user asks to open a URL in Chrome, provide a direct URL."
    )