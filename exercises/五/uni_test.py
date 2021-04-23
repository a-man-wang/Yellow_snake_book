import unittest
from city_functions import show


class ShowTestCase(unittest.TestCase):

    """测试city_functions.py"""

    def test_ture_show(self):
        """能够正确展示吗"""
        result = show("北京","中国")
        self.assertEqual(result,"北京 中国 ")


    def test_ture_show_2(self):
        """能够正确展示吗"""
        result = show("北京","中国",population=50000)
        self.assertEqual(result,"北京 中国 50000")


if __name__ == '__main__':

    unittest.main