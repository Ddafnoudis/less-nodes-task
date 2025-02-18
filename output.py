"""
A script that gives the output file: nodes-to-remove.txt
"""
from typing import Dict


def save_output_file(min_nodes: Dict[int, int])-> str:
    """
    Output file
    """
    # Open the file
    with open("data_folder/nodes-to-remove.txt", "w") as file:
        # Write
        file.write(f"Nodes removed: {str(min_nodes)}")

    
if __name__=="__main__":
    save_output_file()
