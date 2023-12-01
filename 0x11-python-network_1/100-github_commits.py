#!/usr/bin/python3
"""script that takes 2 arguments (the repo name and the owner)
    in order to return the last 10 commit to the specified repo"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
    commits = r.json()[:10]
    for commit in commits:
        commit_sha = commit.get('sha')
        commit_name = commit.get('commit').get('author').get('name')
        print(f"{commit_sha}: {commit_name}")
