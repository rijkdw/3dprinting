from sys import argv
import math

import matplotlib.pyplot as plt


def main():
    n_buttons = int(argv[1])

    list_n_modeswitches = [0]
    list_n_buttonsleft = [n_buttons]
    list_n_totalbuttons = [n_buttons]

    for i in range(1, n_buttons+1):

        n_modeswitches = i
        list_n_modeswitches.append(n_modeswitches)

        n_buttonsleft = n_buttons - n_modeswitches
        list_n_buttonsleft.append(n_buttonsleft)

        #n_modes = 2**n_modeswitches
        n_modes = n_modeswitches
        n_totalbuttons = n_modes*n_buttonsleft
        list_n_totalbuttons.append(n_totalbuttons)

    optimal_index = argmax(list_n_totalbuttons)
    optimal_n_modeswitches = list_n_modeswitches[optimal_index]
    optimal_n_buttonsleft = list_n_buttonsleft[optimal_index]
    optimal_n_totalbuttons = list_n_totalbuttons[optimal_index]

    print(f"Optimal number of mode-switch buttons: {optimal_n_modeswitches} for a total of {optimal_n_totalbuttons} total buttons.")


def argmax(lst):
    return sorted([(i, x) for i, x in enumerate(lst)], key=lambda tup: tup[1], reverse=True)[0][0]

if __name__ == "__main__":
    main()
