
import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"

with open("/home/abc/Documents/wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:

        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered URL -->" + test_url)
