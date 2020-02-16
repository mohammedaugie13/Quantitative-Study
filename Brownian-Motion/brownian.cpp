#include <iostream>
#include <armadillo>
#include <math.h>
int main()
{
    const int paths = 5;
    const int steps = 1000;

    const double mu  = 0.2;
    const double sig = 0.312;
    
    const int T = 10;
    const float dt = 0.01;


    arma::vec T_vec = arma::linspace(0, T, 1000);
    arma::mat norma_dist = arma::randn(paths, steps );
    arma::mat increments = mu * dt + sig * sqrt(dt) * norma_dist;
    arma::mat X = cumsum(increments, 1);
    arma::mat result = trans(X) ; 
    arma::mat plot = arma::join_rows(T_vec, result);
    plot.save("plot.dat", arma::raw_ascii);
    return 0;
}
