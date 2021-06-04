import os

from scrapgitubapi.util import Config


def main():
    repos = {
        # To już jest
        # "tensorflow": ["tensorflow"],
        # "arduino": ["Arduino"],
        # "audacity": ["audacity"],
        # "capistrano": ["capistrano"],
        # "cloudera": ["hue"],

        "floweisshardt": ["atf"],
        "bardsoftware": ["ganttproject"],
        "nginx": ["nginx"],
        "torakiki": ["pdfsam"],
        "scala": ["scala"],
        "Squirrel": ["Squirrel.Windows"],
        "tornadoweb": ["tornado"]
    }
    if len(repos.keys()) <= 0:
        print("Odkomentuj lub dodaj coś do tego pliku w zmiennej repos")
        return
    spiders = [
        "githubapi",
        "contributors",
        'subscribers',
        "users"
    ]

    for owner in repos.keys():
        for repository in repos[owner]:
            print(f"{owner}/{repository}")
            print("Scrap api")
            set_env_command = f"export REPOSITORY_OWNER={owner} && export REPOSITORY_NAME={repository}"
            os.system(set_env_command)
            os.environ['REPOSITORY_OWNER'] = owner
            os.environ['REPOSITORY_NAME'] = repository
            for spider in spiders:
                scrapy_command = f"scrapy crawl {spider}"
                command = f"{set_env_command} && {scrapy_command}"
                os.system(command)
                Config.set_repository_owner(owner)
                Config.set_repository_name(repository)

            print("Scrap repo")
            # scrap_repo()


if __name__ == "__main__":
    main()
