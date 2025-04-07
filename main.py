from compress import compress


#====================================#
# Set compressing type and variables #
#====================================#

USE_SCORING = True
MAX_RULES = 10  # Remove all but MAX_RULES best rules based on scoring
REMOVE_REDUNDANT_RULES = True
PATH_TO_RULES = 'rules.txt'
PATH_TO_DATASET = 'dataset.tsv'
SAVE_RULES_TO_FILE = True   # True - Obvious / False - just print compressed rules
FILE_NAME = 'compressed_rules.txt'

rules = compress(PATH_TO_RULES, PATH_TO_DATASET, USE_SCORING, MAX_RULES, REMOVE_REDUNDANT_RULES)

match SAVE_RULES_TO_FILE:
    case True:
        with open(FILE_NAME, "w", encoding="utf-8") as output:
            for rule in rules:
                output.write(rule+'\n')
    case False:
        for rule in rules:
            print(rule)
    case _:
        raise Exception()