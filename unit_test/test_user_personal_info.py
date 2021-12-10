import unittest
from io import StringIO
from unittest.mock import patch
import budgetplanner.user_subpackage as user
import budgetplanner.user_subpackage.personal_info as personal_info
import budgetplanner.user_subpackage.service as service
import budgetplanner.user_subpackage.bank_info as bank_info
class test_user_personal_info(unittest.TestCase):
    def setUp(self):
        self.personal_info = personal_info.personal_info(userid="001",age=17,email="w12@gmail.com",income=20)
        self.personal_info2 = personal_info.personal_info(userid="002",age=18,email="w12@gmail.com",income=20)
        self.personal_info3 = personal_info.personal_info(userid="003",age=19,email="w12@gmail.com",income=20)
        self.personal_info4 = personal_info.personal_info(userid="004",age=20,email="w12@gmail.com",income=20)
        self.personal_info5 = personal_info.personal_info(userid="005",age=21,email="w12@gmail.com",income=20)
    def test_personal_info(self):
        self.personal_info.update("001",18,"w123@gmail.com",30)
        self.assertEqual(self.personal_info.userid,"001")
        self.assertEqual(self.personal_info.age,18)
        self.assertEqual(self.personal_info.email,"w123@gmail.com")
        self.assertEqual(self.personal_info.income,30)
        self.personal_info2.update("002",18,"w123@gmail.com",30)
        self.assertEqual(self.personal_info.userid,"001")
        self.assertEqual(self.personal_info.age,18)
        self.assertEqual(self.personal_info.email,"w123@gmail.com")
        self.assertEqual(self.personal_info.income,30)
        self.personal_info3.update("003",18,"w123@gmail.com",30)
        self.assertEqual(self.personal_info.userid,"001")
        self.assertEqual(self.personal_info.age,18)
        self.assertEqual(self.personal_info.email,"w123@gmail.com")
        self.assertEqual(self.personal_info.income,30)
        self.personal_info4.update("004",18,"w123@gmail.com",30)
        self.assertEqual(self.personal_info.userid,"001")
        self.assertEqual(self.personal_info.age,18)
        self.assertEqual(self.personal_info.email,"w123@gmail.com")
        self.assertEqual(self.personal_info.income,30)
        self.personal_info5.update("005",18,"w123@gmail.com",30)
        self.assertEqual(self.personal_info.userid,"001")
        self.assertEqual(self.personal_info.age,18)
        self.assertEqual(self.personal_info.email,"w123@gmail.com")
        self.assertEqual(self.personal_info.income,30)
        print("test personl_info_update success")
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.personal_info.show()
            self.assertEqual(fakeoutput.getvalue(),'Userid:{} Age:{} Email:{} Income:{}\n'.format("001",18,"w123@gmail.com",30))
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.personal_info2.show()
            self.assertEqual(fakeoutput.getvalue(),'Userid:{} Age:{} Email:{} Income:{}\n'.format("002",18,"w123@gmail.com",30))
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.personal_info3.show()
            self.assertEqual(fakeoutput.getvalue(),'Userid:{} Age:{} Email:{} Income:{}\n'.format("003",18,"w123@gmail.com",30))
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.personal_info4.show()
            self.assertEqual(fakeoutput.getvalue(),'Userid:{} Age:{} Email:{} Income:{}\n'.format("004",18,"w123@gmail.com",30))
        with patch('sys.stdout',new=StringIO()) as fakeoutput:
            self.personal_info5.show()
            self.assertEqual(fakeoutput.getvalue(),'Userid:{} Age:{} Email:{} Income:{}\n'.format("005",18,"w123@gmail.com",30))
        print("test personal_info_show success")
        self.personal_info.delete()
        self.assertEqual(self.personal_info.userid,"")
        self.personal_info2.delete()
        self.assertEqual(self.personal_info2.userid,"")
        self.personal_info3.delete()
        self.assertEqual(self.personal_info3.userid,"")
        self.personal_info4.delete()
        self.assertEqual(self.personal_info4.userid,"")
        self.personal_info5.delete()
        self.assertEqual(self.personal_info5.userid,"")
        print("test personl_info_delete success")
if __name__ == '__main__':
    unittest.main()