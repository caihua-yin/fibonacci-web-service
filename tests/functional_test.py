#!/usr/bin/python
import sys
import getopt

# Add module search path
sys.path.append('../lib')

import fibonacci
from tornado import httpclient

def usage():
    """
    Print usage
    """
    usage_str = """
SYNOPSIS
    Functional testing for the fibonacci web service

OPTIONS
    Use the following options to specify a function:
    -h, --help
        Print this usage information
    -a, --host <host name or IP address>
        Specify the hostname or IP that the web service is running
        Default value "localhost" will be used if not specified this option
    -p, --port <port>
        Specify the port of that web service is listening on
        Default port 8888 will be used if not specified this option.

EXAMPLES
    # Do functional testing for localhost:8888
    ./%s

    # Do functional testing for 10.32.118.180:8001
    ./%s -a 10.32.118.180 -p 8001
    """
    print usage_str % ((os.path.basename(sys.argv[0]),) * 2)

def getopts():
    """
    Get command opt arguments
    """
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "ha:p:",
            ["help", "host", "port="])
        return opts
    except getopt.GetoptError:
        usage()

def test_case(host, port, length, expect_response_body, 
                    expect_response_code=200):
    """
    Specific test case execution
    """
    http_client = httpclient.HTTPClient()
    url = "http://%s:%d/fibonacci/%s" % (host, port, str(length))
    response = http_client.fetch(url)
    if response.code == expect_response_code and response.body == expect_response_body:
        print "[SUCCESS] Fibonacci request (length=%s) functional testing passed." % str(length)
    else:
        print "[FAIL] Fibonacci request (length=%s) functional testing failed." % str(length)
        print "Response code: %d, expected: %d" % (response.code, expect_response_code)
        print "Response body: %s, expected: %s" % (response.body, expect_response_body)

def test(host, port):
    """
    Functional test trigger method
    """
    http_client = httpclient.HTTPClient()

    # Normal cases
    print "Test normal cases..."
    # Case#1: Fibonacci request (length=0)
    test_case(host, port, 0, "")
    # Case#2: Fibonacci request (length=1)
    test_case(host, port, 1, "0")
    # Case#3: Fibonacci request (length=5)
    test_case(host, port, 5, "0 1 1 2 3")
    # Case#4: Fibonacci request (length=300)
    test_case(host, port, 300, " ".join(str(item) for item in fibonacci.fibonacci_non_recursive(300)))
    # Case#5: Fibonacci request (length=2000)
    test_case(host, port, 2000, " ".join(str(item) for item in fibonacci.fibonacci_non_recursive(2000)))

def main():
    """
    The main function
    """
    # Set default command option value
    cmd = "test"
    host = "localhost"
    port = 8888

    # Get command option and call corresponding function
    opts = getopts()
    for option, value in opts:
        if option in ("-h", "--help"):
            cmd = "help"
        elif option in ("-a", "--host"):
            host = value
        elif option in ("-p", "--port"):
            try:
                port = int(value)
            except ValueError:
                print "Invalid port value: %s" % value
                sys.exit(1)
        else:
            usage()
            sys.exit(1)

    if cmd == "help":
        usage()
    elif cmd == "test":
        test(host, port)
    else:
        usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
