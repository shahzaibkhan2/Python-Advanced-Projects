# Using Biopython module and importing
from Bio.Seq import Seq

# Load DNA sequence from file
with open("sequence.txt", "r") as f:
    dna_seq_str = f.read().strip()

# Create a Seq object from the DNA sequence string
dna_seq = Seq(dna_seq_str)

# Calculate length of the DNA sequence
dna_seq_len = len(dna_seq)

# Calculate the complement of the DNA sequence
dna_seq_complement = dna_seq.complement()

# Calculate the reverse complement of the DNA sequence
dna_seq_rev_complement = dna_seq.reverse_complement()

# results to show
print("DNA sequence length: ", dna_seq_len)
print("DNA sequence complement: ", dna_seq_complement)
print("DNA sequence reverse complement: ", dna_seq_rev_complement)
