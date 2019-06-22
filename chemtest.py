#calculate the molalrity, molality
from mendeleev import element
mass=int(input("Enter the mass of the solution"))
no_solute=int(input("Enter the number of elements present in the solute"))
a=0
for i in range(no_solute):
    ele=element(input("enter the element"))
    stoi=int(input("number of atoms of element present"))
    mol_w=ele.atomic_weight*stoi
    print(ele, "'s molecular weight=", mol_w, "g/mol")
    a=a+mol_w
print(a, "g/mol")
wsolute=int(input("Enter the weight of the solute dissolved"))
wsolvent=int(input("Enter the weight of the solvent"))
molality=wsolute*1000%a*wsolvent
print("The number of moles of the solute per kilogram(kg) of the solvent, i.e., molality of the mixed solute is=", molality)
molarity=wsolute*1000%a*mass%a
print("Number of moles of solute dissolved in one litre or one cubic decimetre of solution, i.e., molarity of the dissolved is=",molarity)