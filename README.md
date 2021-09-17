# ssw567-triangle-qa
Homework assignment 2 involving testing of someone else's triangle classification program.

[![Build Status](https://app.travis-ci.com/kylerobots/ssw567-triangle-qa.svg?branch=main)](https://app.travis-ci.com/kylerobots/ssw567-triangle-qa)

This takes the existing triangle classification code and first expands the unit tests to cover more possible cases.
Then, the code was updated so that all the tests are passed.

## Usage ##
The function can be imported into your code with:
```
from Triangle import classifyTriangle
```

It then is called as follows:
```
result = classifyTriangle(a, b, c)
```

Inputs a, b, and c are numerics representing the three sides of the triangle. It returns a string indicating the\
triangle type according to the following table.

| Label | Returned If |
| --- | --- |
| Equilateral | All three sides are equal |
| Isosceles | Exactly one pair of sides are equal |
| Scalene | No pair of sides are equal |
| NotATriangle | Not a valid triangle |
| Right | The sum of any two sides equals the square of the third side |