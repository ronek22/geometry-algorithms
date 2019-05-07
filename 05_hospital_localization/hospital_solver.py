from point import Point
from copy import deepcopy
from matplotlib import pyplot as plt


class HospitalSolver:
    def __init__(self, cities: list, hospitals_amount):
        if hospitals_amount > len(cities) or hospitals_amount < 1:
            raise AttributeError("There have to be less hospitals than cities or more than 1 hospital")
        print(len(cities))
        self.cities = cities
        self.hospitals_amount = hospitals_amount
        self.hospitals = []
        self.furthest_distance = 0.0
        self.optimized_distance = 0.0
        self.all_cities = deepcopy(cities)

    def run(self):
        print("HOSPITAL LOCALIZATION PROBLEM")
        if self.hospitals_amount == len(self.cities):
            self.hospitals.extend(self.cities)
            self.cities = []
        else:
            first_hospital = self.cities[0]
            self.hospitals.append(first_hospital)
            self.cities.remove(first_hospital)
            self.calculate_new_hospital_with_optimized_distance(self.hospitals_amount)
        self.display_results()
        self.draw()

    def display_results(self):
        print("="*30)
        print(f"HOSPITALS: {len(self.hospitals)}")
        for i, hospital in enumerate(self.hospitals):
            print(f"\tHospital {i+1}: {hospital}")

        print("Radius = ", self.optimized_distance)

    def draw(self):
        x, y = [x.x for x in self.all_cities], [x.y for x in self.all_cities]
        fig = plt.figure()
        plt.scatter(x, y)
        for hospital in self.hospitals:
            plt.plot(*hospital.get_xy, "or", color="r")

    def calculate_new_hospital_with_optimized_distance(self, k):
        self.calculate_new_hospitals(k)
        self.calculate_optimized_distance()

    def calculate_new_hospitals(self, k: int):
        for j in range(1, k):
            furthest = Point()
            for city in self.cities:
                dist = self.calculate_optimized_distance_for_one_city(city, self.hospitals[j-1])
                if self.furthest_distance < dist:
                    self.furthest_distance = dist
                    furthest = city
            self.furthest_distance = 0.0
            self.hospitals.append(furthest)
            self.cities.remove(furthest)

    def calculate_optimized_distance_for_one_city(self, city: Point, hospital: Point):
        optimized_distance = city.dist
        dist = city.get_distance(hospital)
        if optimized_distance:
            optimized_distance = min(optimized_distance, dist)
        else:
            optimized_distance = dist
        city.dist = optimized_distance
        return optimized_distance

    def calculate_optimized_distance(self):
        for city in self.cities:
            dist = self.calculate_optimized_distance_for_one_city(city, self.hospitals[-1])
            if self.furthest_distance < dist:
                if self.optimized_distance:
                    self.optimized_distance = max(self.optimized_distance, dist)
                else:
                    self.optimized_distance = dist
