print("You have selected find atomic weight using relative mass calc!")
mass_list = []
abundance_list = []
product_list = []
while True:
  
  
    mass = input("Enter the mass of a known isotope (or type 'done' to finish): ")
    if mass == 'done':
        break
    else:
        abundance = input("Enter the abundance of the known isotope: ")
        mass_list.append(float(mass))
        abundance_list.append(float(abundance))
        product = float(mass) * float(abundance)
        product_list.append(product)
relative_mass = float(input("Enter the relative mass of the isotope: "))
abunance = 100 - sum(abundance_list)
atomic_weight = relative_mass * 100
for i in range(len(mass_list)):
    atomic_weight -= product_list[i]
atomic_weight /= abunance
print("The atomic weight of the unknown isotope is: ", atomic_weight)


