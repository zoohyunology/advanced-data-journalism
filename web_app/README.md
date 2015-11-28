# Building a web application

Now that we've already reverse engineered a couple web applications in our web scraping and API units, we'll spend the next couple weeks looking at web applications from another perspective: namely, engineering them in the first place.

Interactive applications and data visualizations are typically composed of several pieces, each of which can live on the client or the server, depending on the application.

<table>
    <tr>
        <th>Component</th>
        <th>Client-side version</th>
        <th>Server-side version</th>
    </tr>
    <tr>
        <td>Data</td>
        <td>JSON files</td>
        <td>Database (MySQL, PostgreSQL, etc.)</td>
    </tr>
    <tr>
        <td>Text and layout elements</td>
        <td>Raw HTML files, Javscript templates</td>
        <td>Dynamic templating (Jinja)</td>
    </tr>
    <tr>
        <td>Visualization components</td>
        <td>Javascript (D3.js, etc.)</td>
        <td>Visualization libraries such as matplotlib (rarely used)</td>
    </tr>
</table>

As computers and web browsers have become more powerful, more and more interactives have started relying on client-side technologies rather than server-side ones. This is largely because client-side visualizations tend to offer better performance, while at the same time being cheaper to host and more resistent to crashes. Here are a couple examples of this more client-side model:

  - [Mapping the Decline of Stop and Frisk](http://www.nytimes.com/interactive/2014/09/19/nyregion/stop-and-frisk-map.html)
  - [2014 Midterm Election Results](http://elections.nytimes.com/2014/results/senate)

The server-side model still has a place -- particularly when it comes to more complex applications that might involve exploring multiple pages, or integrated search functionality, where the added muscle of a server can come in handy. We'll contrast the above examples with these, to illustrate the difference:

  - [Dollars for Docs](https://projects.propublica.org/docdollars/)
  - [Texas Government Salaries Explorer](http://salaries.texastribune.org/)

Finally, we'll build our own simple application so you can see these differences firsthand.