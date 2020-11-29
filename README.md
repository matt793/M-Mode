# M-Mode
What is M-Mode?

M-Mode is a simple pyhton script with coded bash comands, to turn a WiFi card (equipt with Monitor-Mode): Monitor-Mode on.

## Instructions

Instructions are simple. Just run the `M-Mode.sh` script in a Linux terminal.
You will then be shown a list of network conections: chose your WiFi card name to be entered.
You will then be asked to enter the {name} of your WiFi card, copy and paste the name in the prompt.
Once you press enter, a READY, SET, GO, prompt will turn the card's Monitor Mode on.

## Varifing 

To make sure the script was successful run the comand 'iwconfig'.
If your card for some reason is still in Manage Mode, run the script once more, and the card should read Monitor-Mode. 

## Installation

Run `sudo ./install.sh`.

![Example](/images/2ScreenShot.png "Example")
