Logs Analysis
-------------------------
Uses SQL to answer the following questions based on the information found on the PostgreSQL database news.

    1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

    2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

    3. On which days did more than 1% of requests lead to errors?

The news data base contains tables: articles, authors, and logs. These tables track the authors, articles, and traffic to the site.

Getting Started
-------------------------
This project consists of these files: logs_analysis.py, create_views.sql, and news_data.sql. By running logs_analysis.py on the command line or terminal the program will print the answers to the above questions. Follow the steps below to set up database and run the program.

The psql news database was set up on the vagrant virtual machine (https://www.vagrantup.com/). Once vagrant is installed the newsdata.sql (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), logs_analysis.py, and create_view.sql files included in this project should be added to the vagrant directory. To run the VM use commands 'vagrant up'; 'vagrant ssh'; 'cd /vagrant'. To load the data, use the command 'psql -d news -f newsdata.sql'.

Once the data is loaded into your database, the tables and database schema can be found by connecting to your database using command 'psql -d news' and '\dt' to display the tables and '\d <name of table>' to show the schema for that table. To exit the database type exit (or Ctrl-D) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell

create_views.sql contains the following views: topThree, pathViews, authorViews, errorViews, and allViews. To create these views use command 'psql -d news -f create_views.sql' from within the VM. These were created with the following statements:

    create view topThree (path, num) as select
        substring(path,10, length(path)), count(*) as num
        from log where path != '/' group by path
        order by num desc limit 3;

    create view pathViews (path, num) as
        select substring(path,10, length(path)), count(*) as num from
        log group by path order by num desc;

    create view authorViews (name, views) as
        select authors.name, pathViews.num from articles,
        pathViews, authors where articles.slug = pathViews.path and
        articles.author = authors.id order by pathViews.num desc;

    create view errorViews (time, num) as
        select to_char(time,'Mon, DD YYYY'), count(*)
        from log where status != '200 OK' group by to_char(time,'Mon, DD YYYY');

    create view allViews (time, num) as
        select to_char(time,'Mon, DD YYYY'), count(*)
        from log group by to_char(time,'Mon, DD YYYY');

Prerequisites
-------------------------
Python
Access to the PostgreSQL database news


Authors
-------------------------
Michael Ryden

