
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

```