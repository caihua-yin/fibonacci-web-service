#!/usr/bin/python

import unittest
import test_fibonacci

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # Add test cases
    suite.addTest(unittest.TestLoader().loadTestsFromModule(test_fibonacci))

    unittest.TextTestRunner(verbosity=2).run(suite)

