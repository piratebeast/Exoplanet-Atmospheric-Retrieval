import os
from astropy.io import ascii

def convert_tbl_to_csv(tbl_filepath, csv_filepath):
    print(f"📄 Analyzing NASA .tbl file: {os.path.basename(tbl_filepath)}...")
    
    try:
        # Astropy automatically detects the weird NASA IPAC formatting and reads it
        data_table = ascii.read(tbl_filepath)
        
        # Convert the astronomy table into a standard Pandas DataFrame
        df = data_table.to_pandas()
        
        # Save it to your hard drive as a normal CSV
        df.to_csv(csv_filepath, index=False)
        
        print("\n✅ Conversion Successful!")
        print(f"💾 Saved as: {csv_filepath}")
        print("-" * 50)
        print(f"Total Rows   : {len(df):,}")
        print(f"Total Columns: {len(df.columns)}")
        print("-" * 50)
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find the file at {tbl_filepath}")
    except Exception as e:
        print(f"❌ An error occurred during conversion: {e}")

if __name__ == "__main__":
    
    # --- CONFIGURATION ---
    # 1. Put the exact path to your downloaded .tbl file here
    INPUT_TBL_FILE = r"E:\Dataset for KE\parameters\parameters.tbl"
    
    # 2. Put what you want the new CSV file to be named here
    OUTPUT_CSV_FILE = r"E:\Dataset for KE\converted_data.csv"
    
    convert_tbl_to_csv(INPUT_TBL_FILE, OUTPUT_CSV_FILE)