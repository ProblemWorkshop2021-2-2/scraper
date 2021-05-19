#!/bin/bash
git ls-files | wc -l >./../../data/files_in_repo.txt
find . -type f -not -path '*/.git/*' -exec echo {} \; >./../list_files.txt
echo "Generatring changed_files.txt"
#echo "commith_hash,file" >./../data/changed_files.txt
cat ../list_files.txt | while read line; do
  #authors=$(git -C ./tensorflow/ log --pretty=format:"%an" $line | sort | uniq -u)
  echo "file: ${line}"
  git log --pretty=format:"%an" $line | sort | uniq -u | while read author; do
    echo "${line},${author}" >>./../../data/changed_files.txt
  done
done
