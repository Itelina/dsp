[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

> Roughly 34.2% of the US population of male is within the height range specified by the Blue Man Group (5'10" to 6'1"). Calculation code  below:

```
import scipy.stats
scipy.stats.norm.cdf(0)
'''5'11" is 177.8cm. 6'1" is 185.4cm.'''
scipy.stats.norm.cdf(185.4, loc=178, scale=7.7) - scipy.stats.norm.cdf(177.8, loc=178, scale=7.7)
```
