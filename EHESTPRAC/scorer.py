def score(choices, num_questions):
    max_score = 2 * num_questions
    caution_boundary = max_score * 0.2
    high_risk_boundary = max_score * 0.4
    
    total_score = 0
    for scores in choices.values():
        total_score += int(scores)

    if total_score < caution_boundary:
        risk = "Acceptable risk"
    elif total_score < high_risk_boundary:
        risk = "Caution"
    else:
        risk = "High risk"

    sub_d_close = 50 * total_score / max_score
    sub_d_rounded = sub_d_close - sub_d_close % 1
    nearest_sub_d = sub_d_rounded / 50
    risk_numeric = max_score * (nearest_sub_d ** 2) + 5

    risk_numeric_as_percentage = (risk_numeric - 5) / max_score * 95 + 5


    return risk, total_score, risk_numeric, risk_numeric_as_percentage