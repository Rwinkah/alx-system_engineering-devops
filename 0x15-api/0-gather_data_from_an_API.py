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
        if i['userId'] == int(argv[1]) and i['completed']:
            count += 1
            comp_title.append(i['title'])

    print('Employee {} is done with tasks({}/20):'
          .format(user['name'], count))
    for i in comp_title:
        print('\t {}'.format(i))


if __name__ == '__main__':
    main()
