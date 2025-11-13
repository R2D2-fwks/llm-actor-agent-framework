import requests
import json

url = "http://127.0.0.1:11434/api/generate"
headers = {'Content-Type': 'application/json'}
payload = {
    "model": "llama3",
    "prompt": "Hello, world!",
    "stream": False
}

print("Attempting to connect to:", url)
print("Payload:", json.dumps(payload, indent=2))

try:
    response = requests.post(
        url, 
        headers=headers, 
        json=payload,
        timeout=60
    )
    print(f"✅ Status Code: {response.status_code}")
    print(f"✅ Response: {response.text}")
except requests.exceptions.ConnectionError as e:
    print(f"❌ Connection Error: {e}")
    print("\nTroubleshooting:")
    print("1. Is Ollama running? Check with: curl http://localhost:11434")
    print("2. Check firewall settings")
    print("3. Try using 127.0.0.1 instead of localhost")
except requests.exceptions.Timeout as e:
    print(f"❌ Timeout Error: {e}")
except Exception as e:
    print(f"❌ Unexpected Error: {type(e).__name__}: {e}")