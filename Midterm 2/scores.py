import numpy as np

scores_list = [[90, 92, 85.2, 76, 89, 91, 54], [23, 45.5, 76.4, 82.3, 59.5, 89, 90], [72, 69, 80.5, 52, 44, 87, 56], [67.6, 60, 100, 99, 90, 91, 66]]
scores = np.array(scores_list)

f_count = 0
for i in scores:
    for score in i:
        if score < 60:
            f_count += 1

percent_f = f_count / np.size(scores_list) * 100
print("The percentage of unsatisfactory scores in this dataset is: {:.0f}%".format(percent_f))
