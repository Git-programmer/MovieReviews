fprintf('Recommender system \n');

#Computes cost function
function [J, grad] = cofiCostFunc(params, Y, R, num_users, num_movies, ...
                                  num_features, lambda)

X = reshape(params(1:num_movies*num_features), num_movies, num_features);
Theta = reshape(params(num_movies*num_features+1:end), num_users, num_features);


J = 0;
X_grad = zeros(size(X));
Theta_grad = zeros(size(Theta));

M=R.*((X*Theta')'-Y);
J=sum(sum((0.5)*R.*M.^2))+(0.5)*lambda*sum(sum(X.^2))+(0.5)*lambda*sum(sum(Theta.^2));

#size(M) ,size(Theta), size(X)
X_grad=M'*Theta+lambda*X;
Theta_grad=M*X+lambda*Theta;


grad = [X_grad(:); Theta_grad(:)];

end

#Reads in Y,R where Y(i,j) is the rating of the ith movie by the jth person and R is indicating wether he watched it.
Y=csvread('YMatlab.csv',[0,0,1,4]);
R=csvread('RMatlab.csv',[0,0,1,4]);


[num_users,num_movies]=size(Y)

num_features=1

X = randn(num_movies, num_features);
Theta = randn(num_users, num_features);
lambda=1;

#[J, grad]=cofiCostFunc([X(:);Theta(:)]	, Y, R, num_users, num_movies, num_features, lambda)

initial_parameters = [X(:); Theta(:)];

% Set options for fmincg
options = optimset('GradObj', 'on', 'MaxIter', 100);

% Set Regularization
lambda = 0;
theta = fmincg (@(t)(cofiCostFunc(t, Y, R, num_users, num_movies, ...
                                num_features, lambda)), ...
                initial_parameters, options);

% Unfold the returned theta back into U and W
X = reshape(theta(1:num_movies*num_features), num_movies, num_features);			
Theta = reshape(theta(num_movies*num_features+1:end), ...
                num_users, num_features);

(Theta*X'-Y)
Y
R

