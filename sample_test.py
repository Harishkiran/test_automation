import global_var
import unittest
import create_test_report


#
#
#
#
class SampleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger = global_var.logger
        global_var.create_test_report = create_test_report.createTestReport()
        global_var.create_test_report.create_test_report_header()
        global_var.create_test_report.create_test_report_table()

    @classmethod
    def tearDownClass(cls):
        # Suite Deconfig
        # cls.commonLibHdl.suite_deconfig()
        pass

    def setUp(self):
        self.testresult = {}
        pass

    def tearDown(self):
        global_var.create_test_report.write_to_test_report(self.testresult)

    def test_b(self):
        self.testresult['name'] = 'Test_B'
        self.testresult['summary'] = 'Sample Passing test'
        self.testresult['result'] = 'PASS'
        self.testresult['comment'] = ''

        self.assertTrue(True)

    def test_a(self):
        self.testresult['name'] = 'Test_B'
        self.testresult['summary'] = 'Sample Passing test'
        self.testresult['result'] = 'FAIL'
        self.testresult['comment'] = 'Here,,This Can contain Error Logs'

        self.assertTrue(False)


if __name__ == '__main__':
    print('Main')
    unittest.main()