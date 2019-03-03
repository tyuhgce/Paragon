Paragon pet application
=============================

Thank you for looking Paragon - a simple rest api to provide addition information about image.

[![Build Status](https://secure.travis-ci.org/yiisoft/yii.png)](http://travis-ci.org/yiisoft/yii)


INSTALLATION
------------

First you’ll need to run a python 3+ interpreter with app.py file. 
It runs server with rest api.

REQUIREMENTS
------------

The minimum requirement by Paragon is that your system supports
python 3+.

QUICK START
-----------

For quick look you can run tests in Test directory. 
The apllication runs rest api with one post query.

FUNCTIONALITY
-----------

Rest Api contains only one method that realize all functionality:

- /image. <br />
response in a format json with number of light pixels, number of dark pixel, decision (true of false, where true means that more light pixels, false means that more dark pixels)

WHAT'S NEXT
-----------

- Replace FileCacheService to DataBase interaction.
- Implement centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services like Zookeeper or anything like that..
- Implement system for automating deployment, scaling, and management of multiple containerized copies this application.

Created by
Marinich Roman
