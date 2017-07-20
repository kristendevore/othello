# othello
#This is the specification we were given, explains how python files behaves when the UI runs. 

This project asks you to implement the game logic of Othello, along with a console-mode program with a very spartan user interface that you'll use to test it — and that we'll use to automatically test it, making it crucial that you get the format of the program's input and output right according to the specification below. Spacing, capitalization, and other seemingly-minor details are critical.

Using your test program, you'll be capable of playing a single game of Othello on a single computer. There are a handful of options that allow you to specify, before the game begins, how the game will be played. The program begins by reading input that selects these options; the game is then played by requiring input directly into the console that specifies a player's next move, continuing until the game is complete, at which point the program ends.

When you're finished, you'll have the game logic that will form the basis of your completed version of Othello in the next project.

A detailed look at how your program should behave

Your program will take its input via the console, printing no prompts to a user. The intent here is not to write a user-friendly user interface; what you're actually doing is building a tool for testing your game logic, which we'll then be using to automatically test your game logic. So it is vital that your program reads inputs and writes outputs precisely as specified below. You can freely assume that the input will match the specification described; we will not be testing your program on any inputs that don't match the specification.

Your program begins by printing a line of output specifying which of the two sets of Othello rules are supported by your program, by printing either FULL or SIMPLE. (See the section titled Simplified Othello rules below for a description of the simplified set of rules, which you can implement for partial credit if you're unable to complete the full rules.)
Note that this is not a user option; this is something your program prints, before it does anything else, so we'll know (when we're grading it) how it should behave.
Your program then reads four lines of input, specifying the options that will be used to determine how the game will be played.
The first line specifies the number of rows on the board, which will be an even integer between 4 and 16 (inclusive).
The second line specifies the number of columns on the board, which will be an even integer between 4 and 16 (inclusive) and does not have to be the same as the number of rows.
The third line specifies which of the players will move first: B for black, W for white.
The fourth line selects how the game is won: > means that the player with the most discs on the board at the end of the game wins, < means the player with the fewest.
Next, your program will read the initial contents of the board. To make it simpler to test a variety of scenarios, your game will need to support any initial arrangement of discs, so it will be necessary to read the entire contents of the board from the input. It will be appear in the input in this form:
Each row will occupy a single line of input, with one space separating the cells in that row. Each cell will be specified as either B (if a black disc is in that cell), W (if a white disc is in that cell), or . (if the cell is empty).
The number of rows and columns described in this way will match the number of rows and columns specified in the first two lines of the input.
For example, if there are 8 rows and 8 columns on the board, the initial contents of the board might appear in the input this way:
. . . . . . . .
. . . . . . . .
. . . . . . . .
. B W B W . . .
. . . W B . . .
. . . . B W . .
. . . . . B . .
. . . . . . . .
After the initial arrangement of the board is specified in the input, the game begins, proceeding one move a time until it's complete.
Before each turn, the following information is printed to the console:
The character B, followed by a colon and a space, followed by the number of discs on the board that are black. This is followed by two spaces, the character W, a colon and a space, and the number of discs on the board that are white.
The contents of the board, with each row occupying one line of output, and one space separating each pair of cells. Each cell is written either as a B (if a black tile occupies that cell), a W (if a white tile occupies that cell), or a . (if no tile occupies that cell). For example:
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . B W . . .
. . . W B . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
The word TURN (in all-caps), followed by a colon and a space, followed by B if it's the black player's turn, W if it's white's turn.
After printing the information above, the program reads a line of input specifying the current player's move. The move is specified as two integers on a line, separated by a space. The first integer specifies the row number (with 1 being the top row, 2 being the row below that, and so on) and the second integer specifies the column number (with 1 being the leftmost column, 2 being the one to the right of that, and so on).
If the move is valid, print the word VALID alone on a line, apply that move (i.e., make the appropriate changes to the state of the game) and then continue the game..
If the move is invalid (see the rules if you're curious what makes a move invalid), print the word INVALID alone on a line and wait for the user to specify another move.
At the conclusion of the game (i.e., after the last move is made and there are no more legal moves on the board), the final state of the game is printed to the console, quite similarly to how it's printed before each turn:
The character B, followed by a colon and a space, followed by the number of discs on the board that are black. This is followed by two spaces, the character W, a colon and a space, and the number of discs on the board that are white.
The contents of the board, in the same format described above.
The word WINNER (in all-caps), followed by a colon and a space, followed by B if the black player has won, W if the white player has won, and NONE if no player has won (i.e., the final score is tied).
The program ends when the game is over.

