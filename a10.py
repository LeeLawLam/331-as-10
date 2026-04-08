#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 <<Insert your name here>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
# ---------------------------------------------------------------

"""
Assignment 10
Author: <<Insert your name here>>
"""

from sys import flags

def cliSSD(ciphertext: str, files):
    """
    Args:
        ciphertext (str)
        files (list of str)
    Returns:
        dict
    """
    raise NotImplementedError()

def cliDPD(ciphertext: str, files):
    """
    Args:
        ciphertext (str)
        files (list of str)
    Returns:
        dict
    """
    raise NotImplementedError()

def cliSSDTest(ciphertext_files, sampletext_files):
    """
    Args:
        ciphertext_files (list of str)
        sampletext_files (list of str)
    Returns:
        dict
    """
    raise NotImplementedError()

def cliDPDTest(ciphertext_files, sampletext_files):
    """
    Args:
        ciphertext_files (list of str)
        sampletext_files (list of str)
    Returns:
        dict
    """
    raise NotImplementedError()

def generateMapping(dictionary: dict):
    """
    Args:
        dictionary (return value of cliSSDTest or cliDPDTest)
    Returns:
        A classification mapping (dict) of the ciphertexts.
        Please refer to the assignment instructions for the required format.
    """
    raise NotImplementedError()

def generateMatrix(mapping):
    """
    Args:
        mapping (dictionary returned by generateMapping)
    Returns:
        None (prints a formatted confusion matrix)
    """
    languages = ["bg", "de", "el", "en", "es", "fr", "it", "nl", "pl", "ru"]

    header = "     " + " | ".join(languages)
    print("\n")
    print(header)
    print("   " + "-" * len(header))

    for actual in languages:
        row = [f"{mapping.get((actual, predicted), 0):>2}" for predicted in languages]
        print(f"{actual} | {' | '.join(row)}")
    print("\n") 


def test():

# Test cases for Problem 1 and Problem 2.
# Floating-point results are considered correct within an absolute tolerance of 1e-5.
# Feel free to add more test cases here 
    cipher = """fukvuvu osyxhwuyxg wxhobsuv gxrxvbepxsy ucybsbpbck ewbixty povvobs xtc ybyuv tbky povvobs xtc
ylx xcwbexus gopxskobs luwpbsokosh bdixtyorxk kywctycwuv mcsgk xntlushosh osmbwpuyobs xnexwoxstx usg ogxuk tbvvudbwuyorx fbwa pbsoybwosh kbtouv euwysxwk v
xcwbexus tbppokkobs
xcwbexus gxtokobsk bs ylx opevxpxsyuyobs bmylx tbppbs kxtcwoyj usg gxmxstx ebvotj ostvcgosh ylbkx osoyouyosh u pokkobs uk wxmxwwxg yb os ylok uwyotvx kluvv dx ugbeyxg dj ylx tbcstov bm posokyxwk utyosh csusopbckvj bs u ewbebkuv mwbp ylx csobs posokyxw mbw mbwxohs ummuowk bw mwbp u pxpdxw kyuyx
oo yb xskcwx yluy ylx xcwbexus ewbebkuv vosxk mwupxk exw kxtbsg ewbhwxkkorx ktussosh ok ugbeyxg uk ylx koshvx fbwvg kyusg uwg
ylx pbwx xmmotoxsy ylx bexwuybwk osrbvrxg ylx pbwx xmmotoxsy ylx xcwbexus yxvxtbppcsotuyobsk puwaxy fovv dx
yuos ylx ybyuv ruvcx bm ylx wxkeowuyovx gcky tbstxsywuyobs mbw kextomoxg yopx osyxwruvk
oyv
dj vxyyxw guyxg puwtl gw gx gbposotok fuk osmbwpxg dj gh nro yluy ylx ewbixty bm ylx mbcsguyobs lug sby dxxs kxvxtyxg dxtuckx oy gog sby pxxy ylx ussbcstxg twoyxwou
bs yb sbrxpdxw os tbsicstyobs foyl ylx sxylxwvusgk posokywj bm lxuvyl usg ylx xsrowbspxsy ylx tbppokkobs lxvg us osyxwsuyobsuv tbsmxwxstx uy ylx luhcx bs tvxus yxtlsbvbhoxk bkuv yb ylx tbcstov tbstxwsosh u pcvyousscuv ewbhwuppx os ylx moxvg bm dobpbvxtcvuw xshosxxwosh osgowxty utyobs ylx xtbsbpot usg kbtouv tbppoyyxx pxxyosh bs usg sbrxpdxw gxvorxwxg us beosobs bs ylx tbppokkobs ewbebkuv yb ylx tbcstov tbstxwsosh cwusocp xnevbwuyobs usg xnywutyobs osgowxty utyobs
"""
    a = cliSSD(cipher, ["texts/sample_bg.txt", "texts/sample_de.txt", "texts/sample_el.txt", "texts/sample_en.txt", "texts/sample_es.txt", "texts/sample_fr.txt", "texts/sample_it.txt", "texts/sample_nl.txt", "texts/sample_pl.txt", "texts/sample_ru.txt"])
    assert a == {'texts/sample_bg.txt': 0.0008686304175672087, 'texts/sample_de.txt': 0.0030282241681359465, 'texts/sample_el.txt': 0.003900768672618399, 'texts/sample_en.txt': 0.0009685983479506998, 'texts/sample_es.txt': 0.0014847832596343855, 'texts/sample_fr.txt': 0.002342377137372695, 'texts/sample_it.txt': 0.0008613778129189986, 'texts/sample_nl.txt': 0.00658594015644843, 'texts/sample_pl.txt': 0.004795508346043341, 'texts/sample_ru.txt': 0.002884312599878665}

    b = cliDPD(cipher, ["texts/sample_bg.txt", "texts/sample_de.txt", "texts/sample_el.txt", "texts/sample_en.txt", "texts/sample_es.txt", "texts/sample_fr.txt", "texts/sample_it.txt", "texts/sample_nl.txt", "texts/sample_pl.txt", "texts/sample_ru.txt"])
    assert b == {'texts/sample_bg.txt': 0.03760706244775398, 'texts/sample_de.txt': 0.019627307148711397, 'texts/sample_el.txt': 0.010778849211054852, 'texts/sample_en.txt': 0.004254877302061767, 'texts/sample_es.txt': 0.017505446082276693, 'texts/sample_fr.txt': 0.0120039286951674, 'texts/sample_it.txt': 0.01241955510016762, 'texts/sample_nl.txt': 0.009751349385997449, 'texts/sample_pl.txt': 0.03375909319348446, 'texts/sample_ru.txt': 0.03334088648579243}

if __name__ == "__main__" and not flags.interactive:
    test()