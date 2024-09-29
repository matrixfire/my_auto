# # Install necessary packages
# pip install PocketSphinx
# pip install SpeechRecognition


# pyttsx3 3


import pyttsx3 as pyttsx

def save_text_to_audio(text, output_file):
    # Initialize the engine
    engine = pyttsx.init()
    # Say the text
    engine.say(text)
    # Save the audio to a file
    engine.save_to_file(text, output_file)
    # Run and wait for the speech to finish
    engine.runAndWait()

# Example usage:
text_to_say = "你好，你在干什么。"  # Text to convert to speech
output_audio_file = "output_audio.wav"  # Output file path

# save_text_to_audio(text_to_say, output_audio_file)







import speech_recognition as sr

def recognize_speech(audio_file):
    # Initialize the recognizer
    r = sr.Recognizer()

    # Process the audio file
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

        # Recognize speech using PocketSphinx
        try:
            # recognized_text = r.recognize_sphinx(audio, language="zh-CN")
            recognized_text = r.recognize_sphinx(audio)
            # recognized_text = r.recognize_sphinx(audio) # For default language
            return recognized_text
        except Exception as e:
            print(e)
            return None



from moviepy.editor import VideoFileClip
import os

def convert_video_to_wav(video_file, output_audio_file):
    # Load the video clip
    video_clip = VideoFileClip(video_file)

    # Extract the audio
    audio_clip = video_clip.audio

    # Write the audio to a WAV file
    audio_clip.write_audiofile(output_audio_file)

    # Close the video clip
    video_clip.close()

# Example usage:
video_file = r"C:\Users\Administrator\Desktop\very_temp\ttt.mp4"  # Replace this with the path to your video file
output_audio_file = "output_audio.wav"

# convert_video_to_wav(video_file, output_audio_file)



# Example usage:
output_audio_file = "output_audio.wav"  # Replace this with the path to your audio file
recognized_text = recognize_speech(output_audio_file)
if recognized_text:
    print("文本内容:", recognized_text)
