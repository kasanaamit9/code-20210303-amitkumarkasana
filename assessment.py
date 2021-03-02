import sys
import operator
import json
from collections import Counter

def calculate_bmi(person_details):
    '''
    this method takes list of objects as input and yields the object with its calculated BMI to the caller.
    '''
    for person in person_details:
        bmi = round((person["WeightKg"]*10000) / (operator.pow(person["HeightCm"], 2)), 2)
        yield person, bmi

def get_bmi_category_and_health_risk(bmi):
    '''
    this method take the BMI value as input and returns BMI category and corresponding health risk to the caller.
    '''
    if bmi < 18.5:
        return "Underweight", "Malnutrition risk"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight", "Low risk"
    elif bmi >= 25 and bmi < 30:
        return "Overweight", "Enhanced risk"
    elif bmi >= 30 and bmi < 35:
        return "Moderately obese", "Medium risk"
    elif bmi >= 35 and bmi < 40:
        return "Severely obese", "High risk "
    else:
        return "Very severely obese", "Very high risk"

def get_count_of_overweight_people(person_details):
    '''
    this method takes list of people(objects) as input and returns the number of 'overweight' people inside the list of people.
    '''
    count_of_overweight_people = 0
    for person in person_details:
        count_of_overweight_people=count_of_overweight_people + Counter(person.values())["Overweight"]
    return count_of_overweight_people

def get_body_mass_index(person_details):
    '''
    this method takes the list of people as input and returns the same list with added BMI details as new fields.
    '''
    print("calculating BMI, category and health risks for each person")
    for person, bmi in calculate_bmi(person_details):
        # Not sure what adding columns meant in the problem statement. So, added fields/keys in the existing json.
        person["BMI"] = bmi
        person["BMICategory"], person["HealthRisk"] = get_bmi_category_and_health_risk(bmi)
    return person_details

def main(person_details, output_file):
    '''
    this method takes list of people and output filename as input and writes the final result into the output file.
    '''
    result = get_body_mass_index(person_details)
    print("counting total number of overweight people")
    count_of_overweight_people = get_count_of_overweight_people(person_details)
    print("Number of Overweight people are: ", count_of_overweight_people)
    result.append({"CountOfOverweightPeople": count_of_overweight_people})
    #writing the final result into json file in the same directory.
    with open(output_file, "w") as fw:
        print("writing people's BMI details into output file")
        fw.write(json.dumps(result, indent=4))

if __name__ == "__main__":
    print("********START*************")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f"provided input file is: {input_file}  and output file is: {output_file}")
    try:
        print("reading people's details from input file")
        with open(input_file, "r") as f:
            person_details = eval(f.read())
    except Exception as err:
        print(f'JSON data in file is not Serializable. Please check and try again.')
    finally:
        main(person_details, output_file)
        print("BMI details written to output file. Please check the output.")
        print("********END*************")
    