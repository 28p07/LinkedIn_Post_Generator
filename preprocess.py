import json
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm import llm

def extract_metadata(post):
    template = ''' 
    You are given a LinkedIn Post. You need to extract number of lines,langugae and tags form the post
    1. Return a valid JSON. No preamble.
    2. JSON object should exactly have three keys: line_count,language,tags
    3. tags should be in the form of array. extract maximum five tags
    4. tags should be unified and should fulfill the requirements below
       Example 1: "Jobseekers", "Job Hunting" can be all merged into a single tag "Job Search". 
       Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation"
       Example 3: "Personal Growth", "Personal Development", "Self Improvement" can be mapped to "Self Improvement"
       Example 4: "Scam Alert", "Job Scam" etc. can be mapped to "Scams"
    5. Each tag should be follow title case convention. example: "Motivation", "Job Search"
    6. Language should be English or Hinglish(hindi+english)

    Here is the actual post you need to perform the task:
    {post}
    '''
    prompt = PromptTemplate.from_template(template=template)
    chain = prompt|llm
    response = chain.invoke({'post':post})
    parser = JsonOutputParser()
    res = parser.parse(response.content)

    return res

def process_posts(raw_file_path,processed_file_path ="data/processed_posts.json"):
    processed_post = []
    with open(raw_file_path,"r",encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            processed_post.append(post_with_metadata)
    
    with open(processed_file_path,"w",encoding='utf-8') as file:
        json.dump(processed_post,file,indent=4)

if __name__ == "__main__":
    process_posts("data/raw_posts.json","data/processed_posts.json")