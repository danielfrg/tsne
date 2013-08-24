function mappedX = fast_tsne(X, initial_dims, perplexity, theta)
%FAST_TSNE Runs the (landmark) C++ implementation of t-SNE
%
%   mappedX = fast_tsne(X, initial_dims, perplexity, theta)
%
% Runs the C++ implementation of Barnes-Hut-SNE. The high-dimensional 
% datapoints are specified in the NxD matrix X. The dimensionality of the 
% datapoints is reduced to initial_dims dimensions using PCA (default = 50)
% before t-SNE is performed. Next, t-SNE reduces the points to two 
% dimensions. The perplexity of the input similarities may be specified
% through the perplexity variable (default = 30). The variable theta sets
% the trade-off parameter between speed and accuracy: theta = 0 corresponds
% to standard, slow t-SNE, while theta = 1 makes very crude approximations.
% Appropriate values for theta are between 0.1 and 0.7 (default = 0.5).
% The function returns the two-dimensional data points in mappedX.
%
% NOTE: The function is designed to run on large (N > 5000) data sets. It
% may give poor performance on very small data sets (it is better to use a
% standard t-SNE implementation on such data).
%
%
% (C) Laurens van der Maaten
% Delft University of Technology, 2012


    if ~exist('initial_dims', 'var') || isempty(initial_dims)
        initial_dims = 50;
    end
    if ~exist('perplexity', 'var')
        perplexity = 30;
    end
    if ~exist('theta', 'var')
        theta = 0.5;
    end
    
    % Perform the initial dimensionality reduction using PCA
    X = double(X);
    X = bsxfun(@minus, X, mean(X, 1));
    covX = X' * X;
    [M, lambda] = eig(covX);
    [~, ind] = sort(diag(lambda), 'descend');
    if initial_dims > size(M, 2)
        initial_dims = size(M, 2);
    end
	M = M(:,ind(1:initial_dims));
    X = X * M;
    clear covX M lambda
    
    % Run the fast diffusion SNE implementation
    write_data(X, theta, perplexity);
    tic, system('./bh_tsne'); toc
    [mappedX, landmarks, costs] = read_data;   
    landmarks = landmarks + 1;              % correct for Matlab indexing
    delete('data.dat');
    delete('result.dat');
end


% Writes the datafile for the fast t-SNE implementation
function write_data(X, theta, perplexity)
    [n, d] = size(X);
    h = fopen('data.dat', 'wb');
	fwrite(h, n, 'integer*4');
	fwrite(h, d, 'integer*4');
    fwrite(h, theta, 'double');
    fwrite(h, perplexity, 'double');
	fwrite(h, X', 'double');
	fclose(h);
end


% Reads the result file from the fast t-SNE implementation
function [X, landmarks, costs] = read_data
    h = fopen('result.dat', 'rb');
	n = fread(h, 1, 'integer*4');
	d = fread(h, 1, 'integer*4');
	X = fread(h, n * d, 'double');
    landmarks = fread(h, n, 'integer*4');
    landmarks = landmarks + 1;
    costs = fread(h, n, 'double');      % this vector contains only zeros
    X = reshape(X, [d n])';
	fclose(h);
end
