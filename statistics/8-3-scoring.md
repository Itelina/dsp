# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

In games like hockey and soccer, the time between goals is roughly exponential. So you could estimate a team’s goal-scoring rate by observing the number of goals they score in a game. This estimation process is a little different from sampling the time between goals, so let’s see how it works.

Write a function that takes a goal-scoring rate, lam, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.

> See Code attached:
```
def GoalEstimates(lam=2):
    playtime = 0
    goals = 0
    n=10
    while playtime <= 1:
        xs = np.random.exponential(lam, n)
        L = 1 / np.mean(xs)
        playtime += L
        goals += 1
    return goals
```

Write another function that simulates many games, stores the estimates of lam, then computes their mean error and RMSE.
> See Code attached:
```
def GameEstimates(lam=2, m=20):
    n=10
    Scores =[]
    for i in range(m):
        playtime = 0
        goals = 0
        while playtime <= 1:
            xs = np.random.exponential(lam, n)
            L = 1 / np.mean(xs)
            playtime += L
            goals += 1
        Scores.append(goals)
    print('RMSE L', RMSE(Scores, lam))
    print('Mean Error L', MeanError(Scores, lam))
```

Is this way of making an estimate biased? Plot the sampling distribution of the estimates and the 90% confidence interval. 
```
def GameEstimateScores(lam=2, m=20):
    n=10
    Scores =[]
    for i in range(m):
        playtime = 0
        goals = 0
        while playtime <= 1:
            xs = np.random.exponential(lam, n)
            L = 1 / np.mean(xs)
            playtime += L
            goals += 1
        Scores.append(goals)
    return Scores

estimates = GameEstimateScores(2, 100)
cdf = thinkstats2.Cdf(estimates)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='Estimated Scores', ylabel='CDF')
ci = cdf.Percentile(10), cdf.Percentile(90)
print('confidence interval', ci)
```

What is the standard error? What happens to sampling error for increasing values of lam?'''
```
def GameEstimateError(lam=2, m=20):
    n=10
    Scores =[]
    for i in range(m):
        playtime = 0
        goals = 0
        while playtime <= 1:
            xs = np.random.exponential(lam, n)
            L = 1 / np.mean(xs)
            playtime += L
            goals += 1
        Scores.append(goals)
    return RMSE(Scores, lam)

GameEstimateError()
GameEstimateError(3, 20)
GameEstimateError(5, 20)
GameEstimateError(10, 20)
GameEstimateError(100, 20)
```

---
