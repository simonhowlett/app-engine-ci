'''
Collect user data given an attached document
Use the output to create csv file for easier consumption 
Date the export file
'''
'''
Issues: 
- NavexEngage Export needs a top level attribute or script will fail
- ISO date format designation fails the test, remove, or handle.
ToDo:
- Sort folder structure correctly
- Make file selectable
- Sort output by lastname
'''
import json
import csv
import datetime

dt_date = datetime.datetime.now()

# Opening JSON file and loading the data 
# into the variable data 
with open('_add_Filename.json') as json_file:
    data = json.load(json_file)
    
employee_data = data['emp_details']
  
# now we will open a file for writing
data_file = open(dt_date.strftime("%d+%b+%Y") + '-navexEngageUsers.csv', 'w', newline='')

# create the csv 
csv_writer = csv.writer(data_file) 
count = 0
for emp in employee_data: 
    if count == 0: 
        # Writing headers of CSV file 
        header = emp.keys() 
        csv_writer.writerow(header) 
        count += 1
    # Writing data of CSV file 
    csv_writer.writerow(emp.values()) 
data_file.close() 
print(f'All Done! See {data_file.name} for results')
