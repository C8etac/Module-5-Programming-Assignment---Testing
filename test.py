import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()


"""What’s Happening Here?
The Test Name:
test_list_int (test.TestSum) tells you exactly what test was run.
test_list_int: This is the method in your test class you wrote to test summing integers.
TestSum: The test case class that groups all the tests for your sum() function.

The Result:
That little "ok" at  i, that’s the golden ticket the test passed without any iThis means thatt means the code did what was expected: it took [1, 2, 3] and gave back 6. 

Test Summary:
Ran 1 test means that unittest successfully ran exactly one test. The "OK" at the bottom means all the tests run passed. The function is bug-free, at least for the scenarios tested.

If Things Go Wrong:
The test ran but didn’t pass, the 'AssertionError:' is the test runner’s way of saying, “The output didn’t match what you were expecting.”

Why Does This Matter?
Passing a test means that the 'sum()' function behaves as expected for this specific case. Saying, 'Hey, your code is solid when it comes to adding up a list of integers.' But there is a catch, just because it passed one test doesn’t mean it’s foolproof. Like taking one quiz and getting an A, there is still a whole semester of material to cover. The more tests we write and pass, tt more confidence we can be that our code won’t break when someone tries something funky, like passing a tuple or a single inte'ger. Testing isnt just about looking g'ood in green. Its our safety net, so as we tweak, refactor, or scale our code, nothing sneaky breaks in the background."""
