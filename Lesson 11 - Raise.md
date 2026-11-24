# Lesson 11 - Raise


We have used try and except to catch errors and stop our programs from
crashing. These errors are built into Python to stop you from doing things that
cannot work. The ones we have seen:

- `NameError` (a variable doesn't exist)
- `ValueError` (an invalid value for what you are trying to do)
- `TypeError` (an invalid type for what you are trying to do)
- `IndexError` (an index value doesn't exist)
- `KeyError` (a key doesn't exist)

For example, `int("abc")` **raise**s a `ValueError`: `int()` takes a string, but
that string doesn't hold a number.

There are many more types of errors, but these are the ones we mostly see in
this course.

The key word used above is **raise** - when these functions/methods are written by programmers, they have to determine what could potentially go wrong and **raise** the error message that we see.

## isinstance()

Before learning how to **raise** our own errors, we'll first learn how to check if a value is a certain type using: `isinstance()`.

```python
name = "Mr K"

isinstance(name, str)           # is name a string? (True)
isinstance(name, int)           # is name an integer? (False)
isinstance(name, (int, float))  # is name an int or a float? (False)

not isinstance(name, bool)      # is name NOT a boolean? (True)
```

## raise

Until now our functions returned `None` if something was wrong with the parameters. That is not ideal: good Python style is for a function to have one return type. A function should not return either an integer or `None`, so that it is clear to anyone using it.

In `raise_errors.py` I've copied `late_calculator()` from Lesson 9. We will now:

- `raise` an error if a parameter is the wrong type
- `raise` an error if a parameter has an invalid value (no more `None`)
- use try/except when calling the function, since it can now raise an error

`raise` works similar to `return` - as soon as you reach one, the function is over (the rest of the code doesn't execute).  For this reason, always check the type first. If you check a value first (`if lates < 0`, for example), you get a different error when `lates` is a string.

`as e` in the `except` line stores the error you caught in the variable `e`. You can name it anything and use it however you like; here we print its message.

In Lesson 12 you will document these errors in a Raises section.

## Preventing errors

In your programming assignment you used if statements and loops to prevent errors. Even if your main code still does that, your functions are expected to have full error checking.

That keeps a function safe for any future use, including when you or another programmer use it in a different program.

## Lab

That is it for the lesson. Move on to Lab 11, in `README.md`.
