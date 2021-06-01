import os

import progressbar

from scrapgitubapi.util import Config, Util


def scrap_repo():
    repo_download_dir = f"{Config.working_directory()}/{Config.repo_dir()}/{Config.repository_owner()}_{Config.repository_name()}"
    repo_url = f"https://github.com/{Config.repository_owner()}/{Config.repository_name()}.git"
    Util.mkdir(repo_download_dir)
    if os.path.exists(repo_download_dir):
        print(f"git -c {repo_download_dir} fetch\ngit -c {repo_download_dir} pull")
        os.system(f"git -C {repo_download_dir} fetch")
        os.system(f"git -C {repo_download_dir} pull")
    else:
        print(f"git clone -q {repo_url} {repo_download_dir}")
        os.system(f"git clone -q {repo_url} {repo_download_dir}")

    data_dir = f"{Config.working_directory()}/{Config.data_dir()}/{Config.repository_owner()}_{Config.repository_name()}"
    temp_dir = f"{Config.working_directory()}/{Config.temp_dir()}/{Config.repository_owner()}_{Config.repository_name()}"

    commits_csv_file_path = f"{data_dir}/commits.csv"
    commit_hash_csv_file_path = f"{temp_dir}/commits_hash.txt"
    author_names_csv_file_path = f"{temp_dir}/author_names.txt"
    commiter_names_csv_file_path = f"{temp_dir}/commiter_names.txt"
    user_names_csv_file_path = f"{temp_dir}/user_names.txt"
    files_in_repo_csv_file_path = f"{data_dir}/files_in_repo.txt"
    list_files_csv_file_path = f"{temp_dir}/list_files.txt"
    changed_files_csv_file_path = f"{data_dir}/changed_files.txt"
    insertions_files_csv_file_path = f"{data_dir}/insertions_commits.csv"

    for file in [
        commits_csv_file_path,
        commit_hash_csv_file_path,
        author_names_csv_file_path,
        commiter_names_csv_file_path,
        user_names_csv_file_path,
        files_in_repo_csv_file_path,
        changed_files_csv_file_path,
        insertions_files_csv_file_path
    ]:
        Util.mkdir(file)

    commands = [
        'echo "tree_hash\$commith_hash\$author_name\$author_email\$author_timestamp\$committer_name\$committer_email\$committer_timestamp" > ' + commits_csv_file_path,
        'git -C ' + repo_download_dir + ' log --pretty=format:\'%T$%H$%an$%ae$%at$%cn$%ce$%ct\' --abbrev-commit >> ' + commits_csv_file_path,
        'git -C ' + repo_download_dir + ' log --pretty=format:\'%H\' --abbrev-commit | sort | uniq -u >> ' + commit_hash_csv_file_path,
        'git -C ' + repo_download_dir + ' log --pretty=format:\'%ae\' --abbrev-commit | sort | uniq -u | grep -o \'^[^@]*\' > ' + author_names_csv_file_path,
        'git -C ' + repo_download_dir + ' log --pretty=format:\'%ce\' --abbrev-commit | sort | uniq -u | grep -o \'^[^@]*\' > ' + commiter_names_csv_file_path,
        'echo "tree_hash,commith_hash,changed,insert,delete" > ' + insertions_files_csv_file_path,
        'git -C ' + repo_download_dir + ' log  --oneline --pretty="@%T,%H,"  --stat   |grep -v \| |  tr "\n" " "  |  tr "@" "\n" >> ' + insertions_files_csv_file_path,
        'cat ' + author_names_csv_file_path + ' > ' + user_names_csv_file_path + '.tmp',
        'cat ' + commiter_names_csv_file_path + ' >> ' + user_names_csv_file_path + '.tmp',
        'cat ' + user_names_csv_file_path + '.tmp | sort | uniq -u > ' + user_names_csv_file_path,
        'git -C ' + repo_download_dir + ' ls-files | wc -l > ' + files_in_repo_csv_file_path,
    ]
    for command in commands:
        print(f"command: {command}")
        os.system(command)

    find_files_command = f"find {repo_download_dir} -type f -not -path '*/.git/*' -exec echo {{}} \;"
    repo_files = []
    for repo_file in os.popen(find_files_command).readlines():
        x = repo_file.strip()[len(repo_download_dir) + 1:]
        repo_files.append(x)
    with open(list_files_csv_file_path, 'w') as list_files:
        for x in repo_files:
            list_files.write(f"{x}\n")
        list_files.close()

    with open(changed_files_csv_file_path, 'w') as changed_files:
        for repo_file in progressbar.progressbar(repo_files):
            authors_command = f"git -C {repo_download_dir} log --pretty=format:\"%an\" {repo_file} | sort | uniq -u"
            # print(f"command: {authors_command}")
            authors = []
            for author in os.popen(authors_command).readlines():
                authors.append(author.strip())
            # print(authors)
            for author in authors:
                changed_files.write(f"{repo_file},{author}\n")
        changed_files.close()
