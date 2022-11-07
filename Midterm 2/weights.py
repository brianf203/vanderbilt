def normalize_weight(weight_list):
    new_weights = []
    max_weight = 0
    for weight in weight_list:
        if weight > max_weight:
            max_weight = weight
    for i in range(len(weight_list)):
        new_weights.append(float(f'{weight_list[i] / max_weight:.2f}'))
    return new_weights
    
patient_weights = [100, 200, 150, 100.5, 130.2]
normed_weights = normalize_weight(patient_weights)
print("Given weight list:\n\n" + str(patient_weights) + "\n\nNormalized weight list:\n\n" + str(normed_weights))
