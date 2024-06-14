import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "<your key>"



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