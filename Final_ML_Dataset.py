import pandas as pd

print("Loading your 20,000 binned planets...")

# 1. Load your X data 
X_data = pd.read_csv(r'E:\Dataset for KE\Binned_X_Matrix.csv')
X_data['Spectrum_ID'] = X_data['Spectrum_ID'].astype(str)

target_ids = X_data['Spectrum_ID'].tolist()

print("Scanning the massive 30-million-row file safely...")

# 2. Load the y data safely using "Chunking"
y_data_chunks = []
chunk_size = 100000 

for chunk in pd.read_csv(r'E:\Dataset for KE\INARA_summary_parameters.csv', chunksize=chunk_size):
    # THE FIX: Changed 'PlanetIndex' to 'planet_index'
    chunk['planet_index'] = chunk['planet_index'].astype(str)
    
    # Filter: Only keep rows where the planet_index is in our target_ids list
    filtered_chunk = chunk[chunk['planet_index'].isin(target_ids)]
    y_data_chunks.append(filtered_chunk)
    
    total_found_so_far = sum(len(c) for c in y_data_chunks)
    if total_found_so_far >= len(target_ids):
        print("Found all 20,000 planets! Stopping the search early to save time.")
        break

# Combine our collected chunks
y_data = pd.concat(y_data_chunks)

print("Merging datasets together...")

# 3. The Final Merge
final_dataset = pd.merge(
    X_data, 
    y_data, 
    left_on='Spectrum_ID', 
    right_on='planet_index', # THE FIX: Changed to match your file
    how='inner' 
)

# Clean up the duplicate ID column
final_dataset = final_dataset.drop(columns=['planet_index'])

# 4. Save the ultimate file!
save_path = r'E:\Dataset for KE\Final_ML_Dataset.csv'
final_dataset.to_csv(save_path, index=False)

print(f"\n✅ SUCCESS! Dataset merged and saved to: {save_path}")
print(f"Total Rows: {final_dataset.shape[0]}")
print(f"Total Columns: {final_dataset.shape[1]}")