#!/bin/bash

if [ -d "./capistrano" ]; then
  git -C ./capistrano/ fetch
  git -C ./capistrano/ pull
else
  git clone https://github.com/capistrano/capistrano.git
fi
echo "tree_hash\$commith_hash\$author_name\$author_email\$author_timestamp\$committer_name\$committer_email\$committer_timestamp" >./../data/commits.csv
git -C ./capistrano/ log --pretty=format:'%T$%H$%an$%ae$%at$%cn$%ce$%ct' --abbrev-commit >>./../data/commits.csv
git -C ./capistrano/ log --pretty=format:'%H' --abbrev-commit | sort | uniq -u >>./commits_hash.txt
git -C ./capistrano/ log --pretty=format:'%ae' --abbrev-commit | sort | uniq -u | grep -o '^[^@]*' >author_names.txt
git -C ./capistrano/ log --pretty=format:'%ce' --abbrev-commit | sort | uniq -u | grep -o '^[^@]*' >commiter_names.txt
cat ./author_names.txt >tmp_user_names.txt
cat ./commiter_names.txt >>tmp_user_names.txt
cat ./tmp_user_names.txt | sort | uniq -u >user_names.txt
