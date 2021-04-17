import unittest
from tests.home.login_tests import LoginTests
from tests.Products.purchase_test import TestOrderProduct

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestOrderProduct)

smokeTests = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTests)
