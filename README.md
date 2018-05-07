# PyAutoClicker

## Description

Auto-clicker written in Python for Windows

## Usage

Possible args are:<br />

| Option | Description |
| ------- | --- |
| \-c X Y | Set integer coordinates to (X, Y). Defaults to (0, 0). |
| \-d D | Set start delay to integer value D. Defaults to 3 seconds. |
| \-r R | Set integer number of clicks per second. Defaults to 1 click per second. |
| \-q | Start in quit mode. |

While the program is running the user may press:<br /> 
P key to toggle the auto clicker. <br />
Q key to quit the program. <br />

## Examples

`PyAutoClicker.py -c 350 350`<br />
Start auto clicker at coordinates (350, 350).<br />
<br />

`PyAutoClicker.py -c 350 350 -r 6`<br />
Start auto clicker at coordinates (350, 350) at a rate of 6 clicks per second.<br />
<br />

`PyAutoClicker.py -q -d 5 -c 350 350`<br />
Start auto clicker in quiet mode with a delay of 5 seconds at coordinates (350, 350).<br />
<br />