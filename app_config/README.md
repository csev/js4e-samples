Initial Setup
-------------

The initial setup of this Django project is different than that
which is created by `django-admin startproject` to reduce confusion
for beginners.  Here is how this project is setup:

    cd django_projects   # Or wherever you want to start your project
    django-admin startproject app_config

    # Rename the folder to whatever you want (perhaps a git repo name)
    mv app_config js4e-samples
    cd js4e-samples/app_config

    # Rename the urls.py to avoid confusion with the urls.py in each app
    mv urls.py root_urls.py

Then edit `settings.py` and change the string `app_config.urls` to `app_config.root_urls`.

The name `app_config` was chose with an underscore and starting with 'a' to
by at or near the top of the Django application folders.

The name `root_urls.py` was so named to reflect that it is setting up the
top level url routing for the whole project:

    https://drchuck.pythonanywhere.com/xxx/....
                                       ^^^ The top level or "root" paths

