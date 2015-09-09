#!/usr/bin/python

import os
import sys
import getopt

# Add module search path
sys.path.append('../lib')

import fibonacci
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url

def usage():
    """
    Print usage
    """
    usage_str = """
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
        * Cache first 1000 number - need about 244KB additional memory
        * Cache first 2000 number - need about 840KB additional memory
        * Cache first 3000 number - need about 1756KB additional memory

EXAMPLES
    # Start the server with default port 8888 and with cache disabled
    ./%s

    # Start the server with default port 8001 and cache first 1000 number in sequence
    ./%s -p 8001 -c 1000
    """
    print usage_str % ((os.path.basename(sys.argv[0]),) * 2)

def getopts():
    """
    Get command opt arguments
    """
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hp:c:",
            ["help", "port=", "cache="])
        return opts
    except getopt.GetoptError:
        usage()

class FibonacciHandler(RequestHandler):
    # Static variable definition
    cache = []
    cache_in_str = []

    @classmethod
    def initialize_cache(cls, cache_size):
        """
        Initialize cache according to specified size
        """
        print "Initialize cache (size: %d)..." % cache_size
        # The int list cache is for requested length is larger than cache,
        # so the furthr calculation can base on it
        cls.cache = fibonacci.fibonacci_non_recursive(cache_size)

        # The string list cache for the requested length is not larger than cache,
        # so the response can be constructed directly from it.
        # Maintain this list can avoid the int to string convertion for every request handling
        cls.cache_in_str = [str(item) for item in cls.cache]

    def get(self, fibonacci_length):
        """
        Handle get request
        """
        length = int(fibonacci_length)
        if length <= len(FibonacciHandler.cache_in_str):
            self.write(' '.join(FibonacciHandler.cache_in_str[:length]))
        else:
            result = fibonacci.fibonacci_non_recursive(length, base=FibonacciHandler.cache)
            self.write(' '.join(str(item) for item in result))

def make_application():
    return Application([
        url(r"/fibonacci/([0-9]+)", FibonacciHandler),
    ])

def start(port, cache_size):
    """
    Start the server
    """
    print "Starting the server..."
    if cache_size > 0:
        # Initialize FibonacciHandler cache
        FibonacciHandler.initialize_cache(cache_size)

    # Start server and listen on specified port
    make_application().listen(port)
    print "Listen on %d..." % port
    IOLoop.current().start()

def main():
    """
    The main function
    """
    # Set default command option value
    cmd = "start"
    port = 8888
    cache_size = 0

    # Get command option and call corresponding function
    opts = getopts()
    for option, value in opts:
        if option in ("-h", "--help"):
            cmd = "help"
        elif option in ("-p", "--port"):
            try:
                port = int(value)
            except ValueError:
                print "Invalid port value: %s" % value
                sys.exit(1)
        elif option in ("-c", "--cache"):
            try:
                cache_size = int(value)
            except ValueError:
                print "Invalid cache size value: %s" % value
                sys.exit(1)
        else:
            usage()
            sys.exit(1)

    if cmd == "help":
        usage()
    elif cmd == "start":
        start(port, cache_size)
    else:
        usage()
        sys.exit(1)

if __name__ == "__main__":
    main()
