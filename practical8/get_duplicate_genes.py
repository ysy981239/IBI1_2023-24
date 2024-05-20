import os
import re

os.chdir("D:\IBI1_2023-24\practical8")

input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open('duplicate_genes.fa', 'w')

seq = ''
gene_name = []
i = 0
flag = 0

for line in input_file:
    if line.startswith(">"):
        if flag == 1:
            output_file.write(name[0] + '\n' + seq + '\n')
            flag = 0
        
        description = line.strip().split()[1]
        if 'duplication' in description:
            gene_name = re.findall(r'gene:(.+)\sgene_biotype', line)[0]
            output_file.write(gene_name + '\n' + seq + '\n')
        
        seq = ''
        i += 1
        flag = 1  
    else:
        seq += re.sub(r'\n', '', line)
input_file.close()
output_file.close()