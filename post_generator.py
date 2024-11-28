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

def generate_prompt(tag,length,language,purpose,audience,domain):
    length_str = get_length(length)
    prompt = f'''
    Generate a linkedin post using the informatio below. No preamble.
    1. Topic : {tag}
    2. Length : {length_str}
    3. Language : {language}
    4. Purpose : {purpose}
    5. Audience : {audience}
    6. Domain : {domain}
    If the language is Hinglish it means hindi and english mixed but the script in which it is written is English
    '''
    examples = fs.get_final_post(length,language,tag,purpose,audience,domain)

    if len(examples)>=0:
        prompt += "4. You can take these posts as examples for better understanding"
        for i,post in enumerate(examples):
            text = post['text']
            prompt += f"\n\n Example{i} \n {text}"

    return prompt

def generate_post(tag,length,language,purpose,audience,domain):
    prompt = generate_prompt(tag,length,language,purpose,audience,domain)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    res = generate_post("Short","English","Job Search")
    print(res)
