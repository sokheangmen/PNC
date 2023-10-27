
person_1_year = int( input('Person 1 - birth year: ') )
person_1_month = int( input('Person 1 - birth month: ') )
person_1_day = int( input('Person 1 - birth day: ') )

person_2_year = int( input('Person 2 - birth year: ') )
person_2_month = int( input('Person 2 - birth month: ') )
person_2_day = int( input('Person 2 - birth day: ') )

message = ""
if person_1_year  > person_2_year or person_1_month > person_2_month or person_1_day > person_2_day:
    message = "The first person is the youngest"
elif person_1_year  == person_2_year and person_1_month == person_2_month and person_1_day == person_2_day:
    message = "Both persons have the same age!"
else:
    message = "The second person is the youngest"
print(message)
