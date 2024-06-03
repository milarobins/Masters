**EducAItion**: _can GPT help revive an underutilised art by effectively marking and providing feedback on oral examinations in STEM?_

Hello and welcome to the repository for my Final Year Master's Thesis in Design Engineering at Imperial College London. Here are the files used throught my research to test and mark various oral examination transcripts using the GPT4-turbo-preview model. I include my abstract below to contextualise the project more, and then I will briefly outline the structure of this repository.

**Abstract**:
With Large Language Models (LLMs) such as ChatGPT becoming widely avail-
able – and particularly popular amongst university students – current approaches
to instruction are being questioned and assessments redesigned. Driving this are
concerns with balancing authenticity and rigour while still teaching students to use
these powerful technological tools, especially in STEM courses. Reviving the oral
examination method can address the aforementioned concerns and this paper ex-
plores the use of the GPT4-turbo-preview model (referred to as GPT for simplicity)
via API as well as OpenAI’s web-based ChatGPT as an assessor for oral examina-
tions in STEM. The research is structured around four trials to: evaluate GPT’s
accuracy and consistency when marking exam transcripts, compare its variance to
that of humans, gauge student experience with the oral exam format, and test its
robustness against bad actors and transcript modifications. The findings indicate
that GPT can effectively mark transcripts with less variance when compared with
different human examiners and generate personalised feedback which participants
find useful. While GPT shows promise, it can be influenced by the language in
transcripts, especially professor’s. Tests show that modifications which emulate a
“cruel professor” can significantly impact GPT’s marking (p=0.003). The quality
of feedback also varies; the most constructive results from a transcript that has
been pre-processed to remove over-enthusiastic phrases from the professor such as
“perfect”, or “very very good”. Complications due to non-verbal communication
between the student and examiner which GPT can’t access, and native language
considerations aside, this research indicates GPT’s potential as a consistent and ef-
ficient assessor for oral examinations in STEM

As outlined above, the scripts in this repository are organised around **four trials** and each subfolder here contains the Python script to mark and feedback an oral examination transcript. Due to privacy reasons, I am not able to provide the transcripts here for replication, but I have included the exam questions and clear instructions in each .py file where to upload your own transcripts.

Briefly, Trial 1 may be the least relevant, as it was based on an oral examination specific to Imperial College London. Trial 2 is an oral examination easily conducted, with 5 questions that are STEM related. Trial 3 is a more rigorous engineering maths based oral examination which I designed myself for this research. Finally, Trial 4 includes various tests as well as the pre-processing file which I recommend running transcripts through before asking GPT to mark. The Whisper Transcription file is there to use a faster implementation of OpenAI's software, if your computer can handle it.
