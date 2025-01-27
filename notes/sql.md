
**product code**
name //unique
type
desc // not null
stock

// types of product
consumer
business
industry


customer id
name
city
mob no


// order table
order id
ord type
date
status
pcode, cid => foriegn key

// fields - product code, customer id => foriegn key
if order status is left empty, default behaviour is pending.


set autocommit on 