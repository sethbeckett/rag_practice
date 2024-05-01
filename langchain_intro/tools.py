import random
import time

def get_current_wait_time(hospital: str) -> int | str:
    """Function to generate fake wait times"""

    if hospital not in ["A", "B", "C", "D"]:
        return f"Hosipital {hospital} does not exist"
    
    # fake API delay
    time.sleep(1)

    return random.randint(0,10000)