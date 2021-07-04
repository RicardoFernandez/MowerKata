# MowerKata

Kata based in MarsRover kata.
This kata has intended overengineering in order to put in practice DDD based in Hexagonal Architecture and some design patterns.

In other languages would be easy to show decoupling implementing for Interfaces, I was thinking about do this using ABC classes but I decided not to do it.

Developed using TDD outside-inside approach, trying to test from the point of view of the user and of course avoiding to test implementation details.

Some validations are not finished:
* Mower instructions moves the mower to an out of bounds point
* I assumed that the input of the facing direction is always valid
* I assumed that plateau will always receive a valid positive integer
* I assumed that the number of characters introduced is valid for mower initial point and plateau

Implemented validations are to show how to raise a domain exception that is handled in the application layer:
* A domain exception will be raised when the initial position of the mower is out of bounds, this exceptions is hadled and a message is shown.

Example:
```
5 5
6 6 N
```

* A domain exception will be raised when one of the instructions are not correct, this exception is handled and a message is shown.

Example:
```
LMRX
```


## Launching the application 🚀

### Pre-requirements 📋

* Python 3.7 or higher is required to run this proyect

* To run test suit Pytest should be installed
```
pip install pytest
```

### Introducing new plateau, mowers and inststructions 🔧

To introduce new orders you should include them in the file called `instructions.txt` in the root of the proyect.
An example:

```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

To run the application move to the root of the proyect in your cmd and run the next command:

```
python main.py ./instructions.txt
```

The outpull will be the final locations of the mowers

```
1 3 N
5 1 E
```
