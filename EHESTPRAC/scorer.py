def score(num_questions, data):
    max_score = 2 * num_questions
    caution_boundary = max_score * 0.2
    high_risk_boundary = max_score * 0.4
    
    total_score = 0
    mitigated_score = 0
    for scores in data.values():
        total_score += int(scores['ChoiceScore'])
        if scores.get('MitigationScore') and scores.get('MitigationText') and (int(scores['ChoiceScore']) > int(scores.get('MitigationScore'))):
            mitigated_score += int(scores['MitigationScore'])
        else:
            mitigated_score += int(scores['ChoiceScore'])
            scores['MitigationScore'] = scores['ChoiceScore']
            scores['MitigationText'] = ""

    if mitigated_score < caution_boundary:
        risk = "Acceptable Risk"
    elif mitigated_score < high_risk_boundary:
        risk = "Caution"
    else:
        risk = "High Risk"

    sub_d_close_mitigated = 50 * mitigated_score / max_score
    sub_d_rounded_mitigated = sub_d_close_mitigated - sub_d_close_mitigated % 1
    nearest_sub_d_mitigated = sub_d_rounded_mitigated / 50
    risk_numeric_mitigated = round(max_score * (nearest_sub_d_mitigated ** 2) + 5, 2)
    risk_numeric_as_percentage_mitigated = round(sub_d_close_mitigated * 2, 2)

    sub_d_close = 50 * total_score / max_score
    sub_d_rounded = sub_d_close - sub_d_close % 1
    nearest_sub_d = sub_d_rounded / 50
    risk_numeric = round(max_score * (nearest_sub_d ** 2) + 5, 2)
    risk_numeric_as_percentage = round(sub_d_close * 2, 2)


    return risk, total_score, mitigated_score, risk_numeric, risk_numeric_as_percentage, risk_numeric_mitigated, risk_numeric_as_percentage_mitigated, data