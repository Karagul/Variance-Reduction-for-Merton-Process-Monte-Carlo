# Variance-Reduction-for-Merton-Process-Monte-Carlo


Qianfan Wu, Advisor: Prof. Gustavo Schwenkler\
MS. Mathematical Finance, Boston University

The variance of a Monte-Carlo estimator is an important component of the computional efficiency. A high MC variance will negatively affect the robustness and precision of the estimation, especially when the input paramters tend to change drastically. In this project, we implemented an importance sampling variance reduction method on pricing European put options. Under the project setting, we assue the underlying seurity price follows a Merton Jump-Diffusion model. We used change of measures to change the frequency distributions of jumps in order to obtain MC samples for security dynamics. We also derived the distribution paramter value that miminized the Mean-Squared-Error and minimized the computational efficiency.
