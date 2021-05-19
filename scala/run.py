import os


def main():
    spiders = [
        # "githubapi",
        # "contributors",
        # 'subscribers',
        "users"
    ]
    for spider in spiders:
        os.system(f"scrapy crawl {spider}")


if __name__ == "__main__":
    main()
