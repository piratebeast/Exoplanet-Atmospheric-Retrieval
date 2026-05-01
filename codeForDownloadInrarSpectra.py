import requests 
import os
import time

def download_spectrum_batch(base_tmp_url, start_id, end_id, save_directory):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
        print(f"Created directory: {save_directory}")

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br'
    })

    print(f"Starting download from ID {start_id} to {end_id}...\n")

    for current_id in range(start_id, end_id + 1):
        str_id = str(current_id).zfill(7)
        
        dir_1 = f"dir_{str_id[0:2]}"
        dir_2 = f"dir_{str_id[2:4]}"
        
        filename = f"{str_id}_spectrum_components.csv"  
        file_url = f"{base_tmp_url}/{dir_1}/{dir_2}/{str_id}/{filename}" 
        save_path = os.path.join(save_directory, filename)

        if os.path.exists(save_path) and os.path.getsize(save_path) > 0:
            print(f"Skipping: {filename} (Already downloaded)")
            continue

        print(f"Fetching: {filename} ...")

        try:
            response = session.get(file_url, stream=True, timeout=20)
            
            if response.status_code == 404:
                print(f"  -> 404 Not Found. Skipping.")
                continue
                
            response.raise_for_status()

            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
            
            print(f"  -> Success!")
            time.sleep(0.3)  # Short delay to be polite to the server

        except requests.exceptions.RequestException as e:
            print(f"  -> Failed: {e}")
            time.sleep(2)  # Longer delay on failure to avoid hammering the server

if __name__ == "__main__":
    BASE_URL = "https://exoplanetarchive.ipac.caltech.edu/work/TMP_ycina6_24002/FDL/PSG/data" 
    START_NUMBER = 5051
    END_NUMBER = 19999
    SAVE_FOLDER = r"E:\Dataset for KE\INARA_Spectra_5000_to_19999"
    
    download_spectrum_batch(BASE_URL, START_NUMBER, END_NUMBER, SAVE_FOLDER)