import unittest
from main import evaluate_security_status

class TestSecuritySystem(unittest.TestCase):

    def setUp(self):
        self.base_model = {
            "MotionLivingRoom": False,
            "MotionKitchen": False,
            "MotionGarage": False,
            "WindowKitchen": False,
            "WindowBedroom": False,
            "DoorFront": False,
            "DoorBack": False,
            "SmokeDetector": False,
            "Morning": False,
            "Day": False,
            "Evening": False,
            "Night": False,
            "FamilyHome": False,
            "FamilyAsleep": False
        }

    def test_smoke_detector_triggers_safety_issue(self):
        model = self.base_model.copy()
        model["SmokeDetector"] = True
        self.assertEqual(evaluate_security_status(model), "Safety issue detected.")

    def test_night_time_motion_in_garage_family_asleep_triggers_security_breach(self):
        model = self.base_model.copy()
        model.update({"MotionGarage": True, "Night": True, "FamilyAsleep": True})
        self.assertEqual(evaluate_security_status(model), "Security breach detected.")

    def test_window_open_at_night_triggers_security_breach(self):
        model = self.base_model.copy()
        model.update({"WindowKitchen": True, "Night": True})
        self.assertEqual(evaluate_security_status(model), "Security breach detected.")

    def test_front_door_open_family_home_prompts_to_check_doors(self):
        model = self.base_model.copy()
        model.update({"DoorFront": True, "FamilyHome": True})
        self.assertEqual(evaluate_security_status(model), "Check doors.")

    def test_everything_secure_during_the_day(self):
        model = self.base_model.copy()
        model["Day"] = True
        self.assertEqual(evaluate_security_status(model), "Home is secure.")

    def test_motion_in_living_room_at_night_with_family_home(self):
        model = self.base_model.copy()
        model.update({"MotionLivingRoom": True, "Night": True, "FamilyHome": True})
        self.assertEqual(evaluate_security_status(model), "Home is secure.")

    def test_back_door_open_at_night_triggers_security_breach(self):
        model = self.base_model.copy()
        model.update({"DoorBack": True, "Night": True})
        self.assertEqual(evaluate_security_status(model), "Security breach detected.")

    def test_motion_in_kitchen_with_family_asleep_at_night_triggers_security_breach(self):
        model = self.base_model.copy()
        model.update({"MotionKitchen": True, "Night": True, "FamilyAsleep": True})
        self.assertEqual(evaluate_security_status(model), "Security breach detected.")

    def test_bedroom_window_open_with_family_home(self):
        model = self.base_model.copy()
        model.update({"WindowBedroom": True, "FamilyHome": True})
        self.assertEqual(evaluate_security_status(model), "Home is secure.")

    def test_garage_motion_during_the_day(self):
        model = self.base_model.copy()
        model.update({"MotionGarage": True, "Day": True})
        self.assertEqual(evaluate_security_status(model), "Home is secure.")

if __name__ == "__main__":
    unittest.main()
