import requests
import os

GL_TOKEN = os.getenv("GITLAB_TOKEN")
GL_URL = "git.sysu.edu.cn"
GL_USER = os.getenv("GITLAB_USERNAME")


def headers():
    return {"PRIVATE-TOKEN": GL_TOKEN}


def create_repo(repo):
    r = requests.post(
        f"{GL_URL}/api/v4/projects",
        headers=headers(),
        data={"name": repo, "visibility": "private"}
    )
    return r.status_code


def push_ci_file(repo):
    ci_content = """
stages:
  - mirror

mirror:
  stage: mirror
  script:
    - git config --global user.email "sync@bot"
    - git config --global user.name "sync-bot"

    - git remote add github https://{user}:${{GHP_TOKEN}}@github.com/{user}/{repo}.git || true
    - git fetch --all

    - msg=$(git log -1 --pretty=%B)
    - if echo "$msg" | grep -q "mirror-sync"; then exit 0; fi

    - git push github --all
    - git push github --tags
""".format(user=GL_USER, repo=repo)

    requests.post(
        f"{GL_URL}/api/v4/projects/{GL_USER}%2F{repo}/repository/files/.gitlab-ci.yml",
        headers=headers(),
        data={
            "branch": "main",
            "content": ci_content,
            "commit_message": "init mirror ci"
        }
    )
