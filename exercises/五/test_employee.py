"""

为Employee编写一个测试用例，其中包含两个测试方法：test_give_default_raise()和test_give_custom_raise()。
使用方法setUp()，以免在每个测试方法中都新建雇员实例。运行这个测试用例，确认两个测试都通过了。

"""


import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.someone = Employee("lao","wang",6000)

    def test_give_default_raise(self):
        self.assertEqual(self.someone.raises,6000)

    def test_give_custom_raise(self):
        self.someone.give_raise(6000)
        self.assertEqual(self.someone.raises,12000)


if __name__ == '__main__':
    unittest.main