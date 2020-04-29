#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:30:15 2020

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

from pymol import cmd

import os

#os.chdir("/Users/eric/Dropbox/Sars-Cov-2/COVID19_GIST-HSA/Github_repository/COVID19_GIST_HSA/6JYT/6JYT_apo_rigid")

from glob import glob

cmd.delete("all")

protein=glob("./protein_prep/*nowat.pdb")[0]

ligand=glob("./protein_prep/*lig*pdb")[0]



cmd.load(protein,"pro")
cmd.load(ligand,"lig")
cmd.save("pro_lig_initial.pdb","all")

cmd.delete("all")

# align the pro_lig.pdb with the firstframe of the simulation





first_frame=glob("./amber/*firstframe*nowat*pdb")


cmd.load("pro_lig_initial.pdb","initial_com")
cmd.load(first_frame[0],"first_frame")

cmd.align("initial_com","first_frame")

cmd.save("aligned_complex.pdb","initial_com")

cmd.delete("all")


#extract the organic molecules from the aligned_complex 

cmd.load("aligned_complex.pdb","complex")

cmd.select("lig","organic")

cmd.save("aligned_lig.pdb","lig")

cmd.delete("all")



#combind the ligand with first frame pdb


cmd.load(first_frame[0],"first_frame")

cmd.load("aligned_lig.pdb","lig")

cmd.save("aligned_firstframe_lig.pdb","all")

cmd.delete("all")





