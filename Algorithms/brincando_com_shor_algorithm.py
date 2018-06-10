def fastExpModSeq(a,N,x):
    axs=[1]
    axa=1
    for v in range(1,x+1):
        axa=(axa*a)%N
        axs+=[axa]
    return axs

def find_period(a,N):
    axa=1
    p=0
    axa=(axa*a)%N
    p+=1
    while axa != 1:
        axa=(axa*a)%N
        p+=1
    return p

# Exemplo 6.5.4, Figura 6.4, dados equacao 6.160
xs=fastExpModSeq(24,371,526)
# bar vem do matplolib
from matplotlib.pyplot import bar
from numpy import arange

bar(arange(len(xs)), xs, alpha=0.5)