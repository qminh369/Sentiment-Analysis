import openai
import pandas as pd

model = 'text-davinci-003'
with open('B:\\Đồ án I\\Project I\\ChatGPT labelling\\apikey.txt', 'r') as f:
    openai.api_key = f.readline()
    
question = 'Xác định các khía cạnh, đối tượng cho từng câu bằng cách xác định các từ khóa liên quan về chủ đề sách (nội dung, chất lượng, đóng gói, giao hàng, dịch vụ, giá cả), đưa ra tối đa 3 khía cạnh; Đưa ra một trong ba sắc thái: positive, negative, neutral cho từng khía cạnh đó'

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
        max_tokens = 1024,
        n = 1,
        temperature = 0.5,
    )
    
    return response.choices[0].text

with open('B:\\Đồ án I\\Project I\\ChatGPT labelling\\aspect\\label_aspect.txt', 'w', encoding = 'utf-8') as file:
    for i in range(0, 10, 5):
        sentiment = label_sentiment(comments[i] + comments[i+1] + comments[i+2] + comments[i+3] + comments[i+4])
        labeled_data.append(sentiment)
        file.write(sentiment)
    print(labeled_data)




            
    
