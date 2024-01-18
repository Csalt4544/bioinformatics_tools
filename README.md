## bioinformatics_tools
# Various useful scripts created for projects and other scenarios

This repository contains useful bioinformatics scripts that were created for various class assignments, projects, and other ventures.

The ex05 and ex06 scripts are parsing programs that can be used to parse through GFF3 and BLASTN output files for specific information, respectively.

The PhiPsi scripts (PDB_parser and SecondaryPrediction) are programs created to parse through a downloaded PDB format file for a protein's structure and use coordinates to determine structure and predict the secondary structure found at the residue using the phi and psi angles of the protein backbone. Predictions were based using a standard Ramachandran plot.

The StopCodonRemover was utilize to prepare a FASTA sequence user-input to replace stop codons (TAG, TAA, or TGA) with three dashes and remove any whitespaces that are present so that analysis with several evolutionary selection tools contained within the DataMonkey site can be done.

# License

These scripts are distributed under the GNU license 3.0
