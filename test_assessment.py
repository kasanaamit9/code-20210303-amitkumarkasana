import sys
import inspect
import unittest
import json
from assessment import *

#pre-defined values for test cases
person_details = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 85 },{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
bmi = 32

class TestAssessment(unittest.TestCase):
    def test_calculate_bmi(self):
        expected_output = 32.83
        for person, actual_bmi in calculate_bmi(person_details):
            pass
        self.assertTrue(actual_bmi == expected_output, msg= "'calculate_bmi' method is not working as expected")
    
    def test_get_bmi_category_and_health_risk(self):
        expected_category, expected_risk = "Moderately obese", "Medium risk"
        actual_category, actual_risk = get_bmi_category_and_health_risk(bmi)
        self.assertTrue(actual_category == expected_category and expected_risk == actual_risk, msg="'get_bmi_category_and_health_risk' method is not working as expected")
    
    def test_get_count_of_overweight_people(self):
        expected_count = 1
        for person, bmi in calculate_bmi(person_details):
            person["BMI"] = bmi
            person["BMICategory"], person["HealthRisk"] = get_bmi_category_and_health_risk(bmi)
        actual_count = get_count_of_overweight_people(person_details)
        self.assertTrue(actual_count == expected_count, msg= "'get_count_of_overweight_people' method is not working as expected")

if __name__ == "__main__":
    unittest.main()