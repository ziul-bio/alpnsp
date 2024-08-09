#screen -d -m -L -Logfile pydca_screen_clean_algn5Ang python mfdca_and_plot.py Trimmed_aligned_Unique_from_blast_results_PV-2C_intersection_hitsC-RVDB_first_2500_extracted_2C_unique_gt200_cleaned_gap_threshold_0.95/Trimmed_aligned_Unique_from_blast_results_PV-2C_intersection_hitsC-RVDB_first_2500_extracted_2C_unique_gt200_cleaned_gap_threshold_0.95.fa AAN85442_2C_annotated.fasta AAN85442_2C_annotated_6mer_relaxed_rank_001_alphafold2_multimer_v3_model_4_seed_000.pdb

ALIGNFILE='aligned_mafft_blast_results_PV-2C_intersection_hitsC-RVDB_with_PVref_extraction_unique_seqs.fasta'
REFSEQ='AAN85442_2C_annotated.fasta'
PDB='PV_Mahoney_2C.pdb' 
#AAN85442_2C_annotated_6mer_relaxed_rank_001_alphafold2_multimer_v3_model_4_seed_000.pdb

AFILE="${ALIGNFILE//".fasta"/}"
TRIMMED="Trimmed_${AFILE}/Trimmed_${AFILE}.fa"
#if the file has NOT been trimmed, do it
if [ ! -e $TRIMMED ]; then
	pydca trim_by_refseq protein $ALIGNFILE $REFSEQ --remove_all_gaps --verbose
fi

screen -d -m -L -Logfile pydca_screen_mafft_uniqueseqs_monomer.txt python mfdca_and_plot.py $TRIMMED $REFSEQ $PDB



ALIGNFILE='aligned_mafft_blast_results_PV-2C_intersection_hitsC-RVDB_with_PVref_extraction.fasta'
REFSEQ='AAN85442_2C_annotated.fasta'
PDB='PV_Mahoney_2C.pdb' 
#AAN85442_2C_annotated_6mer_relaxed_rank_001_alphafold2_multimer_v3_model_4_seed_000.pdb

AFILE="${ALIGNFILE//".fasta"/}"
TRIMMED="Trimmed_${AFILE}/Trimmed_${AFILE}.fa"
#if the file has NOT been trimmed, do it
if [ ! -e $TRIMMED ]; then
        pydca trim_by_refseq protein $ALIGNFILE $REFSEQ --remove_all_gaps --verbose
fi

screen -d -m -L -Logfile pydca_screen_mafft_uniqueseqs_monomer.txt python mfdca_and_plot.py $TRIMMED $REFSEQ $PDB

PDB='AAN85442_2C_annotated_6mer_relaxed_rank_001_alphafold2_multimer_v3_model_4_seed_000.pdb'

screen -d -m -L -Logfile pydca_screen_mafft_uniqueseqs_monomer.txt python mfdca_and_plot.py $TRIMMED $REFSEQ $PDB