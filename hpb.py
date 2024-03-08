from gosc import Gosc
from bandyta import Bandyta
from random import randrange
from matplotlib import pyplot as plt
from warnings import filterwarnings
filterwarnings('ignore') # Bardzo profesjonalne podejście do ostrzeżeń

machine_count = 100
guest_count = 200
iterations = 500

centered_value = 5
centered_range = 0.2
centered_step = 0.1
center_scale = 10

deviation_range = (0.1, 1)
deviation_step = 0.05
deviation_scale = 20

machine_output = 'machines.out'
guest_output = 'guests.out'

def main():
    machines = []
    guests = []
    for _ in range(machine_count):
        machines.append(Bandyta(randrange(center_scale*centered_value*(1-centered_range), center_scale*centered_value*(1+centered_range), center_scale*centered_step)/center_scale, randrange(deviation_scale*deviation_range[0], deviation_scale*deviation_range[1], deviation_scale*deviation_step)/deviation_scale))
    for _ in range(guest_count):
        guests.append(Gosc(machine_count))

    with open(machine_output, 'w') as file:
        for i in range(len(machines)):
            file.write('Machine {}:\n'.format(i))
            file.write('\tMean: {}\n\tStandard Deviation: {}\n'.format(machines[i].mean, machines[i].std))
    
    for step in range(iterations):
        print('iteration {}...'.format(step), end='')
        for guest in guests:
            machine_to_pull = guest.choose_machine()
            result = machines[machine_to_pull].pull()
            guest.receive_result(result, machine_to_pull)
        print('Done')

    x_axis = list(range(machine_count))
    y_axis = [0] * machine_count

    with open(guest_output, 'w') as file:
        for i in range(len(guests)):
            file.write('Guest {}:\n'.format(i))
            favorite_machine = guests[i].get_favorite_machine()
            file.write('\tMean: {}\n\tFavorite Machine: {}\n'.format(guests[i].get_mean(), favorite_machine))
            y_axis[favorite_machine] += 1
    
    plt.plot(x_axis, y_axis)
    plt.xlabel('Numer bandyty')
    plt.ylabel('Ilość ulubionych')
    plt.show()

if __name__ == '__main__':
    main()