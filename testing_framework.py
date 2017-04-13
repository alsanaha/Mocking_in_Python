import unittest
from mock import Mock
from ex_source_module import SomeClass

class test_ex_source_module_1(unittest.TestCase):
    def test_example_1(self):
        mock_twitter = Mock()
        args = [2, 5]
        ex_source_module = SomeClass()
        ex_source_module.one_plus_one_tweet(mock_twitter, args)
        # .mock_calls is really powerful and records all the calls to the mock and it's children
        # Mock(spec=SomeModule) defines and interface to the mock to only defined functions from SomeModule can be
        # called
        print(mock_twitter.mock_calls)
        print()

    def test_example_2(self):
            mock_twitter = Mock()
            args = [4, 15]
            ex_source_module = SomeClass()
            ex_source_module.one_plus_one_tweet(mock_twitter, args)
            # .mock_calls is really powerful and records all the calls to the mock and it's children
            # Mock(spec=SomeModule) defines and interface to the mock to only defined functions from SomeModule can be
            # called
            print(mock_twitter.mock_calls)


if __name__ == '__main__':
    unittest.main()