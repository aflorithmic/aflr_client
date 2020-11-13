from aflr_client import AFLRClient

client = AFLRClient("YOUR_API_KEY")

url = client.synthesize_speech("This is an exaple speech synthesis file.", "YOUR_VOICE")

print(f"url: {url}")
