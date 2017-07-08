from logs_analysisdb import answer1, answer2, answer3

import psycopg2


# pulls and prints which three articles have been viewed the most
# answer to question 1
topThree=answer1()
print "answer #1: "
for i in topThree:
    print i[0], '-', i[1] , "views"


# pulls and prints which three authors have been viewed the most
# answer to question 2
topAuthors=answer2()
print
print "answer #2: "
for i in topAuthors:
    print i[0], '-', i[1] , "views"

# pulls and prints which date resulted in > 1 percent errors
# answer to question 3
oneDayErrors=answer3()
print
print "answer #3: "
for i in oneDayErrors:
    print i[0], "-", round(float(i[1]) / float(i[2]) * 100,1), "% errors"