import boto3
from config import settings

def initialize_tts_client():
    return boto3.client(
        'polly',
        aws_access_key_id=settings['aws']['access_key_id'],
        aws_secret_access_key=settings['aws']['secret_access_key'],
        region_name=settings['aws']['region_name']
    )

def generate_speech(text, voice='Amy'):
    polly_client = initialize_tts_client()
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice
    )
    return response['AudioStream'].read()
