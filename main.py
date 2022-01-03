import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main() -> None:

    # 0. Overview
    plt.style.use('ggplot')
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.serif'] = 'Ubuntu'
    plt.rcParams['font.monospace'] = 'Ubuntu Mono'
    plt.rcParams['font.size'] = 14
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    plt.rcParams['legend.fontsize'] = 12
    plt.rcParams['figure.titlesize'] = 12
    plt.rcParams['image.cmap'] = 'jet'
    plt.rcParams['image.interpolation'] = 'none'
    plt.rcParams['figure.figsize'] = (12, 10)
    plt.rcParams['axes.grid'] = False
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markersize'] = 8
    colors = ['xkcd:pale orange', 'xkcd:sea blue', 'xkcd:pale red', 'xkcd:sage green', 'xkcd:terra cotta',
              'xkcd:dull purple', 'xkcd:teal', 'xkcd: goldenrod', 'xkcd:cadet blue', 'xkcd:scarlet']

    # 1. Random Walks
    start = 0
    x = []
    n = 10000
    for i in range(n):
        step = np.random.choice([-1, 1], p=[0.5, 0.5])
        start = start + step
        x.append(start)

    plt.plot(x)
    plt.xlabel('Steps', fontsize=20)
    plt.ylabel(r'$S_{n}$', fontsize=20)
    plt.show()

    x = []
    p = [[0.5, 0.5], [0.9, 0.1], [0.8, 0.2], [0.6, 0.4], [0.4, 0.6], [0.2, 0.8], [0.1, 0.9]]
    label_p = ['Simple', r'$p=0.9$', r'$p=0.8$', r'$p=0.6$', r'$p=0.4$', r'$p=0.2$', r'$p=0.1$']
    n = 10000
    x = []
    for couple in p:
        x_p = []
        start = 0
        for i in range(n):
            step = np.random.choice([-1, 1], p=couple)
            start = start + step
            x_p.append(start)
        x.append(x_p)

    i = 0
    for time_series in x:
        plt.plot(time_series, label=label_p[i])
        i = i + 1
    plt.xlabel('Steps', fontsize=20)
    plt.ylabel(r'$S_{n}$', fontsize=20)
    plt.legend()
    plt.show()

    # 2. Gambler’s Ruin Chain
    def gamblers_ruin_chain(start, first, last, n):
        for k in range(n):
            if start == first or start == last:
                start = start
            else:
                step = np.random.choice([-1, 1], p=[0.5, 0.5])
                start = start + step
        return start

    state_list = []
    for i in range(100000):
        state_list.append(gamblers_ruin_chain(3, 0, 5, 2))
    data_state = pd.DataFrame({'Final State': state_list})
    data_occ = pd.DataFrame(data_state.value_counts('Final State')).rename(columns={0: 'Count'})
    data_occ['Count'] = data_occ['Count'] / 100000
    sns.barplot(x=data_occ.index, y=data_occ['Count'], palette='plasma')
    plt.ylabel('Normalized Count')
    plt.show()

    # 3. Custom Markov Chain
    state_1 = [0.2, 0.5, 0.3, 0, 0]
    state_2 = [0, 0.5, 0.5, 0, 0]
    state_3 = [0, 0, 1, 0, 0]
    state_4 = [0, 0, 0, 0, 1]
    state_5 = [0, 0, 0, 0.5, 0.5]
    trans_matrix = [state_1, state_2, state_3, state_4, state_5]
    trans_matrix = np.array(trans_matrix)
    print(trans_matrix)

    def t(N):
        step = np.arange(1, N + 1, 1)
        y = []
        for s in step:
            v = 0.5 ** s
            y.append(v)
        return y

    plt.plot(t(10))
    plt.ylabel(r'$t(N-1)$', fontsize=20)
    plt.xlabel(r'$N-1$', fontsize=20)
    plt.show()

    def prob(N):
        states = np.arange(1, 6, 1)
        steps = np.arange(1, N + 1, 1)
        n = 1000
        state_collection = []
        for k in range(n):
            start = 2
            for i in range(N):
                start = np.random.choice(states, p=trans_matrix[start - 1])
            if start == 2:
                state_collection.append(1)
            else:
                state_collection.append(0)
        state_collection = np.array(state_collection)
        return state_collection.sum() / n

    p_20 = p(20)
    plt.plot(t(20), label=r'Theory, $t(N-1)$')
    plt.plot(p_20, 'x', label=r'Simulation, $p(N-1)$', color='navy')
    plt.ylabel(r'Result', fontsize=20)
    plt.xlabel(r'$N-1$', fontsize=20)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
