a = """Adaptive Boosting.ipynb
Extreme Gradient Boosted Trees.ipynb
Gradient Boosted Trees.ipynb
Linear Regression.ipynb
Random Forest.ipynb
Ridge Regression.ipynb"""

from os import system

for x in a.split("\n"):
    system('git add "{}"'.format(x))
    system('git commit -m "{} Updated"'.format(x.split(".")[0]))
system("git push origin")