
**This is a free online repository for sharing GIST/HSA/3D-RISM data of COVID19 related protein targets**

Currently, we have the GIST/HSA/3D-RISM data for 7 targets:

Structures 1-5  (SARS-CoV-2 structures)
Main Protease (Mpro, 3CLpro): **_6LU7_** (2.16 Å), **_6YB7_** (1.25 Å), **_6M03_** (2.00 Å), **_6Y84_** (1.39 Å), **_6W63_** (2.10 Å), **_6WX4_** (1.7 Å) . Target the substrate binding site of Mpro.

Structure 6  (SARS-CoV-1 structure)
Helicase (Nsp13): **_6JYT_** (2.80 Å). Target (1) the ADP binding site but discourage (2) the nucleic acids binding site. *No SARS-CoV-2 structure exists for this protein.

Structure 7  (SARS-CoV-2 structure)
Nsp16 (2’-O-methyltransferase, nsp 10/16): **_6W4H_** (1.80 Å). Target: S-adenosylmethionine (SAM) binding site.


We ran two MD simulations for each target, with the protein heavy atoms restrained (denoted as "*rigid*") or with the protein side chains left flexible (denoted as "*SCflex*"). For 6W63 and 6Y84, we ran MD on both apo structure (denoted as "*APO*") and protein-ligand complex (denoted as "*LIG*"). For targets 6W63 and 6YB7, we also provided the data that generated by Dr. Dan McKay( From Novartis)'s prepared structures and MD protocols (The data were in *_Mckay folder under those two targets). In Mckay's MD protocol, the protein were total left flexible (denoted as "*BBflex*") except the alpha C of a few residues (For details, please refer to the amber parameters files under its amber directory).

For an explanation of the names of the files under the target directory, please refer to the "File_list_explanation.csv" file.


**If requesting GIST/HSA data for other COVID-19 related targets, please contact Dr. Tom Kurtzman at simpleliquid@gmail.com**
