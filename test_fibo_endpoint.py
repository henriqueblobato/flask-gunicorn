from app import app
import unittest
from cache_test import cache

'''
For the tests, please use cache_test on app.py

    from cache_test import cache
'''


class TestFibonacci(unittest.TestCase):

    def value_parameter(self, n=1):
        tester = app.test_client()
        response = tester.get('/fib', query_string=dict(n=n))
        self.assertEqual(200, response.status_code)
        value = int(response.data.decode())
        self.assertEqual(cache[n], value)

    def test_1_to_300(self):
        for i in range(1,301):
            self.value_parameter(n=i)


if __name__ == '__main__':
    unittest.main()