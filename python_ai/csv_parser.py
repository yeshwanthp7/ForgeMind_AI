import pandas as pd

def read_csv_file(csv_path):
    """
    Read a CSV file and return a DataFrame.
    """
    try:
        data = pd.read_csv(csv_path)
        return data
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None


# Test
if __name__ == "__main__":
    csv_file = "sample_data/sample_log.csv"

    data = read_csv_file(csv_file)

    if data is not None:
        print("CSV Loaded Successfully!")
        print(data.head())