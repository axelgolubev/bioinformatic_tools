# The script was created to parse genomes to find polyproline containing motifs that could be regulated by EF-P protein
# 
# References: 
# 1) Elongation factor P: new mechanisms of function and an evolutionary diversity of translation regulation.
# AA Golubev, SZ Validov, KS Usachev, MM Yusupov. Molecular Biology
# 2) Analysis of the polyproline protein content of Staphylococcus aureus.
# A Golubev, D Blokhin, SZ Validov, MM Yusupov, K Usachev Molecular Biology of the cell

from os import remove

# Put the name of the fasta file here:
fasta_file = 's_aureus_proteins.txt'

# define list of motifs for search. Database would contain protein number + protein name as key and sequence as 
motifs = ['PPP','APP','PPD','PPG','PPK','PPT','PPA','PPQ','PPE','SPP','DPP','APPP','PPPD','PPPG','PPPK','PPPT','PPPA','PPPQ','PPPE','SPPP','DPPP']
motifs_calculations = dict.fromkeys(motifs, 0)

# TO DO: change transient file to csv with title and sequence columns
# part one - strip titles and add corresponding sequence after the title. Each protein would be in its own line for counting
with open(fasta_file,'r') as fasta_sequences, open('transient.txt','w') as transient_file:
    for line in fasta_sequences:
        if line[0] == '>':
            transient_file.write('\n'+ line.rstrip('\n'))
        else:
            transient_file.write(line.rstrip('\n'))

# second part - count motifs and generate results
with open('transient.txt','r') as transient_file, open('results.txt','w') as results:
    # Write a table header
    motifs_names = '\t'.join(motifs)
    results.write('PEPTIDES\n'+'Number\tName\t'+ motifs_names)
    for line in transient_file:
        for motif in motifs:
            if line.count(motif) > 0:
                motifs_calculations[motif] = line.count(motif)

        # Protein number and name extraction
        i_number = line.find(' ')
        number = line[1:i_number]
        i_title = line.find(' [')
        protein_name = line [(i_number+1):i_title]
        motifs_numbers = '\t'.join(str(list(motifs_calculations.values())))
        results.write(number+'\t'+ protein_name + motifs_numbers +'\n')
        motifs_calculations = dict.fromkeys(motifs, 0)

remove('transient.txt')
