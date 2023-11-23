from pulp import *

s1 = 2
s2 = 3
s3 = 5
s4 = 6
s5 = 7
s6 = 10

wp1 = 11
wp2 = 9
wp3 = 7
wp4 = 5
wp5 = 3
wp6 = 2

p1 = 11.8
p2 = 11.7
p3 = 10.5
p4 = 9.4
p5 = 9.3
p6 = 10


x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)
x3 = pulp.LpVariable('x3', lowBound=0)
x4 = pulp.LpVariable('x4', lowBound=0)
x5 = pulp.LpVariable('x5', lowBound=0)
x6 = pulp.LpVariable('x6', lowBound=0)

problem = pulp.LpProblem('0', LpMaximize)

#целевая ф-ция
problem += p1 * x1 + p2 * x2 + p3 * x3 + p4 * x4 + p5 * x5 + p6 * x6
problem += s1 * x1 + s2 * x2 + s3 * x3 + s4 * x4 + s5 * x5 + s6 * x6 <= 204
problem += wp1 * x1 + wp2 * x2 + wp3 * x3 + wp4 * x4 + wp5 * x5 + wp6 * x6 <= 180

problem.solve()

print("Result\n")

print("function")
print(abs(value(problem.objective)))

print("\n")

print("target cells")
for v in problem.variables():
    print(v.name, ' = ', v.varValue)

a = input()
