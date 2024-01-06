# Read Me

To use this you need [Python](https://www.python.org)

Optionally you shuld probably create a python virtual environment.

Once you have this set up you can install the required dependencies by opening a terminal in the root directory of the project and issuing the command

```pip install -r requirements.txt```

[Register an application with Tumblr](https://www.tumblr.com/oauth/apps) then create a copy of ```.env.template``` and rename it to ```.env``` and paste your application keys into the file.

If you want to pull posts from a tag in ```post_pulling/__init__.py``` you change the tag, start and end time to match the desired search term.

Once you have done this you can start the program using the command ```python "35 Caught.py"```