# ![aflr logo](https://github.com/aflorithmic/aflr_client/blob/master/docs/images/aflr-logo.svg?raw=true) Aflorithmic Client

Tiny client for communicating with the Aflorithmic TTS API.

## Installation

```
    pip install git+ssh://git@github.com/aflorithmic/aflr_client.git

```
## Example usage

```
    from aflr_client import AFLRClient

    client = AFLRClient("YOUR_API_KEY")

    url = client.synthesize_speech("This is an exaple speech synthesis file.", "YOUR_VOICE")

    print(f"url: {url}")
```
