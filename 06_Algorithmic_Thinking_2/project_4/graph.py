import matplotlib.pyplot as plt

trials = [0, 0, 0, 0, 1, 2, 16, 20, 33, 51, 50, 59, 69, 72, 71, 68, 71, 46, 44, 32, 36, 33, 40, 25, 29, 20, 13, 11, 4, 11, 12, 10, 5, 1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
for idx in range(len(trials)):
    trials[idx] /= float(1000)

print trials

scores = [elem for elem in range(len(trials))]

for idx in range(len(scores)):
    scores[idx] += 35

width = 100

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
y = trials
N = len(y)
x = range(N)
width = 1/1.5


# plt.bar(trials, scores, width, color="blue")
plt.bar(scores, y, width, color="red")


plt.xlabel("Scores")
plt.ylabel("Trials")
plt.title("Hypothesis distribution (1000 trials)")
# plt.xscale('log')
# plt.yscale('log')
plt.legend(bbox_to_anchor=(0.4, 1), loc=2, borderaxespad=0.0)
plt.show()
