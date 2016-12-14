# Description
The tests directory maintains the unit testing and functional testing scripts. The information below shows how to run unit test and functional test. For more detail, refer to doc/fibonacci-web-service.docx.

# Run Unit Test
Execute unit_test.py to run the unit test for fibonacci library as follows:
```
./unit_test.py
test_fibonacci (test_fibonacci.FibonacciTestCase) ... ok
test_fibonacci_no_recursive (test_fibonacci.FibonacciTestCase) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

# Run Functional Test
Execute functional_test.py to run the functional test for this Fibonacci web service as follows:
```
./functional_test.py
Host: localhost, Port: 8888
Test normal cases...
[SUCCESS] Fibonacci request (length=0) functional testing passed.
[SUCCESS] Fibonacci request (length=1) functional testing passed.
[SUCCESS] Fibonacci request (length=5) functional testing passed.
[SUCCESS] Fibonacci request (length=300) functional testing passed.
[SUCCESS] Fibonacci request (length=2000) functional testing passed.
```
For negative cases like negative or invalid length, or invalid URL, 404 Error are expected, and they can be tested by web browser manually. They are not automated by functional_test.py currently due to time limitation.

