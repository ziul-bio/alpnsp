# import pydca modules
from pydca.plmdca import plmdca
from pydca.meanfield_dca import meanfield_dca
from pydca.sequence_backmapper import sequence_backmapper
from pydca.msa_trimmer import msa_trimmer
from pydca.contact_visualizer import contact_visualizer
from pydca.dca_utilities import dca_utilities
from matplotlib import pyplot as plt



# create MSATrimmer instance 
def trim_msa(protein_msa_file, biomol, protein_refseq_file, trimmed_data_outfile):
    print("Trimming MSA")
    trimmer = msa_trimmer.MSATrimmer(protein_msa_file, biomolecule=biomol, refseq_file=protein_refseq_file)
    trimmed_data = trimmer.get_msa_trimmed_by_refseq(remove_all_gaps=True)
    #write trimmed msa to file in FASTA format
    with open(trimmed_data_outfile, 'w') as fh:
        for seqid, seq in trimmed_data:
            fh.write('>{}\n{}\n'.format(seqid, seq))


# Compute DCA scores using Pseudolikelihood maximization algorithm
def compute_DCA(trimmed_data_outfile, biomol, seqIdt, lh, lj):
    print("Computing DCA scores using plmDCA")
    print('Parameters: seqIdt = ', seqIdt, ' lh = ', lh, ' lj = ', lj)
    plmdca_inst = plmdca.PlmDCA(
        trimmed_data_outfile,
        biomol,
        seqid = seqIdt,
        lambda_h = lh,
        lambda_J = lj,
        num_threads = 64,
        max_iterations = 500,
    )
    # compute DCA scores summarized by Frobenius norm and average product corrected
    plmdca_FN_APC = plmdca_inst.compute_sorted_FN_APC()
    
    # save results to file
    with open(dca_output, 'w') as f:
        f.write('first_site\tsecond_site\tAPC\n')
        for item in plmdca_FN_APC:
            indices, value = item
            f.write("%d\t%d\t%.10f\n" % (indices[0], indices[1], value))
            #f.write("%s\n" % str(item))
    return plmdca_FN_APC



def plot_true_contact(biomol, chain, PDB, protein_refseq_file, plmdca_FN_APC, Ang):
    print('Plotting contact map for plmDCA')
    plmdca_visualizer = contact_visualizer.DCAVisualizer(biomol, chain, PDB,
        refseq_file = protein_refseq_file,
        sorted_dca_scores = plmdca_FN_APC,
        linear_dist = 4,
        contact_dist = Ang,
    )
    # plot contact map
   
    contact_map_data = plmdca_visualizer.plot_contact_map()
    plt.savefig(contact_output)
    plt.close()
    # tp_rate_data = plmdca_visualizer.plot_true_positive_rates()
    # plt.savefig("results/DCA/nsP4/plots/compact2/tp_plmdca_psiblast_" + f + ".png")
    # plt.close()


if __name__ == '__main__':

    ################################ Define arguments ########################
    Ang=10
    seqIdt=0.85
    lh=1
    lj=20
    biomol='protein'
    chain='X'
    protein_msa_file = 'data/nsP4/psiblast_res/alphavirus_nsP4_psiblast_rvdb_rmdup2_seq_idt30_filteredX_ref_aligned.fasta'
    base_outpath = 'results/DCA/nsP4/v03/'

    # #PDB='data/nsP4/nsP4_pdb/nsp4-RdRp_compact_neff_colored_v03_chainX.pdb'
    # protein_refseq_file = 'data/nsP4/nsP4_pdb/nsp4-RdRp_compact_pdb_seq.fasta'
    # PDB='data/nsP4/nsP4_pdb/nsp4-RdRp_compact_chainX.pdb'
    # file_name = 'nsp4-RdRp-compact'

    # PDB='data/nsP4/nsP4_pdb/nsp4-RdRp_SAXS_extended_neff_colored_v03_chainX.pdb'
    # protein_refseq_file = 'data/nsP4/nsP4_pdb/nsp4-RdRp-SAXS_extended_pdb_seq.fasta'
    # PDB='data/nsP4/nsP4_pdb/nsp4-RdRp-SAXS_extended_chainX.pdb'
    # file_name = 'nsp4-RdRp-extended'

    protein_refseq_file = 'data/nsP4/nsP4_pdb/nsp4-SAXS-extended-conf-MDsimulated_V25E91_LUO_pdb_seq.fasta'
    PDB='data/nsP4/nsP4_pdb/nsp4-SAXS-extended-conf-MDsimulated_V25E91_LUO_chainX.pdb'
    file_name = 'nsp4-RdRp-extended_LUO'


    args = 'seqIdt'+str(seqIdt)+'_lh'+str(lh)+'_lj'+str(lj)
    trimmed_data_outfile = base_outpath + 'Trimmed_MSA_' + file_name + '.fa'
    dca_output = base_outpath + 'PLMDCA_FN_APC_' + file_name + '_' + args + '.txt' 
    contact_output = base_outpath + "contact_map_" + file_name + '_' + args + ".png"
    ########################################################################



    
    # trim msa
    trim_msa(protein_msa_file, biomol, protein_refseq_file, trimmed_data_outfile)
    
    # compute DCA scores
    plmdca_FN_APC = compute_DCA(trimmed_data_outfile, biomol, seqIdt, lh, lj)
                
    # plot contact map
    plot_true_contact(biomol, chain, PDB, protein_refseq_file, plmdca_FN_APC, Ang)
    
    print('Done')