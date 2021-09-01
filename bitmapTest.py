#! /usr/bin/python3
# 20210828 bitmap project
# Author: Jeremy Beard
# Source: The Big Book of Small Python Projects

import sys

# (!) Try changing this multiline string to any image you like:

# there are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from
# https://inventwithpython.com/bitmapworld.txt)
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Message, by Al Swigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input ('> ')
if message == '':
    sys.exit()
    
# loops over each line in the bitmap
for line in bitmap.splitlines():
    # loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # print a character from the message:
            print(message[i % len(message)], end='')
    print() #print a newline
    

















