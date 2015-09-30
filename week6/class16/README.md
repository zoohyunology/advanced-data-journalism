# Class 16 (Wednesday, Sept. 30, 2015)

We'll talk about the solution to the first assignment (which I'll load into the "assignments" folder after class) and then start writing a simple scraper, which will grab the names of inmates booked each night into the [Boone County jail](https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s).

We'll also use this as an opportunity to discuss how to break down large programming problems into small, discrete tasks, which is an organizational trick many developers use to simplify complex tasks. Specifically, we'll break down our scraper like this:

  - First, get the HTML of the Boone County jail page and load it into Python
  - Next, isolate the part of the page we want to scrape
  - Grab just one field from the inmates table and print it out
  - Now that we can grab one field, try grabbing all of them from a single row
  - Store that row as a Python data structure
  - Repeat the above with all rows
  - Save the results to a CSV