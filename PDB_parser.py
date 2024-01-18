#!/usr/bin/python3

# imported modules and packages

import Bio.PDB
import re
import math

# portion of program below is based on the tutorial of Phi and Psi angles (Cock, 2006)

with open('angles.txt', 'w') as file:
    for model in Bio.PDB.PDBParser().get_structure("8F2I", "8F2I.pdb"):
        for chain in model:
            polypeptides = Bio.PDB.PPBuilder().build_peptides(chain)
            for poly_index, poly in enumerate(polypeptides):
                file.write("Model {0} Chain {1}\n".format(str(model.id), str(chain.id))),
                file.write("from {0}{1}\n".format(poly[0].resname, poly[0].id[1])),
                file.write("to {0}{1}\n".format(poly[-1].resname, poly[-1].id[1]))
                phi_psi = poly.get_phi_psi_list()
                for res_index, residue in enumerate(poly):
                    res_name = "Residue {0}{1}".format(residue.resname, residue.id[1])
                    file.write("{0} {1}\n".format(res_name, phi_psi[res_index]))

# stdout print function helps confirm that .txt file was generated

print("Values attained in radial format.")

# .txt file that was generated will now be parsed through using the for loop below
# regex split is used to split the string line in file into values of an array
# array values that correspond to the phi and psi angles can be calculated into angle values

with open("angles_degrees.txt", "w") as file_2:
    for line in open("angles.txt"):
        phi = 0
        psi = 0
        if line.startswith("Residue"):
            line = line.strip()
            columns = re.split(r"[\s\(\),]", line)
            if columns[3] == ("None"):
                pass
            else:
                phi = float(columns[3])
                phi = ((phi * 180) / math.pi)
                if phi > 180:
                    phi = (phi - 360)
                elif phi < -180:
                    phi = (phi + 360)

            if columns[5] == ("None"):
                pass
            else:
                psi = float(columns[5])
                psi = ((psi * 180) / math.pi)
                if psi > 180:
                    psi = (phi - 360)
                elif psi < -180:
                    psi = (phi + 360)
            file_2.write("{0} {1} ({2}, {3})\n".format(columns[0], columns[1], phi, psi))
        else:
            file_2.write(line)

print("Values attained in degree format.")
