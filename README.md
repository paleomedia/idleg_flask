# IDleg
Being a spinoff of the #idleg Twitter hashtag, pronounced by some as Idle-G.

## Interactive Portal to Idaho Legislature - Under Construction
### In development, i.e. use at your own risk

This project is part of a master's degree in "Data Journalism" at Boise State University. I'm building an alternative legislative portal for the state of Idaho that:

- Uses data from the Sunlight Foundation [Open States Project API] (https://sunlightlabs.github.io/openstates-api/) to provide a rich dataset of state legislative data
- Provides social tools for bills and other legislative actions, allowing constituents to "testify" on bills online
- Provides some basic statistics on legislative actions
- Provides a means to parse votes in various ways - by bill, lawmaker, party, etc.
- Demonstrates the type of information that hacker-journalists can access
- Demonstrates the cross-over between "open government" and "open news" initiatives

- In this idleg_flask repo, I'm refactoring and building out the project with Python Flask

You can read more about my [MA project on my blog] (http://www.paleomedia.org/2013/09/30/data-journalism/) and look for beta releases and other updates [at idleg.info](http://idleg.info/) soon.

## Setup for Developers

### Requirements
- Python 2.6 or higher
- A [Sunlight Labs API Key](http://sunlightfoundation.com/api/accounts/register/) - Read their instructions to [install the key and use the Python library](http://python-sunlight.readthedocs.org/en/latest/#usage)
- Recommend installing in [virtualenv](http://flask.pocoo.org/docs/0.10/installation/)

```python
    $ pip install virtualenv
    $ virtualenv idleg_flask
    $ cd idleg_flask
    $ source bin/activate
    $ pip install flask
```

- Then [fork the repository](https://github.com/paleomedia/idleg_flask#fork-destination-box) if you want or just clone it to your virtualenv:

```python
    $ git clone https://github.com/paleomedia/idleg_flask.git
```

- Finally, install dependencies (note: requirements.txt contains some bloat... will clean up dependencies at a later date)

```python
    $ pip install -r requirements.txt
```

I think that will work... but please let us know if you run into problems getting it running. And remember, the app is still in development...

### How to run

```python
    python run.py
```
or
```python
    ./run.py
```
## Contributors
[@paleomedia](http://twitter.com/paleomdia)
[@nilabmm](http://twitter.com/nilabmm)
