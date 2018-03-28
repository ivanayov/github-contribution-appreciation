import requests, json
from github import Github

def handle(req):

    kudo_data = json.loads(req)

    g = Github(kudo_data["auth"])
    repo = g.get_repo(kudo_data["repo"])
    pull = repo.create_pull("Accept Kudo Badge from " + kudo_data["maintainer"], kudo_data["kudo-body"])

    return pull.json()