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
        with open(file_path, 'r') as file:
            return file.read()

def write_response_to_file(response, base_output_path, student_name, run_number):
    # Append run_number to file name to avoid overwriting
    output_file_path = os.path.join(base_output_path, f"{student_name}_Feedback_Run_{run_number}.txt")
    with open(output_file_path, 'w') as file:
        file.write(response)

def call_gpt4_api(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant helping a professor mark the oral exam transcript of a university student."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content

def main():
    base_transcript_path = '/Users/admin/Desktop/Masters/Trial 3 Oral Exams/Transcripts'
    base_question_path = '/Users/admin/Desktop/Masters/Trial 3 Oral Exams/Questions'
    base_output_path = '/Users/admin/Desktop/Masters/Trial 3 Oral Exams/Results'

    student_name = "Chang"  # Replace with student name
    transcript_file_path = os.path.join(base_transcript_path, f'{student_name} Transcript.docx')
    transcript = read_file(transcript_file_path)

    question_files = [f'Question{i}.pdf' for i in range(1, 7)]
    question_marks = [10, 8, 8, 6, 3, 4]  # Corresponding marks for each question

    for run_number in range(3):  # Loop to run the script 3 times
        total_score = 0
        feedback = []

        for i, (question_file, marks) in enumerate(zip(question_files, question_marks), start=1):
            question_path = os.path.join(base_question_path, question_file)
            question = read_file(question_path)

            # Check if question file exists
            if not os.path.exists(question_path):
                raise FileNotFoundError(f"No such file: {question_path}")

            prompt = f"""
            Mark the student's response to this question from the transcript step by step:

            Question {i}: {question}

            Student's Transcript:
            {transcript}

            Step 1: Mark the response to the question and briefly justify your reasoning. The question is worth {marks} marks.
            Step 2: Provide brief personalized feedback for the student, including specific quotations from the transcript that highlight both strengths and weaknesses in their answer.

            """

            response = call_gpt4_api(prompt)
            feedback.append(response)

            # Extract score from response
            score_match = re.search(r'Total score for this question: (\d+)', response)
            if score_match:
                total_score += int(score_match.group(1))

        collated_feedback_text = "\n".join(feedback)
        final_feedback = f"{collated_feedback_text}\n\nTotal score for all questions: {total_score}/42"

        # Store the final feedback for the current run
        write_response_to_file(final_feedback, base_output_path, student_name, run_number + 1)

if __name__ == "__main__":
    main()
