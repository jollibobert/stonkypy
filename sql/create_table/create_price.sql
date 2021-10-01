

drop table if exists price;
create table price(
    priceID int primary key,
    symbol  char(10),
    date    date,
    open    decimal(18, 4),
    close   decimal(18, 4),
    high    decimal(18, 4),
    low     decimal(18, 4),
    volume  int
);
