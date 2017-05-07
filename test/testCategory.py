# -*- coding: UTF-8 -*-
import unittest
from picture_category import category

class TestAll(unittest.TestCase):

    def setUp(self):
        self.inputDir = 'F:\\photos\\2016.1 vivo'
        self.destDir = 'D:\\test'

    def tearDown(self):
        self.inputDir = None
        self.destDir = None

    def testScanDir(self):
        categoryPicList, unCategoryPicList = category.scanDirGetPic(self.inputDir)
        self.assertEqual(len(categoryPicList),6,'category picture list ')
        self.assertEqual(len(unCategoryPicList), 5, 'uncategory picture list ')

    def testCategory(self):
        self.assertIsNone(category.category(self.inputDir, self.destDir), 'process done')

if __name__=='__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestAll("testScanDir"))
    suite.addTest(TestAll("testCategory"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)