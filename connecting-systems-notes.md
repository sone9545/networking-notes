# connecting-systems-notes 💯 ✨
## request/response server-side view (how a web-server handles requests/response) 

Web browsers *communicate* with web servers using **H**yper **T**ext **T**ransfer **P**rotocol **(HTTP)**:
when click a link, submit a form, run a search, the browser send an HTTP request to the server.

### This request includes:
* URL (e.g. HTML file, a particular data point on a server, or a tool to run) identifying the target server and resource
* Method that defines the required action (to get a file or to save/update some data) examples listed below:
  * `GET`: get a specific resource (e.g. HTML file containing information about a product or list of products)
  * `POST`: create a new resource (e.g. add a new article to a wiki)
  * `PUT`: Update an existing resource
* additional information can be encoded with the request (for example, HTML form data)

Web servers wait for client request messages, process them when they arrive, and reply to the web browser with an HTTP response message. The response contains an HTTP Response status code indicating whether or not the request succeeded; the body of a sucessful response to `GET` request would contain the requested resource.

## Status Codes examples:
Status | Meaning | Examples
------------ | ------------- | -------------
2xx | OK (No Error) | 200 OK, 204 No content
3xx | Redirect to different URL | 301 Moved Permanently, 302 Moved Temporarily
4xx | Client Error | 400 Bad Request, 403 Forbidden, 404 Not Found, 418 I'm a teapot
5xx | OK (No Error | 500 Internal Server Error, 503 Service Unavailable

Both static and dynamic websites use exactly the same communication protocol/patterns.

### GET request/response example 
a simple `GET` request by clicking on a link or searching on a site (like a search engine homepage). 

#### The Request
![Screenshot 2023-10-22 at 22 28 55](https://github.com/sone9545/networking-notes/assets/146074161/07d2c9a7-791a-4379-8fde-fece8e3b99f1)

Each line of request contains information about it. The first part is called the **header**, and contains useful information about the request (same way an HTML head contains useful information about the document)

The first and second lines contain most of the information:
* the type of request (`GET`)
* the target resource URL (`/en-US/search`)
* the URL parameters (`q=client%2Bserver%2Boverview&topic=apps&topic=html&topic=css&topic=js&topic=api&topic=webdev`)
* the target/host website (developer.mozilla.org)
* the end of the first line also includes a short string identifying the specific protocol version (`HTTP/1.1`)

The remaining lines contain information about the browser the client used and the sort of responses it can handle.

HTTP requests can also have a body, but it is empty in this case.

#### The response 
Below is the first part of the response

![Screenshot 2023-10-22 at 22 45 12](https://github.com/sone9545/networking-notes/assets/146074161/12742fd3-987c-480a-bcff-64260525a1cf)

* the first line includes the response code `200 OK`, which tells us the request succeeded
* we can see that the response is `text/html` formatted (`Content-Type`).
* we can also see that it uses the UTF-8 character set (`Content-Type: text/html; charset=utf-8`)

At the end of the message we see the **body** content - which contains the actual HTML returned by the request.

The remainder of the response header includes information about the response (e.g. when it was generated), the server, and how it expects the browser to handle the page. 

## Static sites
A static site returns the same hard coded content from the server whenever a particular source is requested. E.g. if you have a page about a product at `/static/myproduct1.html`, the same page will be returned to every user. If you add another similar product to your site, you will need to add another page and this will be inefficient once you have to add thousands of page.

![image](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview/basic_static_app_server.png)

when a user wants to navigate to a page:
1. the browser sends an HTTP `GET` request, specifying the URL of its HTML.
2. the server *retrieves* the requested document from its file system and returns an HTTP response containing the document and an **HTTP Response status code** of "`200 OK`" (server might return a different status code "`404 Not Found`", if the file is not present on the server, or "`301 Moved Permanently`" if the file exists but has been redirected to a different location.

server for a static site will only ever need to process GET requests, because the server doesn't store any modifiable data. It also doesn't change its response based on HTTP request data.

## Dynamic sites
A dynamic site can generate and return content based on the specific request URL and data (rather than always returning the same hard code file for a particular URL). Using the example of a product site, the server would store product "data" in a database rather than individual HTML files.

When receiving an HTTP `GET` Request for a product:
- server determines the product ID, fetches the data from the database
- and then constructs the HTML page for the response by **inserting the data into an HTML template**

using a database allows the product information to be stored efficiently in an extensible, modifiable, and searchable way.

### Anatomy of a dynamic HTTP request
#### Example: a website for a coach to select the team name and team size in an HTML form and get back a suggested "best lineup" for the next game

The main elements of the website and the sequence number of the operations are shown in the diagram below. The parts of the website that make it dynamic are Web Application (the server-side code that processes HTTP requests and return HTTP responses), the database which contains info about players, teams, coaches and HTML templates.


![image](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview/web_application_with_html_and_steps.png)

After the coach submits the form with the team name and number of players, the sequence of operations is:
1. web browser creates an HTTP `GET` request to the server using the base URL for the resource (`/best`) and encoding the team and player number either as URL parameters (`/best/team=my_team_name&show=11`)(note: `GET` request is used because the request is only fetching data.
2. Web Server detects that the request is "dynamic" and forwards it to the Web Application for processing.
3. Web Application identifies that the intention of the request is to get the "best lineup" based on the URL (`/best/`) and finds out the required team name and number of players from the URL. Web Application then gets the required information from the database (using additional "internal" parameter to define which players are "best")
4. Web Application dynamically creates an HTML page by putting the data of "best players" (from the Database) into **placeholders** inside an HTML template.
5. Web Application returns the generated HTML to the web browser (via the Web Server), along with an HTTP status code of "`200 OK`". If anything prevents the HTML from being returned then the Web Application will return another code.
6. web browser start to process the return HTML, sending separate requests to get any other CSS or Javascript files that it references.
7. Web Server loads static files from the file system and returns them to the broswer directly. 

[Reference](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview)
