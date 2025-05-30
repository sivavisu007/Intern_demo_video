from agent.validate_plan import ValidateHSNPlan
from agent.suggest_plan import SuggestHSNPlan

class HSNAgent:
    def __init__(self):
        self.validator = ValidateHSNPlan()
        self.suggester = SuggestHSNPlan()

    def run(self):
        print("Welcome to the HSN Code Validation and Suggestion Agent (ADK Powered)")
        while True:
            choice = input("\nChoose an option:\n1. Validate HSN Code\n2. Suggest HSN Code\n3. Exit\n> ")
            if choice == '1':
                code = input("Enter HSN Code to validate: ")
                result = self.validator.validate_code(code)
                print(result)
            elif choice == '2':
                desc = input("Enter product/service description: ")
                suggestions = self.suggester.suggest_codes(desc)
                for s in suggestions:
                    print(s)
            elif choice == '3':
                break
            else:
                print("Invalid choice.")
