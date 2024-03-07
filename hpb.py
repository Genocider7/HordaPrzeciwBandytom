from gosc import Gosc
from bandyta import Bandyta
from random import randrange
from warnings import filterwarnings
filterwarnings('ignore')

machine_count = 5
guest_count = 50
iterations = 25

guests_test = 3

centered_value = 5
centered_range = 0.2
centered_step = 0.1
center_scale = 10

deviation_range = (0.1, 1)
deviation_step = 0.05
deviation_scale = 20

def main():
    machines = []
    guests = []
    for _ in range(machine_count):
        machines.append(Bandyta(randrange(center_scale*centered_value*(1-centered_range), center_scale*centered_value*(1+centered_range), center_scale*centered_step)/center_scale, randrange(deviation_scale*deviation_range[0], deviation_scale*deviation_range[1], deviation_scale*deviation_step)/deviation_scale))
    for _ in range(guest_count):
        guests.append(Gosc(machine_count, guests_test))

    for i in range(len(machines)):
        print('Machine {}:'.format(i))
        print('\tMean: {}\n\tStandard Deviation: {}'.format(machines[i].mean, machines[i].std))
    
    for step in range(iterations):
        print('iteration {}...'.format(step), end='')
        for guest in guests:
            machine_to_pull = guest.choose_machine()
            result = machines[machine_to_pull].pull()
            guest.receive_result(result, machine_to_pull)
        print('Done')
    
    for i in range(len(guests)):
        print('Guest {}:'.format(i))
        print('\tMean: {}\n\tFavorite Machine: {}'.format(guests[i].get_data()[0], guests[i].get_favorite_machine()))

if __name__ == '__main__':
    main()