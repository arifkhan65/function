def vamp(buying,selling):
    actual_profit=selling-buying
    print('so you profited: ',actual_profit)
    return actual_profit


y=float(input('input buying price: '))
z=float(input('input selling price: '))


x=vamp(y,z)
print(x)

