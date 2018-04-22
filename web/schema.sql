drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  url string not null,
  family string not null,
  brand string not null,
  series string not null,
  subseries string not null,
  article_number string not null,
  spliter string not null,
  date date not null,
  site string not null,
  language string not null
);