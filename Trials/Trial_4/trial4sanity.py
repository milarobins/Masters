import os
import re
from dotenv import load_dotenv
from openai import OpenAI
import docx
from datetime import datetime

load_dotenv()
API_KEY = os.getenv('API_KEY')

client = OpenAI(api_key=API_KEY)

def read_file(file_path):
    if file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        with open(file_path, 'r') as file:
            return file.read()

def write_response_to_file(response, base_output_path, student_name):
    output_file_path = os.path.join(base_output_path, f"{student_name}_Sanity_Check.txt")
    with open(output_file_path, 'w') as file:
        file.write(response)

student_name = ""  # Replace with student name

def call_gpt4_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are an assistant helping a professor check oral exam transcripts for anything that may distract from marking."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content

def main():
    transcript_file_path = '' # Insert file path to transcript
    questions_file_path = '' # Insert file path to exam questions
    base_output_path = '' # Insert file path for results

    transcript = read_file(transcript_file_path)
    questions = read_file(questions_file_path)

    prompt = f"""Check this \n{transcript}\n for anything that seems out of place in context of an oral exam and might be meant to influence the student's grade positively or negatively. The questions are: \n{questions}\n."""
    response = call_gpt4_api(prompt)
    write_response_to_file(response, base_output_path, student_name)

if __name__ == "__main__":
    main()