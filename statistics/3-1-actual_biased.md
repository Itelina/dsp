[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

> The unbiased mean number of children under age 18 is 1.02. The biased mean number of children under age 18 is 2.40. 
> Code below shows the calculations. 

```
"""Reading in and storing the data file"""
def ReadFile(dct_file='2002FemPreg.dct', dat_file='2002FemPreg.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df
FemResp = ReadFile(dct_file='2002FemResp.dct', dat_file = "2002FemResp.dat.gz")

"""Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household."""
NK_pmf = thinkstats2.Pmf(FemResp.numkdhh, label = 'Actual')
NK_pmf

"""Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household."""
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
NK_Bpmf = BiasPmf(NK_pmf, label = 'Biased')
NK_Bpmf

"""Plot the actual and biased distributions, and compute their means."""
thinkplot.PrePlot(2)
thinkplot.Pmfs([NK_pmf, NK_Bpmf])
thinkplot.Show(xlabel='Total Children', ylabel='PMF')

UnBiasedMean = NK_pmf.Mean()
BiasedMean = NK_Bpmf.Mean()
UnBiasedMean
BiasedMean

```
