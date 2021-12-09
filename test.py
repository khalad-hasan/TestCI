import unittest
from unit_test.test_freemembership import TestFreeMembersip
from unit_test.test_basicmembersip import TestBasicMembersip
from unit_test.test_premiummembership import TestPremiumMembersip
from unit_test.test_user_bankinfo import test_user_bank_info
from unit_test.test_user_personal_info import test_user_personal_info
from unit_test.test_user_service import test_user_service

# if __name__=="__main__":
#     unittest.main(argv=[''],verbosity=2)


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    tests=[TestFreeMembersip,TestBasicMembersip,TestPremiumMembersip,test_user_bank_info,test_user_personal_info,test_user_service]
    for test in tests:
        suite.addTest(unittest.makeSuite(test))    
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()