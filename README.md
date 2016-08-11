# KVRX Django Website

A KVRX website redesign using Django

## Features

- Create users and grant/revoke certain permissions
- Groups (such as 'Deejay' or 'Staff') automatically grant specific permissions to users in those groups
- Store Deejays, Shows, Playlists, and Songs
  - Specific detail pages for Deejays and Shows (which show Playlists)
  - Specific page showing all Deejays and Shows
- Create your own pages with custom HTML on the KVRX template
  - Display link to pages on the front page

## File Documentation

Coming soon!

## Run locally

Mac instructions

1. Navigate to the project directory in terminal `$ cd Downloads/KVRX-Website/`
2. Install the requirements `$ pip install -r requirements.txt` (or `$ sudo pip install -r requirements.txt`)
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
  - Create multiple Song objects with one form input. Use a [formset](https://docs.djangoproject.com/en/dev/topics/forms/formsets/)
  - Saves to playlist
  - User can only create playlists for their show
- Documentation and instruction
- Implement navbar/homepage song information
  - Add BooleanField "currentSong" to Song model, then [override the Save method](http://stackoverflow.com/questions/1455126/unique-booleanfield-value-in-django) to enforce it's uniqueness. Just add the song to getBaseInfo() in pages/views!
- Add Semester and Year field to the Show class
- Add support for shows that start and end on different days (e.g. 11pm to 1am)

## Issues
- Default backend doesn't let you add a date to your playlists
- Default backend uses military time for show start/end times
- Playlist isn't showing all songs or repeat songs on show detail page
- Users can create pages with same link as pre-defined pages (e.g. 'shows')