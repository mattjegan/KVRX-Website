# KVRX Django Website

A KVRX website redesign using Django

## Features

- Users can create and manage playlists
- Users can create and manage KVRX pages
- Users can manage a KVRX blog

## File Documentation

Coming soon!

## How to Use

To view the live project, follow these steps:

1. Navigate to the project directory in terminal
2. Install the requirements (`$ pip install -r requirements.txt`)
3. Run `$ python manage.py runserver`
4. Navigate to `http://127.0.0.1:8000/` in your browser of choice.

## Todo

0. Fix this issue - "..migrations are part of your code, and must be in version control." http://stackoverflow.com/questions/38134535/django-on-heroku-relation-does-not-exist

1. Create login infrastructure
  1. User login page
  	a. If user is logged in, redirect to user bio
  2. Dj bio page
  3. Dj edit information page (only accessable if current user is logged in or if superuser/genadmin logged in)
  	a. On accessing page, redirect to home page is above criteria is not met
2. Create playlist backend
  1. Create show page with all playlists
  2. Create 'add playlist' page to create a playlist
    a. You should only be able to select your own 
3. Create blog infrastructure for home page
4. Add player to navbar
5. Documentation lol

## Deploy to Heroku instructions

1. `git commit -am "YOUR_COMMIT_MESSAGE"`		Commits changes
2. `git push`									Pushes to GitHub
3. `git push heroku master`						Pushes to Heroku (master can be changed for branch currently working on)
4. `heroku run bash`							Creates shell to make changes on Heroku
5. `python manage.py makemigrations pages`		Migrates changes in Pages
6. `python manage.py makemigrations shows`		Migrates changes in Shows
  * If you created any other apps, you would need to do the above for them too.
7. `python manage.py migrate`					Migrates everything

Good to go!