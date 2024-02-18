
class Tutee:
    """
    inputs: array of necessary inputs for the Tutee object
    inputs[0] = str name
    inputs[1], inputs[2] = email and phone number, strings
    inputs[3] = dict scored subjects, subj:score
    inputs[4] = List times when available
    inputs[5] = int virtual (0) vs in-person (1) preference
    inputs[6] = str misc info/whether requires extra help, learning challenges
    """
    def __init__(self, inputs):
        self.name = inputs[0]
        self.contact = (inputs[1], inputs[2])
        scored_subjects = inputs[3]
        self.subjvector = []
        for ss in scored_subjects.keys():
            self.subjvector.append(scored_subjects[ss])
        self.available = inputs[4]
        self.pref = inputs[5]
        self.extra_help = inputs[6]

def makeTutee(inputs):

    if len(inputs) == 7:
        return Tutee(inputs)
    else:
        return None
    
def makeTutees(inputs_arr):

    lstTuts = []
    for il in inputs_arr:
        lstTuts.append(makeTutee(il))
    return lstTuts