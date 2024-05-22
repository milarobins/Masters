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

def write_response_to_file(response, base_output_path, student_name, run_number):
    # Append run_number to file name to avoid overwriting
    output_file_path = os.path.join(base_output_path, f"{student_name}_Feedback_Run_{run_number}.txt")
    with open(output_file_path, 'w') as file:
        file.write(response)

student_name = "Theo"  # Replace with student name

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
    transcript_file_path = '/Users/admin/Desktop/Masters/Trial 1 Oral Exams/Transcripts/Theo Transcript.docx'
    questions_file_path = '/Users/admin/Desktop/Masters/Trial 1 Oral Exams/Questions/Theo questions.docx'
    base_output_path = '/Users/admin/Desktop/Masters/Trial 1 Oral Exams/Results/Theo'

    transcript = read_file(transcript_file_path)
    questions = read_file(questions_file_path)

    for i in range(10):  # Loop to run the script 10 times
        prompt = f"""Mark this \n{transcript}\n step by step:

Step 1: Mark the responses to each of the five \n{questions}\n and briefly justify your reasoning. Each question is equally weighted and worth 4 marks.
Question 4 requires separate answer uploads. You should provide commentary on the discussion surrounding Question 4 but 
leave the score blank for the professor's evaluation.
Step 2: Leave brief personalised feedback for the student. Include specific quotations from the transcript that highlight both strengths and 
weaknesses in their performance, such as when their answers were creative, confident, or professional, but also if they were ambiguous or unclear. Comment
on the tone and vibe of the exam if relevant.
Step 3: Report the student's total score."""
        
        response = call_gpt4_api(prompt)
        write_response_to_file(response, base_output_path, student_name, i+1)

if __name__ == "__main__":
    main()