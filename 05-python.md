# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>A tuple is a one-dimensional, fixed-length, immutable sequence of Python objects - tuples are defined by (). Lists are variable-length and their contents can be modified - lists are defined by []. Tuples will work as keys in dictionaries, because the keys of a dict have to be immutable objects (hashability). 

---

---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>Lists can have duplicates; sets contain only unique elements. Lists are ordered while sets are not ordered. Sets are significantly faster when it comes to determining if an object is present in the set (as in x in s), but are slower than lists when it comes to iterating over their contents (because sets are not ordered). The timeit module can be used to see which is faster for the particular situation.

---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>'Lambda' is an "anonymous" function or just simple functions consisting of a single statement, the result of which is the return value. They are defined using the 'lambda' keyword. These functions are convenient for data analysis because 1) less typing and 2) many data transformation functions take functions as arguments. 

>An example use of lambda is :

```
  sorted(['foo', 'card', 'bar', 'aaaa', 'abab'], key=lambda x: len(set(x)))
```
  
>This function sorts string by the number of distinct letters in each string.

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>List comprehensions allows for concisely forming a new list by filtering the elements of a collection and transforming the elements passing the filter in one concise expression. They take the basic form:
  [*expr* for val in collection if *condition*]
  
>An example using list comprehension is:
```
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
Fahrenheit
```

>The equivalent using  ```map``` is:
```
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
Fahrenheit
```

>As second example using list comprehension is:
```
Fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
newFibs = [x for x in fibs if x%2]
newFibs
```

>The equivalent using  ```filter``` is:
```
Fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
newFibs = filter(lambda x: x%2, Fib)
newFibs
```

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
