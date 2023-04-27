#!/usr/bin/python3
"""
Python script using rest API to get a response.
with the urlib library
"""
import json
from sys import argv
from urllib import request


def main():
    """rest API script that returns information about employee progress."""

    count = 0
    comp_title = []
    base_url = 'https://jsonplaceholder.typicode.com/'
    todo = json.loads(request.urlopen(base_url + 'todos').read().decode())
    user = json.loads(request.urlopen(base_url + 'users/' + argv[1])
                      .read().decode())

    for i in todo:
        if i['userId'] == int(argv[1]):
            count += 1
            print('"{}","{}","{}","{}"'.format(i['userId'], user['username'],
                  i['completed'], i['title']))


if __name__ == '__main__':
    main()
