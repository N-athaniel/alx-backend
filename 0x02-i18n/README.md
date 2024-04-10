0x02. i18n

Back-end

Tasks

0. Basic Flask app

Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page

1. Basic Babel setup

Install the Babel Flask extension:

Then instantiate the Babel object in your app. Store it in a module-level variable named babel.

In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.

2. Get locale from request

Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.

3. Parametrize templates

Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.

Create a babel.cfg file containing extensions=jinja2.ext.autoescape,jinja2.ext.with  

4. Force locale with URL parameter

In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.

In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

5. Mock logging in

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.

This will mock a database user table. Logging in will be mocked by passing login_as URL parameter containing the user ID to log in as.

Define a get_user function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed.

Define a before_request function and use the app.before_request decorator to make it be executed before all other functions. before_request should use get_user to find a user if any, and set it as a global on flask.g.user.

6. Use user locale

Change your get_locale function to use a user’s preferred local if it is supported.

The order of priority should be

Locale from URL parameters
Locale from user settings
Locale from request header
Default locale

7. Infer appropriate time zone

Define a get_timezone function and use the babel.timezoneselector decorator.

The logic should be the same as get_locale:

Find timezone parameter in URL parameters
Find time zone from user settings
Default to UTC

Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use pytz.timezone and catch the pytz.exceptions.UnknownTimeZoneError exception.

8. Display the current time

Based on the inferred time zone, display the current time on the home page in the default format.
