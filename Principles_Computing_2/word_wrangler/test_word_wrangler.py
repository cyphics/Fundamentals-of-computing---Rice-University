import unittest
import word_wrangler as ww


class Tests(unittest.TestCase):

    def testRemoveDuplicates1(self):
        list = [1, 1, 2, 3]
        new_list = ww.remove_duplicates(list)
        self.assertEqual(new_list, [1, 2, 3])

    def testRemoveDuplicates2(self):
        list = [1, 1, 2, 3, 3]
        new_list = ww.remove_duplicates(list)
        self.assertEqual(new_list, [1, 2, 3])

    def testRemoveDuplicates3(self):
        list = [1, 2, 2, 2, 3, 3]
        new_list = ww.remove_duplicates(list)
        self.assertEqual(new_list, [1, 2, 3])

    def testIntersect1(self):
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        self.assertEqual(ww.intersect(list1, list2), [2, 3])

    def testIntersect2(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertEqual(ww.intersect(list1, list2), [1, 2, 3])

    def testIntersect3(self):
        list1 = [1, 2, 3]
        list2 = [4, 4, 5]
        self.assertEqual(ww.intersect(list1, list2), [])

    def testIntersect4(self):
        list1 = [1, 2, 3, 3]
        list2 = [3, 4, 5]
        self.assertEqual(ww.intersect(list1, list2), [3])

    def testIntersect5(self):
        list1 = [1, 2, 3, 3]
        list2 = [3, 3, 4, 5]
        self.assertEqual(ww.intersect(list1, list2), [3, 3])

    def testMerge1(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(ww.merge(list1, list2), [1, 2, 3, 4, 5, 6])

    def testMerge2(self):
        list2 = [1, 2, 3]
        list1 = [4, 5, 6]
        self.assertEqual(ww.merge(list1, list2), [1, 2, 3, 4, 5, 6])

    def testMerge3(self):
        list2 = [1, 2, 3]
        list1 = [3, 4, 5]
        self.assertEqual(ww.merge(list1, list2), [1, 2, 3, 3, 4, 5])

    def testMerge4(self):
        list2 = [1]
        list1 = []
        list3 = [1, 2]
        part1 = list2[:len(list2) // 2 + 1]
        part2 = list2[len(list2) // 2:]
        part3 = list3[:len(list3) // 2 + 1]
        part4 = list3[len(list3) // 2:]

        print(part1, part2)
        print(part3, part4)
        self.assertEqual(ww.merge(list1, list2), [1])

    def testMerge5(self):
        list2 = []
        list1 = []
        self.assertEqual(ww.merge(list1, list2), [])

    def testMergeSort1(self):
        list = [2, 1, 4, 3]
        self.assertEqual(ww.merge_sort(list), [1, 2, 3, 4])

    def testMergeSort2(self):
        list = [2, 2, 2, 1]
        self.assertEqual(ww.merge_sort(list), [1, 2, 2, 2])

    def testMergeSort3(self):
        list = [6, 4, 2, 2, 1]
        self.assertEqual(ww.merge_sort(list), [1, 2, 2, 4, 6])

    def testMergeSort4(self):
        list = [1, 2]
        self.assertEqual(ww.merge_sort(list), [1, 2])

    def testGenAllStrings1(self):
        word = "a"
        a_list = []
        a_list.append("")
        self.assertEqual(ww.gen_all_strings(word), ['', 'a'])

    def testGenAllStrings2(self):
        word = "ab"
        self.assertEqual(ww.gen_all_strings(word), ['', 'a', 'b', 'ab', 'ba'])

    def testGenAllStrings3(self):
        word = "aab"
        self.assertEqual(ww.gen_all_strings(word), ['', 'a', 'a', 'aa', 'aa', 'b', 'ab', 'ba', 'ab', 'aab', 'aab', 'aba', 'ba', 'aba', 'baa', 'baa'])




def main():
    unittest.main()

if __name__ == '__main__':
    main()
