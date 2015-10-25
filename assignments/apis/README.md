# API assignment (Oct. 24)

For this assignment, you'll ne using the State Department's unofficial FOIA Virtual Reading Room API to download and process information about Hillary Clinton's e-mails. The API powers [this site](https://foia.state.gov/search/results.aspx), which is an online dumping ground of documents released by the State Department under FOIA.

Some (rough) documentation for the API follows:

  - **Base URL**: https://foia.state.gov/searchapp/Search/SubmitSimpleQuery
  - **API Key**: Like most unofficial APIs, this doesn't have one.

Parameters:

  - **searchText**: Returns e-mails with text matching particular string. Use * to return everything
  - **beginDate** and **endDate**: Filter by the range of dates on which the e-mails were sent. Format for each date is MM/DD/YYYY. Or enter false to return everything.
  - **postedBeginDate** and **postedEndDate**: Filter by the range of dates on which the e-mails were posted. Format for each date is MM/DD/YYYY. Or enter false to return everything.
  - **caseNumber**: Return an e-mail corresponding to a specific case number. Use false to return everything.
  - **collectionMatch**: No idea. Just pass false.
  - **page**: The page number returned from a series of paginated results. Works in conjunction with "limit."
  - **start**: The first record to return from a series of paginated results.
  - **limit**: The number of records that should be returned per page in the response.

** Questions **

You'll be writing code to answer several different questions. All code should be kept in the same file -- just indicate which piece of your code answers which question using comments.

  1. Filter to just Hillary Clinton's e-mails (case number F-2014-20439)
  2. Request all e-mails containing the word Benghazi
  3. Return all e-mails and print the information necessary to download their raw files from the State Department.

The assignment is due on **Friday, Oct. 30**. Good luck!