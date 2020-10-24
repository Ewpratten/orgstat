import argparse
import requests
from tqdm import tqdm


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("org", help="Name of GitHub organization")
    ap.add_argument("-k", "--key", help="GitHub API key", required=True)
    args = ap.parse_args()

    repo_names = []
    page = 1

    while True:
        # print(f"https://api.github.com/users/{args.org}/repos?page={page}")
        response = requests.get(
            f"https://api.github.com/users/{args.org}/repos?page={page}&per_page=100", headers={
                "Authorization": f"token {args.key}"
            })

        if int(response.status_code / 100) != 2:
            break

        response_json = response.json()

        if len(response_json) == 0:
            break

        for repo in response_json:
            repo_names.append(repo["full_name"])

        page += 1

    if len(repo_names) == 0:
        print(f"Could not find any repos for org: {args.org}")
        exit(1)

    contributors = {}

    for repo in tqdm(repo_names, ascii=True, desc="repos"):

        page = 1
        while True:

            response = requests.get(
                f"https://api.github.com/repos/{repo}/commits?page={page}&per_page=100", headers={
                    "Authorization": f"token {args.key}"
                })

            if int(response.status_code / 100) != 2:
                break

            response_json = response.json()

            if len(response_json) == 0:
                break

            for author in tqdm(response_json, position=1, ascii=True, desc=repo):

                author_name = author["commit"]["author"]["name"]

                if author_name not in contributors:
                    contributors[author_name] = 1
                else:
                    contributors[author_name] += 1

            page += 1

    sorted_contributors = {k: v for k, v in sorted(
        contributors.items(), key=lambda item: item[1])}

    print()

    for contributor in sorted_contributors:
        value = sorted_contributors[contributor]
        print(f"{value}\t {contributor}")


if __name__ == "__main__":
    main()
