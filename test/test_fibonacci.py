import unittest
import sys

# Add module search path
sys.path.append('../lib')

import fibonacci

class FibonacciTestCase(unittest.TestCase):
    def test_fibonacci(self):
        # Test valid length input and verify result
        self.assertEqual(fibonacci.fibonacci(0), [])
        self.assertEqual(fibonacci.fibonacci(1), [0])
        self.assertEqual(fibonacci.fibonacci(2), [0,1])
        self.assertEqual(fibonacci.fibonacci(5), [0,1,1,2,3])        
        self.assertEqual(fibonacci.fibonacci(10), [0,1,1,2,3,5,8,13,21,34])

        # Test negative length input and expect exception
        self.assertRaises(Exception, fibonacci.fibonacci, -4)

    def test_fibonacci_no_recursive(self):
        # Test valid length input and verify result
        self.assertEqual(fibonacci.fibonacci_non_recursive(0), [])
        self.assertEqual(fibonacci.fibonacci_non_recursive(1), [0])
        self.assertEqual(fibonacci.fibonacci_non_recursive(2), [0,1])
        self.assertEqual(fibonacci.fibonacci_non_recursive(5), [0,1,1,2,3])
        self.assertEqual(fibonacci.fibonacci_non_recursive(10), [0,1,1,2,3,5,8,13,21,34])

        # Test a long length input and verify the results between 
        # fibonacci.ibonacci_non_recursive(length) and fibonacci.fibonacci(length)
        self.assertEqual(fibonacci.fibonacci_non_recursive(150), 
            fibonacci.fibonacci(150))

        # Test the result when base sequence input is specified
        self.assertEqual(fibonacci.fibonacci_non_recursive(10), 
            fibonacci.fibonacci_non_recursive(10, [0,1,1,2,3]))

        self.assertEqual(fibonacci.fibonacci_non_recursive(200), 
            fibonacci.fibonacci_non_recursive(200, fibonacci.fibonacci_non_recursive(100)))

        # Test negative length input and expect exception
        self.assertRaises(Exception, fibonacci.fibonacci_non_recursive, -2)
