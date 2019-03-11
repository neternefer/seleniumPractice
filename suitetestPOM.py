import unittest
from testPOM import TestHome
from testPOM import TestAbout

def suite():
    suite = unittest.TestSuite()
    
    suite.addTest(TestHome('test_TC001_py3_doc_button'))
    suite.addTest(TestHome('test_TC002_search_blabla'))
    suite.addTest(TestHome('test_TC004_assert_title'))
    suite.addTest(TestAbout('test_TC003_up_events'))
    suite.addTest(TestAbout('test_TC005_assert_url_contains'))
    '''
    #suites combined
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestHome)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestAbout)
    suite = unittest.TestSuite([suite1, suite2])
    '''
    return suite
    

if __name__ == "__main__":
    suite = suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
