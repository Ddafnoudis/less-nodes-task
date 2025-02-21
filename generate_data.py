"""
A script that generates a text file with nodes and edges
(graph.txt)
"""
import os
import random
import pandas as pd
from pandas import DataFrame



# Generate a text file that contains the nodes and edges form 1 to 5
def generate_data(folder_name)-> DataFrame:
    """
    Generate DataFrame
    """
    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    with open("data_folder/graph.txt", "w") as f:
        # Columns
        f.write("node1 node2\n")
        # Write 4 rows with random.randint nodes from 1 to 5 without one number in on one row
        for node in range(4):
            if node != node:
                continue
            else:
                f.write(f"{random.randint(1, 5)} {random.randint(1, 5)}\n")

    # Read and define the data
    data = pd.read_csv("data_folder/graph.txt", sep=" ")

    # Return data to main
    return data


if __name__=="__main__":
    generate_data()
