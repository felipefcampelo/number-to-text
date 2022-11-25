# Number To Text - Study Case
## Trellis

---------

### How to setup the project

- Using a terminal (Shell, Bash, CMS, etc.) go to the local where you want to install the project on your computer
- Create the folder where you will install the project

		mkdir [folder_name]

- Enter in the folder

		cd [folder_name]

- We are going to create a Python Virtual Environment

		python -m venv env

- Now let's initiate the git on this project and link it with our remote repository in order to download the project files

		git init
		git remote add origin https://github.com/felipefcampelo/trellis-study-case.git
		git pull origin master

- Now we need to activate our virtual environment

		. env/Scripts/activate

- Let's run the requirements.txt file to install the dependencies for this project
	
		pip install -r requirements.txt

- Before we can run our API, we will need to run the migrations, not to have blockers coming from Django Framework

		python manage.py migrate

- Let's start a server to use the API (that will create a SQLite database and will show a message about migrations. Ignore both)

		python manage.py runserver

- We can use a browser to test the API (GET requests) or some software to send POST requests, like Postman or Insomnia. The endpoint is http://localhost:8000/num_to_english. If you want to send a GET request, just set the "number" parameter in the URL

		http://localhost:8000/num_to_english?number=[number]

- If you want to send a POST request, you can send a body content using JSON format and the endpoint is just: http://localhost:8000/num_to_english

			{
				"number": "12345"
			}

- The response will be in JSON format as well

		{
			"status": "ok",
			"message": "twelve thousand three hundred and forty-five"
		}