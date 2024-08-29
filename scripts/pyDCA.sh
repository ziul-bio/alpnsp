#!/bin/bash
set -e

MSA=data/nsP4/psiblast_data/alphavirus_nsP4_psiblast_rvdb_rmdup2_seq_idt30_filteredX_ref_aligned.fasta
PDB=data/nsP4/nsP4_pdb/nsp4-RdRp_SAXS_extended_neff_colored_v03_chainX.pdb
REFSEQ=data/nsP4/nsP4_pdb/nsp4-RdRp-SAXS_extended_pdb_seq.fasta
OUTDIR=results/DCA/nsP4/

filename=$(basename "${MSA%.*}")
MAXITER=500
NUMTHREADS=64
LBh=1.0
LBj=20.0
SEQID=0.85



# Trim sequence
#pydca trim_by_refseq <biomolecule>  <alignment.fa>  <refseq_file.fa> --remove_all_gaps --verbose
#pydca trim_by_refseq protein $MSA $REFSEQ --remove_all_gaps --verbose


# DCA Computation

### The command compute_fn computes DCA scores obtained from the Frobenius norm of the couplings. 
### --apc performs average product correction (APC). 
### To obtain DCA scores from direct-information (DI) we replace the subcommand compute_fn by compute_di.


## Using pydca's Pseudolikelihood Maximization Algorithm

#plmdca compute_fn <biomolecule> <alignment.fa> --max_iterations 500 --num_threads 6 --apc --verbose 
plmdca compute_fn protein "Trimmed_${filename}/Trimmed_${filename}.fa" --refseq_file $REFSEQ --apc --seqid $SEQID --lambda_h $LBh --lambda_J $LBj --max_iterations $MAXITER --num_threads $NUMTHREADS --output_dir $OUTDIR --verbose
                           

## Using pydca's Mean-Field Algorithm
#mfdca compute_fn <biomolecule> <alignment.fa> --apc --pseudocount 0.5 --verbose
#mfdca compute_fn protein "Trimmed_${filename}/Trimmed_${filename}.fa" --refseq_file $REFSEQ --apc --seqid $SEQID --output_dir $OUTDIR --pseudocount 0.5 --verbose


# Plotting
#pydca plot_contact_map <biomolecule> <PDB_chain_name> <PDB_id/PDB_file.PDB> <refseq.fa> <DCA_file.txt> --verbose  
#pydca plot_contact_map protein X $PDB $REFSEQ "PLMDCA_apc_fn_scores_Trimmed_${filename}/Trimmed_${filename}.fa" --verbose  | tee -a $log_file
#pydca plot_contact_map protein X $PDB $REFSEQ results/DCA/nsP4/PLMDCA_seqid_80_apc_fn_scores_Trimmed_alphavirus_nsP4_psiblast_rvdb_rmdup2_seq_idt30_filteredX_ref_aligned.txt --verbose  | tee -a $log_file