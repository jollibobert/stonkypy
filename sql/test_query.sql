
select
    a.symbol,
    a.currency,
    a.exchange,
    p.priceId,
    p.date,
    p.close
from
    price p
    left join (
        asset a
        ) on p.symbol = a.symbol
where 1=1
    and p.symbol in ('DOCN', 'SNOW', 'DDOG')
    and p.date >= '2021-09-01'
order by date
limit 10;
