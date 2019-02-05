# ihome

## Build Setup

```shell
# celery deploy
$ celery -A ihome.tasks.main worker -l info

# init data
$ python manage.py init_data

# launch server
$ python manage.py runserver
```

