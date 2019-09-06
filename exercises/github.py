#!/usr/bin/env python3


import requests
import os
import sys


token = "1828cd0c721f4e91f67358d78ab2f8ef04a36e17"
url_API = "https://api.github.com/user/repos"
url = "{}?access_token={}".format(url_API, token)
response = requests.get(url)
data = response.json()


def write_file(path, data):
    with open(path, "wb") as f:
        f.write(data)

def init(repo):
    """Create a directory for the repo and initialize the .git directory"""
    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.git'))
    for name in ['object', 'refs', 'ref/heads']:
        os.mkdir(os.path.join(repo, '.git', name))
    write_file(os.path.join(repo,'.git', 'HEAD'), b'ref: refs/heads/master')


repo = input("what is your repository name?: ")

init(repo)



