# Python Concepts – README

This README explains some important Python concepts commonly used in real-world projects:

* Virtual Environment
* `pip freeze` command
* Lambda Functions
* `join()` method
* `format()` method
* `map()`, `filter()`, and `reduce()`

---

## 1. Virtual Environment (venv)

A **virtual environment** is an isolated Python environment where you can install packages without affecting the global Python installation.

### Why use a virtual environment?

* Avoid version conflicts between projects
* Keep dependencies project-specific
* Easy to share and reproduce projects

### Creating a virtual environment

```bash
python -m venv venv
```

### Activating the virtual environment

* **Windows**:

```bash
venv\Scripts\activate
```

* **Linux / macOS**:

```bash
source venv/bin/activate
```

### Deactivating

```bash
deactivate
```

---

## 2. `pip freeze` Command

The `pip freeze` command lists all installed packages and their versions in the current environment.

### Example

```bash
pip freeze
```

### Saving dependencies

```bash
pip freeze > requirements.txt
```

### Installing from `requirements.txt`

```bash
pip install -r requirements.txt
```

This helps in sharing projects with the exact same dependencies.

---

## 3. Lambda Functions

A **lambda function** is a small anonymous function written in a single line.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

Lambda functions are often used with `map()`, `filter()`, and `reduce()`.

---

## 4. `join()` Method

The `join()` method joins elements of an iterable (like a list or tuple) into a single string.

### Syntax

```python
separator.join(iterable)
```

### Example

```python
names = ["Alice", "Bob", "Charlie"]
result = ", ".join(names)
print(result)
# Output: Alice, Bob, Charlie
```

Note: All elements must be strings.

---

## 5. `format()` Method

The `format()` method is used to insert values into a string.

### Example

```python
name = "John"
age = 20

text = "My name is {} and I am {} years old".format(name, age)
print(text)
```

### Using indexes

```python
text = "{1} is older than {0}".format("Alice", "Bob")
print(text)
```

---

## 6. `map()` Function

The `map()` function applies a function to every item in an iterable.

### Syntax

```python
map(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, numbers))
print(squares)
# Output: [1, 4, 9, 16]
```

---

## 7. `filter()` Function

The `filter()` function selects items from an iterable based on a condition.

### Syntax

```python
filter(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
# Output: [2, 4, 6]
```

---

## 8. `reduce()` Function

The `reduce()` function applies a function cumulatively to items of an iterable.
It is available in the `functools` module.

### Syntax

```python
from functools import reduce
reduce(function, iterable)
```

### Example

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)
# Output: 24
```

---

## Summary

* Virtual environments isolate project dependencies
* `pip freeze` helps manage and share dependencies
* Lambda functions create small one-line functions
* `join()` combines strings
* `format()` inserts values into strings
* `map()`, `filter()`, and `reduce()` help process iterables efficiently

---

**Suggested file name:** `README.md`
