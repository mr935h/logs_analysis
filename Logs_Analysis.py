import psycopg2


DBNAME = "news"


db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute("create view topThree (path, num) as select substring(path,10, length(path)), count(*) as num from log group by path order by num desc limit 4")
c.execute("select articles.title, topThree.num from articles, topThree where articles.slug = topThree.path order by topThree.num desc")
topThree = c.fetchall() #the page name equates to articles.slug

print topThree

#c.execute("select authors.name, count(articles.id) as num from articles left join authors on articles.author = authors.id group by authors.name order by num")
c.execute("select articles.title, authors.name from articles, authors where articles.author = authors.id")
titleAuthors = c.fetchall()

#c.execute("select path, count(*) from log group by path order by count desc")
#pathViews = c.fetchall()

# print topThree
# print titleAuthors
# print pathViews

# c.execute("create view pathViews select substring(path,10, length(path)), count(*) as num from log group by path")
# c.execute("select ")
# print c.fetchall()
# print titleAuthors

db.close