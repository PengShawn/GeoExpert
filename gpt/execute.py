import json
from backend import call_chat_gpt
import geometry_theorem_prompt as prompt
import re

def data_call_gpt(model, start_index=0, end_index=0):
    
    for i in range(start_index, end_index):
        pid = str(i)
        result = {}
        result[pid] = {}
        text_logics = text_logic_tables[pid]["text_logic_forms"]
        diagram_logics = diagram_logic_tables[pid]["diagram_logic_forms"]
        problem_text = ",".join(diagram_logics + text_logics).replace('\n', '').replace('\r', '') + "."
        messages = [
            {"role": "system", "content": prompt.MATH_CHAT_BETA_SYSTEM_MESSAGE},
            {"role": "user", "content": prompt.MATH_CHAT_BETA_PROMPT + problem_text}
        ]
        try:
            ans = call_chat_gpt(messages, model)
        except Exception as e:
            print(e)
            ans = ''
        # 匹配定理列表
        match = re.search(r'Theorems: \[(\d+(?:,\s*\d+)*)\]', ans)
        if match:
            theorem_list = match.group(1).split(',')
            theorem_list = [int(x) for x in theorem_list]
        else:
            theorem_list = []
        print(theorem_list)
        result[pid]["problem_text"] = problem_text
        result[pid]["answer"] = ans
        result[pid]["theorem_list"] = theorem_list
        json.dump(result, open(OUTPUT_PATH + pid + ".json", "w"), indent = 2)

if __name__ == '__main__':
    TEXT_INPUT_PATH = "../data/geometry3k/logic_forms/text_logic_forms_annot_dissolved.json"  # human annotated
    DIAGRAM_INPUT_PATH = "../data/geometry3k/logic_forms/diagram_logic_forms_annot.json" 
    OUTPUT_PATH = "results/gpt3.5/"
    model = "gpt-3.5-turbo"
    # Read data
    with open(TEXT_INPUT_PATH, "r") as f1:
        text_logic_tables = json.load(f1)
    with open(DIAGRAM_INPUT_PATH, "r") as f2:
        diagram_logic_tables = json.load(f2)

    THEOREM_LENGTH = 23
    QUESTION_LENGTH = 3002
    data_call_gpt(model, start_index=2400,end_index = QUESTION_LENGTH)

    