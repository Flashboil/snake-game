# Overview

This program is a version of the classic Snake Game replicated in Python using PyGame. I made this program so that I could practice more with classes in Python and learn how to do things like get keyboard input from the user in real time to make a playable game.

To play the game, you use WASD or the arrow keys to change direction. The snake will constantly move forward. You collect "apples" by running into them. Each apple makes your snake longer. The game ends when you colide with the wall or yourself. You cannot double back from the direction you are facing (If you are going right, you cannot go left instantly).

[Software Demo Video](https://youtu.be/MZ-NQV5J0vU)

# Development Environment

This program was developed in Python using VS Code as the workspace.

The PyGame library is used as the engine to make and run the game.

# Useful Websites

* [Coolors.co](https://coolors.co/) Useful for generating alternate palettes
* [PyGame.org](https://www.pygame.org/docs/) PyGame documentation

# AI Usage Disclosure

ChatGPT was used to help with refreshing my knowledge on some things about Python class structuring. Additionally, I got help from AI for some debugging, partiuclarly with things related to rendering the game and getting the pygame clock timing right.
I referenced some palettes generated on coolors.co for the alternate palettes, but ultimately turned to ChatGPT to help make some quick 4 color palettes that would work well. I was careful to ask if they were sourced from a particular site; it said that if generated them itself using standard guidelines for good design and readability.

# Future Work
* SFX for apple pickup, perhaps music as well.
* Allow for easier restart with a menu.
* Allow for adjustable map size, apple counts, etc.