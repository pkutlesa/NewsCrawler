# NewsCrawler
Application that crawls and scrapes large news site (e.g., NY times) and pumps data into mongodb atlas cluster.

-    Create new virtual enviornment (venv)

-   Install required dependencies (i.e., scrapy, pymongo) 

-    use 'scrapy startproject news' command that creates the following project structure: 

.


├── scrapy.cfg               # deploy configuration file


└── news                     # project's Python module


    ├── __init__.py
    
    
    ├── items.py             # items definition file
    
    
    ├── middlewares.py
    
    
    ├── pipelines.py         # project pipelines file
    
    
    ├── settings.py          # project settings
    
    
    └── spiders              # dir to store spiders
    
    
        └── __init__.py

-  Run 'scrapy crawl news' command 

