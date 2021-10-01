

drop table if exists watch;
create table watch(
    symbol          char(10) primary key,
    nickname        char(20),
    watchIndustry   char(20)
);
