import numpy as np


class SimParam(object):
    """
    Contains all important simulation parameters
    """

    def __init__(self, setting):
        """
        Setting is a dict with all the parameters :
        SPLIT : Int
        Users: Collided Users
        Branch_Prob : Prob to select the next slot
        KMPR = The NOMA parameter

        Biased_Split: Whether Fair Splitting is to be employed
        Modified : Whether Modified Tree
        Unisplit : Whether Optimim static splt
        SIC : Whether SIC

        """
        self.SPLIT = setting['SPLIT']
        self.biased_split = setting['Biased_Split']
        if self.biased_split:
            # set branching probability for binary split
            self.branchprob = setting['Branch_Prob']
        else:
            self.branchprob = 1 / self.SPLIT
        # Set branching probability for a split
        self.branch_biased = np.full(self.SPLIT, (1 - self.branchprob) / (self.SPLIT - 1))
        self.branch_biased[0] = self.branchprob

        # The number of packets that can be resolved in a multipacekt reception system in one slot.
        self.K = setting['K']

        # The type of Resolution Algorithm
        self.modified = setting['Modified']
        self.unisplit = setting['Unisplit']
        self.sic = setting['SIC']

        # Number of collided users
        self.users = setting['Users']

