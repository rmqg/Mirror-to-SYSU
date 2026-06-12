import requests
import os

GHP_TOKEN = os.getenv("GHP_TOKEN")


def get_repos():
    repos = []
    page = 1
    while True:
        r = requests.get(f"https://api.github.com/user/repos?per_page=100&page={page}&affiliation=owner",
            headers={"Authorization": f"token {GHP_TOKEN}"})
        r.raise_for_status()
        data = r.json()
        if not data:
            break
        for repo in data:
            if not repo["archived"]:
                repos.append(repo["name"])
        page += 1
    return repos


if __name__ == "__main__":
    repos = get_repos()
    open("repos.txt", "w").write("\n".join(repos))
    print("探索到的仓库数:", len(repos))
