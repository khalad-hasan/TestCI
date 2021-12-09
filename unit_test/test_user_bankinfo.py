import unittest
from io import StringIO
from unittest.mock import patch
import budgetplanner.user_subpackage as user
import budgetplanner.user_subpackage.personal_info as personal_info
import budgetplanner.user_subpackage.service as service
import budgetplanner.user_subpackage.bank_info as bank_info
class test_user_bank_info(unittest.TestCase):
    def setUp(self):
        self.password = bank_info.password("001","abc")
        self.password2 = bank_info.password("002","def")
        self.password3 = bank_info.password("003","defg")
        self.password4 = bank_info.password("004","defgh")
        self.password5 = bank_info.password("005","defgh")
    def test_password(self):
        self.password.update("001","abcd")
        self.assertEqual(self.password.password,"abcd")
        self.password2.update("002","abcd")
        self.assertEqual(self.password2.password,"abcd")
        self.password3.update("003","abcd")
        self.assertEqual(self.password3.password,"abcd")
        self.password4.update("004","abcd")
        self.assertEqual(self.password4.password,"abcd")
        self.password5.update("005","abcd")
        self.assertEqual(self.password5.password,"abcd")
        
        print("test password update success")
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.password.show()
            self.assertEqual(fakeoutput.getvalue(),'userid: {} password: {}\n'.format("001","abcd"))
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.password2.show()
            self.assertEqual(fakeoutput.getvalue(),'userid: {} password: {}\n'.format("002","abcd"))
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.password3.show()
            self.assertEqual(fakeoutput.getvalue(),'userid: {} password: {}\n'.format("003","abcd"))
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.password4.show()
            self.assertEqual(fakeoutput.getvalue(),'userid: {} password: {}\n'.format("004","abcd"))
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.password5.show()
            self.assertEqual(fakeoutput.getvalue(),'userid: {} password: {}\n'.format("005","abcd"))
        
        print("test password show success")
        self.password.delete()
        self.assertEqual(self.password.userid,"")
        self.assertEqual(self.password.password,"")
        self.password5.delete()
        self.assertEqual(self.password5.userid,"")
        self.assertEqual(self.password5.password,"")
        self.password2.delete()
        self.assertEqual(self.password2.userid,"")
        self.assertEqual(self.password2.password,"")
        self.password3.delete()
        self.assertEqual(self.password3.userid,"")
        self.assertEqual(self.password3.password,"")
        self.password4.delete()
        self.assertEqual(self.password4.userid,"")
        self.assertEqual(self.password4.password,"")
        print("test password delete success")
if __name__ == '__main__':
    unittest.main()