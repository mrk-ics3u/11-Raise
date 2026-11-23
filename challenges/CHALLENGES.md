# Optional Challenges - Lab 11

**These challenges are optional.** Try them once Lab 11 is finished. They are not
assessed, and they do not affect your lab result.

| File | Challenge |
|---|---|
| `age_check.py` | Age Check |
| `parse_time.py` | Time Parser (harder) |

Each challenge has two functions. The first one `raise`s errors. The second one
calls the first, catches its errors with `as e`, and returns a message.

## Age Check

Open `age_check.py` and complete both functions.

1. Write `check_age(age)`. Check in this order:
   - If `age` is not an `int`, raise a `TypeError` with the message
     `Age must be a whole number.`
   - If `age` is below 0 or above 130, raise a `ValueError` with the message
     `Age must be between 0 and 130.`
   - Otherwise return `Child` (0 to 12), `Teen` (13 to 19) or `Adult` (20 and up).
2. Write `describe_age(age)`. It calls `check_age(age)` inside a try block.
   - If it works, return the age group.
   - If a `TypeError` is raised, return `TypeError: ` followed by its message.
   - If a `ValueError` is raised, return `ValueError: ` followed by its message.

For example:

- `check_age(15)` returns `"Teen"`
- `describe_age(-4)` returns `"ValueError: Age must be between 0 and 130."`
- `describe_age("ten")` returns `"TypeError: Age must be a whole number."`

## Time Parser (harder)

Open `parse_time.py` and complete both functions.

1. Write `parse_time(text)`. `text` should be a time like `"2:30"` (minutes, a
   colon, then seconds). Return the total number of seconds as an `int`. Check in
   this order:
   - If `text` is not a `str`, raise a `TypeError`: `Time must be text.`
   - If `text` does not have exactly one `:`, or either side of it is not all
     digits, raise a `ValueError`: `Time must look like MM:SS.`
   - If the seconds are 60 or more, raise a `ValueError`:
     `Seconds must be less than 60.`
2. Write `time_message(text)`. It calls `parse_time(text)` inside a try block.
   - If it works, return `____ is ____ seconds.` with the original text first.
   - If an error is raised, return its type and message, as in Age Check.

For example:

- `parse_time("2:30")` returns `150`
- `time_message("2:30")` returns `"2:30 is 150 seconds."`
- `time_message("1:75")` returns `"ValueError: Seconds must be less than 60."`

Hints:

- `.count(":")` tells you how many colons there are.
- `.split(":")` gives a list of the parts on each side.
- `.isdigit()` is `True` only if every character is a digit (an empty string gives `False`).

Do not rename any `def` line. The tests call the functions by name.

## Running your program

Open the challenge file and press the Run button in the top right corner of VS
Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B**, the same as for the lab. The Lab 11 results appear first.
Scroll down to the **OPTIONAL CHALLENGES** section for these.

`SKIP` means you have not started that challenge yet. It is not an error.

## Reminders

- These are optional. Finish Lab 11 first.
- Check the type first, then the value.
- Raise errors in the first function. Catch them in the second.
- Returned text is matched exactly, including capitals and the period.
