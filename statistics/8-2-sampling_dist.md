[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

> The standard error of the estimate is 0.7382 and the 90% confidence interval is 1.4262 and 3.0708. 
> Code attached below:

```
'''Suppose you draw a sample with size n=10 from an exponential distribution with λ=2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L.'''
def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def MeanError(estimates, actual):
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)

def Estimate3(n=7, m=1000):
    lam = 2

    means = []
    medians = []
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        Lm = math.log(2) / thinkstats2.Median(xs)
        means.append(L)
        medians.append(Lm)

    #print('rmse L', RMSE(means, lam))
    #print('rmse Lm', RMSE(medians, lam))
    #print('mean error L', MeanError(means, lam))
    #print('mean error Lm', MeanError(medians, lam))
    
    return means

estimates = Estimate3(n=10, m=1000)
cdf = thinkstats2.Cdf(estimates)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='estimator', ylabel='CDF')

'''Compute the standard error of the estimate and the 90% confidence interval.'''

RMSE(estimates, 2)

ci = cdf.Percentile(10), cdf.Percentile(90)
print('confidence interval', ci)

'''Repeat the experiment with a few different values of n and make a plot of standard error versus n.'''

def Estimate4(n=7, m=1000):
    lam = 2

    means = []
    #medians = []
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        #Lm = math.log(2) / thinkstats2.Median(xs)
        means.append(L)
        #medians.append(Lm)

    #print('rmse L', RMSE(means, lam))
    #print('rmse Lm', RMSE(medians, lam))
    #print('mean error L', MeanError(means, lam))
    #print('mean error Lm', MeanError(medians, lam))
    return RMSE(means, lam)

nvalues = range(2, 20)
RMSEs= []
for value in nvalues:
    a = Estimate4(value, 1000)
    RMSEs.append(a)

thinkplot.Plot(nvalues, RMSEs)
thinkplot.Show(xlabel='n', ylabel='RMSEs')
'''
