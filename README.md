# Web-Scraping
Here's some code for scraping data from realestate website www.99acres.com using python scrapy package.I hope it would be helpfull for beginners in web scraping.

Install scrapy by :  pip install scrapy
 #Creating to project
 Before you start scraping, you will have to set up a new Scrapy project. Enter a directory where you’d like to store your code and run:

      scrapy startproject tutorial

This will create a tutorial directory with the following contents:

tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py

