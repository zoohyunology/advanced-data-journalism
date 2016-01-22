# Class 2 (Friday, Jan. 22, 2016)

Some housekeeping on tap today, along with some discussion of the three traditional career paths that have developed in the world of "advanced" data journalism: CAR/data analysis, data visualization and building software in newsrooms.

## CAR/data analysis

Sarah Cohen, my colleague at the Times, draws a distinction between "data journalism" and "journalism about data." The former uses data as a tool to pursue a story, like the investigative/CAR-style analyses you're used to. In the latter, the data *is* the story. Think [FiveThirtyEight](http://www.fivethirtyeight.com). Either way, doing data analysis for news requires many of the same skills -- database and spreadsheet skills, statistics, simple programming -- most of which have been in use for [decades](http://www.unc.edu/~pmeyer/book/).

## Data visualization/news applications

The mid to late 2000s saw an explosion in digital story forms that used data in new and interesting ways. Rather than simply analyzing data and providing results in the form of a story, data journalists started building news applications to allow readers to explore and contextualize the data on their own. Others started building sophisticated charts, maps and interactive presentations that used data to tell stories visually.

## Software development for news

Attracted by data visualizations and the growing popularity of data journalism, software developers and data scientists without traditional journalism backgrounds have been pouring into newsrooms over the last several years. Although some work on CAR and data visualization projects, others have focused on tools, templates and open source projects, using their tech skills to solve long-standing newsroom problems and create new products.

- **[Listy](http://www.nytimes.com/interactive/2015/04/14/dining/field-guide-to-the-sandwich.html?_r=0**): Developers at the Times have built a tool that makes it easy for producers and reporters to create list-shaped articles, popularizing a new story form that has been used dozens of times.

- NPR

- **[Campaign finance data deduplication](https://github.com/cjdd3b/fec-standardizer/wiki)**: Most campaign finance data is organized by contribution, not donor. Joe Smith might give three different contributions and be listed in the data in three different ways. Connecting those records into a single canonical Joe Smith is often the first step to doing sophisticated campaign finance analysis. Over the last few years, people have developed highly accurate methods to do this using both supervised and unsupervised machine learning.

- **[NYT Cooking](http://cooking.nytimes.com/)**: The new Cooking website and app has been one of the Times' most successful new products, but it was initially based largely on recipes stored in free-text articles. The Times extracted many of those recipes using an algorithmic technique known as [conditional random fields](http://open.blogs.nytimes.com/2015/04/09/extracting-structured-data-from-recipes-using-conditional-random-fields/). The L.A. Times did something [similar](https://source.opennews.org/en-US/articles/how-we-made-new-california-cookbook/) in 2013.