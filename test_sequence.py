from unittest import TestCase
from sequence import Sequence

 
class TestSequence(TestCase):
 def test_process(self):
     self.assertEqual([0], Sequence().sequence(""), "Empty Sequence")
     self.assertEqual([1], Sequence().sequence("1"), "Empty Sequence")