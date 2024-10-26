### Assignment: Build a Hangman Game in Python

#### Objective:
Create a Python-based command-line version of the classic Hangman game. The player will guess a word based on its definition, and the game will provide visual feedback after each guess. The goal is to guess the word before the player runs out of attempts.

#### Requirements:
1. **Word List:**
   - The program will load a list of words and their definitions from a `words.json` file (found in this folder).
   
2. **Gameplay:**
   - At the start of the game, the program will randomly select a word from the `words.json` file and display its definition to the user.
   - The player has as many attempts as there are letters in the word.
   - For each guess:
     - If the guessed letter is in the word, all occurrences of that letter will be revealed in the word.
     - If the guessed letter is not in the word, it will be recorded as a wrong guess.
   - The game will display:
     - A first line with the correctly guessed letters in the word, separated by spaces.
     - A second line that displays an underline (`‾`) for each letter in the word (to visually represent the letters as "blanks").
     - A third line that shows all the wrong guesses the player has made so far.
   
3. **End of Game:**
   - The game ends when the player either guesses the word correctly or runs out of attempts.
   - If the player guesses the word, the program will display a congratulatory message.
   - If the player fails to guess the word, the correct word will be displayed.

#### Input File Format:
The `words.json` file should be in the following format:
```json
{
  "python": "A high-level programming language used for general-purpose programming.",
  "algorithm": "A process or set of rules to be followed in problem-solving or calculation operations.",
  ...
}
```

#### Example of Gameplay:
```
> python hangman.py

Definition: A high-level programming language used for general-purpose programming.


‾ ‾ ‾ ‾ ‾ ‾

Enter a letter: p
P
‾ ‾ ‾ ‾ ‾ ‾

Enter a letter: o
P       O
‾ ‾ ‾ ‾ ‾ ‾

Enter a letter: v
P       O
‾ ‾ ‾ ‾ ‾ ‾
V
Enter a letter: h
P     H O
‾ ‾ ‾ ‾ ‾ ‾
V
Enter a letter: y
P Y   H O
‾ ‾ ‾ ‾ ‾ ‾
V
Enter a letter: n
P Y   H O N
‾ ‾ ‾ ‾ ‾ ‾
V
Enter a letter: t
P Y T H O N
‾ ‾ ‾ ‾ ‾ ‾
V
Congratulations! You guessed the word 'PYTHON'.

Do you want to play again? (y/n):
```

#### Additional Requirements:
- The player should only be allowed to enter single letters (both uppercase and lowercase are accepted). If the player enters something invalid (e.g., more than one letter or a non-alphabet character), prompt them to try again.
- The program should not allow duplicate guesses and should prompt the player if they try to guess the same letter multiple times.
- The program should be case-insensitive (i.e., treat 'A' and 'a' as the same letter).
- Assume all answers are single words only, with no spaces or other special characters

#### Submission:
- Please add your script to the folder HW5-Hangman to your homework repo.
