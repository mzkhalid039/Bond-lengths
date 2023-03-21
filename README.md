# Bond-lengths
Analyze Bond Lengths in VASP POSCAR Files

bond_length_comparison.py 

Script to Analyze Bond Lengths in VASP POSCAR Files Overview: This script is designed to analyze bond lengths in VASP POSCAR files and plot histograms of the bond lengths. Specifically, the script calculates the bond lengths between Nb/B/K atoms and O atoms, and generates histograms of the bond lengths for two different structures. Usage: The script can be run using the following command format:

python bond_lengths.py input_file1 input_file2 cutoff_length
Here, `input_file1` and `input_file2` are the paths to two different POSCAR files, and `cutoff_length` is the maximum distance to consider a bond. The script will analyze the bond lengths in the two input files and plot histograms of the bond lengths. Requirements: This script requires the following Python packages: - spglib - ase - matplotlib These packages can be installed using `pip`, the Python package manager. Limitations: This script assumes a specific type of analysis and bond length calculation for Nb/B/K-O bonds in VASP POSCAR files. It may not be applicable for other types of systems or bond analyses. Additionally, the script has limited error handling and may break if used with unsupported file formats, input structures, or parameters. Care should be taken to ensure that the input files and parameters are appropriate for the analysis.

bond_length.py
