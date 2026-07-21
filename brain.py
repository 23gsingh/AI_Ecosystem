from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def think(task):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=task
    )

    print(response.output_text)
