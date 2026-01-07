# Data Analysis for "A fold switch regulates conformation of an alphavirus RNA-dependent RNA polymerase"

## Overview
This repository contains the computational data analysis for the study investigating the conformational regulation of alphavirus RNA-dependent RNA polymerase (RdRp) through a fold switch mechanism.

## Analysis Components
The data analysis is organized into three main Jupyter notebooks:

1. Direct Coupling Analysis (DCA):              
Notebook: [DCA](https://github.com/ziul-bio/alpnsp/blob/main/notebooks/alphavirus_nsP4_DCA.ipynb).              
Analysis of co-evolutionary constraints in alphavirus RdRp sequences using Direct Coupling Analysis to identify functionally important residue pairs and structural contacts.   

2. Neff Analysis:           
Notebook: [Neff](https://github.com/ziul-bio/alpnsp/blob/main/notebooks/alphavirus_nsP4_Neff.ipynb).            
Computation of effective sequence numbers (Neff) to quantify sequence diversity and conservation patterns across the multiple sequence alignment.   

3. Relative Solvent Accessibility (RSA) Analysis:                
Notebook: [RSA](https://github.com/ziul-bio/alpnsp/blob/main/notebooks/alphavirus_nsP4_RSA.ipynb).                 
Calculation and analysis of relative solvent accessibility to correlate surface exposure patterns with functional and conformational switching regions.    

## Data Files

### Sequence Data

1. [nsP4 references sequences](https://github.com/ziul-bio/alpnsp/blob/main/data/nsP4/alphavirus_nsP4_refseqs.fasta): Reference sequences for alphavirus nsP4 proteins
nsP4_ONNV.fasta: O'nyong-nyong virus nsP4 sequence.      

2. [MSA for nsP4 proteins](https://github.com/ziul-bio/alpnsp/blob/main/data/nsP4/psiblast_res/alphavirus_nsP4_psiblast_rvdb_rmdup2_seq_idt30_filteredX_ref_aligned.fasta): Multiple sequence alignment obtained through PSI-BLAST against the RVDB database, with redundancy removal, 30% sequence identity threshold, and filtering.     

3. [Wild type reference sequence](https://github.com/ziul-bio/alpnsp/blob/main/data/nsP4/nsP4_ONNV.fasta): Wild type sequence for ONNV used in the analusis.    

### Structural Data

1. [nsP4 PDB files](https://github.com/ziul-bio/alpnsp/tree/main/data/nsP4/nsP4_pdb): Directory containing PDB structure files representing different conformational states of nsP4.   
