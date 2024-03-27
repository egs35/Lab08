# Reflection

## What is a web server?
A web server is software or hardware that serves content, such as web pages, to clients over the internet or a local network. It processes requests from clients (typically web browsers) and returns the requested resources, such as HTML files, images, or other types of data.

## How do users access resources from a web server?
Users access resources from a web server by sending HTTP requests to the server using a web browser or other client applications. These requests specify the desired resource (e.g., a URL for a web page or a file) and the server responds with the requested resource, typically in the form of an HTTP response containing the resource's data.

## What are GET and POST?
GET and POST are two HTTP methods used to send data from a client (such as a web browser) to a web server.

- **GET**: This method is used to request data from a specified resource. When a client sends a GET request, the data is sent in the URL's query string. GET requests are typically used for retrieving data and should not be used for sensitive or large amounts of data, as the data is visible in the URL.
  
- **POST**: This method is used to submit data to be processed to a specified resource. Unlike GET requests, POST requests send data in the HTTP request body, making them suitable for sending large amounts of data and for sending sensitive information, such as login credentials. POST requests are commonly used for submitting forms and interacting with web applications.
