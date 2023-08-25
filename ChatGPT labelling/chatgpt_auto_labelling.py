import openai
import pandas as pd

# Cài đặt thông tin model
#model = 'gpt-3.5-turbo'
model = 'text-davinci-003'
with open('B:\\Đồ án I\\Project I\\ChatGPT labelling\\apikey1.txt', 'r') as f:
    openai.api_key = f.readline()
    
question = 'Hãy cho tôi biết các câu bình luận sau đây là tích cực, tiêu cực hay trung lập. Ứng với mỗi câu bình luận thì đưa ra câu trả lời là số thứ tự câu + một trong các từ sau: positive, negative, neutral '

data = pd.read_csv('B:\\Đồ án I\\Project I\\ChatGPT labelling\\data_main.csv')
unlabel_data = data['content']

comments = []
labeled_data = []
for i in range(len(data)):
    comments.append('Câu '+ str(i) + '.' + data['content'][i] + '. ')

def label_sentiment(comment):
    response = openai.Completion.create(
        engine = model,
        prompt = question + comment,
        max_tokens = 48,
        n = 1,
        temperature = 0.5,
    )
    
    return response.choices[0].text


with open('B:\\Đồ án I\\Project I\\ChatGPT labelling\\label.txt', 'w', encoding = 'utf-8') as file:
    for i in range(0, 10, 5):
        sentiment = label_sentiment(comments[i] + comments[i+1] + comments[i+2] + comments[i+3] + comments[i+4])
        labeled_data.append(sentiment)
        file.write(sentiment)
    print(labeled_data)