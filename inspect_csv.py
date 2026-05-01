import pandas as pd

def preview_csv_columns(file_path):
    try:
        # We only need to read the first 3 rows to get examples!
        # This makes it lightning fast.
        df = pd.read_csv(file_path, nrows=3)
        
        print(f"\n📄 Analyzing File: {file_path}")
        print(f"📊 Total Columns: {len(df.columns)}\n")
        print("=" * 50)
        
        # Loop through every single column one by one
        for column_name in df.columns:
            # Grab the first two items in that column as a list
            examples = df[column_name].dropna().head(2).tolist()
            
            print(f"Column Name :  {column_name}")
            
            # Format the examples nicely
            if len(examples) == 2:
                print(f"Examples    :  {examples[0]}  |  {examples[1]}")
            elif len(examples) == 1:
                print(f"Examples    :  {examples[0]}")
            else:
                print(f"Examples    :  [Empty/Blank Column]")
                
            print("-" * 50)
            
    except FileNotFoundError:
        print(f"❌ Error: Could not find the file at {file_path}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    # Point this directly to the very first file you downloaded
    TARGET_FILE = r"E:\Dataset for KE\ABC\Level1Data\Level1Data\all_data.csv"
    
    preview_csv_columns(TARGET_FILE)