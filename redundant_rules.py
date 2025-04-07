from sympy import symbols, And, Not, simplify_logic
from sympy.parsing.sympy_parser import parse_expr
from sympy.logic.inference import satisfiable


def get_all_variables(rules):
    import re
    var_set = set()
    for rule in rules:
        vars_in_rule = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', rule)
        var_set.update(vars_in_rule)
    return {v: symbols(v) for v in var_set}

def parse_rule(rule_str, vars_dict):
    rule_str = rule_str.split("=>")[0].strip()
    expr = rule_str.replace("AND", "&").replace("NOT", "~").replace("OR", "|")
    return simplify_logic(parse_expr(expr, local_dict=vars_dict, evaluate=False), form='dnf')

def has_duplicate_literals(expr):
    if isinstance(expr, And):
        literals = set()
        for arg in expr.args:
            if arg in literals:
                return True
            literals.add(arg)
    return False

def is_logically_redundant(expr1, expr2):
    test_expr = And(expr1, Not(expr2))
    return not satisfiable(test_expr)

def remove_all_redundant_rules(rules):
    vars_dict = get_all_variables(rules)
    parsed_rules = [parse_rule(r, vars_dict) for r in rules]
    
    keep_flags = [True] * len(rules)
    reasons = [""] * len(rules)

    for i in range(len(parsed_rules)):
        expr_i = parsed_rules[i]

        if has_duplicate_literals(expr_i):
            keep_flags[i] = False
            reasons[i] = "Duplicate literals"

        for j in range(len(parsed_rules)):
            if i != j and keep_flags[i]:
                if is_logically_redundant(expr_i, parsed_rules[j]):
                    keep_flags[i] = False
                    reasons[i] = f"Redundant (covered by rule {j + 1}: {rules[j]})"
                    break

    final_rules = []
    for i, keep in enumerate(keep_flags):
        if keep:
            final_rules.append(rules[i])
        else:
            print(f"Rule {i+1} removed: {rules[i]} — {reasons[i]}")

    return final_rules
