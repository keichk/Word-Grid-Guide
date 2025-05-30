# Word-Grid-Guide
In this challenge you have a grid in which you need to find a list of words.  After you find all the words in the grid, the remaining characters flattened will be the password for the password-protected archive which contains the flag.
The patterns you can find in the grid are the following:

Horizontal

Vertical

Diagonal

L-pattern (Horizontal and Vertical combined with one angle, direction only changes once from Horizontal to Vertical or vice versa)

All the words in the grid can be written in forward or backward direction (also for Diagonal & L-pattern words).

Letters cannot be part of more than one word in the grid.

## Example

### Input file (challenge.txt)

Grid:
C U P B O A R D P A
R I W E I H E D R C
D B C K J B R R D S
A B E N E F A C T R
E O T I C K L E R P
H C D M X W U Q E F
M Y T R E V O P S I
U L D E T T E P S D
R B C K Z E R S V G
D L I M A E G F H X

Words:
PETTED
CUPBOARD
DRUMHEAD
BENEFACTRESS
TICKLE
POVERTY

### Step 1: Find all words and cancel them from the grid

_ _ _ _ _ _ _ _ P A
R I W E I H E D R C
_ B C K J B R R D S
_ _ _ _ _ _ _ _ _ R
_ O _ _ _ _ _ _ _ P
_ C D M X W U Q _ F
_ _ _ _ _ _ _ _ _ I
_ L _ _ _ _ _ _ _ D
_ B C K Z E R S V G
_ L I M A E G F H X

### Step 2: Gather the password by flattening remaining characters

## In this example the password is: PARIWEIHEDRCBCKJBRRDSROPCDMXWUQFILDBCKZERSVGLIMAEGFHX

IMPORTANT! - Some tools for opening encrypted zip files show some issues in decrypting the zip containing the flag. Please don't trust the Windows Explorer unzip tool on Windows machine or unzip on Unix machine. Use instead other tools such as for example 7zip.

