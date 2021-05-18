#!/bin/bash

if [ -d "./tensorflow" ]; then
  git -C ./tensorflow/ fetch
  git -C ./tensorflow/ pull
else
  git clone https://github.com/tensorflow/tensorflow.git
fi
echo "tree_hash,commith_hash,author_name,author_email,author_timestamp,committer_name,committer_email,committer_timestamp" >./../data/commits.csv
git -C ./tensorflow/ log --pretty=format:'%T,%H,%an,%ae,%at,%cn,%ce,%ct' --abbrev-commit >>./../data/commits.csv
git -C ./tensorflow/ log --pretty=format:'%ae' --abbrev-commit | uniq -u | grep -o '^[^@]*' >author_names.txt
git -C ./tensorflow/ log --pretty=format:'%ce' --abbrev-commit | uniq -u | grep -o '^[^@]*' >commiter_names.txt
cat ./author_names.txt >tmp_user_names.txt
cat ./commiter_names.txt >>tmp_user_names.txt
cat ./tmp_user_names.txt | uniq -u >user_names.txt
