# 呼叫 OpenAI / Mistral API
import os
import openai
openai.api_key = os.getenv("LLM_API_KEY")

def call_llm(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
