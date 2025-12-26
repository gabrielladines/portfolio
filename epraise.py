
# create a dictionary that shows the year group and number of epraise points overall

import matplotlib.pyplot as plt
epraise_points_per_form = {
    '7A': 5206,
    '7C': 4247,
    '7H': 5344,
    '7P': 4226,
    '8A': 4983,
    '8C': 4220,
    '8H': 4943,
    '8P': 4281,
    '8T': 5419,
    '9A': 3184,
    '9C': 4390,
    '9H': 3676,
    '9L': 4451,
    '9P': 3657,
    '9T': 5300,
    '10A': 4418,
    '10C': 3736,
    '10H': 5379,
    '10L': 4792,
    '10P': 4130,
    '10T': 4520,
    '11A': 2942,
    '11C': 3110,
    '11H': 2963,
    '11L': 2917,
    '11P': 2669,
    '11T': 3146,
    '12C': 1505,
    '12P': 1327,
    '12T': 1720,
    '13C': 1939,
    '13P': 2439,
    '13T': 2399
}


# find the sum of epraise points for each year group

total7 = sum(value for key, value in epraise_points_per_form.items()
             if key.startswith('7'))
# print(total7)

total8 = sum(value for key, value in epraise_points_per_form.items()
             if key.startswith('8'))
# print(total8)

total9 = sum(value for key, value in epraise_points_per_form.items()
             if key.startswith('9'))
# print(total9)

total10 = sum(value for key, value in epraise_points_per_form.items()
              if key.startswith('10'))
# print(total10)

total11 = sum(value for key, value in epraise_points_per_form.items()
              if key.startswith('11'))
# print(total11)

total12 = sum(value for key, value in epraise_points_per_form.items()
              if key.startswith('12'))
# print(total12)

total13 = sum(value for key, value in epraise_points_per_form.items()
              if key.startswith('13'))
# print(total13)


# open matplotlib to show the trand of epraise points over the year groups

year_groups = ['7', '8', '9', '10', '11', '12', '13']
total_points = [total7, total8, total9, total10, total11, total12, total13]

plt.plot(year_groups, total_points, 'bx')
plt.plot(year_groups, total_points, "green")
plt.xlabel('Year Group')
plt.ylabel('Total Epraise Points')
plt.title('Epraise Points by Year Group')
plt.show()
