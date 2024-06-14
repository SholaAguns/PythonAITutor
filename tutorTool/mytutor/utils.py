import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "sk-proj-dL6yIdQ2XJWq9xqo6RYzT3BlbkFJfMBKbzGhTptZcVssxNt4"
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-proj-dL6yIdQ2XJWq9xqo6RYzT3BlbkFJfMBKbzGhTptZcVssxNt4")

# def get_gpt_response(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # or "gpt-4" if you have access
#         #model="gpt-4",  # or "gpt-4" if you have access
#         messages=[
#             {"role": "system", "content": "You are a tutor."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=200,
#         temperature=0.7,
#     )
#     return response.choices[0].message['content'].strip()

def get_gpt_response(prompt):
    client = OpenAI(
        api_key = os.getenv("OPENAI_API_KEY"),
    )

    response = client.chat.completions.create(
      model = "gpt-3.5-turbo",
      messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
      ]
    )

    return response.choices[0].message.content.strip()