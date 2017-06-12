# Dictionary is also used to store more than one value in variables .

# it is not in sequence or indexing , it is basically just mapping.
# dictionary items are in {} , one key with one value seperated by : and multiple keys seperated by ,.
# {'k1':'v1','k2':'v2' }


student = {'id': '001' ,'degree':'masters','majors':'engineering','year':2016}

print(student)

id = student['id']

print(id)

sum_1 = student['id'] + '2'

print(sum_1)

#you can chnge the values in the list by following method

student['id'] = 721056
student ['degree'] = "bachelors"
student ['majors'] =  'arts'
student ['year']  = '2017'

print("##############################")

print(student)

grades = {'A+': 95, 'A': 90 , 'A-': 85, 'B+' : 80 ,'B': 75}

print(grades)
