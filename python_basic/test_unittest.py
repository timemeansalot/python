import unittest

def func(value):
    if value==1:
        return 1
    elif value==-1:
        return -1
    else:
        return 0

class MyTest(unittest.TestCase):
    def test_func(self):
        self.assertEqual(func(1),1)
        self.assertEqual(func(-1),-1)
        for i in range(-100,100):
            if i==1 or i==-1:
                continue
            self.assertEqual(func(i),0)


unittest.main()