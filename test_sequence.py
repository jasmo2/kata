from unittest import TestCase
from sequence import Sequence

 
class TestSequence(TestCase):
 def test_n_elements(self):
     self.assertEqual([0], Sequence().sequence(""), "Empty Sequence")
     self.assertEqual([1], Sequence().sequence("1"), "1 number Sequence")
     self.assertEqual([2], Sequence().sequence("1,2"), "2 number Sequence")
     self.assertEqual([4], Sequence().sequence("0,1,2,3"), "N number sequence")

 def test_min_element(self):
     self.assertEqual([0,0], Sequence().min_el(""), "Empty Sequence min Elements")
