from Rabbit import Rabbit
from Veggie import Veggie
from Captain import Captain
from Snake import Snake
import os
import random
import pickle


# Class Game Engine!
class GameEngine:
    # Define Private Constant Variables
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    # Create a new instance and set all required variables to private
    def __init__(self):
        self.__field = []
        self.__rabbits = []
        self.__captain = None
        self.__possibleVeggies = []
        self.__score = 0

        # Bonus
        self.__snake = None

    def initVeggies(self):
        """
        initVeggies() prompts the uer for configuration file in the format of .csv,
        parse the data in the file, for field size and vegetables. Randomly distributes
        the vegetables in the field.
        :return: None
        """

        # Prompt the user for input configuration file
        input_file = input("Please enter the name of the vegetable point file: ")
        # If the file does not exist, inform the user and prompt for new name.
        while os.path.exists(input_file) == 0:
            input_file = input(f"{input_file} does not exist! Please enter the name of the vegetable point file:")

        # Open the .csv file in read mode
        with open(input_file, "r") as file:

            # Read the lines in the file
            lines = file.readlines()

            # Split a comma separated string in the first row and store it in a list
            field_data = lines[0].strip().split(",")

            # Last element of the list is the height of the field
            height = int(field_data[-2])
            # Second last element of the list is the width of the field. It was observed that in the output file,
            # The width of the field is 3 times the corresponding input value
            width = int(field_data[-1]) * 3

            # Generate a 2d list and store it in the private member '__field' with all elements as none
            for i in range(height):
                row = []
                for j in range(width):
                    row.append(None)
                self.__field.append(row)

            # for loop to parse row 2 till the end of file. 'Row 1 index is 0'
            for line in lines[1:]:
                # split the comma separated string and convert it into a list
                veggie_info = line.strip().split(",")

                # Extract data from the generated list
                name = veggie_info[0]
                symbol = veggie_info[1]
                points = int(veggie_info[2])

                # Create an instance of class Veggie
                veggie = Veggie(name, symbol, points)

                # Append this new instance to the private member __possibleVeggies
                self.__possibleVeggies.append(veggie)

            # Close the file after reading
            file.close()

            # Randomly Distribute vegetables in the field
            for i in range(self.__NUMBEROFVEGGIES):

                # Choose a random veggie from the list __possibleVeggies
                veggie = random.choice(self.__possibleVeggies)

                # Generate random x and y coordinate within the field
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)

                # If the generated coordinates are occupied, Regenerate new coordinates
                while self.__field[y][x] != None:
                    x, y = random.randint(0, width - 1), random.randint(0, height - 1)

                # Place a randomly selected vegetable in a random unoccupied spot in the field area
                self.__field[y][x] = veggie

    def initCaptain(self):
        """
        initCaptain() Randomly selects a point in the field that is not occupied and assigns captain at that point
        :return: none
        """

        # Generate a random x and y coordinates
        x, y = random.randint(0, len(self.__field[0]) - 1), random.randint(0, len(self.__field) - 1)

        # Check if the location is empty, if not generate a new random spot.
        while self.__field[y][x] != None:
            x, y = random.randint(0, len(self.__field[0]) - 1), random.randint(0, len(self.__field) - 1)

        # Create an instance of captain and assign it to the private member captain
        self.__captain = Captain(x, y)
        self.__field[y][x] = self.__captain

    def initRabbits(self):
        """
        initRabbits() generates number of specified rabbits in a random empty location
        :return: none
        """
        # for loop for generating multiple rabbits
        for j in range(self.__NUMBEROFRABBITS):
            # Generate a random xy coordinates for rabbit.
            x, y = random.randint(0, len(self.__field[0]) - 1), random.randint(0, len(self.__field) - 1)

            # Check if the generated coordinates are empty, if not generate new random coordiantes
            while self.__field[y][x] != None:
                x, y = random.randint(0, len(self.__field[0]) - 1), random.randint(0, len(self.__field) - 1)

            # generate a new instance of rabbit with empty coordinates and add them to the private member rabbits
            rabbit = Rabbit(x, y)
            self.__rabbits.append(rabbit)
            self.__field[y][x] = rabbit

    def initializeGame(self):
        """
        initializeGame() initialises the game, calls initVeggies(), initCaptain(), initRabbits()
        :return: none
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        self.initSnake()

    def remainingVeggies(self):
        """
        remainingVeggies() counts the number of veggies in the field
        :return: none
        """
        # initialise a count variable
        count = 0

        # Check every element of the field, if it is an instance of class Veggie, increment the count
        for row in self.__field:
            for fieldObject in row:
                if isinstance(fieldObject, Veggie):
                    count += 1
        return count

    def intro(self):
        """
        intro() prints custom messages to welcome the user and inform them the rules. prints the list of veggies
        present with points and symbols for captain and rabbits
        :return: none
        """

        # Print custom messages to welcome the player and inform them the rules
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest")
        print("as many vegetables as possible before the rabbits eat them")
        print("all! Each vegetable is worth a different number of points")
        print("so go for the high score!")

        # Print all the vegetables present in the field
        print("\nThe vegetables are:")
        for veggie in self.__possibleVeggies:
            print(veggie)

        # Print Captain and rabbit symbols
        print(
            f"\nCaptain Veggie is {self.__captain.getSymbol()}, and the rabbits are {self.__rabbits[0].getSymbol()}'s")
        print("Snake Symbol:", self.__snake.getSymbol())
        print("\nGood luck!")

    def printField(self):
        """
        printFiled() prints the field with vegetables, Captain, Rabbits and Snake
        :return: none
        """

        # Print the top # border
        for i in range(len(self.__field[0]) + 2):
            print("#", end="")
        print()

        # Print the field with field objects and # at the start and end
        for row in self.__field:
            print("#", end="")
            for fieldObject in row:
                if fieldObject is None:
                    print(" ", end="")
                else:
                    print(fieldObject.getSymbol(), end="")
            print("#")

        # Print the bottom # border
        for i in range(len(self.__field[0]) + 2):
            print("#", end="")
        print()

    def getScore(self):
        """
        getScore() returns the score, sum of all the vegetables collected by the player
        :return: none
        """
        return self.__score

    def moveRabbits(self):
        """
        moveRabbits() moves the rabbits one space, either up down left right or diagonal or does not move_rabbit at all.
        :return: none
        """
        for rabbit in self.__rabbits:
            # Get the rabbit's current position
            x = rabbit.getX()
            y = rabbit.getY()

            # randomly choose a move_rabbit
            move_rabbit = random.randint(1, 9)

            # Move the rabbit in the randomly chosen move_rabbit

            # Case 1, if randomly chosen movement is UP
            if move_rabbit == 1:
                new_y = y - 1
                # Check if new_y >= 0, ensures that new_y is in bounds of the field
                if new_y >= 0:
                    # allow the rabbit to move_rabbit in an empty space or on a vegetable
                    if self.__field[new_y][x] is None or isinstance(self.__field[new_y][x], Veggie):
                        rabbit.setY(new_y)  # Set new y for rabbit
                        self.__field[y][x] = None  # set the previous location to none
                        self.__field[new_y][x] = rabbit  # Update rabbit position

            # Case 2, if randomly chosen movement is DOWN
            elif move_rabbit == 2:
                new_y = y + 1
                # Check if new_y is within the field.
                if new_y < len(self.__field):
                    # allow the rabbit to move_rabbit in an empty space or on a vegetable
                    if self.__field[new_y][x] is None or isinstance(self.__field[new_y][x], Veggie):
                        rabbit.setY(new_y)  # Set new y for rabbit
                        self.__field[y][x] = None  # set the previous location to none
                        self.__field[new_y][x] = rabbit  # Update rabbit position

            # Case 3, if randomly chosen movement is LEFT
            elif move_rabbit == 3:
                new_x = x - 1
                # Check if new_x is within the field.
                if new_x >= 0:
                    # allow the rabbit to move_rabbit in an empty space or on a vegetable
                    if self.__field[y][new_x] is None or isinstance(self.__field[y][new_x], Veggie):
                        rabbit.setX(new_x)  # Set new x for rabbit
                        self.__field[y][x] = None  # set the previous location to none
                        self.__field[y][new_x] = rabbit  # Update rabbit position

            # Case 4, if randomly chosen movement is RIGHT
            elif move_rabbit == 4:
                new_x = x + 1
                # Check if new_x is within the field.
                if new_x < len(self.__field[0]):
                    # allow the rabbit to move_rabbit in an empty space or on a vegetable
                    if self.__field[y][new_x] is None or isinstance(self.__field[y][new_x], Veggie):
                        rabbit.setX(new_x)  # Set new x for rabbit
                        self.__field[y][x] = None  # set the previous location to none
                        self.__field[y][new_x] = rabbit  # Update rabbit position

            # Case 5, if randomly chosen movement is UP_LEFT
            elif move_rabbit == 5:
                new_x = x - 1
                new_y = y - 1
                # Check if new position is within the field.
                if new_x >= 0 and new_y >= 0:
                    # allow the rabbit to move_rabbit in an empty space or on a vegetable
                    if self.__field[new_y][new_x] is None or isinstance(self.__field[new_y][new_x], Veggie):
                        rabbit.setX(new_x)  # Set new x for rabbit
                        rabbit.setY(new_y)  # Set new y for rabbit
                        self.__field[y][x] = None  # set the previous location to none
                        self.__field[new_y][new_x] = rabbit  # Update rabbit position

            # Case 6, if randomly chosen movement is UP_RIGHT
            elif move_rabbit == 6:
                new_x = x + 1
                new_y = y - 1
                # Check if new position is within the field.
                if new_x < len(self.__field[0]) and new_y >= 0:
                    # allow the rabbit to move_rabbit in an empty space or on a vegetable
                    if self.__field[new_y][new_x] is None or isinstance(self.__field[new_y][new_x], Veggie):
                        rabbit.setX(new_x)  # Set new x for rabbit
                        rabbit.setY(new_y)  # Set new y for rabbit
                        self.__field[y][x] = None  # set the previous location to none
                        self.__field[new_y][new_x] = rabbit  # Update rabbit position

            # Case 7, if randomly chosen movement is DOWN_LEFT
            elif move_rabbit == 7:
                new_x = x - 1
                new_y = y + 1
                # Check if new position is within the field.
                if new_x >= 0 and new_y < len(self.__field):
                    # allow the rabbit to move_rabbit in an empty space or on a vegetable
                    if self.__field[new_y][new_x] is None or isinstance(self.__field[new_y][new_x], Veggie):
                        rabbit.setX(new_x)  # Set new x for rabbit
                        rabbit.setY(new_y)  # Set new y for rabbit
                        self.__field[y][x] = None  # set the previous location to none
                        self.__field[new_y][new_x] = rabbit  # Update rabbit position

            # Case 8, if randomly chosen movement is DOWN_RIGHT
            elif move_rabbit == 8:
                new_x = x + 1
                new_y = y + 1
                # Check if new position is within the field.
                if new_x < len(self.__field[0]) and new_y < len(self.__field):
                    # allow the rabbit to move_rabbit in an empty space or on a vegetable
                    if self.__field[new_y][new_x] is None or isinstance(self.__field[new_y][new_x], Veggie):
                        rabbit.setX(new_x)  # Set new x for rabbit
                        rabbit.setY(new_y)  # Set new y for rabbit
                        self.__field[y][x] = None  # set the previous location to none
                        self.__field[new_y][new_x] = rabbit  # Update rabbit position

                # Case 9, if randomly chosen movement is NONE
                elif move_rabbit == 9:
                    new_x = x
                    new_y = y
                    # Do nothing

    def moveCptVertical(self, movement):
        """
        moveCptVertical() takes in a movement integer and moves the captain in vertical direction.
        collects the veggies if captain steps on them, prints appropriate message if captain steps on bunnies
        :param movement: Int
        :return: none
        """
        new_y = self.__captain.getY() + movement
        # Check if the captain can move vertically and the space is empty
        if 0 <= new_y < len(self.__field) and self.__field[new_y][self.__captain.getX()] is None:
            # Update captain position
            self.__captain.setY(new_y)
            self.__field[self.__captain.getY()][self.__captain.getX()] = self.__captain
            # set previous coordinates to none
            self.__field[self.__captain.getY() - movement][self.__captain.getX()] = None

        # Check if the captain can move vertically and the space is occupied with vegetable
        elif 0 <= new_y < len(self.__field) and isinstance(self.__field[new_y][self.__captain.getX()], Veggie):
            # Collect the vegetable
            veggie = self.__field[new_y][self.__captain.getX()]
            # print customised message
            print(f"Yummy! A delicious {veggie.getName()}")
            # append the collected veggie
            self.__captain.addVeggie(veggie)
            # add the points of the veggie to score
            self.__score += veggie.getPoints()
            # Update the object's location
            self.__field[new_y][self.__captain.getX()] = None
            self.__field[self.__captain.getY()][self.__captain.getX()] = self.__captain
            self.__field[self.__captain.getY() - movement][self.__captain.getX()] = None

        elif 0 <= new_y < len(self.__field) and isinstance(self.__field[new_y][self.__captain.getX()], Rabbit):
            # if the space is occupied with rabbit
            print("Don't step on the bunnies!")

        else:
            # if captain tries to move out of bounds
            print("You can't move that way!")

    def moveCptHorizontal(self, movement):
        """
        moveCptHorizontal() takes in a movement integer and moves the captain in horizontal direction.
        collects the veggies if captain steps on them, prints appropriate message if captain steps on bunnies
        :param movement: int
        :return: none
        """
        new_x = self.__captain.getX() + movement
        # Check if the captain can move horizontally and the space is empty
        if 0 <= new_x < len(self.__field[0]) and self.__field[self.__captain.getY()][new_x] is None:
            # Update captain position
            self.__captain.setX(new_x)
            self.__field[self.__captain.getY()][self.__captain.getX()] = self.__captain
            # set previous coordinates to none
            self.__field[self.__captain.getY()][self.__captain.getX() - movement] = None

        # Check if the captain can move horizontally and the space is occupied with vegetable
        elif 0 <= new_x < len(self.__field[0]) and isinstance(self.__field[self.__captain.getY()][new_x], Veggie):
            # Collect the vegetable
            veggie = self.__field[self.__captain.getY()][new_x]
            # print customised message
            print(f"Yummy! A delicious {veggie.getName()}")
            # append the collected veggie
            self.__captain.addVeggie(veggie)
            # add the points of the veggie to score
            self.__score += veggie.getPoints()
            # Update the object's location
            self.__field[self.__captain.getY()][new_x] = None
            self.__field[self.__captain.getY()][self.__captain.getX()] = self.__captain
            self.__field[self.__captain.getY()][self.__captain.getX() - movement] = None

        elif 0 <= new_x < len(self.__field[0]) and isinstance(self.__field[self.__captain.getY()][new_x], Rabbit):
            # if the space is occupied with rabbit
            print("Don't step on the bunnies!")

        else:
            # if captain tries to move out of bounds
            print("You can't move that way!")

    def moveCaptain(self):
        """
        moveCaptain() takes directional input from the user and moves the captain in the user specified direction by one
        block
        :return: none
        """
        captain_movement = input("Would you like to move up(W), down(S), left(A), or right(D):")

        if captain_movement == "w":
            self.moveCptVertical(-1)
        elif captain_movement == "s":
            self.moveCptVertical(1)
        elif captain_movement == "a":
            self.moveCptHorizontal(-1)
        elif captain_movement == "d":
            self.moveCptHorizontal(1)
        else:
            print(f"{captain_movement}is not a valid option")

    def gameOver(self):
        """
        gameOver() notifies the player that the game is over, prints all the collected vegetables
        Prints the score of the player.
        :return: none
        """
        print("GAME OVER!")

        # Print out the vegetables the __captain harvested
        veggies_harvested = self.__captain.getVeggies()
        if veggies_harvested:
            print("You managed to harvest the following vegetables:")
            for veggie in veggies_harvested:
                print(veggie.getName())
        else:
            print("No vegetables harvested.")

        # Print out the player's __score
        print("Your score was:", self.__score)

    def highScore(self):
        """
        highScore() prompts the user for their first 3 initials, adds the initials and score to a file
        in descending order
        :return:
        """
        high_scores = []

        # Check if the highscore.data file exists
        if os.path.exists(self.__HIGHSCOREFILE):
            with open(self.__HIGHSCOREFILE, "rb") as file:
                high_scores = pickle.load(file)

        # Prompt the user for their initials
        initials = input("Please enter your three initials to go on the scoreboard: ")
        initials = initials.upper()[:3]

        # Add the player's __score to the high scores list
        high_scores.append((initials, self.__score))

        # Sort the high scores list in descending order
        high_scores.sort(reverse=True)

        # Display the high scores
        print("\nHIGH SCORES:")
        print("Name     Score")
        for initials, score in high_scores:
            print(f"{initials}           {score}")

        # Save the high scores to the file
        with open(self.__HIGHSCOREFILE, "wb") as file:
            pickle.dump(high_scores, file)

