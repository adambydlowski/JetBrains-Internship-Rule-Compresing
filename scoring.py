# -*- coding: utf-8 -*-
import pandas as pd


def cut_by_score(rules, dataset, max_rules):
    ranking = {}
    for rule in rules:
        print(rule)
        tokens = rule.split(" ")
        tokens = tokens[:tokens.index("=>")]
        condition = ""
        mask = ""
        for token in tokens:
            match token:
                case "AND":
                    condition += " & "
                case "NOT":
                    condition += " ~"
                case _:
                    condition += f"dataset['{token}']"
                    mask += f" & dataset['{token}'].notna()"
        mask = "condition" + mask
        condition = eval(condition)
        mask = eval(mask)

        support = mask.sum() / len(dataset)

        confidence = dataset.loc[mask, 'donor_is_old'].mean()

        base_rate = dataset['donor_is_old'].mean()
        lift = confidence / base_rate if base_rate > 0 else None


        length_penalty = 1 / rule_length(rule)

        ranking[rule] = support * lift * confidence * length_penalty
    
    return dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True)[:max_rules])



def rule_length(rule_str):
    return len(rule_str.replace("NOT", "").split("AND"))

