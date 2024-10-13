from logic import *
import copy

# TODO 1: Define the Symbols
# EXAMPLE: motion_living_room = Symbol("MotionLivingRoom")



# TODO 2: Construct the Knowledge Base
knowledge = And(
    # YOUR CODE HERE
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
    my_knowledge = copy.deepcopy(knowledge)
    
    # Add the model to the knowledge base and check for safety and security issues
    
    raise NotImplementedError

if __name__ == "__main__":

    # Example models for testing 
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
