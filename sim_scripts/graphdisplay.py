from graphviz import Digraph
import os
import base64


def displaygraph(sim):
    real_tree_branch = sim.branch_node.branch_array[:-1]
    branch_array = sim.branch_node.ghost_array[:-1]
    result_array = sim.tree_state.ST_result_array
    number_array = sim.tree_state.ST_number_in_slot
    cot = Digraph(comment="Simple Tree", format='svg')
    cot.attr(compound='true')
    cot.node('Start', label=str(number_array[0]), shape='doublecircle', xlabel=str(result_array[0]))
    # Create All Nodes
    for i in range(len(branch_array)):
        current_node = branch_array[i]
        current_result = str(result_array[i + 1])
        if current_node not in real_tree_branch:
            cot.node(current_node, label=str(number_array[i + 1]), xlabel=current_result, fillcolor='red',
                     style='filled')
        else:
            cot.node(current_node, label=str(number_array[i + 1]), xlabel=current_result)
        if len(current_node) == 0:
            print("Graphviz Error")
        elif len(current_node) == 1:
            cot.edge('Start', current_node, label=current_node)
    for i in range(len(branch_array)):
        for j in range(i + 1, len(branch_array)):
            fixed_node = branch_array[i]
            variable_node = branch_array[j]
            if variable_node[:-1] == fixed_node:
                cot.edge(fixed_node, variable_node, variable_node)
    cot.edge_attr.update(fontcolor='green')
    file_name = 'The_file'
    cot.render(file_name)
    image_base_64 = image_as_base64(F"{file_name}.svg")
    os.remove(F"{file_name}.svg")
    os.remove(file_name)
    return image_base_64


def image_as_base64(image_file, format='svg+xml'):
    """
    :param `image_file` for the complete path of image.
    :param `format` is format for image, eg: `png` or `jpg`.
    """
    if not os.path.isfile(image_file):
        return None

    encoded_string = ''
    with open(image_file, 'rb') as img_f:
        encoded_string = base64.b64encode(img_f.read()).decode('utf-8')
    return F"data:image/{format};utf-8;base64,{encoded_string}"
