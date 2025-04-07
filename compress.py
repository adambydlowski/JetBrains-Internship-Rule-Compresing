from redundant_rules import *
from scoring import *


def compress(PATH_TO_RULES, PATH_TO_DATASET, USE_SCORING, MAX_RULES, REMOVE_REDUNDANT_RULES):
    compressed_rules = []
    
    with open(PATH_TO_RULES, "r", encoding="utf-8") as file:
        for i in file:
            compressed_rules.append(i.strip())

    if REMOVE_REDUNDANT_RULES:

        compressed_rules = remove_all_redundant_rules(compressed_rules)

    if USE_SCORING:
        dataset = pd.read_csv(PATH_TO_DATASET, sep="\t", encoding="utf-8")
        dataset = dataset.astype(bool)
        compressed_rules = cut_by_score(compressed_rules, dataset, MAX_RULES)
    
    return compressed_rules


