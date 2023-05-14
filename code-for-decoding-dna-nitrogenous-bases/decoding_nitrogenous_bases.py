# Define a dictionary that maps each codon to its corresponding amino acid
codon_table = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
}

# Define a function to decode a DNA sequence into its corresponding nitrogenous bases
def decode_dna(dna_sequence):
    codons = [dna_sequence[i:i+3] for i in range(0, len(dna_sequence), 3)]
    amino_acids = [codon_table.get(codon, 'X') for codon in codons]
    return ''.join(amino_acids)

# Example usage:
dna_sequence = 'GGTCTTTGAAGATGCTTTTGAAACTCCGAGGAAATAGCTGATCTTGTTCATCCAAATTTTGAGGAGGAGGCTGTTGTTGGGAGTTGTACCCACAGATACCTCTCTTCTACTTGGGGAGATGCTTGATGAAGTTTTTCTACTTTGAGAAGAAGAAATGCTTTGCAAGGAAATGAGATGATGACTGATCCAGGACTACACCCACCTTACATGTCTG...'

decoded_sequence = decode_dna(dna_sequence)
print(decoded_sequence)
