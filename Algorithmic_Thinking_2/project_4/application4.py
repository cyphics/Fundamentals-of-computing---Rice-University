""" Application 4 """

DESKTOP = True

import math
import random
import provided


if DESKTOP:
    import matplotlib.pyplot as plt
    import project_4 as student
else:
    import simpleplot
    import userXX_XXXXXXX as student


# URLs for data files
PAM50_URL = "alg_PAM50.txt"
HUMAN_EYELESS_URL = "alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "assets_scrabble_words3.txt"


def compute_alignment(seq_x, seq_y, score_matrix, global_flag):
    """ Sythetic function that computes alignment matrix,
    local/global alignment of sequences  and returns
    correspondant sequences, with its score """
    alignment_matrix = student.compute_alignment_matrix(seq_x, seq_y, score_matrix, global_flag)
    if global_flag:
        return student.compute_global_alignment(seq_x, seq_y, score_matrix, alignment_matrix)
    else:
        return student.compute_local_alignment(seq_x, seq_y, score_matrix, alignment_matrix)

# Load data
human_protein = provided.read_protein(HUMAN_EYELESS_URL)
fruitfly_protein = provided.read_protein(FRUITFLY_EYELESS_URL)
pam50 = provided.read_scoring_matrix(PAM50_URL)
consensus_pax_domain = provided.read_protein(CONSENSUS_PAX_URL)

# Question 1
print "QUESTION 1"
print "Given the two provided sequences, what are their global alignment, and the correspondant score?"
local_alignment_hum_fly = compute_alignment(human_protein, fruitfly_protein, pam50, False)
print "Local algnment between human and fruitfly protein gives:"
print "Human sequence:", local_alignment_hum_fly[1]
print
print "Fly sequence:", local_alignment_hum_fly[2]
print
print "Score:", local_alignment_hum_fly[0]
print
print

##############
# QUESTION 2 #
##############
print "QUESTION 2"
# Delete dashes in sequences
human_local = "HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEKQQ"


global_human_consensus = compute_alignment(human_local, consensus_pax_domain, pam50, True)
global_fly_consensus = compute_alignment(local_alignment_hum_fly[2], consensus_pax_domain, pam50, True)

# Compute first percentage
length = len(global_human_consensus[1])
counter = 0
for idx in range(length):
    if global_human_consensus[1][idx] == global_human_consensus[2][idx]:
        counter += 1

delta = length - counter
decrease = (delta / float(length)) * 100
similitudes = 100 - decrease
print similitudes

# Compute second percentage
length = len(global_fly_consensus[1])
counter = 0
for idx in range(length):
    if global_fly_consensus[1][idx] == global_fly_consensus[2][idx]:
        counter += 1

delta = length - counter
decrease = (delta / float(len(global_fly_consensus[1]))) * 100
similitudes = 100 - decrease
print similitudes

##############
# QUESTION 4 #
##############
print "Question 4"


def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    result = {}
    for idx in range(30, 100):
        result[idx] = 0
    first_sequence = str(seq_x)
    increment = 0
    while increment < num_trials:
        temp_list = list(seq_y)
        random.shuffle(temp_list)
        second_sequence = ''.join(temp_list)
        score = compute_alignment(first_sequence, second_sequence, scoring_matrix, False)[0]
        result[score] += 1
        increment += 1
    return result


number_trials = 10
print "Computation takes time. Please wait, or try a lower trials value"
result = generate_null_distribution(human_protein, fruitfly_protein, pam50, number_trials)
for key in result:
    result[key] /= float(number_trials)
scores = []
trials = []


plt.bar(range(len(result)), result.values(), width=(0.3), align='center')
plt.xticks(range(len(result)), result.keys())

plt.xlabel("Scores")
plt.ylabel("Normalized trials")
plt.title("Hypothesis distribution (1000 trials)")
plt.legend(bbox_to_anchor=(0.4, 1), loc=2, borderaxespad=0.0)
plt.show()


# QUESTION 5
