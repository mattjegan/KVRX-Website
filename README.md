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

- Add images to DJ page
  - Have to host off a media server - most likely Amazon S3. [Instructions here](http://caseypt.github.io/2012/01/02/s3-heroku-django.html)
- Create singular login page
  - If accessed by someone who's already logged in, redirect to their Deejay page
- Create backend for all information
  - Edit page for all Deejay information (accessible by that DJ or any staff)
  - Edit page for Deejays show information (accessible by that DJ or any staff)
    - Should only allow user to edit their own show
  - Edit page for Playlist information (accessible by that DJ or any staff)
    - Should only allow user to edit playlists for their show
- Create playlist backend
  - Create multiple Song objects with one form input
  - Saves to playlist
  - User can only create playlists for their show
- Add player to navbar
- Documentation and instruction

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