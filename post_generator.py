from llm import llm
from fewshots import fewshot
fs = fewshot()

def get_length(length):
    if length=="Short":
        return "5 to 10 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"

def generate_prompt(tag,length,language):
    length_Str = get_length(length)
    prompt = f'''
    Generate a linkedin post using the informatio below. No preamble.
    1. Topic : {tag}
    2. Length : {length_Str}
    3. Language : {language}
    If the language is Hinglish it means hindi and english mixed but the script in which it is written is English
    '''
    examples = fs.get_final_post(length,language,tag)

    if len(examples)>=0:
        prompt += "4. You can take these posts as examples for better understanding"
        for i,post in enumerate(examples):
            text = post['text']
            prompt += f"\n\n Example{i} \n {text}"

    return prompt

def generate_post(tag,length,language):
    prompt = generate_prompt(tag,length,language)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    res = generate_post("Short","English","Job Search")
    print(res)
