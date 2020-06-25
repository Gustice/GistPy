#!/usr/bin/env python -B

from github import Github	# pip install PyGithub
import getpass
import json
import os

all = []

usr = input("Enter username: ")
pw = getpass.getpass("Enter password: ")
g = Github(usr, pw)

for gist in g.get_user().get_gists():
    all.append({
        "id"            : gist.id,
        "description"   : gist.description,
        "public"        : gist.public,
        "clone"         : gist.git_pull_url,
        "updated"       : gist.updated_at.isoformat(),
        "url"           : gist.url,
    })

    print("git clone {0} repos/{1}".format(gist.git_pull_url, gist.id))
    os.system("git clone {0} repos/{1}".format(gist.git_pull_url, gist.id))

with open("index.json", "w") as f:
    f.write(json.dumps(all, indent=4) + "\n")