

drop table if exists asset;
create table asset(
    symbol          char(10) primary key,
    shortName       char(50),
    market          char(20),
    instrumentType  char(20),
    currency        char(6),
    exchange        char(6),
    firstTradeDate  date
);
