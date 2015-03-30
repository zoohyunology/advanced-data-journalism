# Scraping assignment

This assignment will give you a chance to write a simple scraper, along the lines of the one we wrote in class. Except rather than looking at people booked into the Boone County Jail, we'll be looking at lobbyist payments to Columbia officials. In practice, something like this could be scheduled to run daily to notify you whenever a new expense is filed.

Just like last time, we'll be working from two files. The [lobbying data](http://www.mec.mo.gov/EthicsWeb/Lobbying/LB14_PubOff.aspx) comes from the Missouri Ethics Commission. But rather than using urllib2 to scrape it from the internet, we'll be using the static **page.html** file included in this folder as the input. This is mostly so we don't annoy the Ethics Commission with a bunch of requests.

There's a bit of code in **scrape.py** to start from, as before. Your job will again be to fill up the output list.

The [scraper we've already built](https://github.com/cjdd3b/advanced-data-journalism/blob/master/spring-2015/first-scraper/scraper.py) can serve as a useful model here, but we'll be adding a little bit of complexity. The assignment will be due **Wednesday, March 18**.

Parts of assignment
-------------------

- First, grab all the lobbyist expenditures from the table
- Skip, or ignore, the column that says "View"
- If the transaction is for an official in Columbia, add it to the output list
- Remove the &nbsp; string from all output where it appears
- At the end, print the output list
