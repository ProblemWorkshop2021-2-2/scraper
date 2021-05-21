import os


def main():
    repos = {
        # "tensorflow": ["tensorflow"]
        ""
    }

    spiders = [
        "githubapi",
        "contributors",
        'subscribers',
        "users"
    ]

    for organization in repos.keys():
        for repository in repos[organization]:
            for spider in spiders:
                set_env_command = f"export REPOSITORY_OWNER={organization} && export REPOSITORY_NAME={repository}"
                scrapy_command = f"scrapy crawl {spider}"
                command = f"{set_env_command} && {scrapy_command}"
                os.system(command)


if __name__ == "__main__":
    main()
