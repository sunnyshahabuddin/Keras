import requests

def hit_api_with_certificate(url, certificate_path):
    try:
        cert = (certificate_path, certificate_path)
        response = requests.get(url, cert=cert)
        if response.status_code == 200:
            print("Response:", response.text)
        else:
            print("Error:", response.status_code, response.text)

    except Exception as e:
        print("Error occurred:", e)

api_url = "https://api.example.com"
certificate_path = "/path/to/certificate.pem"

hit_api_with_certificate(api_url, certificate_path)
