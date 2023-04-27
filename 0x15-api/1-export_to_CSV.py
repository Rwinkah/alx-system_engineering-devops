#!/usr/bin/python3
"""
Python script using rest API to get a response.
with the urlib library
"""
import csv
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

    with open('{}.csv'.format(argv[1]), 'w', newline='') as f:
        file_write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in todo:
            if i['userId'] == int(argv[1]):
                userid = i['userId']
                username = user['username']
                comp = i['completed']
                title = i['title']
                file_write.writerow(["{}".format(userid), "{}"
                                    .format(username), "{}".format(comp), "{}"
                                    .format(title)])


if __name__ == '__main__':
    main()
