# CS50’s Introduction to Programming with Python

This repository contains code developed for "[CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/)" offered by Harvard OpenCourseWare. The course includes nine problem sets, each with 4-5 predefined tasks, and concludes with a final project. The following section outlines the topics covered in each problem set and provides details about the assignments. 

## Problem Set 0 - Functions, Variables

* [Indoor Voice](https://cs50.harvard.edu/python/2022/psets/0/indoor/) - prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespaces stay unchanged.
* [Playback Speed](https://cs50.harvard.edu/python/2022/psets/0/playback/) - prompts the user for input and then outputs that same input, replacing each ' '(whitespace) with '...'.
* [Making Face](https://cs50.harvard.edu/python/2022/psets/0/faces/) - implements a function called `convert` that accepts a `str` as input and returns that same input with any `:)` converted to 🙂 (otherwise known as a slightly smiling face) and any `:(` converted to 🙁 (otherwise known as a slightly frowning face). All other text is returned unchanged.
* [Einstein](https://cs50.harvard.edu/python/2022/psets/0/einstein/) - prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. 
* [Tip Calculator](https://cs50.harvard.edu/python/2022/psets/0/tip/) - implements two functions: `dollars_to_float` (accepts a `str` as input (formatted as `$##.##`, wherein each `#` is a decimal digit), and removes the leading `$`, and returns the amount as a `float`), and `percent_to_float` (accepts a `str` as input (formatted as `##%`, wherein each `#` is a decimal digit), removes the trailing `%`, and returns the percentage as a float).

## Problem Set 1 - Conditionals

* [Deep Thought](https://cs50.harvard.edu/python/2022/psets/1/deep/) - program prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes` if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. Otherwise the output is `No`.
* [Bank](https://cs50.harvard.edu/python/2022/psets/1/bank/) - program prompts the user for a greeting. If the greeting starts with “hello”, the progam outputs `$0`. If the greeting starts with an “h” (but not “hello”), output is `$20`. Otherwise, output is `$100`. User's greeting is treated case-insenitevely and any leading whitespace in the user’s greeting are ignored.
* [File Extensions](https://cs50.harvard.edu/python/2022/psets/1/extensions/) - program prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes: `.gif`, `.jpg`, `.jpeg`, `.png`, `.pdf`, `.txt`, `.zip`
* [Math Interpreter](https://cs50.harvard.edu/python/2022/psets/1/interpreter/) - program prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. It assumes that the user’s input will be formatted as `x y z`, with one space between `x` and `y` and one space between `y` and `z`, wherein: `x` is an integer, `y` is `+`, `-`, `*`, or `/` and `z` is an integer.
* [Meal Time](https://cs50.harvard.edu/python/2022/psets/1/meal/) - program prompts the user for a time and outputs whether it’s `breakfast time`, `lunch time`, or `dinner time`. If it’s not time for a meal, it does not output anything at all. It assumes that the user’s input will be formatted in 24-hour time as `#:##` or `##:##`. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.




