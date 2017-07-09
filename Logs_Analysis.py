#!/usr/bin/env python


import psycopg2


# database connection and setup


DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()


# pulls and prints which three articles have been viewed the most
# answer to question 1


c.execute("""select articles.title, topThree.num from
    articles, topThree where articles.slug = topThree.path
    order by topThree.num desc""")
topThree = c.fetchall()
print "Top 3 Articles by Views"
print "--------------------------------"
for i in topThree:
    print i[0], '-', i[1], "views"


# pulls and prints which three authors have been viewed the most
# answer to question 2


c.execute("""select authorViews.name, sum(authorViews.views) as views
    from authorViews group by authorViews.name order by views desc""")
topAuthors = c.fetchall()
print
print "Top Authors by Views"
print "--------------------------------"
for i in topAuthors:
    print i[0], '-', i[1], "views"


# pulls and prints which date resulted in > 1 percent errors
# answer to question 3


c.execute("""select errorViews.time, errorViews.num, allViews.num
    from errorViews, allViews where allViews.time = errorViews.time
    and cast(errorViews.num as float) / cast(allViews.num as float) > .01""")
oneDayErrors = c.fetchall()
print
print "Days When Errors > than 1%"
print "--------------------------------"
for i in oneDayErrors:
    print i[0], "-", round(float(i[1]) / float(i[2]) * 100, 1), "% errors"

db.close
