#!/usr/bin/env python

def select_path(open_slits):
    if open_slits == 1:
        print("Following Path 1")
        # Implement trajectory for Path 1 here
    elif open_slits == 2:
        print("Following Path 2")
        # Implement trajectory for Path 2 here
    elif open_slits == 3:
        print("Following Path 3")
        # Implement trajectory for Path 3 here
    else:
        print("Error: Invalid number of open slits.")

if __name__ == "__main__":
    open_slits = 2  # Mock input for testing
    select_path(open_slits)

