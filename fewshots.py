import json
import pandas as pd

class fewshot:
    def __init__(self,file_path = "data\processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)
    
    def load_posts(self,file_path):
        with open(file_path,encoding='utf-8') as f:
            posts = json.load(f)
            df = pd.json_normalize(posts)
            df['length'] = df['line_count'].apply(self.post_len)
            all_tags = df['tags'].apply(lambda x:x).sum()
            self.unique_tags = list(set(all_tags))
            self.df = df
        
    def post_len(self,line_count):
        if line_count<5:
            return "Short"
        elif line_count>=5 and line_count<=10:
            return "Medium"
        else:
            return "Long"
    
    def get_tags(self):
        return self.unique_tags
    
    def get_final_post(self,length,language,tag):
        df_final = self.df[
            (self.df['language'] == language)&
            (self.df['length']==length)&
            (self.df['tags'].apply(lambda tags:tag in tags))
        ]

        return df_final.to_dict(orient="records")
    
if __name__=="__main__":
    fs = fewshot()
    post = fs.get_final_post("Short","English","Job Search")
    print(post)
        