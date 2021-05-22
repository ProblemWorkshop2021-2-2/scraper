import os

from scrap_repo import scrap_repo
from scrapgitubapi.util import Config


def main():
    repos = {
        # "tensorflow": ["tensorflow"],
        "arduino": ["Arduino"]
    }

    spiders = [
        "githubapi",
        "contributors",
        'subscribers',
        "users"
    ]

    for owner in repos.keys():
        for repository in repos[owner]:
            for spider in spiders:
                set_env_command = f"export REPOSITORY_OWNER={owner} && export REPOSITORY_NAME={repository}"
                scrapy_command = f"scrapy crawl {spider}"
                command = f"{set_env_command} && {scrapy_command}"
                os.system(command)
                Config.set_repository_owner(owner)
                Config.set_repository_name(repository)
            scrap_repo()


if __name__ == "__main__":
    main()
