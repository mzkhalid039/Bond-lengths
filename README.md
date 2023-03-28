# Bond-lengths
Analyze Bond Lengths in VASP POSCAR Files for a model system of quaternary compound (4 elements, K, Nb, B, O).

This script calculates and plots bond lengths for a given input file in the POSCAR format. It uses the spglib and ase libraries to perform space group analysis and neighbor list generation, respectively.

## Requirements

This script requires Python 3 and the following Python libraries:

spglib,
ase,
matplotlib,
You can install these libraries using the pip package manager:

"pip install spglib ase matplotlib"

where input_file is the path to your input file in the POSCAR format and cutoff is the maximum distance to consider a bond.

The script will print the average bond lengths for Nb-O, B-O, and K-O bonds for the KNBO (quaternary compounds), and plot histograms of the bond lengths for each bond type.

## bond_lengths.py

You can run the script from the command line as follows:

python script.py input_file cutoff

where input_file is the path to your input file in the POSCAR format and cutoff is the maximum distance to consider a bond.
The script will print the average bond lengths for Nb-O, B-O, and K-O bonds, and plot histograms of the bond lengths for each bond type.



## bond_length_comparison.py 

Script to Analyze Bond Lengths in VASP POSCAR Files Overview: This script is designed to analyze bond lengths in VASP POSCAR files and plot histograms of the bond lengths. Specifically, the script calculates the bond lengths between Nb/B/K atoms and O atoms, and generates histograms of the bond lengths for two different structures. Usage: The script can be run using the following command format:

python bond_lengths.py input_file1 input_file2 cutoff_length

Here, `input_file1` and `input_file2` are the paths to two different POSCAR files, and `cutoff_length` is the maximum distance to consider a bond. The script will analyze the bond lengths in the two input files and plot histograms of the bond lengths. Requirements: This script requires the following Python packages: - spglib - ase - matplotlib These packages can be installed using `pip`, the Python package manager. Limitations: This script assumes a specific type of analysis and bond length calculation for Nb/B/K-O bonds in VASP POSCAR files. It may not be applicable for other types of systems or bond analyses. Additionally, the script has limited error handling and may break if used with unsupported file formats, input structures, or parameters. Care should be taken to ensure that the input files and parameters are appropriate for the analysis.


