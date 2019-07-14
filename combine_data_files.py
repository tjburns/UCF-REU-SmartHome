from datetime import datetime


address_file_1 = "./datasets/motor_states_random3.txt"
address_file_2 = "./datasets/random_dataset3.txt"
address_combined_data = "./datasets/combined_data_set3.csv"
number_of_lines = 5

def get_time(line):
    line_data = line.split()
    return datetime.strptime(line_data[0] + '-' + line_data[1], '%Y-%m-%d-%H:%M:%S.%f')

with open(address_file_1) as motors_states:
    mo_header = motors_states.readline().split()
    mo_data = motors_states.readlines()
with open(address_file_2) as random_data:
    ra_header = random_data.readline().split()
    ra_data = random_data.readlines()

output_header = ra_header + mo_header[1:]
print(output_header)

end_time = get_time(mo_data[0])
interval_data = mo_data[0].split()[2:]
pointer = 0
ignore_first = True

with open(address_combined_data, "w") as combined_data:
    combined_data.write(','.join(output_header))
    combined_data.write('\n')
    for line in ra_data:
        data = line.split()
        time = get_time(line)
        if time >= end_time:
            pointer += 1
            mo_line = mo_data[pointer]
            end_time = get_time(mo_line)
            interval_data = mo_line.split()[2:]
            ignore_first = False
        
        if not ignore_first:
            combined_data.write(','.join([time.strftime('%Y-%m-%d-%H:%M:%S.%f'), *data[2:], *interval_data]))
            combined_data.write('\n')
