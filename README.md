# program-synthesizer-python
This tool synthesizes a python program that contains the implementation of behaviors specified in the design abstraction language.

# Usage

Example:
```
python3 main.py --package ./packages/synthPackage.json 
```

# Overview

This tool will read each entry in the synth package and for each behavior it will:
- Create a function with the name
- Add log statements for the behavior
- Add log statements for the participants before behavior
- synthesize the program from the transformations
- Add log statements for the participants after behavior

The actual synthesis from the transformations is done by first reading the type of transformation. Then using that it will populate the AST node and use that to generate the code. I'll start with just the set operation to establish the structure.

For example:
```
{
    "behavior": "behavior1",
    "pre_participants": [
        "book"
    ],
    "transformations": [
        {
            "targetParticipantName": "book",
            "keys": [
                "name"
            ],
            "valueParticipantName": "Harry Potter"
        }
    ],
    "post_participants": [
        "book",
        "name4"
    ]
}
```
will become
```
def b_behavior1(book):
    semanticLogger.logBehavior("behavior1")
    semanticLogger.logPreParticipant("book")
    book["name"] = "Harry Potter"
    semanticLogger.logPostParticipant("book")
```

Upcoming changes:
- I need to add an export synth package to the engine that will create the required package
- In the engine, I need to specify the relevant metadata for more primitives
- I need to import the genreated package into this program and use it to synthesize the program
- I need to add support for more primitive types in this program
- Obviously this will actually be in the engine, I just wanted to use the python AST library because it is really convenient for now.
- Eventually I will think about scaffolding to connect to reality etc. 