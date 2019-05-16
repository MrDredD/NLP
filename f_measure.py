def get_score(human_list, algo_list):
    tpr, fpr, fnr = 0, 0, 0
    for entry in algo_list:
        if entry in human_list:
            tpr += 1
        else:
            fpr += 1
    for entry in human_list:
        if entry not in algo_list:
            fnr += 1
    precision = tpr / (tpr + fpr)
    recall = tpr / (tpr + fnr)
    f_measure = 2 * precision * recall / (precision + recall)
    return precision, recall, f_measure
