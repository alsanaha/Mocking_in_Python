import unittest
from mock import Mock, MagicMock, patch
#from ex_source_module import SomeClass
import ex_source_module
#real = SC()

class tasting_class(unittest.TestCase):

    # 1 -- Mock Patching Methods
    def test_mock_patch_methods(self):
        print("\n\ntest_mock_patch_methods")
        real = ex_source_module.SomeClass()
        # Mock and MagicMock are usually interchangeable
        # real.one_plus_one = MagicMock(name="one_plus_one")
        real.one_plus_one = Mock(name="one_plus_one")
        real.one_plus_one([4, 5])
        real.one_plus_one.assert_called_with([4, 5])
        print(real.one_plus_one.mock_calls)

    # 2 -- Mocking an object
    def test_mocking_object_methods(self):
        print("\n\ntest_mocking_object_methods")
        real = ex_source_module.SomeClass()
        mock_twitter = Mock(name="mock_twitter")
        real.one_plus_one_tweet(mock_twitter, [1, 2])
        # mock object attribute "PostUpdate" is created on the fly upon call
        mock_twitter.PostUpdate.assert_called_with(3)
        print(mock_twitter.PostUpdate.mock_calls)


    # 3 -- Mocking Classes
    def test_mocking_classes(self):
        print("\n\ntest_mocking_classes")

        def some_function():
             instance = ex_source_module.SomeClass()
             return instance.one_plus_one([0, 2])

        with patch("ex_source_module.SomeClass") as mock:
            inst = mock.return_value
            inst.one_plus_one.return_value = "return value"
            res = some_function()
            assert res == "return value"
            inst.one_plus_one.assert_called_with([0,2])
            print(inst.one_plus_one.mock_calls)

    # 4 -- Naming Mocks
    def test_naming_mocks(self):
        print("\n\ntest_naming_mocks")
        mock = MagicMock(name='foo', return_value=5)
        mock()
        mock.method(17)
        print(mock.mock_calls)

    # 5 -- side effects
    def test_mock_side_efects(self):
        print("\n\ntest_mock_side_efects")
        vals = {(1, 2): 1, (3, 4): 7}

        def side_effect(*args):
            return vals[args]
        mock = Mock(side_effect=side_effect)
        res = mock(3,4)
        assert res == vals[(3,4)]
        # we could set the side effect to be an exception
        # or an iterable. here each call to the mock will return the next item in the iterable

        l = [1, 2, 3]
        mock = Mock(side_effect=l)
        for k in range(0, len(l)):
            res = mock()
            assert res == l[k]

    # 6 -- Specing a mock
    def test_specing_a_mock(self):
        print("\n\ntest_specing_a_mock")
        mock = Mock(spec=ex_source_module.SomeClass)
        mock.one_plus_one([2, 3])

        # spec also enables argument matching and assertion
        def f(a, b, c): pass

        mock = Mock(spec=f)
        mock(1, 2, 3)
        mock.assert_called_with(a=1, b=2, c=3)

        # to prevent 




if __name__ == '__main__':
    unittest.main()

