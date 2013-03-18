import gzip, cPickle
import numpy as np
import matplotlib.pyplot as plt


from py_bh_tsne import fast_tsne


f = gzip.open("mnist.pkl.gz", "rb")
train, val, test = cPickle.load(f)
f.close()

# Get all data in one array
_train = np.asarray(train[0], dtype=np.float64)
_val = np.asarray(val[0], dtype=np.float64)
_test = np.asarray(test[0], dtype = np.float64)
mnist = np.vstack((_train, _val, _test))

# Also the classes, for labels in the plot later
classes = np.hstack((train[1], val[1], test[1]))

perplexity = 30.
theta = 0.5
Y = fast_tsne(mnist, perplexity=perplexity, theta=theta)

digits = set(classes)
fig = plt.figure()
colormap = plt.cm.spectral
plt.gca().set_color_cycle(colormap(i) for i in np.linspace(0, 0.9, 10))
ax = fig.add_subplot(111)
labels = []
for d in digits:
    idx = classes==d
    ax.plot(Y[idx, 0], Y[idx, 1], 'o')
    labels.append(d)
ax.legend(labels, numpoints=1, fancybox=True)
plt.show()
