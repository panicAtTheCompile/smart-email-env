def grade_classification(pred, gt):
    return 1.0 if pred.lower() == gt.lower() else 0.0


def grade_extraction(pred: str, gt: dict):
    score = 0
    if gt["date"].lower() in pred.lower():
        score += 0.5
    if gt["priority"].lower() in pred.lower():
        score += 0.5
    return score


def grade_response(pred: str):
    score = 0
    if "sorry" in pred.lower():
        score += 0.5
    if "refund" in pred.lower():
        score += 0.5
    return score