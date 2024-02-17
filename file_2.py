from openai import OpenAI
from dotenv import load_dotenv
import os
import time

class text_corrector:
    def __init__(self):
        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key = OPENAI_API_KEY)
    def generate_description(self, input_txt):
        print('mensaje en raw:')
        print(input_txt)
        messages = [
            {"role": "system",
            "content": """ You are a text corrector. 
                            It is strictly forbidden to remove or add any words under any circumstances.
                            Correct only the spelling and punctuation errors.
                            Return only the corrected text as output, including the necessary line breaks. The output must be in Spanish."""},
        ]
        messages.append({"role": "user", "content": f"{input_txt}"})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
        reply = completion.choices[0].message.content
        return reply
