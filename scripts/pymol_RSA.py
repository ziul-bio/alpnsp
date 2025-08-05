# PyMOL script to visualize top couplings

#### USAGE ####
# run /Users/luiz/Library/CloudStorage/OneDrive-Personal/WilkeLab/Projects/alphavirus/visualize_interactions_pairs_RSA.py
# select my_selection, resi 50-60
# zoom my_selection


import pymol.cmd as cmd

# Load compact structure
# cmd.load('/Users/luiz/Library/CloudStorage/OneDrive-Personal/WilkeLab/Projects/alphavirus/data/nsP4_pdb/nsp4-RdRp_compact_chainX_RSA_compact_x_extended_LUO.pdb')  
# cmd.spectrum("b", "blue_white_red", minimum=-0.77, maximum=0.77)

# Load extended structure
cmd.load('/Users/luiz/Library/CloudStorage/OneDrive-Personal/WilkeLab/Projects/alphavirus/data/nsP4_pdb/nsp4-SAXS-extended-conf-MDsimulated_V25E91_LUO_chainX_RSA_extended_LUO_x_compact.pdb')
cmd.spectrum("b", "blue_white_red", minimum=-0.77, maximum=0.77)



################## Visualization of the top couplings ##################
# N-term compact
#pairs = [(20, 25),(39, 71),(30, 100),(84, 279),(80, 321),(76, 268),(23, 105),(29, 98),(23, 103),(81, 249),(38, 74),(41, 67),(81, 253),(79, 275),(30, 335),(88, 249),(83, 275),(27, 99),(83, 278),(74, 79),(76, 80),(64, 68),(40, 68)]

# N-term extended
#pairs = [(39, 71),(88, 398),(23, 103),(38, 74),(30, 235),(85, 242),(88, 399),(85, 243)] 


################ Sites from version 2 with psiblast
# N-term compact
# pairs = [
#     (27, 99), (38, 75), (29, 98), (20, 24), 
#     (76, 80), (25, 101), (29, 99), (23, 105), (20, 25), 
#     (81, 88), (30, 99), (30, 100), (31, 96),  
#     (80, 253), (84, 88), (25, 100), (20, 105), (80, 84), 
#     (19, 25), (87, 279), (83, 275), (85, 89), (81, 85), (29, 100), 
#     (85, 278), (25, 103), (31, 98), (28, 97), (88, 249), (27, 98), 
#     (69, 266), (17, 31), (69, 73), (73, 268), 
#     (37, 73), (68, 72), (83, 278),  (39, 74), (30, 98), (74, 257)
# ]

# ONly pairs within at leat 4 aa apart
comp_pairs = [
    (38, 75), (29, 98), (76, 80), 
    (25, 101), (29, 99), (20, 25),  (81, 88), (30, 99), 
    (30, 100), (31, 96), (38, 254), 
    (80, 253), (84, 88), (25, 100), (20, 105), (80, 84), 
    (19, 25),  (85, 89), (81, 85), 
    (29, 100), (73, 260), (85, 278),
    (25, 103), (31, 98), (28, 97), 
    (17, 31), (69, 73), (73, 268), 
    (37, 73), (90, 251), (30, 98),
]


# N-term extended
# pairs = [
#     (38, 75), (20, 24), #(80, 84),  (81, 85),
#     (88, 398), (88, 397), (34, 239), 
#     (87, 398), (20, 105),  (35, 235), 
#     (30, 234), (85, 242), (30, 235), (33, 238), 
#     (25, 103), (35, 238), (39, 74)
#]

# ONly pairs within at leat 4 aa apart
ext_pairs = [
    (87, 90), (20, 24), (76, 80), (80, 242), 
    (25, 101), (22, 25), (77, 242), (25, 103),
    (84, 242), (20, 25), (85, 398), 
    (25, 100), (80, 84), (19, 25), 
    (76, 239), (21, 25), (69, 73), (80, 240),
    (81, 85), (29, 100), (81, 398), (85, 397), 
    (84, 93), (75, 81), (80, 243), (85, 242), (80, 241), 
    (31, 456), (81, 397), (30, 341), (84, 397), 
]


for i, (res1, res2) in enumerate(ext_pairs):
    # Specify carbon alpha atoms for each residue
    ca1 = f"resi {res1} and name CA"
    ca2 = f"resi {res2} and name CA"

    # Connect carbon alpha atoms with a line to measure distance
    cmd.distance(f"connection{i}", ca1, ca2)
    cmd.set("dash_width", 2, f"connection{i}")
    cmd.set("dash_length", 0.5, f"connection{i}")
    cmd.set("dash_gap", 0.0, f"connection{i}")

    # Show the amino acids as sticks
    cmd.show("sticks", f"resi {res1} or resi {res2}")

    # Optional: Adjust the appearance of connections if needed
    cmd.set("dash_color", "yellow", f"connection{i}")  # Set the color of the dash to red for visibility
