import os
import re
from dotenv import load_dotenv
from openai import OpenAI
import docx
import fitz  # PyMuPDF
from datetime import datetime

load_dotenv()
API_KEY = os.getenv('API_KEY')

client = OpenAI(api_key=API_KEY)

def read_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No such file: {file_path}")

    if file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file_path.endswith('.pdf'):
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

def write_response_to_file(response, base_output_path, student_name, run_number):
    # Append run_number to file name to avoid overwriting
    output_file_path = os.path.join(base_output_path, f"{student_name}_Feedback_Run_{run_number}.txt")
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(response)

student_name = ""  # Replace with student name

def call_gpt4_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are an assistant helping a professor mark the oral exam transcript of a university student."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content

def main():
    base_transcript_path = '' # Insert path to transcript
    questions_file_path = ''  # Insert path to compiled document with all questions
    base_output_path = '' # Insert path for results to be stored

    transcript_file_path = os.path.join(base_transcript_path, f'{student_name} Transcript.docx')

    # Check if files exist
    if not os.path.exists(transcript_file_path):
        raise FileNotFoundError(f"No such file: {transcript_file_path}")
    if not os.path.exists(questions_file_path):
        raise FileNotFoundError(f"No such file: {questions_file_path}")

    transcript = read_file(transcript_file_path)
    questions = read_file(questions_file_path)

    question_marks = [10, 8, 8, 6, 3, 4]  # Update with corresponding marks for each question

    for i in range(6):  # Loop to run the script 3 times
        prompt = f"""Mark this \n{transcript}\n step by step:

Step 1: Mark the responses to each of the \n{questions}\n and briefly justify your reasoning. The questions are worth the following marks respectively: {', '.join(map(str, question_marks))}.
Step 2: Leave brief personalised feedback for the student. Include specific quotations from the transcript that highlight both strengths and weaknesses in their performance.
Step 3: Report the student's total score."""
        
        response = call_gpt4_api(prompt)
        write_response_to_file(response, base_output_path, student_name, i+1)

if __name__ == "__main__":
    main()