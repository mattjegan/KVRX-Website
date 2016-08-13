# KVRX Django Website

A KVRX website redesign using Django

## Current Features

- Create users and grant/revoke certain permissions
- Groups (such as 'Deejay' or 'Staff') automatically grant specific permissions to users in those groups
- Store Deejays, Shows, Playlists, and Songs
  - Specific detail pages for Deejays and Shows (which show Playlists)
  - Specific page showing all Deejays and Shows
- Create your own pages with custom HTML on the KVRX template
  - Display link to pages on the front page

## Run locally

Mac instructions

1. Navigate to the project directory in terminal `$ cd Downloads/KVRX-Website/`
2. Install the requirements `$ pip install -r requirements.txt` (or `$ sudo pip install -r requirements.txt`)
3. Run `$ python manage.py runserver`
4. Navigate to `http://127.0.0.1:8000/` in your browser of choice.

## Basic functionality Requirements

|Requirement|Priority|Status|
|-----|-----|-----|
|Connect website to AudioVAULT|High|Not yet started|
|Connect website to existing database<br>- Potentially write seed code to migrate and clean old data into a new database|High|Not yet started|
|Furnishes now playing information (artist, title, album)||Not yet started|
|Furnishes a streaming plugin that activates immediately rather than requiring a .pls file download for iTunes||Complete!|
|Offers Program / show schedule including DJ info and show playlists||Information is available, but not in calendar format|
|Offers album reviews||Not yet started|
|Offers concert and events calendar||Not yet started|
|Music department functionality<br>- Tracking<br>- Tallying of what's added / played for charts<br>- Topless 39<br>- Reporting||Not yet started|
|Must be able to handle ads provided by 3rd floor advertising department|High|Not yet started|
|Offers space for uploading/accessing video content<br>- Concert performances<br>- Local Live<br>- Library Sessions<br>- Interviews||Not yet started| 

## Immediate Todo

- `git branch develop`
- Consolidate functionality and to-do list
- Expand on functionality/to-do list and create step by step requirements
- Move to-do list to Issues page on Github


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
- Make navbar player persistent across pages
  - Check out [PersistJS](https://github.com/jeremydurham/persist-js)
- Switch form using Paper bootswatch to Cosmo bootswatch pre-designer
- Strip unnecessary rules from bootswatch file
- Create .ico file

## Issues
- Default backend doesn't let you add a date to your playlists
- Default backend uses military time for show start/end times
- Playlist isn't showing all songs or repeat songs on show detail page
- Users can create pages with same link as pre-defined pages (e.g. 'shows')

## Future issues
- Host on Dreamhost