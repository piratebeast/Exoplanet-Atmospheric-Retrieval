import os

def verify_downloads(save_directory, start_id, end_id):
    missing_files = []
    empty_files = []

    print(f"Scanning directory: {save_directory}")
    print(f"Checkingf IDs for {start_id} to {end_id}")

    for current_id in range(start_id, end_id + 1):
        str_id = str(current_id).zfill(7)
        filename = f"{str_id}_spectrum_components.csv"
        file_path = os.path.join(save_directory, filename)

        if not os.path.exists(file_path):
            missing_files.append(str_id)
        elif os.path.getsize(file_path):
            empty_files.append(str_id)
    
    if not missing_files and not empty_files:
        print("SUCCESS: All files in the range are present and valid!")
    else:
        if missing_files:
            print(f"❌ MISSING FILES ({len(missing_files)} total):")
            # Only print the first 20 to avoid flooding your screen
            print(f"   {', '.join(missing_files[:20])}")
            if len(missing_files) > 20:
                print(f"   ... and {len(missing_files) - 20} more.")
        
        if empty_files:
            print(f"\n⚠️ CORRUPTED/EMPTY FILES ({len(empty_files)} total):")
            print(f"   {', '.join(empty_files[:20])}")
            if len(empty_files) > 20:
                print(f"   ... and {len(empty_files) - 20} more.")
            print("\nPRO TIP: Delete the empty files so your download script can re-download them!")

if __name__ == "__main__":
    SAVE_FOLDER = r"E:\Dataset for KE\INARA_Spectra"

    START_NUMBER = 0
    END_NUMBER = 999
    verify_downloads(SAVE_FOLDER, START_NUMBER, END_NUMBER)