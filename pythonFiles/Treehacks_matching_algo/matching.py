from tutees import *
from tutors import *
from session import *
import math

def ndim_dist(v1, v2):
    """
    Applies distance formula to two n-dimensional vectors
    """
    res = 0
    for i in range(len(v1)):
        res += (v1[i] - v2[i])**2
    
    res = res ** 0.5
    return res

def time_overlap(tutor: Tutor, tutee: Tutee):
    """
    """
    tutor_times = set(tutor.available)
    tutee_times = set(tutee.available)
    overlaps = tutor_times.intersection(tutee_times)
    return list(overlaps)


def matching(tutorsinfo, tuteesinfo):
    """
    Highest level matching algorithm
    Outputs a dict - times corresponding to pairs of tutor and tutee objects
    """
    tutees = makeTutees(tuteesinfo)
    tutors = makeTutors(tutorsinfo) # we assume num tutees > num tutors

    res = {}
    for _ in range(len(tutees)):
        tutee = tutees.pop()
        curr_mindist = math.inf
        curr_tut = math.inf
        for i in range(len(tutors)):
            tutor = tutors[i]
            poss_times = time_overlap(tutor, tutee)
            if len(poss_times) == 0:
                continue
            else:
                check = ndim_dist(tutee.subjvector, tutor.subjvector)
                if curr_mindist > check:
                    curr_mindist = check
                    curr_tut = i
        if poss_times[0] not in res.keys():
            res[poss_times[0]] = [(tutee, tutors[curr_tut])]
        else:
            res[poss_times[0]].append((tutee, tutors[curr_tut]))
        del tutors[curr_tut]
    
    assert len(tutees) == 0

    return res

def info_queury(tutorsinfo, tuteesinfo, day):
    """
    Names and contact info instantly sorted by day
    """
    d = matching(tutorsinfo, tuteesinfo)
    pair_names = []
    all_contactinfo = []
    for tup in d[day]:
        tutee, tutor = tup
        pair_names.append(tutee.name, tutor.name)
        all_contactinfo.append(tutee.contact)
        all_contactinfo.append(tutor.contact)

def make_sessions(matchings):
    """
    """
    sesh_lst = []
    for day, lst_tups in matchings.items():
        for tup in lst_tups:
            sesh_lst.append(Session(tup[1], tup[0], day))

    return sesh_lst