codons_to_protein = {'AUG': "Methionine", 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine',
    'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan',
    'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}

def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    proteins = []
    for i in codons:
        if not i in codons_to_protein:
            proteins.append(i)
        elif codons_to_protein[i] == 'STOP':
            break
        else:
            proteins.append(codons_to_protein[i])
    return proteins
