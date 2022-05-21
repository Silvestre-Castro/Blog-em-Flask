drop table if exists posts;

create table posts (
    id integer primary key autoincrement,
    criado timestamp default current_timestamp,
    título text not null,
    conteúdo text not null
);