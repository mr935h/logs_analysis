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
