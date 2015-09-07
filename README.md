# Description
This repository isfor Rubicon interview programming exam question#2 - Write a program to process a file:

1. To support a REST GET call.
   - The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. I.e. given n = 5, appropriate output would represent the sequence "0 1 1 2 3".
   - Given a negative number, it will respond with an appropriate error.
2. Include whatever instructions are necessary to build and deploy/run the project. "deploy/run" means the web service is accepting requests and responding to them as appropriate.
3. Add enough unit tests. add some functional tests. list all other tests you would think of.
4. While this project is admittedly trivial, approach it as representing a more complex problem that you'll have to put into production and maintain for 5 years.
5. Target to finish this in 2 days.

All of the runnable scripts has been tested at Linux machine with Python 2.6.8, which is my devkit.

# Deploy and Run
## Install Tornado
The Fibonacci web service leverage [Tornado](http://www.tornadoweb.org/en/stable/index.html) Python web framework, which is an asynchronous networking library. Its source code pacakge (tornado-4.2.1.tar.gz) is put together with this Fibonacci web service repository. Follow the steps below to install it in the machine that are going to run the Fibonacci web service.
```
cd fibonacci-web-service
tar xvzf tornado-4.2.1.tar.gz
cd tornado-4.2.1
python setup.py build
sudo python setup.py install
```

## Start the server
The Fibonacci web service server can be simply started by running fibonacci_web_service.py as follows:
```
cd fibonacci-web-service/bin/
./fibonacci_web_service.py
Starting the server...
Listen on 8888...
```

By default cache is disabled and port is 8888, refer to its usage bellow to enable cache or listen on a customized port:
```
./fibonacci_web_service.py -h

SYNOPSIS
    A RESTful web service server to handle Fibonacci sequence request with length specified

OPTIONS
    Use the following options to specify a function:
    -h, --help
        Print this usage information
    -p, --port <port>
        Specify the port of this server to listen on.
        Default port 8888 will be used if not specified this option.
    -c, --cache <cache size>
        Specify how many cache (keep first xxx number in memory) the server will use to speed up the request handling
        Cache will be disabled if not specified this option. Below gives some cache size for reference:
        * Cache first 1000 number - need about 103KB memory
        * Cache first 2000 number - need about 409KB memory
        * Cache first 3000 number - need about 919KB memory

EXAMPLES
    # Start the server with default port 8888 and with cache disabled
    ./fibonacci_web_service.py

    # Start the server with default port 8001 and cache first 1000 number in sequence
    ./fibonacci_web_service.py -p 8001 -c 1000

```

## Send RESTful Request
Open a web broswer and type URL as follows (replace the IP with the real one of your server, and 10 is the fibonacci sequence length to request):
```
http://10.32.118.189:8888/fibonacci/10
```

The response body will be:
```
0 1 1 2 3 5 8 13 21 34
```

For invalid URL, or invalid length like negative number or non-number string, 404 error will be returned.

# Documentation 
For the 5-year maintenance purpose, a word document doc/fibonacci-web-service.docx is created to cover following table of contents. And the content is also dumped to the wiki of this repository.
```
- Architecture
- Design and Implementation
    - Request and Response Format
    - Fibonacci Web Server
    - Fibonacci Library
    - Cache
- Test
    - Unit Test
    - Functional Test
- Extendibility
- Scalability
```
