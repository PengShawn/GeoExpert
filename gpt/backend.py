import time
import requests
import json
import geometry_theorem_prompt as prompt

api_key = ""
api_base = ""
# GPT API

def call_chat_gpt(messages, model='gpt-4-1106-preview', stop=None, temperature=0., top_p=1.0, max_tokens=2096):
    wait = 1
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        'model': model,
        'max_tokens': max_tokens,
        'stop': stop,
        'messages': messages,
        'temperature': temperature,
        'top_p': top_p,
        'n': 1
    }

    while True:
        try:
            response = requests.post(
                api_base, headers=headers, data=json.dumps(payload))
            # Raises an HTTPError if the HTTP request returned an unsuccessful status code
            response.raise_for_status()

            ans = response.json()
            # print(ans)
            return ans['choices'][0]['message']['content']
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                time.sleep(min(wait, 60))
                wait *= 2
            else:
                raise
    raise RuntimeError('Failed to call chat gpt')


# ques = """Equals(LengthOf(Line(T, R)), x+21), Equals(MeasureOf(Angle(T, R, S)), 4y-10), Equals(MeasureOf(Angle(Z, X, Y)), 3y+5), Equals(LengthOf(Line(Z, X)), 2x-14), Congruent(Triangle(R,S,T),Triangle(X,Y,Z)), Find(y)."""

# messages = [
#     {"role": "system", "content": prompt.MATH_CHAT_BETA_SYSTEM_MESSAGE},
#     {"role": "user", "content": prompt.MATH_CHAT_BETA_PROMPT + ques}
# ]


# print(call_chat_gpt(messages))