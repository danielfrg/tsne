# distutils: language = c++
import numpy as np
cimport numpy as np
cimport cython

cdef extern from "tsne.h":
    cdef cppclass TSNE:
        TSNE()
        void run(double* X, int N, int D, double* Y, int no_dims, double perplexity, double theta, unsigned int seed, unsigned int miter, unsigned int sliter, unsigned int msiter, double m, double fm)


cdef class BH_SNE:
    cdef TSNE* thisptr # hold a C++ instance

    def __cinit__(self):
        self.thisptr = new TSNE()

    def __dealloc__(self):
        del self.thisptr

    @cython.boundscheck(False)
    @cython.wraparound(False)
    def run(self, X, N, D, d, perplexity, theta, seed, miter, sliter, msiter, m, fm):
        cdef np.ndarray[np.float64_t, ndim=2, mode='c'] _X = np.ascontiguousarray(X)
        cdef np.ndarray[np.float64_t, ndim=2, mode='c'] Y = np.zeros((N, d), dtype=np.float64)
        self.thisptr.run(&_X[0,0], N, D, &Y[0,0], d, perplexity, theta, seed, miter, sliter, msiter, m, fm)
        return Y
