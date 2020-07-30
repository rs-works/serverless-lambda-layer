import requests

url = 'https://example.com/'

def main(event, context):
    response = requests.get(url)
    print(response)

if __name__ == "__main__":
    main('', '')
