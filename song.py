class Song:

    def __init__(self, title="", artist="", year=0, is_learned=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        return "{},{},{},{}".format(self.title, self.artist, self.year, self.check_learned())

    def __repr__(self):
        return str(self)

    """
    The purpose of the two functions below is to change the default string values of "l" and "u "from songs.csv 
    into "learned" and "unlearned". This is just for the preference, not a requirement of the assignment
    """

    def str_learn_to_bool(self):
        """
        This class will change the string values of is_learned variable into boolean data type
        """
        if self.is_learned == 'l':
            self.is_learned = True
            return self.is_learned
        elif self.is_learned == 'u':
            self.is_learned = False
            return self.is_learned

    def check_learned(self):
        """This will return the string values upon the boolean statement of is_learned from above function
        """
        self.str_learn_to_bool()
        if not self.is_learned:
            return "Unlearned"
        if self.is_learned:
            return "Learned"

    pass
