# Sample Django project

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/andreif/heroku_django)

```sh
heroku apps:create awesomeapp
git remote add heroku git@heroku.com:awesomeapp.git
heroku addons:create heroku-postgresql:hobby-dev
heroku addons:create memcachier:dev
heroku addons:create scheduler:standard

heroku config:set DJANGO_SETTINGS_MODULE=project.settings.heroku
heroku config:set DJANGO_SECRET_KEY=...
```
