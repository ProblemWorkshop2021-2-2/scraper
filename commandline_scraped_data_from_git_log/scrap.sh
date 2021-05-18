#!/bin/bash

if [ -d "./tensorflow" ]; then
  git -C ./tensorflow/ fetch
  git -C ./tensorflow/ pull
else
  git clone https://github.com/tensorflow/tensorflow.git
fi
echo "tree_hash,commith_hash,author_name,author_email,author_timestamp,committer_name,committer_email,committer_timestamp" >./../data/commits.csv
git -C ./tensorflow/ log --pretty=format:'%T,%H,%an,%ae,%at,%cn,%ce,%ct' --abbrev-commit >>./../data/commits.csv
