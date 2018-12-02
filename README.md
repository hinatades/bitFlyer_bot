# bitFlyer_bot

bitFlyer automated trade Bot in Python

## Installation

Using pip

```
$ pip install git+https://github.com/hinatades/bitFlyer_bot.git
```

Start the server

```
$ cd bitFlyer_bot

# build a virtual environment
$ python3.6 -m venv env
$ source env/bin/activate
(env)$

$ Installing packages
$ pip install -r requirements.txt

# Create database
$ python bot/manage.py migrate

# Create administrator user
$ python bot/manage.py createsuperuser

# Listen on localhost: 8000 when server starts up
$ python bot/manage.py runserver
```

## Author

@hinatades (<hnttisk@gmail.com>)
