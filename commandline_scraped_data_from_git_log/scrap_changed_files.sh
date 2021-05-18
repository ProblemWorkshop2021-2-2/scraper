#!/bin/bash
git -C ./tensorflow/ ls-files | wc -l >./../data/files_in_repo.txt
echo "Generatring changed_files.txt"
echo "commith_hash,file" >./../data/changed_files.txt
cat commits_hash.txt | while read line; do
  #files_changed=$(git -C ./tensorflow/ diff-tree --no-commit-id --name-only -r $line)
  echo "commit: ${line}"
  git -C ./tensorflow/ diff-tree --no-commit-id --name-only -r $line | while read file; do
    echo "${line},${file}" >>./../data/changed_files.txt
  done
done
