# Week 5

## Some Updates
1. The link to me: www.tinyurl.com/swe-python5
2. Join our Slack! https://umiami-orgs.slack.com/messages/C98DU69QF/
3. Check out [Coursera's Python Sequence](https://www.coursera.org/specializations/python)
    - It's great to learn a language from a couple of different perspectives
4. Fun stuff: Go read some of Paul Graham's Essays
    - http://www.paulgraham.com/love.html

## Python Exercises to Get Things Rolling
1. [Google Python Exercises](https://developers.google.com/edu/python/exercises/basic)
    - Start with the `basic` folder. Lots of good stuff!
    - Solutions are provided. Try to go as far as you can yourself, but don't be afraid to get help
    - Reading other people's code is super useful.
2. Don't underestimate the importance of grinding through exercises and practice!
    - Coding is a craft. Loving it makes it super easy to do it well
3. What are you looking to work on?

    
# Version Control: Git
1. First, it's super practical to run programs on your own computer.
2. `Repl.it` is fantastic, but over the long term, use Python on your computer
3. Saving code matters. Sharing code matters! Use Git.
    - [90% of developers](https://insights.stackoverflow.com/survey/2018/#work-version-control) use Git
4. For now, just use a [GitHub account](github.com/)
5. But at home, definitely [download Git](https://git-scm.com/downloads)

# Python Modules 

## A Great Companion Resource

# What is a REST API?
1. How most applications get information from the internet
2. Use cases
    - Communicating between websites: Amazon talks to your PayPal account
    - Programming a website without interacting with the graphical user interface
        - Useful if you want a LOT of data. GUIs make things slower
3. Good resource for more in depth info: https://restful.io/an-introduction-to-api-s-cee90581ca1b

## REST Request Process
![alt text](https://cdn-images-1.medium.com/max/1600/0*bYF8loGdnpHklSKS.gif)

## Types of REST Requests: Methods
1. GET - Ask a server to retrieve content
2. POST - Ask a server to create a 'resource' on the server
3. PUT - Ask the server to edit/update an existing 'resource'
4. DELETE - Ask the server to delete a resource

## Parts of a REST Request
1. URL 
    - who knew it stood for "Uniform Resource Locator"???
2. Method
3. List of Headers 
    - For example: Communicating what types of data we can accept
4. Body 
    - Information about the REST request

## REST Response
![](https://cdn-images-1.medium.com/max/1600/0*EEhV9BlXgsTFnBW8.gif)
1. Classic Status Codes
    - `200` - All clear!
    - `401` - You don't have API credentials. You aren't authenticated
    - `400` - You made a bad request! The server doesn't understand what you asked for
    - `404` - The server couldn't find the item you are trying to access

## Let's Try It Out!
### Things We Will Use
1. Open API From Space: http://open-notify.org/
2. The `requests` module from Python
    - Documentation here: http://docs.python-requests.org/en/master/

### The Open API From Space 
1. Current Location of the ISS
    - `GET` from URL: http://api.open-notify.org/iss-now.json
2. Next time ISS will pass overhead
    - `GET` from same URL with parameters
    - `latitude` and `longitude`

### Using `requests`
1. `requests` library has `get`, `post`, `put`, and `delete` methods
2. For example: `requests.get("google.com")` would get a request from Google.com
3. Depending on the function, we can see what parameters it takes.
    - Let's try it: http://docs.python-requests.org/en/master/api/#requests.get
4. Returns `Response` object

### Let's Try It Out!

```
import requests

space_url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(space_url)

print("Printing 'response':", response)
print("Status Code:", response.status_code)
print("Content:", response.content)

```

### JSON...Merp
1. For now, we'll just figure out how to print it prettily
2. "Magic" Code to make the output of Content to look pretty
```
import json
your_json = your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
parsed = json.loads(your_json)
print json.dumps(parsed, indent=4, sort_keys=True)
```

### Finishing up our example
1. Include the JSON code as a new function 
2. Pass `response.content` to it and print it out
3. But what if we want to just get the latitude and longitude from the response, not the whole text?

### Understanding JSON: JavaScript Object Notation
https://www.digitalocean.com/community/tutorials/an-introduction-to-json
1. JSON is a way to store lists and dictionaries.
2. Very convenient to pass around data
3. When we have a JSON file, we can think of it as just a bunch of text, or  we can use something that will parse it into lists and dictionaries
4. Dictionaries of dictionaries of dictionaries of ...
5. `json` library documentation: https://docs.python.org/2/library/json.html

# Thoughts for Projects to Work On
1. Read through the links on REST APIs. They will help you understand more how REST works.
2. Find an API and figure out how to use it. Some thoughts on APIs to try: 
    - https://automatetheboringstuff.com/list-of-json-apis.html
    - Google Maps
    - Reddit
    - Twitter
    - [NYTimes](https://developer.nytimes.com/)

