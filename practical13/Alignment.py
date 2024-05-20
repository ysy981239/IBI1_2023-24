import blosum as bl

# Load the BLOSUM62 matrix for sequence comparison.
matrix = bl.BLOSUM(62)

# Change the current working directory to where the fasta files are stored.
import os
os.chdir("D:\IBI1_2023-24\practical13")

# Open the input fasta files containing the protein sequences.
human = open('SLC6A4_HUMAN.fa', 'r')
mouse = open('SLC6A4_MOUSE.fa', 'r')
rat = open('SLC6A4_RAT.fa', 'r')

# Define a function to extract the sequence data from the fasta files.
import re
def get(input_file):
    """
    Extract the amino acid sequence from a fasta file.
    
    Parameters:
    input_file (file): The opened fasta file containing the sequence.
    
    Returns:
    list: A list of amino acids in the sequence.
    """
    seq = ""
    for line in input_file:
        if line.startswith(">"):  # Skip the header lines starting with ">"
            continue
        seq += re.sub(r'\n', '', line)  # Remove newline characters and build the sequence string
    return list(seq)  # Convert the sequence string to a list of amino acids

# Use the get function to retrieve the sequences for human, mouse, and rat.
seq_human = get(human)
seq_mouse = get(mouse)
seq_rat = get(rat)

# Define a function to compare two amino acid sequences using the BLOSUM62 matrix.
def Compare(seq1, seq2):
    """
    Compare two amino acid sequences and calculate the BLOSUM score and percentage identity.
    
    Parameters:
    seq1 (list): The first amino acid sequence.
    seq2 (list): The second amino acid sequence.
    """
    # Initialize the score for sequence comparison.
    score = 0
    # Calculate the BLOSUM score for the two sequences.
    for i in range(len(seq1)):
        score += matrix[seq1[i]][seq2[i]]
    print("BLOSUM score:", score)
    
    # Initialize the edit distance.
    edit_distance = 0
    # Calculate the Hamming/edit distance between the two sequences.
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            edit_distance += 1
    # Calculate and print the percentage identity.
    print("Percentage identity:", 100 - 100 * edit_distance / len(seq1), "%")

# Print the results for the pairwise comparisons of the sequences.
print("Comparing SLC6A4_HUMAN and SLC6A4_MOUSE")
Compare(seq_human, seq_mouse)
print("\nComparing SLC6A4_HUMAN and SLC6A4_RAT")
Compare(seq_human, seq_rat)
print("\nComparing SLC6A4_MOUSE and SLC6A4_RAT")
Compare(seq_mouse, seq_rat)

# Close the opened files.
human.close()
mouse.close()
rat.close()