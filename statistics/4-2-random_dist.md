[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)
>Yes - the distribution is uniform, because the CDF graph is approximately a straight line, and the PMF graph shows equal distribution with the PMF of each value equal to 1/n (which is 0.001 in this case). 
>Code shown below:
```import random
sample = []
for i in range(1000):
    sample.append(random.random())
r_cdf = thinkstats2.Cdf(sample, label = "random")
r_pmf = thinkstats2.Pmf(sample, label = "random")
thinkplot.Cdf(r_cdf)
thinkplot.Show(xlabel='random numbers', ylabel='CDF')
thinkplot.Pmfs([r_pmf])
thinkplot.Show(xlabel='random numbers', ylabel='PMF')```
