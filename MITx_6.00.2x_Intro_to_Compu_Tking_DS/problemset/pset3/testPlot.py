from ps3b_precompiled_36 import *
simulationWithoutDrug(100, 1000, 0.1, 0.05, 200)
print("Simulation 1")
simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
print("Simulation 2")
simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
print("Simulation 3")
simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)