import os

from scrapgitubapi.util import Config, Util


def scrap_repo():
    print(Config.repository_name())
    repo_download_dir = f"{Config.working_directory()}/{Config.repo_dir()}/{Config.repository_owner()}_{Config.repository_name()}"
    repo_url = f"https://github.com/{Config.repository_owner()}/{Config.repository_name()}.git"
    Util.mkdir(repo_download_dir)
    if os.path.exists(repo_download_dir):
        os.system(f"git -C {repo_download_dir} fetch")
        os.system(f"git -C {repo_download_dir} pull")
    else:
        os.system(f"git clone -q {repo_url} {repo_download_dir}")

    data_dir = f"{Config.working_directory()}/{Config.data_dir()}/{Config.repository_owner()}_{Config.repository_name()}"
    temp_dir = f"{Config.working_directory()}/{Config.temp_dir()}/{Config.repository_owner()}_{Config.repository_name()}"

    commits_csv_file_path = f"{data_dir}/commits.csv"
    commit_hash_csv_file_path = f"{temp_dir}/commits_hash.txt"
    author_names_csv_file_path = f"{temp_dir}/author_names.txt"
    commiter_names_csv_file_path = f"{temp_dir}/commiter_names.txt"
    user_names_csv_file_path = f"{temp_dir}/user_names.txt"
    for file in [
        commits_csv_file_path,
        commit_hash_csv_file_path,
        author_names_csv_file_path,
        commiter_names_csv_file_path,
        user_names_csv_file_path
    ]:
        Util.mkdir(file)

    commands = [
        'echo "tree_hash\$commith_hash\$author_name\$author_email\$author_timestamp\$committer_name\$committer_email\$committer_timestamp" > ' + commits_csv_file_path,
        'git -C ' + repo_download_dir + ' log --pretty=format:\'%T$%H$%an$%ae$%at$%cn$%ce$%ct\' --abbrev-commit >> ' + commits_csv_file_path,
        'git -C ' + repo_download_dir + ' log --pretty=format:\'%H\' --abbrev-commit | sort | uniq -u >> ' + commit_hash_csv_file_path,
        'git -C ' + repo_download_dir + ' log --pretty=format:\'%ae\' --abbrev-commit | sort | uniq -u | grep -o \'^[^@]*\' > ' + author_names_csv_file_path,
        'git -C ' + repo_download_dir + ' log --pretty=format:\'%ce\' --abbrev-commit | sort | uniq -u | grep -o \'^[^@]*\' > ' + commiter_names_csv_file_path,
        'cat ' + author_names_csv_file_path + ' > ' + user_names_csv_file_path + '.tmp',
        'cat ' + commiter_names_csv_file_path + ' >> ' + user_names_csv_file_path + '.tmp',
        'cat ' + user_names_csv_file_path + '.tmp | sort | uniq -u > ' + user_names_csv_file_path
    ]
    for command in commands:
        print(f"command: {command}")
        os.system(command)
