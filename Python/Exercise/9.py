from math import sqrt
C=50
H=30
def q(D):
    Q=round(sqrt((2*C*D)/H))
    return Q
v_Q=[str(q(int(i))) for i in input("Value range of Q:").split(",")]
print(",".join(v_Q))