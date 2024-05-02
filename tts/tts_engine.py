import os
import boto3
from config import settings

# Ensure the audio directory exists
if not os.path.exists('../audio'):
    os.makedirs('../audio')

def initialize_tts_client():
    return boto3.client(
        'polly',
        aws_access_key_id=settings['aws']['access_key_id'],
        aws_secret_access_key=settings['aws']['secret_access_key'],
        region_name=settings['aws']['region_name']
    )

def text_to_audiostream(text, voice='Salli', polly_client=None):
    if polly_client is None:
        polly_client = initialize_tts_client()
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice
    )
    return response['AudioStream'].read()

def text_to_file(text, voice='Salli', path=None, polly_client=None):
    if polly_client is None:
        polly_client = initialize_tts_client()
    if path is None:
        path = os.path.join("..","audio")
    response = polly_client.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId=voice)
    audio_path = os.path.join(path,f"{voice}_{hash(text)}.mp3")
    with open(audio_path, 'wb') as file:
        file.write(response['AudioStream'].read())
    return audio_path