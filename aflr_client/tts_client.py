import boto3
import requests
import urllib.parse
import urllib.request


class AFLRClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.availlable_voices = set_availlable_voices()

    def set_availlable_voices(self):
        return None

    def get_speech_output(self, ssml, voice):
        return None