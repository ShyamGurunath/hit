import unittest
from sal import add


class Test_sal(unittest.TestCase):
     
     def test_Add(self):
          self.assertEqual(add(10,5),15)
          self.assertEqual(add(-1,1),0)
if __name__ == '__main__':
     unittest.main()         