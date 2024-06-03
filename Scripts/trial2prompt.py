import os
import re
from dotenv import load_dotenv
from openai import OpenAI
import docx
load_dotenv()
API_KEY = os.getenv('API_KEY')

client = OpenAI(api_key=API_KEY)

# Reads file and handles word documents
def read_file(file_path):
    if file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        with open(file_path, 'r') as file:
            return file.read()

# Writes response to file
def write_response_to_file(response, base_output_path, student_name):
    output_file_path = os.path.join(base_output_path, f"{student_name}_Feedback")
    with open(output_file_path, 'w') as file:
        file.write(response)

student_name = "Krish3"  # Replace with student name

# Call GPT-4 API
def call_gpt4_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are marking an oral exam transcript and providing personalised feedback to the participants"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content

# Main function
def main():
    transcript_file_path = '/Users/admin/Desktop/Masters/Trial 2 Oral Exams/Krish Transcript unedited.docx'  # Transcript file path
    questions_file_path = '/Users/admin/Desktop/Masters/Trial 2 Oral Exams/Questions.docx'  # Question file path
    base_output_path = '/Users/admin/Desktop/Masters/Trial 2 Oral Exams/Results/Unedited/' #Feedback file path

    transcript = read_file(transcript_file_path)
    questions = read_file(questions_file_path)
    
    prompt = f"""Mark this \n{transcript}\n step by step:

Step 1: Identify the responses to each of the five \n{questions}\n. Each question is equally weighted and worth 4 marks.
Question 4 requires separate answer uploads. You should provide commentary on the discussion surrounding Question 4 but 
leave the score blank for the professor's evaluation.
Step 2: Score all of the questions and justify your reasoning.
Step 3: Provide a short paragraph of personalised feedback to the participant at the end.
Step 4: Report the student's total score."""
    
    response = call_gpt4_api(prompt)
    write_response_to_file(response, base_output_path, student_name)

if __name__ == "__main__":
    main()