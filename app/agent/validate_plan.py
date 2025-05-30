import pandas as pd
from agent.utils import load_hsn_data

class ValidateHSNPlan:
    def __init__(self):
        self.df = load_hsn_data()
        self.df['HSNCode'] = self.df['HSNCode'].astype(str)
        self.df['Description'] = self.df['Description'].str.upper()
        self.hsn_set = set(self.df['HSNCode'])

    def validate_code(self, code):
        result = {"HSNCode": code}
        if not code.isdigit() or not (2 <= len(code) <= 8):
            result["Valid"] = False
            result["Reason"] = "Invalid format"
            return result

        if code not in self.hsn_set:
            result["Valid"] = False
            result["Reason"] = "Code not found"
            return result

        result["Valid"] = True
        result["Description"] = self.df[self.df['HSNCode'] == code]['Description'].values[0]

        # Hierarchical validation
        hierarchy_valid = all(code[:i] in self.hsn_set for i in range(2, len(code), 2))
        result["HierarchyValid"] = hierarchy_valid

        return result
