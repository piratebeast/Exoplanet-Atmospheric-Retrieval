import pandas as pd
import numpy as np
import glob
import os

# Pointing to your exact dataset folder
folder_path = r'E:\Dataset for KE\INARA_Spectra' 

all_files = glob.glob(os.path.join(folder_path, "*_spectrum_components.csv"))
print(f"Found {len(all_files)} files. Starting processing... Please wait.")

binned_rows = []

for file in all_files:
    df = pd.read_csv(file)
    filename = os.path.basename(file)
    spectrum_id = filename.split('_')[0]
    
    # THE FIX: Force both columns to be numeric. Any text/errors become NaN.
    planet_signal = pd.to_numeric(df['planet_signal_(erg/s/cm2)'], errors='coerce')
    stellar_signal = pd.to_numeric(df['stellar_signal_(erg/s/cm2)'], errors='coerce')
    
    # Calculate transit depth safely
    transit_depth = planet_signal / stellar_signal
    
    # Splitting into 200 chunks
    chunks = np.array_split(transit_depth, 200)
    
    # Using np.nanmean so if a chunk contains a NaN (from a bad row), 
    # it calculates the mean of the valid numbers instead of throwing an error.
    binned_values = [np.nanmean(chunk) for chunk in chunks]
    
    row_data = {'Spectrum_ID': spectrum_id}
    for i, val in enumerate(binned_values):
        row_data[f'bin_{i}'] = val
        
    binned_rows.append(row_data)

final_X_matrix = pd.DataFrame(binned_rows)
final_X_matrix.set_index('Spectrum_ID', inplace=True)

# Saving exactly to your E: drive Dataset folder
save_path = r'E:\Dataset for KE\Binned_X_Matrix.csv'
final_X_matrix.to_csv(save_path)

# This will only print when the file is officially created
print(f"\n✅ SUCCESS! File officially saved exactly here: {save_path}")