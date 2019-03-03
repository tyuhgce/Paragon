Paragon pet application
=============================

Thank you for looking Paragon - a simple rest api to provide addition image information.

[![Build Status](https://secure.travis-ci.org/yiisoft/yii.png)](http://travis-ci.org/yiisoft/yii)


INSTALLATION
------------

First you’ll need to run a python 3+ interpreter with app.py file and install requirement packages.
After all, it runs server with rest api.

REQUIREMENTS
------------

The minimum requirement by Paragon is that your system supports python 3+.

QUICK START
-----------

For quick look you can look at index.html page by address http://localhost:8000/. 
Also you can run tests in Test directory.

FUNCTIONALITY
-----------

Rest Api contains only one method that realize all functionality:

- /image. <br />
response in a format json with number of light pixels, number of dark pixel, decision (true of false, where 'true' means that more light pixels, 'false' means that more dark pixels)

WHAT'S NEXT
-----------

- Replace FileCacheService to Database interaction.
- Implement centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services like Zookeeper or anything like that..
- Implement system for automating deployment, scaling, and management of multiple containerized copies this application.

Created by
Marinich Roman
