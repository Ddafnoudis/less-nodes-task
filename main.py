"""
Main script for the application.
"""
from algorithm import remove_edges
from output import save_output_file
from generate_data import generate_data

# Define the folder name
FOLDER_NAME= "data_folder"


def main(folder_name = FOLDER_NAME):
    # Define the data
    data = generate_data(folder_name)
    # Print the data
    print(f"Data:\n {data}\n")

    # Define the minimum nodes
    min_nodes = remove_edges(data)
    # Print the minimun nodes
    print(min_nodes)

    # Save to the output_file
    save_output_file(min_nodes=min_nodes)


if __name__=="__main__":
    main()
