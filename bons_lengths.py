import spglib
from ase.io import read
from ase.neighborlist import neighbor_list
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Calculate and plot bond lengths for given input file and cutoff distance.')
parser.add_argument('input_file', type=str, help='path to input file in POSCAR format')
parser.add_argument('cutoff', type=float, help='maximum distance to consider a bond')
args = parser.parse_args()

# Read in POSCAR file
poscar = read(args.input_file, format="vasp")

# Run the space group analysis
data = (poscar.get_cell(), poscar.get_positions(), poscar.get_atomic_numbers())
result = spglib.get_symmetry_dataset(data)

# Generate list of nearest neighbors and calculate bond lengths
cutoff = args.cutoff
nb_o_lengths = []
b_o_lengths = []
k_o_lengths = []
neighbor_list = neighbor_list("ijdD", poscar, cutoff, self_interaction=False)
for i, atom in enumerate(poscar):
    symbol = atom.symbol
    neighbors = neighbor_list[0][neighbor_list[1]==i]
    for neighbor in neighbors:
        neighbor_symbol = poscar[neighbor].symbol
        distance = poscar.get_distance(i, neighbor)
        if distance < cutoff:
            if (symbol, neighbor_symbol) == ("Nb", "O"):
                nb_o_lengths.append(distance)
            elif (symbol, neighbor_symbol) == ("B", "O"):
                b_o_lengths.append(distance)
            elif (symbol, neighbor_symbol) == ("K", "O"):
                k_o_lengths.append(distance)

#Average bond lengths
nb_o_avg = sum(nb_o_lengths)/len(nb_o_lengths)
b_o_avg = sum(b_o_lengths)/len(b_o_lengths)
k_o_avg = sum(k_o_lengths)/len(k_o_lengths)

print("Average Nb-O bond length: {:.3f} Å".format(nb_o_avg))
print("Average B-O bond length: {:.3f} Å".format(b_o_avg))
print("Average K-O bond length: {:.3f} Å".format(k_o_avg))

# Plot bond lengths histograms
fig, axs = plt.subplots(1, 3, figsize=(10, 3))
axs[0].hist(nb_o_lengths, bins=30)
axs[0].set_xlabel("Nb-O bond length (Å)")
axs[0].set_ylabel("Count")
axs[1].hist(b_o_lengths, bins=30)
axs[1].set_xlabel("B-O bond length (Å)")
axs[1].set_ylabel("Count")
axs[2].hist(k_o_lengths, bins=30)
axs[2].set_xlabel("K-O bond length (Å)")
axs[2].set_ylabel("Count")
plt.tight_layout()
plt.show()
