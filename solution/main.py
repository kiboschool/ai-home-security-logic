from logic import *
import copy

# TODO 1: Define the Symbols
# EXAMPLE: motion_living_room = Symbol("MotionLivingRoom")

# YOUR CODE HERE
MotionLivingRoom = Symbol("MotionLivingRoom")
MotionKitchen = Symbol("MotionKitchen")
MotionGarage = Symbol("MotionGarage")
WindowKitchen = Symbol("WindowKitchen")
WindowBedroom = Symbol("WindowBedroom")
DoorFront = Symbol("DoorFront")
DoorBack = Symbol("DoorBack")
SmokeDetector = Symbol("SmokeDetector")

# Conditions
Morning = Symbol("Morning")
Day = Symbol("Day")
Evening = Symbol("Evening")
Night = Symbol("Night")
FamilyHome = Symbol("FamilyHome")
FamilyAsleep = Symbol("FamilyAsleep")


# TODO 2: Construct the Knowledge Base
# knowledge = And(
#     # YOUR CODE HERE
# )

knowledge = And(
    # If smoke detector is activated, it's always a safety issue
    Implication(SmokeDetector, Symbol("SafetyIssue")),

    # Motion in the living room, kitchen, or garage during the night when the family is asleep implies a security breach
    Implication(And(Or(MotionLivingRoom, MotionKitchen, MotionGarage), Night, FamilyAsleep), Symbol("SecurityBreach")),

    # Window or door opening at night is a security breach
    Implication(And(Or(WindowKitchen, WindowBedroom, DoorFront, DoorBack), Night), Symbol("SecurityBreach")),

    # If the family is home, door opening is not a security breach but needs to be checked
    Implication(And(Or(DoorFront, DoorBack), FamilyHome), Symbol("CheckDoors")),

    # Define conditions for time of day to handle transitions
    Or(Morning, Day, Evening, Night),

    # At least one condition of family presence is always true
    Or(FamilyHome, FamilyAsleep)
)



# TODO 3: Implement Evaluation Function
"""
@params
model: dictionary of symbols and their values

@returns
string: security status of the home
- "Safety issue detected."
- "Security breach detected."
- "Check doors."
- "Home is secure."
"""
def evaluate_security_status(model):
    ## Deep copy the knowledge base
    knowledge_cp = copy.deepcopy(knowledge)
    
    # Add the model to the knowledge base and check for safety and security issues
    for sym in model:
        if model[sym]:
            knowledge_cp.add(Symbol(sym))

    # Check for safety issue
    if model_check(knowledge_cp, Symbol("SafetyIssue")):
        return "Safety issue detected."

    # Check for security breach
    if model_check(knowledge_cp, Symbol("SecurityBreach")):
        return "Security breach detected."

    # Check doors if family is home
    if model_check(knowledge_cp, Symbol("CheckDoors")):
        return "Check doors."

    return "Home is secure."

if __name__ == "__main__":

    # Example models 
    model_1 = {
        "MotionLivingRoom": False,
        "MotionKitchen": False,
        "MotionGarage": False,
        "WindowKitchen": False,
        "WindowBedroom": False,
        "DoorFront": False,
        "DoorBack": False,
        "SmokeDetector": False, ## Smoke detector is not activated => no safety issue
        "Morning": False,
        "Day": False,
        "Evening": False,
        "Night": True,
        "FamilyHome": False,
        "FamilyAsleep": True
    }

    print(evaluate_security_status(model_1)) # Expected: "Home is secure."

    model_2 = {
        "MotionLivingRoom": False,
        "MotionKitchen": False,
        "MotionGarage": True,
        "WindowKitchen": False,
        "WindowBedroom": False,
        "DoorFront": False,
        "DoorBack": False,
        "SmokeDetector": False, ## Smoke detector is not activated => no safety issue
        "Morning": False,
        "Day": False,
        "Evening": False,
        "Night": True,
        "FamilyHome": False,
        "FamilyAsleep": True
    }

    print(evaluate_security_status(model_2)) # Expected: "Security breach detected."
