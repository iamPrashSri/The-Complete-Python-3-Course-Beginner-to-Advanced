import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = 0.2

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)
k1 = plt.bar(index, korea_scores, bar_width, alpha=0.4, label='Korea')
c1 = plt.bar(index + bar_width, canada_scores, bar_width, alpha=0.4, label='Canada')
ch1 = plt.bar(index + 2*bar_width, china_scores, bar_width, alpha=0.4, label='China')
f1 = plt.bar(index + 3*bar_width, france_scores, bar_width, alpha=0.4, label='France')

def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2, height * 1.05,
                 "%d" % int(height), ha='center', va='bottom')

createLabels(k1)
createLabels(c1)
createLabels(ch1)
createLabels(f1)

plt.xlabel('Subjects')
plt.ylabel('Mean Scores in each subject')
plt.title('Test Scores by Country')

plt.xticks(index + 0.6/2, ('Mathematics', 'Reading', 'Science'))
# plt.legend(edgecolor=None, shadow=False, facecolor=(1, .4, .4))
plt.legend(frameon=False, bbox_to_anchor=(1, 1), loc=2)
plt.grid(True)
plt.show()