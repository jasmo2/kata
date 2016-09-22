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
        self.assertEqual([1,1], Sequence().min_el("1"), "1 number Sequence min Elements")
        self.assertEqual([2,1], Sequence().min_el("1,2"), "2 number Sequence min Elements")
        self.assertEqual([5,3], Sequence().min_el("8,3,6,5,7"), "N number Sequence min Elements")

    def test_max_element(self):
        self.assertEqual([0,0,0], Sequence().max_el(""), "Empty Sequence max Elements")
        self.assertEqual([1,1,1], Sequence().max_el("1"), "1 Sequence max Elements")
        self.assertEqual([2,1,2], Sequence().max_el("1,2"), "2 Sequence max Elements")
        self.assertEqual([5,3,8], Sequence().max_el("8,3,6,5,7"), "N number Sequence min Elements")

    def test_average(self):
        self.assertEqual([0,0,0,0], Sequence().average_el(""), "Empty Sequence average Elements")
        self.assertEqual([1,1,1,1], Sequence().average_el("1"), "1 Sequence average Elements")
        self.assertEqual([2,1,8,4.5], Sequence().average_el("1,8"), "2 Sequence average Elements")
        self.assertEqual([6,1,4,2], Sequence().average_el("1,1,1,2,3,4"), "N Sequence average Elements")


