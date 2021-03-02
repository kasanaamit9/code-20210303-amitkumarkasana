@ echo off
rem python assessment.py "<input_file>" "<output_file>" >> <log_file> 2>&1

python assessment.py "person_list.json" "bmi_result.json" >> assessment.log 2>&1
python test_assessment.py >> test_assessment.log 2>&1