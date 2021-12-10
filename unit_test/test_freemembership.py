import unittest 
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from budgetplanner.budget_subpackage.freemembership import FreeMemberShip
#from budgetplanner.budget_subpackage

class TestFreeMembersip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):        
        print('setupClass TestFreeMembersip')
        
    def setUp(self) :
        print('Setup TestFreeMembersip') 
    

    def tearDown(self):
        print("tearing down TestFreeMembersip")   

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass TestFreeMembersip")

    def test_show_budget_chart(self):
        print("test_show_budget_chart Start")
        budget=2000
        balance=200
        amount=100

        print("test_show_budget_chart 1")
        free_mem=FreeMemberShip(budget)
        free_mem.set_balance(balance)

        print("test_show_budget_chart 2")
        self.assertEqual(free_mem.get_user_budget(),budget)
        self.assertEqual(free_mem.get_balance(),balance)   

        print("test_show_budget_chart 3")
        free_mem=FreeMemberShip(1000)
        free_mem.set_balance(900)

        print("test_show_budget_chart 4")    
        self.assertEqual(free_mem.get_user_budget(),1000)
        self.assertEqual(free_mem.get_balance(),900)
        self.assertAlmostEqual(free_mem.get_balance(),900.0001,2)
        print("test_show_budget_chart end")        

    def test_add_amount(self):
        print("test_add_amount Start")
        budget=2000
        balance=200
        amount=100
        
        print("test_add_amount 0")
        
        free_mem=FreeMemberShip(budget)   
        print("test_add_amount 0_1")
        free_mem.add_amount(amount)
        
        print("test_add_amount 1")
        self.assertEqual(free_mem.get_balance(),amount) 

        free_mem.add_amount(amount)
        self.assertAlmostEqual(free_mem.get_balance(),2*amount+0.0001,2) 

        print("test_add_amount 2")
        free_mem.add_amount(0)
        self.assertEqual(free_mem.get_balance(),2*amount)

        print("test_add_amount 3")    
        free_mem.add_amount(20)
        self.assertEqual(free_mem.get_balance(),2*amount+20)

        print("test_add_amount 4")    
        free_mem.add_amount(40)
        self.assertAlmostEqual(free_mem.get_balance(),2*amount+60.0001,2)
        print("test_add_amount end")
    
    def test_withdraw_amount(self):
        print("test_withdraw_amount Start")
        budget=2000
        balance=200
        amount=100
        free_mem=FreeMemberShip(budget)
        free_mem.set_balance(100)  

        print("test_withdraw_amount 1")

        self.assertEqual(free_mem.withdraw_amount(200),"Please enter lesser amount")
        free_mem.set_balance(1000)
        free_mem.withdraw_amount(250)

        print("test_withdraw_amount 2")
        self.assertEqual(free_mem.get_balance(),750)

        free_mem.set_balance(250)
        free_mem.withdraw_amount(250)
        
        print("test_withdraw_amount 3")

        self.assertEqual(free_mem.get_balance(),0)
        self.assertAlmostEqual(free_mem.get_balance(),0.001,2)

        self.assertEqual(free_mem.withdraw_amount(200),"Please enter lesser amount")
        print("test_withdraw_amount end")


        


    
    

