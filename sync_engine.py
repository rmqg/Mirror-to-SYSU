import os
import subprocess
import shutil
from gitlab_api import create_repo, push_ci_file

GH_USER = os.getenv("GHP_USERNAME")
GH_TOKEN = os.getenv("GHP_TOKEN")

GL_URL = "https://git.sysu.edu.cn"
GL_USER = os.getenv("GITLAB_USERNAME")
GL_TOKEN = os.getenv("GITLAB_TOKEN")


def run(cmd):
    print(">>>", cmd)
    subprocess.run(cmd, shell=True, check=True)


def sync(repo):
    print(f"\n==== {repo} ====")

    gh = f"https://{GH_TOKEN}@github.com/{GH_USER}/{repo}.git"
    gl = f"https://{GL_USER}:{GL_TOKEN}@{GL_URL.replace('https://','')}/{GL_USER}/{repo}.git"

    # 创建 GitLab 仓库 + CI
    create_repo(repo)
    push_ci_file(repo)

    run(f"git clone --mirror {gh}")
    os.chdir(f"{repo}.git")

    run(f"git remote add gitlab {gl} || true")

    run("git fetch --all")

    # 防循环
    msg = subprocess.getoutput("git log -1 --pretty=%B")
    if "mirror-sync" in msg:
        print("skip loop")
        os.chdir("..")
        shutil.rmtree(f"{repo}.git")
        return

    # 双向 push
    run("git push gitlab --all || true")
    run("git push origin --all || true")

    run("git push gitlab --tags || true")
    run("git push origin --tags || true")

    os.chdir("..")
    shutil.rmtree(f"{repo}.git")


if __name__ == "__main__":
    repos = open("repos.txt").read().splitlines()

    for r in repos:
        try:
            sync(r)
        except Exception as e:
            print("ERROR:", r, e)
