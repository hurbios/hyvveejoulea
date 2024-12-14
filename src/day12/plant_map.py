class PlantMap:
    def __init__(self, plantmap):
        self._plantmap = plantmap
        self._plants = {}
        self._plant_amount = {}
        self._plant_fences = {}

        for y,p in enumerate(self._plantmap):
            for x in range(len(p)):
                self._add_plant((x,y))

    def _get_plant_type(self, position):
        return self._plantmap[position[1]][position[0]]

    def _get_plant_area(self, position, plant_type):
        for i,plants in enumerate(self._plants[plant_type]):
            # print(plants)
            if position in plants:
                return i
        return None


    def _check_neighbour_plant_areas(self, position, plant_type):
        areas = {}
        test_areas = [
            self._get_plant_area((position[0], position[1] - 1), plant_type),
            self._get_plant_area((position[0], position[1] + 1), plant_type),
            self._get_plant_area((position[0] - 1, position[1]), plant_type),
            self._get_plant_area((position[0] + 1, position[1]), plant_type)
        ]
        for test_area in test_areas:
            if test_area != None:
                # print("adfds", test_area)
                if test_area not in areas:
                    areas[test_area] = 0
                areas[test_area] += 1
        return areas

    def _add_plant(self, position):
        plant_type = self._get_plant_type(position)
        if plant_type not in self._plants:
            self._plants[plant_type] = []

        neighbour_areas = self._check_neighbour_plant_areas(position, plant_type)
        neighbours_amounts = 0
        newarea = []
        fences = 0
        amount = 0
        
        # combine neighbours
        # if plant_type == "I":
        #     print("combine neighbours",plant_type, "fences:", self._plant_fences, ",neighbours:", neighbour_areas)
        for i in sorted(neighbour_areas.keys(), reverse=True):
            neighbours_amounts += neighbour_areas[i]
            # if plant_type == "I":
            #     print(i, self._plants[plant_type])
            newarea+=(self._plants[plant_type].pop(i))
            # if plant_type == "I":
            #     print("newarea", newarea)
            fences += self._plant_fences[plant_type].pop(i)
            amount += self._plant_amount[plant_type].pop(i)
        
        if plant_type not in self._plant_amount:
            self._plant_amount[plant_type] = []
        if len(neighbour_areas) > 0:
            self._plant_amount[plant_type] += [amount]
        if plant_type not in self._plant_fences:
            self._plant_fences[plant_type] = []
        if len(neighbour_areas) > 0:
            self._plant_fences[plant_type] += [fences]

        self._plant_fences[plant_type].append(self._plant_fences[plant_type].pop() + 4 - 2 * neighbours_amounts if len(self._plant_fences[plant_type]) > 0 and len(neighbour_areas) > 0 else 4 - 2 * neighbours_amounts)
        self._plant_amount[plant_type].append(self._plant_amount[plant_type].pop() + 1 if len(self._plant_amount[plant_type]) > 0 and len(neighbour_areas) > 0 else 1)

        if len(neighbour_areas) <= 0:
            self._plants[plant_type].append([position]) ## joku ongelma
            # if plant_type == "I":
            #     print("plants1",self._plants)
        else:
            newarea += [(position)]
            # if plant_type == "I":
            #     print("newarea2",newarea)
            self._plants[plant_type].append(newarea)
            # if plant_type == "I":
            #     print("plants2",self._plants)

        # if plant_type == "I":
        #     print("AREAS",neighbour_areas, self._plant_fences, self._plant_amount, self._plants)



    def get_plant_scores(self):
        score = 0
        for plant_type in self._plants.keys():
            for i in range(len(self._plants[plant_type])):
                print(f"{plant_type}[{i}], {self._plant_amount[plant_type][i]} * {self._plant_fences[plant_type][i]}  = {self._plant_amount[plant_type][i] * self._plant_fences[plant_type][i]}")
                score += self._plant_amount[plant_type][i] * self._plant_fences[plant_type][i]
        return score
