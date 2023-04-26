#!/usr/bin/python3
""" Python script using rest API """

import sys
import requests as req

def main():
    """ rest API script"""
    list_url = 'https://jsonplaceholder.typicode.com/'
    todo = req.get(list_url + 'todos', params={'userId': sys.argv[1]}).json()
    userid = r.get(list_url + 'users/{}'.format(sys.argv[1]}).json()
    doneTask = [title.get("title") for title in todo if title.get('completed') is True]

    print(done task)
    print("Employee {} is done with tasks({}/{}):".format(userid.get("name"), len(doneTask), len(todo)))

    [print"\t {}".format(title)) for title in donetask]


if __name__ == '__main__':
    main()
