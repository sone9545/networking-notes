# connecting-systems-notes
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





# EMPHASIS
*This text will be italics*
**This text will be bold**
*you **can** combine them*

# BLOCKQUOTES
>this is a blockquote

# LISTS
### unordered lists
* Item 1
* Item 2
  * Item 2a
  * Item 2b

### ordered lists
1. Item 1
2. Item 2
  * Item 2a
  * Item 2b

# IMAGES & LINKS
![image](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview/web_application_with_html_and_steps.png)
[image](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview/web_application_with_html_and_steps.png)

# BACKSLASH ESCAPES
\*this is some text \*

```javascript
function alert()(
  alert("Hello, world");
)
```
`GET`

# TASK LISTS
- [x] This is a complete task
- [ ] This is an incomplete task

# Tables
First Header | Second Header
------------ | -------------
This is data1 | This is data2
This is data1 | This is data2

# EMOJI
:+1: :sparkles: 
