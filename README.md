Registration Sytem
=================

This is the Registration backend used in TEDxPESITBSC V3. It's a simple Django app that imports attendee details from a CSV and helps manage registrations, process lunch queues.

## Usage
Make migrations:
```shell
$ python manage.py makemigrations
```

Migrate:
```shell
$ python manage.py migrate
```

Run the app locally on `localhost:8000`:
```shell
$ python manage.py runserver
```

## Pages

### /login
To login as a member of the Registration team and be allowed to access other pages.

### /register
To register an attendee by looking them up using their ticket id or mobile number and assigning them a new barcode.

### /lunch
To process lunch request for an attendee using their newly allocated barcode.

### /csv_import
To import latest attendee details from the CSV and add only new entries.

## Todo
- Add a dashboard page with stats of how many attendees have registered, had lunch, etc.
