print "Let's play a Quiz!"

""" Fill in The Blanks Quiz.
Asks the player for difficulty level and number of guesses, and
displays the player chosen quiz. The quiz has numbered blanks,
asks the player for their answers for each until the quiz is
complete or they make the maximum number of guesses."""

player_level = raw_input("Type in your difficulty level of quiz(easy, medium, or hard):")

blank_space = ["____1____","____2____","____3____","____4____","____5____","____6____"]

#Prompt asking for the number of guesses the player wants.
print("How many guesses do you want?")
guesses = raw_input()
guesses = int(guesses) - 1


easy_quiz = """ Data Science, also known as ____1____, is an interdisciplinary field about scientific methods, processes,
and systems to extract ____2____ or insights from ____3____ in various forms, either structured or unstructured, similar to
____4____.The term "data science" has existed for over 30 years and was used initially as a substitute for ____5____ by ____6____ in 1960."""

medium_quiz = """ Python is a widely used ____1____ programming language for general-purpose programming, created by
____2____ and first released in 1991. An ____3____ language, Python has a design philosophy that emphasizes code
____4____ , and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages
such as ____5____ or ____6____."""

hard_quiz = """Friends_tv_show_quotes:
               (a)'The fridge broke, so I had to eat everything' by ____1____;
               (b)'I needed a new thing for today, and there's this leather store that always smells so good,
                   and I thought, 'Wow, I never really owned a good smelling pair of pants before.' by ____2____;
               (c)'And that's when it hit me- how much Barry looks like Mr. Potato Head.' by ____3____;
               (d)'Um, Rachel, you want to put the marshmallows in concentric circles.' by ____4____;
               (e)'It's a tradition, like the parade. If the parade decided it was gay, moved out, and abandoned its entire family.' by ____5____;
               (f)'Well, I started naming states, but then I got tired of it. So, I started naming different types
                   of celery. So far I only got one- regular celery.' by ____6____."""

easy_answers  = ["data-driven science","knowledge","data","data mining","computer science","Peter Naur"]
medium_answers = ["high-level","Guido Van Rossum","interpreted","readability","C++","Java"]
hard_answers =  ["Joey Tribbiani","Dr. Ross Geller","Rachel Green","Monica Geller","Phoebe Buffay","Chandler Bing"]

def choose_level(gameLevel):
    """The player chooses the difficulty level they want to play."""
    if gameLevel == "easy":
       return easy_quiz
    elif gameLevel == "medium":
       return medium_quiz
    elif gameLevel == "hard":
       return hard_quiz

def answers(answersFor):
    """The answers corresponding to the chosen quiz will display in
       the screen"""
    if choose_level(answersFor) == easy_quiz:
       return easy_answers
    elif choose_level(answersFor) == medium_quiz:
       return medium_answers
    elif choose_level(answersFor) == hard_quiz:
       return hard_answers

def check_answer(gamer_answer,correct_answers,answers_count):
    """The player answers have to be verified whether it is right
       or wrong."""
    if gamer_answer == correct_answers[answers_count]:
       print "Right answer!"
       return True
    else:
       print  "Wrong answer!"
       return False

def get_answers(game):
    """The corresponding answer key will display according to the
       quiz chosen by the player."""
    if game == easy_quiz:
       answers = easy_answers
       print "Hey!You selected an easy one."
    elif game == medium_quiz:
       answers = medium_answers
       print "Oh!You opted medium."
    elif game == hard_quiz:
       answers = hard_answers
       print "You selected hard."
    return answers

quiz = choose_level(player_level)
answers = get_answers(quiz)

spaceIndex = 0
answerIndex = 0
quizString = quiz

def start_quiz(spaceIndex,answerIndex,quizString):
    """Input:
            level selected by the user and the number of guesses.
    Behavior:
        For a given level it launches the main quiz logic.
        It checks the user input.
        If the user guesses right the current blanks is replaced
        with the right answer then the quiz is print.
        This process happens until all blanks are found
    Return:
        None.
    """

    while answerIndex < len(answers):

        player_answer = raw_input("answer for blank_space"+ blank_space[spaceIndex] + "?")
        answer = check_answer(player_answer,answers,answerIndex)
        count = 0

        if answer == False:

           while count < guesses:

               player_answer = raw_input("answer for blank_space"+ blank_space[spaceIndex] + "?")
               answer = check_answer(player_answer,answers,answerIndex)

               if answer == True: break
               if answer == False:
                 count += 1

           if count == guesses: break

        if answer == True:
           quizString = quizString.replace(blank_space[spaceIndex],answers[spaceIndex])
           print quizString

        answerIndex += 1
        spaceIndex += 1

print choose_level(player_level)
"""The chosen quiz will display on the screen"""

start_quiz(spaceIndex,answerIndex,quizString)

print ("Thank You for playing!!")
"""Ends the game buy thanking the player."""
