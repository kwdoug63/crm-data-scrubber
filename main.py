import pandas as pd
import re

class DataScrubber:
    """Standardizes messy contact data for CRM import."""
    
    @staticmethod
    def clean_name(name):
        return str(name).strip().title()

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        return bool(re.match(pattern, str(email).lower()))

    def process_csv(self, file_path):
        # In a real scenario, this would load a CSV
        # For this demo, we create a 'messy' dataframe
        data = {
            'Name': [' kEnNeTh ', 'john doe', 'SARAH smith'],
            'Email': ['kenneth@relativity.com', 'invalid-email.com', 'sarah@gmail.com']
        }
        df = pd.DataFrame(data)
        
        print("--- Original Messy Data ---")
        print(df)
        
        # Apply cleaning logic
        df['Name'] = df['Name'].apply(self.clean_name)
        df['Email_Valid'] = df['Email'].apply(self.is_valid_email)
        
        print("\n--- Cleaned Data for CRM ---")
        return df

if __name__ == "__main__":
    scrubber = DataScrubber()
    cleaned_data = scrubber.process_csv(None)
    print(cleaned_data)
