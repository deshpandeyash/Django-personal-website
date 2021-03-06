import numpy as np
from .simparam import SimParam
from .simstate import SimState
from .simresult import SimResult
from .slot import TreeSlot
from .treestate import TreeState
from .branchnode import BranchNode
from . import packetlist


class Simulation(object):
    """
    This Holds the entire Simulation object, whose parameters we update according to the outcomes
    """

    def __init__(self, setting):
        # Load simulation parameters
        self.sim_param = SimParam(setting)
        # Load the simulation state parameters
        self.sim_state = SimState()
        # Load the result parameters
        self.sim_result = SimResult()
        # Load the class which perfomrs all the methods governing a simple slot
        self.slot = TreeSlot()
        # Load the branch node which keeps track of a tree
        self.branch_node = BranchNode()
        # Create an array of integers of which will contain all active nodes.
        self.active_array = []
        # For gated access, the arrived packets are put into a queue
        self.queue_array = []
        # The number of packets generated in a single slot
        self.packets_gen = 0
        # THe result of a slot
        self.result = 0
        # The current slot no
        self.slot_no = 0
        # Load the parameters for single tree resolution
        self.tree_state = TreeState(self)

    def reset(self, setting):
        self.sim_param = SimParam(setting)
        self.sim_state = SimState()
        self.sim_result = SimResult()
        self.slot = TreeSlot()
        self.active_array = []
        self.queue_array = []
        self.packets_gen = 0
        self.result = 0
        self.slot_no = 0
        self.tree_state = TreeState(self)
        self.branch_node.reset()

    def do_simulation_simple_tree_static(self, collided_packets):
        """
        Static Simulation, when the number of in initial collided packets is given, it is essentially a single tree res
        :param collided_packets: the no of packets in the resolution

        """
        # Load active array with the collided packets
        if collided_packets > self.sim_param.K:
            self.packets_gen = collided_packets
            packetlist.add_packets_to_tree(self)
            self.tree_state.reset(self)
            # Run the simulation as long as all packets are processed and tree is over
            while self.tree_state.gate_open:
                # Increment the slot
                self.slot_no += 1
                # Simulate the processes that would happen in the tx and rx in one slot, update the active array
                self.slot.oneslotprocess(self)
                # Update the simstate metrics according to the result of the simulation
                self.tree_state.update_metrics(self)
                # check if all the packets are processed and the tree is at its last branch
                if len(self.active_array) == 0 and len(self.branch_node.branch_status) == 0:
                    self.tree_state.gate_open = False
            # update the metrics from a tree to the simulation state
            self.sim_state.update_metrics(self)
            # Update the results
            self.sim_result.get_result(self)
        else:
            self.sim_result.throughput = 0
            self.sim_result.magic_throughput = 0
