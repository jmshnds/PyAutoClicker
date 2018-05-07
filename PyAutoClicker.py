# PyAutoClicker
# Description: Simple autoclicker that can be used for clicking a lot
# Author: jmshnds
# Date: 7 May 2018

import sys
import time

from AutoClicker import AutoClicker

def handleErr(message):
    print("ERROR: %s\n", message)
    sys.exit()

def parseArguments(argv):
    # Default options
    options = {'quiet': False, 'x': 0, 'y': 0, 'delay': 3}
    
    # Parse arguments and set options
    i = 1
    while i < len(argv):
        try:
            # arg was an unmatched value
            int(argv[i])
            float(argv[i])
            handleErr("Invalid argument " + argv[i])
        except ValueError:
            if argv[i] == "-q" or argv[i] == "--quiet":
                options['quiet'] = True
                
            elif argv[i] == "-c" or argv[i] == "--coordinates":
                if i+2 < len(argv):
                    try:
                        # Get coordinates from next args
                        options['x'] = int(argv[i+1])
                        options['y'] = int(argv[i+2])
                    except ValueError:
                        handleErr("Did not enter integer coordinates")
                    i += 2 # increment arg index
                else:
                    handleErr("Missing (x,y) coordinates")

            elif argv[i] == "-d" or argv[i] == "--delay":
                if i+1 < len(argv):
                    try:
                        # Get delay value from next arg
                        options['delay'] = int(argv[i+1])
                    except ValueError:
                        handleErr("Did not enter integer delay")
                    i += 1
                else:
                    handleErr("Missing delay value")
            
            else:
                handleErr("Unknown argument " + argv[i])
        i += 1
    # end While loop
    return options
    

if __name__ == '__main__':

    # Set options from command line arguments
    options = parseArguments(sys.argv)

    # Initialize Autoclicker
    clicker = AutoClicker(options['x'], options['y'])
    
    # Print start message
    if not options['quiet']:
        print("Starting autoclicker at coordinates(%d, %d)" \
              % (clicker.x, clicker.y))
        
        # Delay start
        for i in range(options['delay'])[::-1]:
            print(i+1)
            time.sleep(1)
    else:
        # Delay start
        time.sleep(options['delay'])

    clicker.start() # Start auto clicking, returns once it stops

    if not options['quiet']:
        print("Autoclicking complete")
