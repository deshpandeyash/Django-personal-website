from . import graphdisplay
from .simulation import Simulation
import os

def simulate_tree_branching(setting):
    """
    To get the vizualization of 1 tree for the given settings and number of users as defined by simsettings and simparam
    also prints the obtained throughput, tree progression, result progression and tree depth
    """
    os.environ["PATH"] += os.pathsep + r'C:\Users\deshp\OneDrive\Desktop\MasterThesis\yash_master_thesis\graphviz-2.44.1-win32\Graphviz\bin'
    if setting is None:
        setting = create_default_setting()
    sim = Simulation(setting)

    sim.do_simulation_simple_tree_static(sim.sim_param.users)
    # print("Results were: ")
    # print(sim.tree_state.result_array)
    # print("Tree Progression was: ")
    # print(sim.branch_node.branch_array[:-1])
    # print("Throughput is = " + str(sim.sim_result.throughput / sim.sim_param.K))
    # print("The Depth of the tree is: " + str(sim.sim_result.mean_tree_depth))
    norm_tpt = round((sim.sim_result.throughput / sim.sim_param.K), 3)
    dot = graphdisplay.displaygraph(sim)

    return norm_tpt, dot

def create_default_setting():
    settings = {'SPLIT': 2, 'Biased_Split': True, 'Branch_Prob': 0.5, 'K': 1, 'Modified': False, 'Unisplit': False,
                'SIC': False, 'Users': 10}

    return settings


