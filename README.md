# EducAItion: Can GPT help revive an underutilised art by effectively marking and providing feedback on oral examinations in STEM?

## Introduction
Hello and welcome to the repository for my Final Year Master's Thesis in Design Engineering at Imperial College London. This repository contains files used throughout my research to test and mark various oral examination transcripts using the GPT-4 turbo-preview model.

## Abstract
With Large Language Models (LLMs) such as ChatGPT becoming widely available – and particularly popular amongst university students – current approaches to instruction are being questioned and assessments redesigned. Driving this are concerns with balancing authenticity and rigour while still teaching students to use these powerful technological tools, especially in STEM courses. Reviving the oral examination method can address the aforementioned concerns. This paper explores the use of the GPT-4 turbo-preview model (referred to as GPT for simplicity) via API and OpenAI’s web-based ChatGPT as an assessor for oral examinations in STEM.

The research is structured around four trials to:
1. Evaluate GPT’s accuracy and consistency when marking exam transcripts.
2. Compare its variance to that of humans.
3. Gauge student experience with the oral exam format.
4. Test its robustness against bad actors and transcript modifications.

The findings indicate that GPT can effectively mark transcripts with less variance compared to different human examiners and generate personalized feedback which participants find useful. However, GPT can be influenced by the language in transcripts, especially from professors. Tests show that modifications which emulate a “cruel professor” can significantly impact GPT’s marking (p=0.003). The quality of feedback also varies; the most constructive results from a transcript that has been pre-processed to remove over-enthusiastic phrases from the professor such as “perfect”, or “very very good”. Despite limitations due to non-verbal communication and native language considerations, this research indicates GPT’s potential as a consistent and efficient assessor for oral examinations in STEM.

## Repository Structure
The scripts in this repository are organized around four trials. Each subfolder contains the Python script to mark and provide feedback on oral examination transcripts. Due to privacy reasons, transcripts used in this research are not provided, but exam questions from trial II and III and instructions for uploading your own transcripts are included in each `.py` file.

### Trials Overview
- **Trial 1:** Based on an oral examination specific to Imperial College London students.
- **Trial 2:** Easily conducted oral examination with 5 STEM-related questions.
- **Trial 3:** Rigorous engineering maths-based oral examination designed for this research.
- **Trial 4:** Includes various tests and the pre-processing script recommended for transcript preparation before marking.

### Additional Files
- **Whisper Transcription:** For using a faster implementation of OpenAI's software, if your computer can handle it (mine didn't do so well with `.mp4` uploads >5min)

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/masters
   cd masters
