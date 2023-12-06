from GameEngine import GameEngine


def main():
    """
    main() initialises the game and keeps a track of vegetables present in the field,
    Takes appropriate actions as the game is running and once its over.
    :return:
    """
    # Instantiate and store a GameEngine object as captain_veggie
    captain_veggie = GameEngine()

    # Initialize the game using .initializeGame()
    captain_veggie.initializeGame()

    # Display the game's introduction using .intro()
    captain_veggie.intro()

    # Calculate the number of remaining vegetables using .remainingVeggies()
    remaining_veggies = captain_veggie.remainingVeggies()

    # Play the game as long as there are veggies in the field
    while remaining_veggies > 0:
        # Print the number of remaining veggies and the score
        print(f"{remaining_veggies} veggies remaining. Current score: {captain_veggie.getScore()}")

        # Print out the field using .printField()
        captain_veggie.printField()

        # Move the rabbits using .moveRabbits()
        captain_veggie.moveRabbits()

        # Move the captain using .moveCaptain()
        captain_veggie.moveCaptain()

        # Move the snake using .moveSnake()
        captain_veggie.moveSnake()

        # Evaluate the number of veggies left
        remaining_veggies = captain_veggie.remainingVeggies()

    # Once the game is over, display the GAME OVER information using .gameOver()
    captain_veggie.gameOver()

    # Call the .highScore() to handle highscore functionality
    captain_veggie.highScore()


# Call main() to start the game
main()
