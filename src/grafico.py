import matplotlib.pyplot as plotlib


states= ["kone", "ktwo", "kthree", "kfour", "kfive", "ksix", "kseven", "keight", "knine", "kten", "keleven", "ktwelve"]
y=[2.5,5.0,7.5,10.0,12.5,15.0,17.5,20.0,22.5]
x=[0.0,0.5,1.0,1.5,2.0,2.5,3.0]

def plot_data(x, y, states):
    
    plotlib.bar(states, x, label="Numero de estados cubiertos")
    plotlib.plot(states, y, marker="o", label="Total estados cubiertos")
    plotlib.show()

plot_data(x, y, states)
    
