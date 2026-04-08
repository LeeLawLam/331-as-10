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
    ciphertext = ciphertext.upper()

    cipher_counts = {}
    cipher_total = 0

    for ch in ciphertext:
        if ch.isalpha():
            cipher_total += 1
            if ch in cipher_counts:
                cipher_counts[ch] += 1
            else:
                cipher_counts[ch] = 1

    cipher_ssd = []
    for ch in cipher_counts:
        cipher_ssd.append(cipher_counts[ch] / cipher_total)

    cipher_ssd.sort(reverse=True)

    distances = {}

    for path in files:
        with open(path, encoding="utf8") as f:
            sample = f.read().upper()

        sample_counts = {}
        sample_total = 0

        for ch in sample:
            if ch.isalpha():
                sample_total += 1
                if ch in sample_counts:
                    sample_counts[ch] += 1
                else:
                    sample_counts[ch] = 1

        sample_ssd = []
        for ch in sample_counts:
            sample_ssd.append(sample_counts[ch] / sample_total)

        sample_ssd.sort(reverse=True)

        max_len = max(len(cipher_ssd), len(sample_ssd))
        distance = 0.0

        for i in range(max_len):
            cipher_prob = 0.0
            sample_prob = 0.0

            if i < len(cipher_ssd):
                cipher_prob = cipher_ssd[i]
            if i < len(sample_ssd):
                sample_prob = sample_ssd[i]

            distance += (cipher_prob - sample_prob) ** 2

        distances[path] = distance

    return distances

def cliDPD(ciphertext: str, files):
    """
    Args:
        ciphertext (str)
        files (list of str)
    Returns:
        dict
    """
    ciphertext = ciphertext.upper()

    cipher_words = []
    word = ""

    for ch in ciphertext:
        if ch.isalpha():
            word += ch
        else:
            if word != "":
                cipher_words.append(word)
                word = ""

    if word != "":
        cipher_words.append(word)

    cipher_pattern_counts = {}
    for word in cipher_words:
        letter_counts = {}
        for ch in word:
            if ch in letter_counts:
                letter_counts[ch] += 1
            else:
                letter_counts[ch] = 1

        pattern_list = []
        for ch in letter_counts:
            pattern_list.append(letter_counts[ch])

        pattern_list.sort(reverse=True)
        pattern = tuple(pattern_list)

        if pattern in cipher_pattern_counts:
            cipher_pattern_counts[pattern] += 1
        else:
            cipher_pattern_counts[pattern] = 1

    cipher_dpd = {}
    total_cipher_words = len(cipher_words)

    for pattern in cipher_pattern_counts:
        cipher_dpd[pattern] = cipher_pattern_counts[pattern] / total_cipher_words

    distances = {}

    for path in files:
        with open(path, encoding="utf8") as f:
            sample = f.read().upper()

        sample_words = []
        word = ""

        for ch in sample:
            if ch.isalpha():
                word += ch
            else:
                if word != "":
                    sample_words.append(word)
                    word = ""

        if word != "":
            sample_words.append(word)

        sample_pattern_counts = {}
        for word in sample_words:
            letter_counts = {}
            for ch in word:
                if ch in letter_counts:
                    letter_counts[ch] += 1
                else:
                    letter_counts[ch] = 1

            pattern_list = []
            for ch in letter_counts:
                pattern_list.append(letter_counts[ch])

            pattern_list.sort(reverse=True)
            pattern = tuple(pattern_list)

            if pattern in sample_pattern_counts:
                sample_pattern_counts[pattern] += 1
            else:
                sample_pattern_counts[pattern] = 1

        sample_dpd = {}
        total_sample_words = len(sample_words)

        for pattern in sample_pattern_counts:
            sample_dpd[pattern] = sample_pattern_counts[pattern] / total_sample_words

        all_patterns = sorted(set(cipher_dpd.keys()) | set(sample_dpd.keys()))
        distance = 0.0

        for pattern in all_patterns:
            cipher_prob = 0.0
            sample_prob = 0.0

            if pattern in cipher_dpd:
                cipher_prob = cipher_dpd[pattern]
            if pattern in sample_dpd:
                sample_prob = sample_dpd[pattern]

            distance += (cipher_prob - sample_prob) ** 2

        distances[path] = distance

    return distances

def cliSSDTest(ciphertext_files, sampletext_files):
    """
    Args:
        ciphertext_files (list of str)
        sampletext_files (list of str)
    Returns:
        dict
    """
    results = {}

    for cipher_path in ciphertext_files:
        with open(cipher_path, encoding="utf8") as f:
            ciphertext = f.read()

        distances = cliSSD(ciphertext, sampletext_files)

        best_sample = None
        best_distance = None

        for sample_path in distances:
            if best_distance is None or distances[sample_path] < best_distance:
                best_distance = distances[sample_path]
                best_sample = sample_path

        results[cipher_path] = best_sample

    return results

def cliDPDTest(ciphertext_files, sampletext_files):
    """
    Args:
        ciphertext_files (list of str)
        sampletext_files (list of str)
    Returns:
        dict
    """
    results = {}

    for cipher_path in ciphertext_files:
        with open(cipher_path, encoding="utf8") as f:
            ciphertext = f.read()

        distances = cliDPD(ciphertext, sampletext_files)

        best_sample = None
        best_distance = None

        for sample_path in distances:
            if best_distance is None or distances[sample_path] < best_distance:
                best_distance = distances[sample_path]
                best_sample = sample_path

        results[cipher_path] = best_sample

    return results

def generateMapping(dictionary: dict):
    """
    Args:
        dictionary (return value of cliSSDTest or cliDPDTest)
    Returns:
        A classification mapping (dict) of the ciphertexts.
        Please refer to the assignment instructions for the required format.
    """
    mapping = {}

    for cipher_path in dictionary:
        sample_path = dictionary[cipher_path]

        cipher_name = cipher_path.split("/")[-1]
        sample_name = sample_path.split("/")[-1]

        actual_language = cipher_name.split("_")[1]
        predicted_language = sample_name.split("_")[1].split(".")[0]

        key = (actual_language, predicted_language)

        if key in mapping:
            mapping[key] += 1
        else:
            mapping[key] = 1

    return mapping

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
#     cipher = """fukvuvu osyxhwuyxg wxhobsuv gxrxvbepxsy ucybsbpbck ewbixty povvobs xtc ybyuv tbky povvobs xtc
# ylx xcwbexus gopxskobs luwpbsokosh bdixtyorxk kywctycwuv mcsgk xntlushosh osmbwpuyobs xnexwoxstx usg ogxuk tbvvudbwuyorx fbwa pbsoybwosh kbtouv euwysxwk v
# xcwbexus tbppokkobs
# xcwbexus gxtokobsk bs ylx opevxpxsyuyobs bmylx tbppbs kxtcwoyj usg gxmxstx ebvotj ostvcgosh ylbkx osoyouyosh u pokkobs uk wxmxwwxg yb os ylok uwyotvx kluvv dx ugbeyxg dj ylx tbcstov bm posokyxwk utyosh csusopbckvj bs u ewbebkuv mwbp ylx csobs posokyxw mbw mbwxohs ummuowk bw mwbp u pxpdxw kyuyx
# oo yb xskcwx yluy ylx xcwbexus ewbebkuv vosxk mwupxk exw kxtbsg ewbhwxkkorx ktussosh ok ugbeyxg uk ylx koshvx fbwvg kyusg uwg
# ylx pbwx xmmotoxsy ylx bexwuybwk osrbvrxg ylx pbwx xmmotoxsy ylx xcwbexus yxvxtbppcsotuyobsk puwaxy fovv dx
# yuos ylx ybyuv ruvcx bm ylx wxkeowuyovx gcky tbstxsywuyobs mbw kextomoxg yopx osyxwruvk
# oyv
# dj vxyyxw guyxg puwtl gw gx gbposotok fuk osmbwpxg dj gh nro yluy ylx ewbixty bm ylx mbcsguyobs lug sby dxxs kxvxtyxg dxtuckx oy gog sby pxxy ylx ussbcstxg twoyxwou
# bs yb sbrxpdxw os tbsicstyobs foyl ylx sxylxwvusgk posokywj bm lxuvyl usg ylx xsrowbspxsy ylx tbppokkobs lxvg us osyxwsuyobsuv tbsmxwxstx uy ylx luhcx bs tvxus yxtlsbvbhoxk bkuv yb ylx tbcstov tbstxwsosh u pcvyousscuv ewbhwuppx os ylx moxvg bm dobpbvxtcvuw xshosxxwosh osgowxty utyobs ylx xtbsbpot usg kbtouv tbppoyyxx pxxyosh bs usg sbrxpdxw gxvorxwxg us beosobs bs ylx tbppokkobs ewbebkuv yb ylx tbcstov tbstxwsosh cwusocp xnevbwuyobs usg xnywutyobs osgowxty utyobs
# """
    # a = cliSSD(cipher, ["texts/sample_bg.txt", "texts/sample_de.txt", "texts/sample_el.txt", "texts/sample_en.txt", "texts/sample_es.txt", "texts/sample_fr.txt", "texts/sample_it.txt", "texts/sample_nl.txt", "texts/sample_pl.txt", "texts/sample_ru.txt"])
    # assert a == {'texts/sample_bg.txt': 0.0008686304175672087, 'texts/sample_de.txt': 0.0030282241681359465, 'texts/sample_el.txt': 0.003900768672618399, 'texts/sample_en.txt': 0.0009685983479506998, 'texts/sample_es.txt': 0.0014847832596343855, 'texts/sample_fr.txt': 0.002342377137372695, 'texts/sample_it.txt': 0.0008613778129189986, 'texts/sample_nl.txt': 0.00658594015644843, 'texts/sample_pl.txt': 0.004795508346043341, 'texts/sample_ru.txt': 0.002884312599878665}

    # b = cliDPD(cipher, ["texts/sample_bg.txt", "texts/sample_de.txt", "texts/sample_el.txt", "texts/sample_en.txt", "texts/sample_es.txt", "texts/sample_fr.txt", "texts/sample_it.txt", "texts/sample_nl.txt", "texts/sample_pl.txt", "texts/sample_ru.txt"])
    # assert b == {'texts/sample_bg.txt': 0.03760706244775398, 'texts/sample_de.txt': 0.019627307148711397, 'texts/sample_el.txt': 0.010778849211054852, 'texts/sample_en.txt': 0.004254877302061767, 'texts/sample_es.txt': 0.017505446082276693, 'texts/sample_fr.txt': 0.0120039286951674, 'texts/sample_it.txt': 0.01241955510016762, 'texts/sample_nl.txt': 0.009751349385997449, 'texts/sample_pl.txt': 0.03375909319348446, 'texts/sample_ru.txt': 0.03334088648579243}
    
    import glob

    ciphertext_files = sorted(glob.glob("texts/ciphertext_*.txt"))
    sampletext_files = sorted(glob.glob("texts/sample_*.txt"))

    ssd_results = cliSSDTest(ciphertext_files, sampletext_files)
    dpd_results = cliDPDTest(ciphertext_files, sampletext_files)

    print("SSD confusion matrix:")
    generateMatrix(generateMapping(ssd_results))

    print("DPD confusion matrix:")
    generateMatrix(generateMapping(dpd_results))

if __name__ == "__main__" and not flags.interactive:
    test()