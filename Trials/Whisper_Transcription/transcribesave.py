
# Code from GitHub
from faster_whisper import WhisperModel

model_size = "large-v3"

# Run on CPU with INT8 (change device to "cuda" if you have CUDA support)
model = WhisperModel(model_size, device="cpu", compute_type="int8")

# Transcribe the audio file
segments, info = model.transcribe("", beam_size=5) # Insert path for audio file

# Print and save the detected language
print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# Open a file to save the transcription
with open("/", "w") as file: # Insert path for transcript to be saved
    file.write("Detected language '%s' with probability %f\n\n" % (info.language, info.language_probability))
    
    for segment in segments:
        transcript_line = "[%.2fs -> %.2fs] %s\n" % (segment.start, segment.end, segment.text)
        print(transcript_line, end='')  # Print to console
        file.write(transcript_line)  # Write to file