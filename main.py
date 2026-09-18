import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.6-flash"


def load_prompt():

    with open(
        "prompts/master_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def generate_documentation(transcript, document_type):

    master_prompt = load_prompt()

    final_prompt = master_prompt.replace(
        "{{DOCUMENT_TYPE}}",
        document_type
    )

    final_prompt = final_prompt.replace(
        "{{TRANSCRIPT}}",
        transcript
    )

    response = client.interactions.create(
        model=MODEL,
        input=final_prompt
    )

    return response.output_text