IhubJobsSpider is a spider that crawls "http://ihub.co.ke/jobs" and extracts all available jobs then saves the data in the format of csv/json

The application is written in python.

#TODO:
  1. Add a method that follows each job's link and extracts defined data from the job description 
     i.e deadline, required skills. 
  2. Save the data in a postgreSQL/MySQL database.
  3. Data visualization of scrapped data.
  4. Add social features to the app by crawling ihub's social network pages and making relations to users
     recommendations/activities in
     relation to advertised jobs then saving in a graph database i.e Neo4j.
  5. Develop an api for the scrapped data using django restframework.


TO CRAWL

To crawls "http://ihub.co.ke/jobs"
  1. clone repo
  2. cd IhubJobsSpider
  3. run scrap crawl ihub     # that's it :-)

STORING SCRAPED DATA
Simply cd into project's top directory, then run this command
$ scrapy crawl ihub -o items.csv  # that's to save data as csv
$ scrapy crawl ihub -o items.json # that's to save data as json


NB: Feel free to modify code for your other personal scraping jobs.

__Author__ = 'Edward .A. Okech'
__Email__ = 'okechjobs@gmai.com'


