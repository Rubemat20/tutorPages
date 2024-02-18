
class Tutor:
    """
    inputs: array of necessary inputs for the Tutor object
    inputs[0] = str name
    inputs[1] = str year
    inputs[2], inputs[3] = email and phone number, strings
    inputs[4] = dict scored subjects, subj:score
    inputs[5] = List times when available
    inputs[6] = int virtual (0) vs in-person (1) preference
    """
    def __init__(self, inputs):
        self.name = inputs[0]
        self.year = int(inputs[1])
        self.contact = (inputs[2], inputs[3])
        scored_subjects = inputs[4]
        self.subjvector = []
        for ss in scored_subjects.keys():
            self.subjvector.append(scored_subjects[ss])
        self.available = inputs[5]
        self.pref = inputs[6]
    
def makeTutor(inputs):

    if len(inputs) == 7:
        return Tutor(inputs)
    else:
        return None
    
def makeTutors(inputs_arr):

    lstTuts = []
    for il in inputs_arr:
        lstTuts.append(makeTutor(il))
    return lstTuts

