#Danyelle Palmore 
#24 July 2022
#COMP163 Summer Session II
#User will be able to submit their credit hours and quality points to calculate their semester, major, cumulative, and honors GPA.
#key: cqp = course quality points; cch = course credit hours

from dapalmore_GradecalcIIIrule import *

i = True
course_dividend_list = []
course_credit_hour_list = []
all_full_gpa_list = []

major_course_list = []
course_credit_hour_major_list = []
course_dividend_major_list = []

honors_course_list = []
course_credit_hour_honors_list = []
course_dividend_honors_list = []

def qualityPointGuide ():
    print('A = 94+ = 4.0')
    print('A- = 93-90 = 3.7')
    print('B+ = 89-87 = 3.3')
    print('B = 86-84 = 3.0')
    print('B- = 83-80 = 2.7')
    print('C+ = 79-77 = 2.3')
    print('C = 76-74 = 2.0')
    print('C- = 73-70 = 1.7')
    print('D+ = 69-67 = 1.3')
    print('D = 66-67 = 1.0')
    print('F = 63-0 = 0.0\n')

print('\nWelcome to a GPA calculator. This will calculate your major, honors, semesters, and cumulative GPA.')
print('To check your semesters GPA input data under regular courses.')

semester = input('\nDid you take classes in this semester(type yes or no)? ')
while i is True:
    if semester == 'yes':
        course = input('\nWould you like to enter course stats(type yes or no)? ')
        if course == 'yes':
            course_type = input('\nWhat type of course is this(major, honors, or regular)? ')

            #major course type loop
            if course_type == 'major':
                #input (key: cchm)
                course_credit_hour_major = float(
                input('Enter credit hours for course: '))
                course_credit_hour_major_list.append(course_credit_hour_major)
                qualityPointGuide()
                #input (key: cqpm)
                course_quality_point_major = float(input('Enter quality points for course: '))
                #multiplies cchm of one course by cqpm of one course
                course_dividend_major = gpacalculation(course_credit_hour_major,course_quality_point_major)
                #puts product of one courses cchm and cqpm into list
                course_dividend_major_list.append(course_dividend_major)
                #formula to find gpa
                major_gpa = sum(course_dividend_major_list) / sum(course_credit_hour_major_list)
                #puts answer into list that will be averaged at end
                major_course_list.append(major_gpa)


            #honors course type loop
            elif course_type == 'honors':
                course_credit_hour_honors = float(input('Enter credit hours for course: '))
                course_credit_hour_honors_list.append(course_credit_hour_honors)
                qualityPointGuide()
                course_quality_point_honors = float(input('Enter quality points for course: '))
                j = True
                while j is True:
                    if 1.8 <= course_quality_point_honors <= 4.0:
                        print('Only input classes you have failed. (1.7 or lower)')
                        course_quality_point_honors = float(input('Enter quality points for course: '))
                    #makes sure input is failing quality point
                    elif 0.0 <= course_quality_point_honors <= 1.7:
                        course_dividend_honors = gpacalculation(course_credit_hour_honors,course_quality_point_honors)
                        course_dividend_honors_list.append(course_dividend_honors)
                        honors_gpa = sum(course_dividend_honors_list) / sum(course_credit_hour_honors_list)
                        honors_course_list.append(honors_gpa)
                        j = False
                    else:
                        print('Please enter your quality points.')
                        course_quality_point_honors = float(input('Enter quality points for course: '))

            #regular course type loop
            elif course_type == 'regular':
                course_credit_hour = float(input('Enter credit hours for course: '))
                course_credit_hour_list.append(course_credit_hour)
                qualityPointGuide()
                course_quality_point = float(input('Enter quality points for course: '))
                j = True
                while j is True:
                    #removes the ability of accidently inputing a failed class into the 
                    if 0.0 <= course_quality_point <= 1.7:
                        print('Only input classes you have passed. (1.8 or higher)')
                        course_quality_point = float(input('Enter quality points for course: '))
                    #makes sure input is passing quality point
                    elif 1.8 <= course_quality_point <= 4.0:
                        course_dividend = gpacalculation(course_credit_hour,course_quality_point)
                        course_dividend_list.append(course_dividend)   
                        j = False
                    else:
                        print('Please enter your quality points(1.8 - 4.0).')
                        course_quality_point_honors = float(input('Enter quality points for course: '))

        #if it is a regular course the semesters gpa will calculate and print
        elif course == 'no' and course_type == 'regular':
            full_gpa = sum(course_dividend_list + course_dividend_honors_list) / sum(course_credit_hour_list + course_credit_hour_honors_list)
            all_full_gpa_list.append(full_gpa)

            print('This Semesters GPA is a {:.2f}!'.format(full_gpa))
            semester = input('\nDid you take classes in additional semester(type yes or no)? ')
        
        #if other than regular course type, prompts show up
        elif course == 'no':
            print('Make sure you have entered your regular classes.')
            semester = input('\nDid you take classes in additional semester(type yes or no)? ')

    elif semester == 'no':
        #calculations for each course type
        cumulative_gpa = full_calculation(all_full_gpa_list,all_full_gpa_list)
        print('\nYour Cumulative GPA is a {:.2f}!'.format(cumulative_gpa))

        final_major_gpa = full_calculation(major_course_list,major_course_list)
        print('Your Major GPA is a {:.2f}!'.format(final_major_gpa))

        final_honors_gpa = full_calculation(honors_course_list,honors_course_list)
        #honors gpa is regular course type and honors course type, it just includes passed and failed courses
        real_final_honors_gpa = full_calculation((honors_course_list+all_full_gpa_list) ,(honors_course_list+all_full_gpa_list))
        print('Your Honors GPA is a {:.2f}!\n'.format(real_final_honors_gpa))
        #turns off loop
        i = False
    else:
        print('Please type yes or no.')
        semester = input('\nDid you take classes in this semester(type yes or no)? ')