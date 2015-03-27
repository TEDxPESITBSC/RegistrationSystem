Registration Sytem
=================

This is the Registration backend used in TEDxPESITBSC V3. It's a simple Django app that imports attendee details from a CSV and helps manage registrations, process lunch queues.

##Usage
Make migrations:
```shell
./manage.py makemigrations
```

Migrate:
```shell
./manage.py migrate
```

Run the app locally on `localhost:8000`:
```shell
./manage.py runserver
```


##Todo
- Add a dashboard page with stats of how many attendees have registered, had lunch, etc.
