# There are a lot of ways you could keep track of which letters have been guessed
# A string or a list of strings will probably be helpful
guessed_letters = ""

def get_secret_word():
    """
    Return the word the player is going to have to guess. There are a variety of ways you might accomplish this.
    Some of these ways may include:
      * have a second player input a word
      * choose a random word from a list
      * use a dictionary API to get a random word (advanced skill, I can provide help if this is something you want to try)
    """

    return "You should probably be returning a more useful value"
    

def get_user_guess():
    """
    Return the player's guess. This is probably going to use input().
    I strongly encourage that you validate input here as well.
    """
    return "You should probably be returning a single letter"


def is_in_word(letter):
    """
    Return whether or not the specified letter is in the word. Should probably return a Boolean value.
    May or may not be necessary depending on how you write your code
    """
    pass


def show_current_word_status():
    """
    Display the current state of the word being guessed. It may be helpful to remember that
    you can loop through a string and do something for each letter in the string. For instance, 
    you might display either the same letter or an alternate character, depending on some condition 
    (such as whether or not you've already guessed that letter). You can even create a new string 
    in this way. I'd recommend it's also a good idea to return the current status of the word.
    """
    pass


def word_guessed():
    """
    Return whether or not the word has been fully guessed. There are a variety of ways to accomplish
    this. Some of those ways could include:
     * Assume that the word has been guessed. Loop through each letter in the string, and if any letter disproves that assumption, return False
     * Check to see if the current word status is the same as the secret word
    """
    pass
