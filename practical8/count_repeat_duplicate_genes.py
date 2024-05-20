import re
fasta_file_path = r'D:\IBI1_2023-24\practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
genes_dict = {}

def count_1(string):
    counter = 0
    for i in range(0, len(string)-1):
        substring = string[i:i+6]  
        if substring == 'GTGTGT':
            counter += 1
    return counter

def count_2(string):
    counter = 0
    for i in range(0, len(string)-1):
        substring = string[i:i+6]  
        if substring == 'GTCTGT':
            counter += 1
    return counter

with open(fasta_file_path, 'r') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            gene_name = line
            genes_dict[gene_name] = ""
        else:
            genes_dict[gene_name] += line.strip()
genes = input('Please enter your sequences: ')
if genes == 'GTGTGT':
    with open('GTGTGT_duplicate_genes.fa','w') as f1:  
        for gene_name, gene_sequence in genes_dict.items():
            simplified_name = str(re.findall(r'gene:(.+?)\s',gene_name))
            count = count_1(gene_sequence)
            if count != 0 and 'duplication' in gene_name:
                f1.write(f"The repeat sequence '{'GTGTGT'}' appears {count} times in the gene '{simplified_name}'."+'\n'+ gene_sequence + '\n')
                simplifed_name = ''
if genes == 'GTCTGT':
    with open('GTCTGT_duplicate_genes.fa','w') as f2:
        for gene_name, gene_sequence in genes_dict.items():
            simplified_name = str(re.findall(r'gene:(.+?)\s',gene_name))
            count = count_2(gene_sequence)
            if count !=0 and 'duplication' in gene_name:
                f2.write(f"The repeat sequence '{'GTCTGT'}' appears {count} times in the gene '{simplified_name}'."+'\n'+ gene_sequence + '\n')
                simplified_name = ''