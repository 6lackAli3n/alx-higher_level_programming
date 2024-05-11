#!/usr/bin/python3
# Script to send a POST request with an email parameter to a given URL

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    DATA = urllib.parse.urlencode({"email": email})
    DATA = DATA.encode('ascii')

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode('utf-8'))
