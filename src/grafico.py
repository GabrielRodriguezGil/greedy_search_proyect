import matplotlib.pyplot as plotlib


states= ["kone", "ktwo", "kthree", "kfour", "kfive", "ksix", "kseven", "keight", "knine", "kten", "keleven", "ktwelve"]
num_states_covered = [3, 6, 9, 12, 14, 16, 18, 20, 21, 22]
gradients = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1]


def plot_data(num_states_covered, states_needed,gradients,covered_states):

    plotlib.figure(figsize=(12,6))

    eje_barras = plotlib.gca()
    eje_barras.bar(states_needed, gradients, label="Numero de estados cubiertos")
    
    plotlib
    plotlib.plot(states_needed, num_states_covered, marker="o", label="Total estados cubiertos")
    plotlib.show()

plot_data(num_states_covered, states, gradients)
    
