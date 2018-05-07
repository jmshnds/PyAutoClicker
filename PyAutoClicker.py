# Simple autoclicker that can be used for idle games

import sys
import time
import win32api, win32con

class AutoClicker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def click(self, x, y):
        win32api.SetCursorPos((self.x, self.y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,self.x,self.y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,self.x,self.y,0,0)

def handleErr(message):
    print("ERROR: %s\n", message)
    sys.exit()

def parseArguments(argv):
    # Default options
    options = {'quiet': False, 'x': 0, 'y': 0}
    
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
                
            elif argv[i] == "-c" or argv[i] == "-coordinates":
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













            
        