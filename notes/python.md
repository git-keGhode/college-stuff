- [x] casting
- [x] variables
- [x] basic syntax
- [x] input
- [x] conditionals
- [x] arith operators
- [x] set operations 
- [x] dictionary (keys, values, items)
- [x] set  - indexing slicing
- [x] is operator - membership operator
- [x] identity operator

## TODO : 
- [ ] iterators

**For loop :**
```python
	for i in range(1, 10):
		print(i)
```

```python
	for i in range(1, 10, 2):
		print(i)	
```
// here the loop skips 2 as the third parameter stands for `steps`.

```python
	set = {1,2,3,4,5}
	
	for i in set:
		print(i)
```
// this will iterate through the set and print all the values. 

- [ ] Dictionary
```python
	dict = {'a' : 1, 'b' : 2,'c' : 3, 'd' : 4}\
	for i in dict:
		print (i)
	

```
// there are 3 funcitons in dictionary: 
	1. `dict.keys()` : prints all the keys in dictionary
	2. `dict.values()` : prints all the values in dictionary
	3. `dict.items` : gives both the `key-value` pairs

```python
	# for items
	for i,j in dict.items():
		print(i,j)
```
// this will assign `keys` to `i`, and `values` to `j`. and print them accordingly.

- [ ] list
```python
	list = [1,2,3,4,5]
	for i in list:
		print(i)
```

## ext:
- Python also allows `for loop` to have `else` block. if the for loop fails, the control will reach `else block` related to the `for loop`.
```python
	# else in for loop
	for i in range(1,10):
		print(i)
	else:
		print("loop finished")
```
*NOTE: the else block related to for will only run once the loop is run successfully. if it encounters any error, it will not execute the else block code.*


- [ ] arbitiary args in py
```python
	def add(*args):
		for i in args:
			sum += i
		print(sum)
	# this will take args dynamically. 
	# args are stored in a tuple
	# any no. of args can be given
	# the 'args' is just a variable it can be any other thing.

	add(10,20)
	add(10,20,20)
	add(10,20,30,40)

```





# Resource : 
- `Allboringstuff.com` - Automate the boring stuff in python

gitkeghode@gmail.com
git@123//