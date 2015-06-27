[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

> When setting 6.0 as the upper bound (when we assume that highest income is 10^6 or 1 million dollars), these are the values for sample:

> Mean: 74,278
> Median: 51,226
> Skewness: 4.9499
> Pearson's Skewness: 0.7361

> 66.0% of the households report a taxable income below the mean. 

> When we adjust the upper bound to 8.0 instead, these are the values:

> Mean: 457,453
> Median: 51,226
> Skewness: 14.8924
> Pearson's Skewness: 0.2747

> 97.8% of the households report a taxable income below the mean. 

> We can see that when we adjusted the upper bound, the Pearson's Skewness went down instead. This is because adjusting the upper bound probably has a strong effect on the standard deviation. 

```
import hinc2
import hinc
import numpy as np

'''Compute the median, mean, skewness and Pearson’s skewness of the resulting sample. What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?'''

def RawMoment(xs, k):
    return sum(x**k for x in xs) / len(xs)

def CentralMoment(xs, k):
    mean = RawMoment(xs, 1)
    return sum((x - mean)**k for x in xs) / len(xs)

def StandardizedMoment(xs, k):
    var = CentralMoment(xs, 2)
    std = math.sqrt(var)
    return CentralMoment(xs, k) / std**k

def Median(xs):
    cdf = thinkstats2.Cdf(xs)
    return cdf.Value(0.5)

def Skewness(xs):
    return StandardizedMoment(xs, 3)

def PearsonMedianSkewness(xs):
    median = Median(xs)
    mean = RawMoment(xs, 1)
    var = CentralMoment(xs, 2)
    std = math.sqrt(var)
    gp = 3 * (mean - median) / std
    return gp

df = hinc.ReadData()
log_sample = hinc2.InterpolateSample(df, log_upper=8.0)
  
mean = np.mean(log_sample)
mean

Median(log_sample)
Skewness(log_sample)
PearsonMedianSkewness(log_sample)

cdf = thinkstats2.Cdf(log_sample)
cdf.Prob(mean)

```
