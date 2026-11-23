# Lab 11 - Raising Errors

This lab is open-ended. The tests only check your header and comments. Check
your own work against the lesson and `raise_errors.py`.

Open `main.py` and complete the following:

1. Update the header with your information (Name, Purpose, Author, Created, Updated).
2. Copy all of your code from your Lab 9 `main.py` (functions and main program) to just below the header. Do not copy the Lab 9 header.
3. In each function, check the parameter types first. If a parameter is the wrong type, `raise` a `TypeError` with a clear message.
4. Next, check the parameter values. If a value is invalid, `raise` a `ValueError` with a clear message. Remove the old `return None` lines.
5. In your main program, wrap each function call in try/except, catching `TypeError` and `ValueError` separately.
6. Add try/except anywhere else your program could crash (for example, converting `input()` with `int()`).

## Running your program

Open `main.py` and press the Run button in the top right corner of VS Code. Your output appears in the terminal at the bottom. Try bad inputs on purpose: your program should print a message, not crash.

## Checking your work

Press **Ctrl+Shift+B** to run the tests. You will see one line per test:

```
[PASS] 1. Header is filled in
[FAIL] 2. Code is commented
```

When a test fails it shows what it expected. Fix your code and press Ctrl+Shift+B again. Keep going until all tests pass.

## Reminders

- Fill in every field of the header before you do anything else.
- Write comments as you go, explaining each check you added.
- Check type before value. Checking `lates < 0` when `lates` is a string causes a different error.
- A function should now return only one type. No more `None`.

## Optional challenges

Finished early? Try the optional challenges in the `challenges` folder. Open `challenges/CHALLENGES.md` for instructions. They are not assessed and do not affect your lab result.
