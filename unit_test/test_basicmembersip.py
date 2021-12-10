import unittest 
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from budgetplanner.budget_subpackage.basicmembership import BasicMembership
import io
import sys

class TestBasicMembersip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):        
        print('setupClass')
        
    def setUp(self) :
        print('Setup')

    def tearDown(self):
        print("tearing down")    

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass") 

    def test_user_expenditure_data(self):  
        basic1=BasicMembership()   
        test_data=basic1.user_expenditure_data() 
        result_labels=np.all([list(test_data.iloc[0].values),[1000,500,200,100,200]])
        result_values=np.all([test_data.columns==['Shopping','Groceries','Travel','Restaurant','Gym']])        
        
        self.assertEqual(result_labels,True)
        self.assertEqual(result_values,True) 
        try:
            user_data=pd.read_excel(r'./budgetplanner/budget_subpackage/user_data_test_basic.xlsx')
        except FileNotFoundError:
            print('File not found')
        data=user_data.T
        data.columns=data.iloc[0].values        
        data=data.iloc[1: , :]
        result_labels=np.all([list(data.iloc[0].values),[500,250,1200]])
        result_values=np.all([data.columns,['Dining','Shopping','Lamp']])

        self.assertEqual(result_labels,True)
        self.assertEqual(result_values,'Lamp')  

        result_labels=np.all([list(data.iloc[0].values)==[500,200,1200.0]])
        self.assertEqual(result_labels,False)

    def test_expenditure_chart(self):  
        basic1=BasicMembership()    
        user_data=pd.read_excel(r'./budgetplanner/budget_subpackage/user_data_test_basic.xlsx')
        data=user_data.T
        data.columns=data.iloc[0].values        
        data=data.iloc[1: , :]
        result_labels=np.all([list(data.iloc[0].values),[500,250,1200]])
        result_values=np.all([data.columns==['Dining','Shopping','Groceries']])
       
        self.assertEqual(result_labels,True)
        self.assertEqual(result_values,True)   

        basic1=BasicMembership()   
        test_data=basic1.user_expenditure_data() 
        result_labels=np.all([list(test_data.iloc[0].values),[1000,510,200,100,200]])
        result_values=np.all([test_data.columns==['Shopping','Groceries','Travel','Restaurant','Gym']])        
        
        self.assertAlmostEqual(result_labels,True)
        self.assertEqual(result_values,True) 
        result_labels=np.all([list(test_data.iloc[0].values),[1000,510,200,100,210]])
        self.assertAlmostEqual(result_labels,True)
    
    def test_rewards_calculator(self):
        basic_mem1=BasicMembership()
        self.assertEqual(basic_mem1.rewards_calculator(1,500),"Gift coupon to Starbucks worth {} per month".format(0.015*500))
        self.assertEqual(basic_mem1.rewards_calculator(2,900),"{} off of your next purchase on hudson bay".format(0.15*900))
        self.assertEqual(basic_mem1.rewards_calculator(1,200),"Gift coupon to Starbucks worth {} per month".format(0.015*200))
        self.assertEqual(basic_mem1.rewards_calculator(2,400),"{} off of your next purchase on hudson bay".format(0.15*400))
        self.assertEqual(basic_mem1.rewards_calculator(3,800),"25% off of your membership for the next year")
       
    def test_analysis_and_suggestion(self):
        basic_mem1=BasicMembership()
        test_input = io.BytesIO(b"1\n")
        sys.stdin = test_input

        result1=basic_mem1.analysis_and_suggestion(10000)
        self.assertEqual(result1,1200.0)
        self.assertAlmostEqual(result1,1200.00001,2)

        input_text = b"2\n"
        test_input.write(input_text)
        test_input.seek(-len(input_text), io.SEEK_CUR)       
        

        result1=basic_mem1.analysis_and_suggestion(7000)
        self.assertEqual(result1,2400)
        self.assertAlmostEqual(result1,2400.001,2)

        input_text = b"3\n"
        test_input.write(input_text)
        test_input.seek(-len(input_text), io.SEEK_CUR)    

        result1=basic_mem1.analysis_and_suggestion(10000)
        self.assertAlmostEqual(result1,3000.001,2)

        test_input.close()
        sys.stdin = sys.__stdin__
    
    
    

