import pandas as pd
import glob
import os

def merge_all_csvs(folder_path, output_filename):
    print(f"Scanning folder: {folder_path} ...")
    
    # 1. Find all files ending in .csv in the folder
    search_pattern = os.path.join(folder_path, "*_spectrum_components.csv")
    all_files = glob.glob(search_pattern)
    
    # Sort them so they merge in numerical order (0000000, 0000001, etc.)
    all_files.sort()
    
    total_files = len(all_files)
    print(f"Found {total_files} files! Starting the merge process...\n")
    
    if total_files == 0:
        print("No CSV files found to merge.")
        return

    # 2. Read each file and store it in a list
    dataframe_list = []
    
    for i, file in enumerate(all_files):
        # Extract the ID from the filename (e.g., '0000032')
        file_id = os.path.basename(file).split('_')[0]
        
        # Read the CSV
        df = pd.read_csv(file)
        
        # Add a new column so you know which file each row came from
        df['Spectrum_ID'] = file_id 
        
        dataframe_list.append(df)
        
        # Print progress every 100 files so you know it hasn't frozen
        if (i + 1) % 100 == 0:
            print(f"  -> Processed {i + 1} / {total_files} files...")

    # 3. Glue them all together vertically into one giant table
    print("\nGluing datasets together (this might take a few seconds)...")
    master_df = pd.concat(dataframe_list, ignore_index=True)
    
    print("\nMerge complete! Here is a preview of your massive dataset:")
    print("-" * 50)
    print(master_df.head())
    print("-" * 50)
    print(f"Total Rows: {master_df.shape[0]:,}")
    print(f"Total Columns: {master_df.shape[1]}")
    
    # 4. Save the master dataset back to your hard drive
    final_save_path = os.path.join(folder_path, output_filename)
    print(f"\nSaving master file to: {final_save_path}")
    master_df.to_csv(final_save_path, index=False)
    print("✅ All done!")

if __name__ == "__main__":
    
    # Your specific folder
    FOLDER_PATH = r"E:\Dataset for KE\INARA_Spectra"
    
    # The name of the giant combined file it will create
    OUTPUT_FILE = "MASTER_Spectra_Dataset.csv"
    
    merge_all_csvs(FOLDER_PATH, OUTPUT_FILE)