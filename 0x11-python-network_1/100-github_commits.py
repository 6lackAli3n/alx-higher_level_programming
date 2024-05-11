#!/usr/bin/python3
"""
Script to list 10 commits (from the most recent to oldest) of a repository
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    response = requests.get(url)
    commits = response.json()[:10]  # Get the latest 10 commits
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
