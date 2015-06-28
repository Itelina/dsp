# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

In games like hockey and soccer, the time between goals is roughly exponential. So you could estimate a team’s goal-scoring rate by observing the number of goals they score in a game. This estimation process is a little different from sampling the time between goals, so let’s see how it works.
Write a function that takes a goal-scoring rate, lam, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.
```
def GoalEstimates(lam=2):
    playtime = 0
    goals = 0
    while playtime <= 1:
        time = random.expovariate(lam)
        playtime += time
        goals += 1
    return goals
```
    
Write another function that simulates many games, stores the estimates of lam, then computes their mean error and RMSE. Is this way of making an estimate biased? Plot the sampling distribution of the estimates and the 90% confidence interval. What is the standard error? What happens to sampling error for increasing values of lam?

```
def GameEstimates(lam=2, m=100):
    Scores =[]
    for i in range(m):
        goals = GoalEstimates()
        Scores.append(goals)
    print(Scores)
    print('RMSE L', RMSE(Scores, lam))
    print('Mean Error L', MeanError(Scores, lam))
    
    #pmf = thinkstats2.Pmf(Scores)
    #thinkplot.Hist(pmf)
    #thinkplot.Show(xlabel='Estimated Scores', ylabel='Frequency')
    
    cdf = thinkstats2.Cdf(estimates)
    #thinkplot.Cdf(cdf)
    #thinkplot.Show(xlabel='Estimated Scores', ylabel='CDF')
    ci = cdf.Percentile(10), cdf.Percentile(90)
    print('confidence interval', ci)
```


---
