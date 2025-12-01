import sys
import os
from pathlib import Path

# Add the directory containing the script to sys.path
sys.path.append(os.path.join(os.getcwd(), '.claude', 'scripts'))

try:
    from transkrypcje_db import get_unprocessed_files, start_processing
    
    # Get 1 file to process
    files = get_unprocessed_files('surowa->oczyszczona', limit=1)
    
    if not files:
        print("NO_UNPROCESSED_FILES")
    else:
        file_id, path, name = files[0]
        
        # Try to lock the file
        processing_id = start_processing(file_id, 'surowa->oczyszczona')
        
        if processing_id:
            # Output format: ID|PATH|NAME|PROCESSING_ID
            print(f"{file_id}|{path}|{name}|{processing_id}")
        else:
            print("FILE_LOCKED")
            
except Exception as e:
    print(f"ERROR: {str(e)}")
