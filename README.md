# Assignment: Home Security System

## Objective:
The objective of this assignment is to utilize propositional logic to model and query a basic security system for a home. The home is equipped with three types of sensors:

1. Motion sensors installed in the living room, kitchen, and garage.
2. Window sensors positioned in the kitchen and bedroom.
3. Door sensors placed at the front and back doors.
4. Additionally, there is a smoke detector.


The system should take into account both the time of day (Morning, Day, Evening, Night) and whether the family is expected to be home or asleep.

The goal is to construct a knowledge base capable of deducing potential security breaches or safety concerns under various conditions.

Here are the rules governing the security system:

- Activation of the smoke detector always indicates a safety issue.
- Motion detected in the living room, kitchen, or garage during the night when the family is asleep suggests a security breach.
- Opening a window or door during the night constitutes a security breach.
- If the family is at home, the opening of a door is not considered a security breach but should be investigated.

## Your Task:
In the `main.py` file, follow the to-do comments to:
1. reate a knowledge base to capture the rules governing the security system. This involves translating the rules mentioned in the assignment into propositional logic symbols and rules.
2. Implement the `evaluate_security_status` function.


## Testing:
The `test_main.py` file contains a few test cases to help you verify the correctness of your implementation. You can run the test cases by running the `test_main.py` file.

```bash
python test_main.py
```



