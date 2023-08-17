class AlgorithmeGourmand(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(AlgorithmeGourmand(names[i], values[i], calories[i]))
    return menu


def AlgorithmeFlexible(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)

    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return result, totalValue


def testAlgorithmeFlexible(items, constraint, keyFunction):
    taken, val = AlgorithmeFlexible(items, constraint, keyFunction)
    print("Total value of items taken = ", val)
    for item in taken:
        print("   ", item)


def testAlgorithmeFlexibles(foods, maxUnits):
    print("Use AlgorithmeFlexible by value to allocate", maxUnits, "calories")
    testAlgorithmeFlexible(foods, maxUnits, AlgorithmeGourmand.getValue)
    print("\nUse AlgorithmeFlexible by cost to allocate", maxUnits, "calories")
    testAlgorithmeFlexible(foods, maxUnits, lambda x: 1 / AlgorithmeGourmand.getCost(x))
    print("\nUse AlgorithmeFlexible by density to allocate", maxUnits, "calories")
    testAlgorithmeFlexible(foods, maxUnits, AlgorithmeGourmand.density)


names = ["wine", "beer", "pizza", "burger", "fries", "cola", "apple", "donut", "cake"]
values = [80, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testAlgorithmeFlexibles(foods, 750)

