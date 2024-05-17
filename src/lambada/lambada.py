import os
import time
import sys

FRAME1 = """ 
                           //
( ** )                    //
  \/ ====================/
  @@                    @@ 
"""

FRAME2 = r"""
                        \\
( ** )                   \\
  \/ ====================/
  @@                    @@ 
"""

# Function to clear the screen
def clear_screen():
    # Windows
    os.system('cls') if os.name == 'nt' else os.system('clear')
        
    # macOS and Linux
        

def lambada():
    try:
        while True:
            # Clear screen and print _s1
            clear_screen()
            print(FRAME1)
            time.sleep(0.5)  # Adjust the speed as needed
            
            # Clear screen and print _s2
            clear_screen()
            print(FRAME2)
            time.sleep(0.5)  # Adjust the speed as needed
    except KeyboardInterrupt:
        # Optionally clear the screen one last time when exiting
        # clear_screen()
        print("Animation stopped.")
        sys.exit()

if __name__ == "__main__":
    lambada()