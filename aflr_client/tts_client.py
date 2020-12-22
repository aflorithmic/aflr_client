import boto3
import websockets
import asyncio


class AFLRClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.socket = None
        self.loop = self.get_set_event_loop()
        self.latest_url = None

    async def get_speech_output(self, ssml, voice):
        try:
            async with websockets.connect(
                "wss://tts.aflr.io/", extra_headers=[("x-api-key", self.api_key)]
            ) as websocket:
                await websocket.send(
                    '{"text": "' + ssml + '", "voice": "' + voice + '"}'
                )
                greeting = await websocket.recv()
                url = await websocket.recv()
                self.latest_url = url
                return
        except:
            return "Invalid API Key"

    def synthesize_speech(self, ssml, voice):
        self.loop.run_until_complete(self.get_speech_output(ssml, voice))
        return self.latest_url if self.latest_url != None else "Invalid API Key"

    def get_set_event_loop(self):
        try:
            return asyncio.get_event_loop()
        except RuntimeError as e:
            if e.args[0].startswith("There is no current event loop"):
                asyncio.set_event_loop(asyncio.new_event_loop())
                return asyncio.get_event_loop()
            raise e