from agent.utils import load_hsn_data

class SuggestHSNPlan:
    def __init__(self):
        self.df = load_hsn_data()
        self.df['Description'] = self.df['Description'].str.upper()

    def suggest_codes(self, description, top_n=3):
        description = description.upper()
        matches = self.df[self.df['Description'].str.contains(description, na=False)]
        if matches.empty:
            return [{"Message": "No suggestions found."}]
        return matches[['HSNCode', 'Description']].head(top_n).to_dict(orient='records')
