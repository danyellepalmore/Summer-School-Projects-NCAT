#Danyelle Palmore 
#24 July 2022
#COMP163 Summer Session II
#functions that are specific to calculating GPA's

def gpacalculation(credithour,qualitypoint):
    #dividen of gpa calculation
    gpa = credithour * qualitypoint
    return gpa

def full_calculation(gpafull,lengthgpa):
    #all gpa's (according to assignments) divided by the length of gpa's list
    all = ((sum(gpafull) / (len(lengthgpa))))
    return all
