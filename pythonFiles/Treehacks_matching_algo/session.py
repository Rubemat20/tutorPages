from tutors import *
from tutees import *

class Session:
    """
    """

    def __init__(self, tutor: Tutor, tutee: Tutee, day):
        self.day = day
        self.tutor = tutor
        self.tutee = tutee
        self.format = tutee.pref # prioritize tutee preference
