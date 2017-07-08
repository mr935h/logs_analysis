import psycopg2

DBNAME = "news"


def answer1():
    db=psycopg2.connect(database=DBNAME)
    c=db.cursor()
    # answer to question 1
    c.execute("""create view topThree (path, num)
        as select substring(path, 10, length(path)),
        count(*) as num from log group by path order by num desc limit 4""")
    c.execute("""select articles.title, topThree.num from articles,
        topThree where articles.slug = topThree.path order by topThree.num desc""")
    return c.fetchall()
    db.close()

def answer2():
    db=psycopg2.connect(database=DBNAME)
    c=db.cursor()
    c.execute("""create view pathViews (path, num)
        as select substring(path,10, length(path)),
        count(*) as num from log group by path order by num desc""")
    c.execute("""create view authorViews (name, views)
        as select authors.name, pathViews.num from articles,
        pathViews, authors where articles.slug = pathViews.path
        and articles.author = authors.id order by pathViews.num desc""")
    c.execute("""select authorViews.name, sum(authorViews.views)
        as views from authorViews group by authorViews.name
        order by views desc limit 3""")
    return c.fetchall()
    db.close()

def answer3():
    db=psycopg2.connect(database=DBNAME)
    c=db.cursor()
    c.execute("""create view errorViews (time, num)
        as select to_char(time,'Mon, DD YYYY'),
        count(*) from log where status != '200 OK'
        group by to_char(time,'Mon, DD YYYY')""")
    c.execute("""create view allViews (time, num)
        as select to_char(time,'Mon, DD YYYY'),
        count(*) from log group by to_char(time,'Mon, DD YYYY')""")
    c.execute("""select errorViews.time, errorViews.num,
        allViews.num from errorViews, allViews where
        allViews.time = errorViews.time and
        cast(errorViews.num as float) / cast(allViews.num as float) > .01""")
    return c.fetchall()
    db.close()
