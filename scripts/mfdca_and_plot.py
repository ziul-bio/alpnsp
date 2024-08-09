from pydca.plmdca import plmdca
from pydca.meanfield_dca import meanfield_dca
from pydca.sequence_backmapper import sequence_backmapper
from pydca.msa_trimmer import msa_trimmer
from pydca.contact_visualizer import contact_visualizer
from pydca.dca_utilities import dca_utilities
import matplotlib.pyplot as plt
import sys

msa_file = sys.argv[1] #"Trimmed_ad_hoc_alignment/Trimmed_ad_hoc_alignment.fa"
ref_file = sys.argv[2] #"AAN85442_2C_annotated.fasta"

sudo_ct = 0.5
seqid = 0.8

mfdca_inst = meanfield_dca.MeanFieldDCA(
    msa_file,
    'protein',
    seqid = seqid, #default is 0.8,
    pseudocount = sudo_ct #0.5; literature says this number should be on the order of 1/(2*num_sequences)
)

mfdca_FN_APC = mfdca_inst.compute_sorted_FN_APC()
Ang = 5.0
mfdca_visualizer = contact_visualizer.DCAVisualizer('protein', 'A', 
                                                    sys.argv[3], #'AAN85442_2C_annotated_6mer_relaxed_rank_001_alphafold2_multimer_v3_model_4_seed_000.pdb',
    refseq_file = ref_file,
    sorted_dca_scores = mfdca_FN_APC,
    linear_dist = 4,
    contact_dist = Ang,
)

contact_map_data = mfdca_visualizer.plot_contact_map()
plt.savefig('contactmap_mfdca_'+ msa_file.split('/')[1] + '_sudoct_'+ str(sudo_ct) +sys.argv[3][0:24]+str(Ang)+'Ang_'+ '.png')

tp_rate_data = mfdca_visualizer.plot_true_positive_rates()

plt.savefig('tp_mfdca_'+ msa_file.split('/')[1] +'_sudoct_'+ str(sudo_ct) + sys.argv[3][0:24]+str(Ang)+'Ang_'+'.png')


## Now do it with the pseudoliklihood method which takes a little longer but is supposedly more accurate

l_J = 20.0
l_h = 1.0

plmdca_inst = plmdca.PlmDCA(
    msa_file,
    'protein',
    seqid = 0.8,
    lambda_h = l_h,
    lambda_J = l_J, #Phys Rev E  says the best param was .01
    num_threads = 10,
    max_iterations = 500,
)

plmdca_FN_APC = plmdca_inst.compute_sorted_FN_APC()

plmdca_visualizer = contact_visualizer.DCAVisualizer('protein', 'A', 
                                                    sys.argv[3], #'AAN85442_2C_annotated_6mer_relaxed_rank_001_a>
    refseq_file = ref_file,
    sorted_dca_scores = plmdca_FN_APC,
    linear_dist = 4,
    contact_dist = Ang,
)

contact_map_data = plmdca_visualizer.plot_contact_map()
plt.savefig('contactmap_plmdca_'+ msa_file.split('/')[1] + '_lh_' + str(l_h) +'_lJ_' + str(l_J) +sys.argv[3]+str(Ang)+'Ang_' '.png')

tp_rate_data = plmdca_visualizer.plot_true_positive_rates()

plt.savefig('tp_plmdca_'+ msa_file.split('/')[1] + '_lh_' + str(l_h) +'_lJ_' + str(l_J) + sys.argv[3]+str(Ang)+'Ang_'+ '.png')

