import random

class CaseManager:

    def __init__(self):

        self.current_case = "Museum Theft"

        self.suspect = random.choice([
            "Bob",
            "Sarah",
            "Guard",
            "Owner"
        ])

    def generate_clues(self):

        if self.suspect == "Sarah":

            return {
                "Bob":
                    "I saw Sarah near the museum.",

                "Sarah":
                    "I was home all night.",

                "Guard":
                    "Sarah left in a hurry.",

                "Owner":
                    "Sarah knew the museum schedule."
            }

        elif self.suspect == "Bob":

            return {
                "Bob":
                    "I was sleeping all night.",

                "Sarah":
                    "Bob was near the museum.",

                "Guard":
                    "Bob looked nervous.",

                "Owner":
                    "Bob had a museum key."
            }

        elif self.suspect == "Guard":

            return {
                "Bob":
                    "The Guard disabled alarms.",

                "Sarah":
                    "The Guard entered after closing.",

                "Guard":
                    "I stayed at home.",

                "Owner":
                    "Only the Guard had access."
            }

        else:

            return {
                "Bob":
                    "Owner argued about money.",

                "Sarah":
                    "Owner looked suspicious.",

                "Guard":
                    "Owner entered after hours.",

                "Owner":
                    "I am innocent."
            }