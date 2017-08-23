# -*- coding: UTF-8 -*-
import unittest
from picture_category import pic_exif

class TestPicExif(unittest.TestCase):

    def setUp(self):
        self.picFile = 'F:\\DCIM\\100ANDRO\\DSC_0004.JPG'

    def tearDown(self):
        self.picFile = None

    def testGetExif(self):
        self.assertIsNotNone(pic_exif.get_exif(self.picFile), 'test success')

if __name__=='__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestPicExif("testGetExif"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)