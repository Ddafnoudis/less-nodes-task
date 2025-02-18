"""
A script that generates a text file with nodes and edges
(graph.txt)
"""
import os
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
        # Write the rows
        f.write("1 2\n")
        f.write("1 3\n")
        f.write("2 4\n")
        f.write("3 5\n")

    # Read and define the data
    data = pd.read_csv("data_folder/graph.txt", sep=" ")

    # Return data to main
    return data


if __name__=="__main__":
    generate_data()
