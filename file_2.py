from openai import OpenAI
import os


class TextCorrector:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    model = "gpt-3.5-turbo"
    temperature = 0

    def __init__(self):
        self.client = OpenAI(api_key=self.OPENAI_API_KEY)

    def generate_description(self, input_txt: str):
        assert isinstance(input_txt, str)

        print("mensaje en raw:")
        print(input_txt)
        messages = [
            {
                "role": "system",
                "content": """You are a text corrector. 
                            It is strictly forbidden to remove or add any words under any circumstances.
                            Correct only the spelling and punctuation errors.
                            Return only the corrected text as output, including the necessary line breaks. The output must be in Spanish.""",
            },
        ]
        messages.append({"role": "user", "content": f"{input_txt}"})
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
        )
        reply = completion.choices[0].message.content
        return reply
