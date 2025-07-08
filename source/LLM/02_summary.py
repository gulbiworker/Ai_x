# ctrl+shift+p => 인터픠터 서낵
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# 웹 예제
def askGpt(prompt):
    "gpt에게 prompt여청 결과 반환"
    load_dotenv
    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-4.1-nano",
    message=[{"role":"user", "content":"당신은 텍스트를 한국어 요약하는 전문 어시스턴스입니다"},
            {"role":'user','content':prompt}])
    return response.choices[0].message.content

# 기능구현
def main():
    st.header("요약 프로그램")
    st.markdown("---")
    text = st.text_area("요약할 글을 입력하세요")
    if st.button("요약"):
        prompt = f"""your task is to summarize the text sentences in korean language. summarize in 2 lines. use the format of a bullet point.
                    text : {text}"""
        result = askGpt(prompt=prompt)
        st.info(result)

if __name__ == "__main__":
    main()