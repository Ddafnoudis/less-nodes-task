# Project

Given a graph, find an algorithm that removes the least number of nodes so that no edges are left.

### Folders

There are two folders:
- `task` folder: Main folder. Contains all the scripts and folders
- `data_folder`. Contains the `graph.txt` and `nodes-to-remove.txt` files.

### Instructions and scripts

The **task** folder contains all the scripts.
- The `main.py` is the main script. All the functions are running from that script.
- The `generate_data.py` script generates the input data.
- The `algorithm.py` script takes as input the data and gives the output.
- Lastly, the `output.py` takes the output and saves it in an output_file.

### Files

Two files are generated:
- `Graph.txt`
- `nodes-to-remove.txt`

### Tree of the working environment

```bash
|-- README.md
|-- algorithm.py
|-- data_folder
|   |-- graph.txt
|   `-- nodes-to-remove.txt
|-- generate_data.py
|-- main.py
`-- output.py
```

To run the scriptsm, you need to type the following command:
```bash
python main.py
```

### Tools

```bash
pandas==1.5.3
itertools
networkx==3.2.1
```


