#!/usr/bin/python3
"""Script to fetch the value of X-Request-Id variable from the response header
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
