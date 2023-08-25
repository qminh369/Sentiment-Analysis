import streamlit as st
import openai

st.title("Tích hợp ChatGPT vào bài toán phân loại cảm xúc")

# Cài đặt thông tin model
#model = 'gpt-3.5-turbo'
model = 'text-davinci-003'     
with open("B:\\Đồ án I\\Project I\\ChatGPT labelling\\apikey.txt","r") as f:
    openai.api_key = f.readline()

# Hàm để gọi đến OpenAPI / Phần ChatGPT
def get_response_from_chatgpt(user_question):
    response = openai.Completion.create(
        engine= model,
        prompt = user_question,
        max_tokens = 128, 
        n = 1,      
        temperature = 0.5      
    )

    response_text = response.choices[0].text        
    return response_text

def main():
    user_question = st.text_input("Nhập câu hỏi vào đây:")
    if st.button("Click"):
        response_text = get_response_from_chatgpt(user_question)
        return st.write(f"{response_text}")

main()