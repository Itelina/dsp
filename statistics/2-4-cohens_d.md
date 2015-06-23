[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>First babies tend to be slightly lighter than other babies. The average weight of firstborn babies seen from this dataset is at 7.20 lbs while the average weight of other babies are 7.32. The Cohen d value for the difference is -0.0886. This is slightly more significant compared to the difference in pregnancy length, for which the Cohen d value is 0.02887.

>Codes attached below:

```
import math
import nsfg
import thinkstats2
import thinkplot

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

firsts_mean = firsts.totalwgt_lb.mean()
others_mean = others.totalwgt_lb.mean()

firsts_mean
others_mean

CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
CohenEffectSize(firsts.prglngth, others.prglngth)
```
