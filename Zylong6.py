def find_upstream(dna_sequence):
    global up
    for i in range(len(dna_sequence)- len('ATG')):
        if dna_sequence[i:i+len('ATG')] == 'ATG':
            up = i
            return dna_sequence[0:i]
        else: i+=1

def find_gene(dna_sequence):
    global ATG
    for i in range(len(dna_sequence)- len('ATG')):
        if dna_sequence[i:i+len('ATG')] == 'ATG':
            ATG = i+1
            return dna_sequence[i:]
        else: i+=1
   
def second_codon(gene_sequence):
    for i in range(len(gene_sequence)- len('ATG')):
        if gene_sequence[i:i+len('ATG')] == 'ATG':
            return gene_sequence[i+3:i+6]
        else: i+=1

def third_codon(gene_sequence):
    for i in range(len(gene_sequence)- len('ATG')):
        if gene_sequence[i:i+len('ATG')] == 'ATG':
            return gene_sequence[i+6:i+9]
        else: i+=1

def complementary_nucleotide(nucleotide):
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    
def complementary_sequence(dna_sequence):
    complementary = ''
    for i in range(len(dna_sequence)):
        complementary +=(complementary_nucleotide(dna_sequence[i]))
        i+=1
    complementary = (''.join([complementary]))
    return complementary

def main():

    dna_sequence = input('Please enter a DNA genetic sequence: ')
    print(f'\n\nOriginal sequence: {dna_sequence}')

    geneSequence = find_gene(dna_sequence)
    print(f'\nATG codon at bp {ATG}'
    f'\n    followed by {second_codon(geneSequence)} at bp {ATG +3}'
    f'\n    followed by {third_codon(geneSequence)} at bp {ATG+6}')

    print(f'\nUpstream sequence: {find_upstream(dna_sequence)}'
    f'\nUpstream length:   {up} bp')

    print(f'\nGene sequence: {geneSequence}'
    f'\nGene length:   {len(find_gene(dna_sequence))} bp')

    line = '|'

    print(f'[+ Strand]: {geneSequence}'
    f'\n            {(line * len(geneSequence))}'
    f'\n[- Strand]: {complementary_sequence(geneSequence)}')

if __name__ == "__main__":
    main()
