
import sys
import spglib
from ase.io import read
from ase.neighborlist import neighbor_list
import matplotlib.pyplot as plt

# Parse command line arguments for input files and cutoff length
input_file1 = sys.argv[1]
input_file2 = sys.argv[2]
cutoff_length = float(sys.argv[3])

# Read in first POSCAR file
poscar1 = read(input_file1, format="vasp")

# Run the space group analysis on the first structure
data = (poscar1.get_cell(), poscar1.get_positions(), poscar1.get_atomic_numbers())
result = spglib.get_symmetry_dataset(data)

# Generate list of nearest neighbors and calculate bond lengths for the first structure
nb_o_lengths1 = []
b_o_lengths1 = []
k_o_lengths1 = []
neighbor_list1 = neighbor_list("ijdD", poscar1, cutoff_length, self_interaction=False)
for i, atom in enumerate(poscar1):
    symbol = atom.symbol
    neighbors = neighbor_list1[0][neighbor_list1[1]==i]
    for neighbor in neighbors:
        neighbor_symbol = poscar1[neighbor].symbol
        distance = poscar1.get_distance(i, neighbor)
        if distance < cutoff_length:
            if (symbol, neighbor_symbol) == ("Nb", "O"):
                nb_o_lengths1.append(distance)
            elif (symbol, neighbor_symbol) == ("B", "O"):
                b_o_lengths1.append(distance)
            elif (symbol, neighbor_symbol) == ("K", "O"):
                k_o_lengths1.append(distance)

# Read in second POSCAR file
poscar2 = read(input_file2, format="vasp")

# Run the space group analysis on the second structure
data = (poscar2.get_cell(), poscar2.get_positions(), poscar2.get_atomic_numbers())
result = spglib.get_symmetry_dataset(data)

# Generate list of nearest neighbors and calculate bond lengths for the second structure
nb_o_lengths2 = []
b_o_lengths2 = []
k_o_lengths2 = []
neighbor_list2 = neighbor_list("ijdD", poscar2, cutoff_length, self_interaction=False)
for i, atom in enumerate(poscar2):
    symbol = atom.symbol
    neighbors = neighbor_list2[0][neighbor_list2[1]==i]
    for neighbor in neighbors:
        neighbor_symbol = poscar2[neighbor].symbol
        distance = poscar2.get_distance(i, neighbor)
        if distance < cutoff_length:
            if (symbol, neighbor_symbol) == ("Nb", "O"):
                nb_o_lengths2.append(distance)
            elif (symbol, neighbor_symbol) == ("B", "O"):
                b_o_lengths2.append(distance)
            elif (symbol, neighbor_symbol) == ("K", "O"):
                k_o_lengths2.append(distance)

# Plot bond lengths histograms side by side
fig, axs = plt.subplots(1, 3, figsize=(9, 3))
axs[0].hist([nb_o_lengths1, nb_o_lengths2], bins=30, label=["File 1", "File 2"])
axs[0].set_xlabel("Nb-O bond length (Å)")
axs[0].set_ylabel("Count")
axs[0].legend()
axs[1].hist([b_o_lengths1, b_o_lengths2], bins=30, label=["File 1", "File 2"])
axs[1].set_xlabel("B-O bond length (Å)")
axs[1].legend()
axs[2].hist([k_o_lengths1, k_o_lengths2], bins=30, label=["File 1", "File 2"])
axs[2].set_xlabel("K-O bond length (Å)")
axs[2].legend()
plt.tight_layout()
plt.show()
