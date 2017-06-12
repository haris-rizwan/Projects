
# methods for dictionary


student = {'id': '001' ,'degree':'masters','majors':'engineering','year':2016}

students = {'Haris':{'s.no':7210 ,'degree':'masters','majors':'industrial','year': 2011 },\
           'Sumair':{'s.no':7211 ,'degree':'masters','majors':'computer','year': 2010 } ,\
           'waleed':{'s.no':7212 ,'degree':'masters','majors':'civil','year': 2016 } }

# if you want to see the keys of a particular dictionary

print(student.keys())

print(students.keys())

#if you want to see the values associated with keys

print(student.values())

print(students.values())

print("#############################")

# if you want to see the items

print(student.items())

# if you want to clear a dictionary

#students.clear()

#print(students)

# if you wan to copy a dictionary

students1 = students.copy()

print(students1)
