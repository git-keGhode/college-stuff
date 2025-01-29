- [x] prod
# product
pcode - P
pname - U
ptype - check(consumer, business, industry)
pdesc - not null
pstock


# Customer
cid - P
cname - 
city
mob no
pincode


# order table
pcode - F
cid - F
oid
order type
odate
status - default (pending)


```sql
	select order.name, 
```


- [ ] entry :
![[Pasted image 20250124125538.png]]

# queries : 
- [x] add col `pincode` in `cust` table
- [x] change datatype `size` of `otype`
- [ ] select records from `cust` of `cname` ending with `a`
- [ ] select records from `prod` of `pname` 2nd letter is `u`
- [ ] 