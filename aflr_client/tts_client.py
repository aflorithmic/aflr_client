import boto3
import websockets
import asyncio


class AFLRClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.socket = None
        self.loop = asyncio.get_event_loop()
        self.latest_url = None

    async def get_speech_output(self, ssml, voice):
         async with websockets.connect(
            "wss://tts.aflr.io/", extra_headers=[("x-api-key", self.api_key)]
        ) as websocket:
            await websocket.send('{"text": "' + ssml + '", "voice": "'+ voice +'"}')
            greeting = await websocket.recv()
            url = await websocket.recv()
            self.latest_url = url
            return   
            
    def synthesize_speech(self, ssml, voice):
        self.loop.run_until_complete(self.get_speech_output(ssml, voice))
        return self.latest_url
