It is a opiniated view of the complete Web Application using Web APIs, based on python's **DJANGO** framework. The core authentication mechanism is django based, and it  also includes a mashup consisting of various social logins.

## Docker is use to deploy 
### to AWS EC2
A docker image is built on python 2.7 base image and deployed to EC2 instance running docker host.[1]
### to AWS EC2 Container
the docker image built is pushed to the ECS and a  container is instantiated on a default ec2 container instance.
Configuration for the container logs are sent to the cloud watch east region.

### 

## References
1. _https://docs.docker.com/machine/examples/aws/_
# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
