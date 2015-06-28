[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

> The results show that the two variables are weakly correlated. Their Pearson correlation is 0.0636 and their Spearman's correlation is 0.0845.

```
'''Using data from the NSFG, make a scatter plot of birth weight versus mother’s age.'''
import nsfg
import thinkstats2
data = nsfg.ReadFemPreg()
sample = thinkstats2.SampleRows(data, 5000)
motherage, birthweight = sample.agepreg, sample.totalwgt_lb
thinkplot.Scatter(motherage, birthweight, alpha=0.2)
thinkplot.Show(xlabel='Mother Age',
               ylabel='Birth Weight')

'''Plot percentiles of birth weight versus mother’s age. '''
sp = sample.dropna(subset=['agepreg', 'totalwgt_lb'])
bins = np.arange(10, 45, 2)
indices = np.digitize(sp.agepreg, bins)
groups = sp.groupby(indices)

motheragegroup = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

for percent in [75, 50, 25]:
    birthweights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(motheragegroup, birthweights, label=label)
thinkplot.Show(xlabel='Mother Age', ylabel='Birth Weight')

'''Compute Pearson’s and Spearman’s correlations. How would you characterize the relationship between these variables?'''
motherage, birthweight = sp.agepreg, sp.totalwgt_lb
thinkstats2.Corr(motherage, birthweight)
thinkstats2.SpearmanCorr(motherage, birthweight)
```
