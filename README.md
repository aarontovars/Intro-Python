# Intro-Python

* matplotlib (Figures)
* numpy (Maths)
* scikit-form (ML)
* scikit-image (Image Processing)
* pandas (Data Manipulation)


Python is an interpreted language. No compilation and linking step.
<br/>
Standalone software (C++), prototyping, Data Science, academic staff, wek DEV (Python).
<br/>
Check PEP 8 (Style Guide for Python).

## Basic types

### String
Defining:
```
str1 = "Hello World"
str2 = str("Hello World")
str3 = str(3) %Conversion
```
Printing:
```
print(str1)
```
Concatenate:
```
strc1 = str1 + str2
strc2 = "%s %s"(str1, str2)
strc3 = "%2.2f %s"(485.585, str1)
print(strc3)
>> 85.58 Hello World
str_format = "{} {}".format(str1, str2)
print(len(str1))
```
Test if a string is included in a string:
```
test = "Hello" in str1
print(test)
>> True
```
Count:
```
cat = str1.count("l")
print(cat)
>> 3
```
Index:
```
index_l = str1.index("l")
print(index_l)
>> 2
indexl_2 = str1.index("l", index_l+1)
print(index_l_2)
>> 3
index_l_3 = str1.index("l", index_l_2+1)
print(index_l_3)
>> 9
```

### Integers

```
i = 1
i = 1.5
print(i)
>> 1
```

### Floating values

```
f = 1.5
f = float(1.5)
f = float(1)
```

### Complex type

```
k = 1 + 3j
k = complex(1, 3)
```
