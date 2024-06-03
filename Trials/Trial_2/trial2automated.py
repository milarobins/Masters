import os
import docx
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv('API_KEY')
client = OpenAI(api_key=API_KEY)

def read_file(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to write results to file each run
def write_response_to_file(response, base_output_path, student_name, run_number):
    output_file_path = os.path.join(base_output_path, f"{student_name}_Feedback_Run_{run_number}.txt")
    with open(output_file_path, 'w') as file:
        file.write(response)

# Main function
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

def main():
    transcript_folder_path = '' # Insert path to transcript
    questions_file_path = '' # Insert path to exam questions
    base_output_path = '' # Insert path for results to be stored

    questions = read_file(questions_file_path)

# Function runs for each document in a folder named Transcript
    for file_name in os.listdir(transcript_folder_path):
        if file_name.endswith('.docx') and 'Transcript' in file_name:
            student_name = file_name.split(' Transcript')[0]
            transcript_file_path = os.path.join(transcript_folder_path, file_name)
            transcript = read_file(transcript_file_path)

            for run_number in range(1, 4):
                prompt = f"""Mark this \n{transcript}\n step by step:
    
    Step 1: Identify the responses to each of the five \n{questions}\n. Each question is equally weighted and worth 4 marks.
    Question 4 requires separate answer uploads. You should provide commentary on the discussion surrounding Question 4 but 
    leave the score blank for the professor's evaluation.
    Step 2: Score all of the questions and justify your reasoning.
    Step 3: Provide a short paragraph of personalised feedback to the participant at the end.
    Step 4: Report the student's total score."""
                
                response = call_gpt4_api(prompt)
                write_response_to_file(response, base_output_path, student_name, run_number)

if __name__ == "__main__":
    main()