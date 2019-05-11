from hospital_solver import HospitalSolver
from utility import from_txt
from matplotlib import pyplot as plt


if __name__ == '__main__':
    hospitalSolver = HospitalSolver(from_txt('data2.txt'), 3)
    hospitalSolver.run()
    plt.show()