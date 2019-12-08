# Set the parameters
x0 = 2000
sigma = 0.17
S = 1500
lambda = l = 2
T = 1
a = c = -0.05
b = 0.03
K = 10000

estimator <- function(d){
  xt = numeric()
  zt = numeric()
  for (i in (1:K)){
    jumps = rpois(1,lambda)
    
    if (jumps == 0){
      xt[i] = x0 * exp(-0.5*sigma^2 + sigma*rnorm(1,mean=0,sd=1))
    }
    else{
    later = exp(rnorm(jumps,mean=c,sd=d))
    xt[i] = x0 * exp(-0.5*sigma^2 + sigma*rnorm(1,mean=0,sd=1)) * prod(later)
    }
    
    jumps_2 = rpois(1,l)
    if(jumps_2 == 0){
      zt[i] = 1
    }
    else{
      ln = rnorm(jumps_2,mean=c,sd=d)
      zt[i] = prod(dnorm(ln,mean=c,sd=d)/dnorm(ln,mean=a,sd=b))
    }
  }
  
  mt_vec = numeric()
  for (j in (1:K)){
    mt_vec[j] = max(S-xt[j],0)/zt[j]
  }
  mt = mean(mt_vec)
  return(mt)
}

true_option_price = 29.97
d_vec = seq(from=0.005,to=0.1,by=0.005)

estimator_vec = numeric()
mse_vec = numeric()
time_vec = numeric()
time2 = numeric()
eff = numeric()

for (i in (1:length(d_vec))){ 
   time = system.time(
   for (j in 1:500){
    estimator_vec[j] = estimator(d_vec[i])
   }
   )
  mse_vec[i] = mean( (estimator_vec - true_option_price)^2 ) 
  time_vec[i] = time[3]
  eff[i] = 1/(time_vec[i] * mse_vec[i])
}

plot(d_vec,eff,type = 'l',xlab = 'd', ylab = 'Computational Efficiency',col = 'blue'，)
plot(d_vec,mse_vec,type = 'l',xlab = 'd', ylab = 'MSE',col = 'red')