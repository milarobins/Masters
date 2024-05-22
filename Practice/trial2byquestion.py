import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv('API_KEY')
client = OpenAI(api_key=API_KEY)

questions = [
    "Can you explain the concept of probability in everyday life?",
    "How does the concept of exponential growth differ from linear growth? Can you provide an example of each from real-world phenomena?",
    "Considering the concept of exponential growth, how would you explain the importance of early intervention in controlling the spread of a contagious disease?",
    "Given the previous question, can you sketch a graph to illustrate the exponential spread of a disease over time? Please label your axes, starting with Patient X being infected at time t=0. Assume that the number of infected individuals doubles at each subsequent time interval. Indicate this growth factor of 2 on your graph.",
    "Can you discuss how different strategies might alter the shape of this curve?"
]

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
    transcript = """Paste or input the transcript here."""
    all_responses = []
    total_score = 0

    # Iterate over each question and make an API call, except for Question 4
    for i, question in enumerate(questions, start=1):
        if i == 4:
            prompt = f"Mark this response to question {i}:\n\nTranscript:\n{transcript}\n\nQuestion:\n{question}\n\nProvide commentary on the discussion surrounding Question 4 but leave the score blank for the professor's evaluation."
        else:
            prompt = f"Mark this response to question {i}:\n\nTranscript:\n{transcript}\n\nQuestion:\n{question}\n\nProvide a score and justify your reasoning."
        response = call_gpt4_api(prompt)
        if i != 4:
            score = int(input(f"Enter the score for question {i}: "))  # Assuming scoring is done manually for non-automated parts
            total_score += score
            all_responses.append(f"Response and Score for Question {i}:\n{response}\nScore: {score}")
        else:
            all_responses.append(f"Commentary for Question {i} (No Score):\n{response}")

    # Collect personalized feedback
    feedback_prompt = "Provide a short paragraph of personalized feedback to the participant based on the responses marked."
    feedback_response = call_gpt4_api(feedback_prompt)
    all_responses.append(f"Personalized Feedback:\n{feedback_response}")

    # Report the student's total score
    all_responses.append(f"Total Score (excluding Question 4): {total_score} out of 16")

    # Output all responses to console or write them to a file
    for response in all_responses:
        print(response)

if __name__ == "__main__":
    main()
