# KVRX Django Website

A KVRX website redesign using Django

## Features

- Users can create and manage playlists
- Users can create and manage KVRX pages
- Users can manage a KVRX blog

## File Documentation

Coming soon!

## Run locally

Mac instructions

1. Navigate to the project directory in terminal `$ cd Downloads/KVRX-Website/`
2. Install the requirements `$ pip install -r requirements.txt` (or `$ sudo pip install -r requirements.txt`)
3. Run `$ python manage.py runserver`
4. Navigate to `http://127.0.0.1:8000/` in your browser of choice.

## Todo

- Deploy sample to Heroku
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
  - Create multiple Song objects with one form input. Use a [formset](https://docs.djangoproject.com/en/dev/topics/forms/formsets/)
  - Saves to playlist
  - User can only create playlists for their show
- Documentation and instruction