import matplotlib.pyplot as plotlib


states= ['kone', 'ksix', 'keight', 'keleven', 'ktwo', 'kthree', 'knine', 'kten', 'kfive', 'ktwelve']
num_states_covered = [3, 6, 9, 12, 14, 16, 18, 20, 21, 22]
gradients = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1]


def plot_data(num_states_covered, states_needed,gradients):

    plotlib.figure(figsize=(12,6))

    eje_barras = plotlib.gca()
    eje_barras.bar(states_needed, gradients,color="blue", label="Numero de nuevos estados cubiertos")
    
    eje_linea = eje_barras.twinx()
    eje_linea.plot(states_needed,num_states_covered,color="red", marker="o",label="Todos los estados")

    plotlib.show()

plot_data(num_states_covered, states, gradients)
    
