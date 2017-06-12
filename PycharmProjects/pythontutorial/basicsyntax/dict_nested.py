
#nested dictionary

# d {'k1':{'nestedk1':'nestedv1','nestedk2':'nestedv2'}}
# you can create multiple nested dictionaries with in a dictionary


student = {'Haris':{'s.no':7210 ,'degree':'masters','majors':'industrial','year': 2011 },\
           'Sumair':{'s.no':7211 ,'degree':'masters','majors':'computer','year': 2010 } ,\
           'waleed':{'s.no':7212 ,'degree':'masters','majors':'civil','year': 2016 } }

print(student)

print(student['Haris']['degree'])
print(student['waleed']['s.no'])
print(student['Haris']['majors'])
