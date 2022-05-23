## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/damildrizzy/gr-test.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Run tests
```sh
(env)$ pytest
```

Start the application
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`

## Assumptions
- A reservation cannot be made on a rental for dates that are already booked
- The checkout date for a reservation cannot be earlier than the checkin date