## Uruchomienie

1. Aplikacja wymaga pythona 3.8
2. Zainstaluje brakujące zależności ```pip -r .requirements.txt```
3. Uruchomienie scrapera ```githubapi``` ```scrapy crwal githubapi```

## Kolejność uruchamiania scraperów

1. ```githubapi```
2. ```contributors```

## Dataset

insertions_commits.csv
	tree_hash - tree_hash id
	commith_hash - commith_hash id 
	changed - number of changed files
	insert -  number of insert
	delete - number of delete
lines_of_code.txt - contains two columns with information about the file name and the number of lines of code in it
files_in_repo.txt - contains one data for the number of files in the repository
changed_files.txt - contains two columns with information about the file name and the user name, who edit the file
commits.csv
	tree_hash - tree_hash id
	commith_hash - commith_hash id 
	author_name - author's name
	author_email - author's email
	author_timestamp - author's timestamp
	committer_name - comitter's name
	committer_email - comitter's email
	committer_timestamp  - comitter's timestamp
subscribers.csv
	id - subscriber's id
	login - subscriber's login
	site_admin - is subscriber admin of repository
	type - subscriber's type
users.csv
	id - user's id
	login - user's login
	site_admin - is user admin of repository
	type - user's type
	name - user's name
	email - user's e-mail 
	hireable - is user hireable
milestones.csv
	number - number of milestone
	id - id of milestone
	created_at - milestone creation date 
	closed_at - milestone close date
	title - title of milestone
	description - description of milestone 
releases.csv
	tag_name - release tag name
