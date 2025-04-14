import os
import time
from datetime import datetime

# Target shutdown time
shutdown_time = "07:20"

while True:
    # Get the current time
    current_time = datetime.now().strftime("%H:%M")
    
    # Check if the current time matches the shutdown time
    if current_time == shutdown_time:
        # Shutdown the PC
        os.system("shutdown /s /t 1")
        break
    
    # Wait for 30 seconds before checking again to reduce CPU usage
    time.sleep(30)
