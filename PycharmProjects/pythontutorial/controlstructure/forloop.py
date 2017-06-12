"""
execute statements repeatedly
iteratable items are strings, list , tuple , dictionary
conditions are used stop execution of loops
"""


# in for loop range (start,end, condition) end is not inclusive
# #strings in for loop

#
# my_string = "abcdefgh"
#
# for c in my_string:
#
#     print(c)
#
#
# print("*"*20)
#
# #list in for loop
#
# cars = ['bmw','honda','astin martin']
#
#
# for car in cars:
#
#     if car == "bmw":
#
#         print("this is a german company")
#     elif car == "astin martin":
#
#         print("this is a british company")
#
#
#     else:
#
#          print(car)
#
# print("#*"*30)

# dictionary in for loops

student = {'Haris':{'s.no':7210 ,'degree':'masters','majors':'industrial','year': 2011 },\
           'Sumair':{'s.no':7211 ,'degree':'masters','majors':'computer','year': 2010 } ,\
           'waleed':{'s.no':7212 ,'degree':'masters','majors':'civil','year': 2016 } }


# print("Details of Haris")
#
# print('S.no: ' + str(student["Haris"]['s.no']) )
# print('degree: ' + student["Haris"]['degree'] )
# print('majors: ' + student["Haris"]['majors'] )
# print('Year: ' + str(student["Haris"]['year']) )
#
#
# print("*#-"*30)

# now to access information of each student using for loop



for applicant_name, applicant_information in student.items():
    if applicant_name == "waleed":
        print("\nHere is what I know about %s:" % applicant_name.title())

    # Each students dictionary is in 'information'

        for data in applicant_information:

                print(data + ": " + str(applicant_information[data]))














    # if applicant == "Haris":
    #
    #   print(str(student['Haris']))

