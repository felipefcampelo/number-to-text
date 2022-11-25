# Number To Text - Study Case
## Trellis

---------

### How to setup the project

- Using a terminal (Shell, Bash, CMS, etc.) go to the local where you want to install the project in your computer
- Create the folder where you will install the project

		mkdir [folder_name]

- Enter in the folder

		cd [folder_name]

- We are going to create a Python's Virtual Environment

		python -m venv venv

- Now let's initiate the git on this project and link it with our remote repository in order to download the project files

		git init
		git remote add origin https://github.com/felipefcampelo/trellis-study-case.git
		git pull origin master

- Now we need to activate our virtual environment

		. venv/Scripts/activate

- Let's run the requirements.txt file to install the dependencies for this project
	
		pip install -r requirements.txt

- Let's start a server to use the API