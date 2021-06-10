## Uruchomienie

1. Aplikacja wymaga pythona 3.8
2. Zainstaluje brakujące zależności ```pip -r .requirements.txt```
3. Uruchomienie scrapera ```githubapi``` ```scrapy crwal githubapi```

## Kolejność uruchamiania scraperów

1. ```githubapi```
2. ```contributors```

## Dataset

1. insertions_commits.csv
	1.1 tree_hash - tree_hash id
	1.2 commith_hash - commith_hash id 
	1.3 changed - number of changed files
	1.4 insert -  number of insert
	1.5 delete - number of delete
2. lines_of_code.txt - contains two columns with information about the file name and the number of lines of code in it
3. files_in_repo.txt - contains one data for the number of files in the repository
4. changed_files.txt - contains two columns with information about the file name and the user name, who edit the file
5.commits.csv
	5.1 tree_hash - tree_hash id
	5.2 commith_hash - commith_hash id 
	5.3 author_name - author's name
	5.4 author_email - author's email
	5.5 author_timestamp - author's timestamp
	5.6 committer_name - comitter's name
	5.7 committer_email - comitter's email
	5.8 committer_timestamp  - comitter's timestamp
6. subscribers.csv
	6.1 id - subscriber's id
	6.2 login - subscriber's login
	6.3 site_admin - is subscriber admin of repository
	6.4 type - subscriber's type
7. users.csv
	7.1 id - user's id
	7.2 login - user's login
	7.3 site_admin - is user admin of repository
	7.4 type - user's type
	7.5 name - user's name
	7.6 email - user's e-mail 
	7.7 hireable - is user hireable
8. milestones.csv
	8.1 number - number of milestone
	8.2 id - id of milestone
	8.3 created_at - milestone creation date 
	8.4 closed_at - milestone close date
	8.5 title - title of milestone
	8.6 description - description of milestone 
9. releases.csv
	9.1 tag_name - release tag name
