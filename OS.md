
```sh
#!/bin/bash
read -p "Enter a number:" num1
read -p "Enter a smaller number:" num2
echo "Addition: $(($num1 + $num2))"
echo "Subtraction: $(($num1 - $num2))"
echo "Multiplication: $(($num1 * $num2))"
echo "Division: $(($num1 / $num2))"

----------------------------------------------------------

#!/bin/bash
read -p "Enter a number:" num1
read -p "Enter a smaller number:" num2
read -p "Enter an operand:" op
if [ $op == + ]; then
  echo "$num1 + $num2 = $((num1+num2))"
elif [ $op == - ]; then
  echo "$num1 - $num2 = $((num1-num2))"
elif [ $op == * ]; then
  echo "$num1 * $num2 = $((num1*num2))"
elif [ $op == / ]; then
  echo "$num1 / $num2 = $((num1/num2))"
else
  echo "Operator not listed"
fi

```

---

```sh
#!/bin/bash
echo $((1 + RANDOM % 50))
```

---

```sh
#!/bin/bash
read -p "Enter minimum range:" min
read -p "Enter maximum range:" max
r_num=$(( $RANDOM % ($max - $min + 1) + $min ))
echo "Random Number: $r_num"

```


---

```sh
#!/bin/bash
read -p "Enter two numbers: " num1 num2
read -p "Enter operation to perform (AND, OR, NOT): " op
case $op in
  AND) echo "Result: $num1 & $num2 = $((num1&num2))";;
  OR) echo "Result: $num1 | $num2 = $((num1|num2))";;
  NOT) echo "Result: $num1 ^ $num2 = $((num1^num2))";;
  *) echo "Invalid operator.";;
esac
```

---

```sh
#!/bin/bash
read -p "Enter a number:" num
if [ $((num%2)) == 0 ]; then
  echo "The number is even"
else
  echo "The number is odd"
fi
```

---

```sh
#!/bin/bash
read -p "Enter two values: " val1 val2
read -p "Enter an operation(and/or/not) to perform:" op
case $op in
  and)
    if [[ $val1 == true && $val2 == true ]]; then
      echo "Result: true"
    else
      echo "Result: false"
    fi;;
  or)
    if [[ $val1 == true || $val2 == true ]]; then
      echo "Result: true"
    else
      echo "Result: false"
    fi;;
  not)
    if [[ $val1 == true ]]; then
      echo "Result: false"
    else
      echo "Result: true"
    fi;;
  *) echo "Invalid operator.";;
esac
```

---

```sh
#!/bin/bash
read -p "Enter an email ID: " id
if [[ $id =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
  echo "This is a valid email ID!"
else
  echo "This is not a valid email ID!"
fi

#!/bin/bash
read -p "Enter a URL: " url
if [[ $url =~ ^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
  echo "This is a valid URL!"
else
  echo "This is not a valid URL!"
fi
```

---

```sh
#!/bin/bash
read -p "Enter a number:" num
if [ $num -gt 0 ]; then
  echo "The number is Positive!"
elif [ $num -lt 0 ]; then
  echo "The number is Negative!"
else
  echo "The number is Zero!!"
fi
```

--- 

```sh
#!/bin/bash
read -p "Enter a File Name:" fname
if [ -w $fname ]; then
  echo "The File $fname is writable."
else
  echo "The File $fname is not writable."
fi

#!/bin/bash
read -p "Enter a File Name:" fname
if [ ! -f $fname ]; then
  echo "The File $fname does not exist!"
  exit 1
fi
echo "The File $fname exists."

#!/bin/bash
read -p "Enter a Filename: " dir
if [ ! -d $dir ]; then
  echo "The directory $dir does not exist!"
  exit 1
fi
echo "The directory $dir exists."

```

---

```sh
#!/bin/bash
n=5
until [ $n == 0 ]
do
  echo $n
  n=$((n-1))
done

#!/bin/bash
for (( i=1; i<=10; i++ ))
do
  if [ $((i%2)) == 0 ]
  then
    echo $i
  fi
done

#!/bin/bash
read -p "Enter a number: " num
for (( i=1; i<=10; i++ ))
do
  echo "$num x $i = $((num*i))"
done

#!/bin/bash
read -p "Enter a number: " num
sum=0
while [ $num -gt 0 ]
do
  dig=$((num%10))
  sum=$((sum+dig))
  num=$((num/10))
done
echo "The sum of digits of the given number: $sum"

#!/bin/bash
read -p "Enter a number: " num
temp=1
for (( i=1; i<=$num; i++ ))
do
  temp=$((temp*i))
done
echo "The factorial of $num is: $temp"

#!/bin/bash
read -p "Enter a number: " num
sum=0
for (( i=1; i<=$num; i++ ))
do
  sum=$((sum + i))
done
echo "Sum of first $num numbers: $sum"

#!/bin/bash
read -p "Enter the file names: " files
IFS=' ' read -ra array <<< "$files"
for file in "${array[@]}"
do
  if [ -e "$file" ]; then
    echo "Contents of $file:"
    cat "$file"
  else
    echo "Error: $file does not exist"
  fi
done

#!/bin/bash
read -p "Enter the file name: " file
read -p "Enter destination path:" dest
if [ -e "$file" ]; then
  cp $file $dest
  file_location=$(readlink -f $dest)
  echo "A copy of $file is now located at: $file_location"
else
  echo "Error: $file does not exist"
fi

#!/bin/bash
read -p "Enter the file name: " file
echo "Enter text to write:"
read text
echo "$text" > "$file"
echo "-----------------------------------"
echo "The File $file is created!"

#!/bin/bash
read -p "Enter the 1st file name: " file1
read -p "Enter the 2nd file name: " file2
if [ ! -f $file1 ] || [ ! -f $file2 ]; then
  echo "Error! One of the files does not exists."
  exit 1
fi
if cmp -s "$file1" "$file2"; then
  echo "The Files $file1 and $file2 are identical."
else
  echo "The Files $file1 and $file2 are different."
fi

#!/bin/bash
read -p "Enter the file name for deletion: " file
if [ -f $file ]; then
  rm $file
  echo "The file $file deleted successfully!"
else
  echo "Error! The file $file does not exist."
fi

#!/bin/bash
read -p "Enter the file name: " file
read -p "Enter new file name: " new_file
if [ -f $file ]; then
  mv "$file" "$new_file"
  echo "The file $file has been renamed as $new_file!"
else
  echo "Error! The file $file does not exist."
fi

```