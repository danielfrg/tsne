Barnes-Hut-SNE v0.1
-------------------------------------------
© Laurens van der Maaten
Delft University of Technology, 2012
===========================================


DESCRIPTION

This code contains a C++ implementation of Barnes-Hut-SNE as described in the corresponding paper. Please cite this paper whenever you use this code.

The code also contains a Matlab wrapper for the C++ code (fast_tsne.m). Please refer to the help text in fast_tsne.m for more information on the input format for the data. Based on the code in fast_tsne.m, it is straightforward to develop wrappers in other programming languages.


COMPILATION

Compilation of the files is relatively straightforward, but requires a working installation of CBLAS. Please refer to the compile_mac and compile_linux shell scripts to see the required compilation command. Note that paths may be different on your machine, so may have to be changed in order for the files to compile.


LEGAL 

You are free to use, modify, or redistribute this software in any way you want, but only for non-commercial purposes. The use of the software is at your own risk; the authors are not responsible for any damage as a result from errors in the software. 


CONTACT
If you encounter problems with the implementations or have questions about Barnes-Hut-SNE, make sure you read the paper and the online FAQ first! If your question is not answered afterwards, feel free to send me an email at: lvdmaaten@gmail.com
