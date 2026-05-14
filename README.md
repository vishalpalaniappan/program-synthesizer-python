# program-synthesizer-python
This tool synthesizes a python program that contains the implementation of behaviors specified in the design abstraction language.

Overview:

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