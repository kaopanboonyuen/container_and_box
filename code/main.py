from .constants import RotationType, Axis
from .auxiliary_methods import intersect, set_to_decimal

DEFAULT_NUMBER_OF_DECIMALS = 1
START_POSITION = [0, 0, 0]

class Box:
    def __init__(self, name, width, height, depth, weight):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.weight = weight
        self.rotation_type = 0
        self.position = START_POSITION
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS

    def format_numbers(self, number_of_decimals):
        self.width = set_to_decimal(self.width, number_of_decimals)
        self.height = set_to_decimal(self.height, number_of_decimals)
        self.depth = set_to_decimal(self.depth, number_of_decimals)
        self.weight = set_to_decimal(self.weight, number_of_decimals)
        self.number_of_decimals = number_of_decimals

    # def string(self):
    #     return "%s(%sx%sx%s, weight: %s) pos(%s) rt(%s) vol(%s)" % (
    #         self.name, self.width, self.height, self.depth, self.weight,
    #         self.position, self.rotation_type, self.get_volume()
    #     )

    def string(self):
        return "%s(%sx%sx%s, weight: %s) pos(%s)  vol(%s)" % (
            self.name, self.width, self.height, self.depth, self.weight,
            self.position, self.get_volume()
        )

    def get_volume(self):
        return set_to_decimal(
            self.width * self.height * self.depth, self.number_of_decimals
        )

    def get_height(self):
        return set_to_decimal(
            self.height, self.number_of_decimals
        )

    # def get_dimension(self):
    #     if self.rotation_type == RotationType.RT_WHD:
    #         dimension = [self.width, self.height, self.depth]
    #     elif self.rotation_type == RotationType.RT_HWD:
    #         dimension = [self.height, self.width, self.depth]
    #     elif self.rotation_type == RotationType.RT_HDW:
    #         dimension = [self.height, self.depth, self.width]
    #     elif self.rotation_type == RotationType.RT_DHW:
    #         dimension = [self.depth, self.height, self.width]
    #     elif self.rotation_type == RotationType.RT_DWH:
    #         dimension = [self.depth, self.width, self.height]
    #     elif self.rotation_type == RotationType.RT_WDH:
    #         dimension = [self.width, self.depth, self.height]
    #     else:
    #         dimension = []

    #     return dimension

    def get_dimension(self):
        return self.width, self.height, self.depth

class Container:
    def __init__(self, name, width, height, depth, max_weight):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.max_weight = max_weight
        self.items = []
        self.unfitted_items = []
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS

    def format_numbers(self, number_of_decimals):
        self.width = set_to_decimal(self.width, number_of_decimals)
        self.height = set_to_decimal(self.height, number_of_decimals)
        self.depth = set_to_decimal(self.depth, number_of_decimals)
        self.max_weight = set_to_decimal(self.max_weight, number_of_decimals)
        self.number_of_decimals = number_of_decimals

    def string(self):
        return "%s(%sx%sx%s, max_weight:%s) vol(%s)" % (
            self.name, self.width, self.height, self.depth, self.max_weight,
            self.get_volume()
        )

    def get_volume(self):
        return set_to_decimal(
            self.width * self.height * self.depth, self.number_of_decimals
        )

    def get_total_weight(self):
        total_weight = 0

        for item in self.items:
            total_weight += item.weight

        return set_to_decimal(total_weight, self.number_of_decimals)

    def put_item(self, item, pivot):
        fit = False
        valid_item_position = item.position
        item.position = pivot

        for i in range(0, len(RotationType.ALL)):
            item.rotation_type = i
            dimension = item.get_dimension()
            if (
                self.width < pivot[0] + dimension[0] or
                self.height < pivot[1] + dimension[1] or
                self.depth < pivot[2] + dimension[2]
            ):
                continue

            fit = True

            for current_item_in_bin in self.items:
                if intersect(current_item_in_bin, item):
                    fit = False
                    break

            if fit:
                if self.get_total_weight() + item.weight > self.max_weight:
                    fit = False
                    return fit

                self.items.append(item)

            if not fit:
                item.position = valid_item_position

            return fit

        if not fit:
            item.position = valid_item_position

        return fit

class Container:
    def __init__(self, name, width, height, depth, max_weight):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth
        self.max_weight = max_weight
        self.items = []
        self.unfitted_items = []
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS

    def format_numbers(self, number_of_decimals):
        self.width = set_to_decimal(self.width, number_of_decimals)
        self.height = set_to_decimal(self.height, number_of_decimals)
        self.depth = set_to_decimal(self.depth, number_of_decimals)
        self.max_weight = set_to_decimal(self.max_weight, number_of_decimals)
        self.number_of_decimals = number_of_decimals

    # def string(self):
    #     return "%s(%sx%sx%s, max_weight:%s) vol(%s)" % (
    #         self.name, self.width, self.height, self.depth, self.max_weight,
    #         self.get_volume()
    #     )

    def string(self):
        return 
        
    def get_volume(self):
        return set_to_decimal(
            self.width * self.height * self.depth, self.number_of_decimals
        )

    def get_height(self):
        return set_to_decimal(
            self.height, self.number_of_decimals
        )

    def get_total_weight(self):
        total_weight = 0

        for item in self.items:
            total_weight += item.weight

        return set_to_decimal(total_weight, self.number_of_decimals)

    def put_item(self, item, pivot):
        fit = False
        valid_item_position = item.position
        item.position = pivot

        for i in range(0, len(RotationType.ALL)):
            item.rotation_type = i
            dimension = item.get_dimension()
            

            if (
                self.width < pivot[0] + dimension[0] or
                self.height < pivot[1] + dimension[1] or
                self.depth < pivot[2] + dimension[2]
            ):
                continue

            fit = True

            for current_item_in_bin in self.items:
                if intersect(current_item_in_bin, item):
                    fit = False
                    break

            if fit:
                if self.get_total_weight() + item.weight > self.max_weight:
                    fit = False
                    return fit

                self.items.append(item)

            if not fit:
                item.position = valid_item_position

            return fit

        if not fit:
            item.position = valid_item_position

        return fit


class Packer:
    def __init__(self):
        self.bins = []
        self.items = []
        self.unfit_items = []
        self.total_items = 0

    def add_bin(self, bin):
        return self.bins.append(bin)

    def add_item(self, item):
        self.total_items = len(self.items) + 1

        return self.items.append(item)

    def pack_to_bin(self, bin, item):
        fitted = False

        if not bin.items:
            response = bin.put_item(item, START_POSITION)

            if not response:
                bin.unfitted_items.append(item)

            return

        for axis in range(0, 3):
            items_in_bin = bin.items

            for ib in items_in_bin:
                pivot = [0, 0, 0]
                w, h, d = ib.get_dimension()
                if axis == Axis.WIDTH:
                    pivot = [
                        ib.position[0] + w, 
                        ib.position[1],
                        ib.position[2]
                    ] 
                elif axis == Axis.HEIGHT:
                    pivot = [
                        ib.position[0],
                        ib.position[1] + h,
                        ib.position[2]
                    ]
                elif axis == Axis.DEPTH:
                    pivot = [
                        ib.position[0],
                        ib.position[1],
                        ib.position[2] + d
                    ]

                if bin.put_item(item, pivot):
                    fitted = True
                    break
            if fitted:
                break

    # def pack_to_bin(self, bin, item):
    #     fitted = False

    #     if not bin.items:
    #         response = bin.put_item(item, START_POSITION)

    #         if not response:
    #             bin.unfitted_items.append(item)

    #         return

    #     for axis in range(0, 3):
    #         items_in_bin = bin.items

    #         for ib in items_in_bin:
    #             pivot = [0, 0, 0]
    #             w, h, d = ib.get_dimension()
    #             if axis == Axis.WIDTH:
    #                 pivot = [
    #                     ib.position[0] + w, 
    #                     ib.position[1],
    #                     ib.position[2]
    #                 ] 
    #             elif axis == Axis.HEIGHT:
    #                 pivot = [
    #                     ib.position[0],
    #                     ib.position[1] + h,
    #                     ib.position[2]
    #                 ]
    #             elif axis == Axis.DEPTH:
    #                 pivot = [
    #                     ib.position[0],
    #                     ib.position[1],
    #                     ib.position[2] + d
    #                 ]

    #             if bin.put_item(item, pivot):
    #                 fitted = True
    #                 break
    #         if fitted:
    #             break

        if not fitted:
            bin.unfitted_items.append(item)

    def bubble_sort(seq):
        """Inefficiently sort the mutable sequence (list) in place.
           seq MUST BE A MUTABLE SEQUENCE.

           As with list.sort() and random.shuffle this does NOT return 
        """
        changed = True
        while changed:
            changed = False
            for i in xrange(len(seq) - 1):
                if seq[i] > seq[i+1]:
                    seq[i], seq[i+1] = seq[i+1], seq[i]
                    changed = True
        return None

    def partition(arr, low, high):
        i = (low-1)      # index of smaller element
        pivot = arr[high]    # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:

                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:

            pi = partition(arr, low, high)
            quickSort(arr, low, pi-1)
            quickSort(arr, pi+1, high)
        
    def pack(
        self, status='Normal',sorting_by_height=True, sorting_by_size=True, distribute_items=False,
        number_of_decimals=DEFAULT_NUMBER_OF_DECIMALS
    ):
        for bin in self.bins:
            bin.format_numbers(number_of_decimals)

        for item in self.items:
            item.format_numbers(number_of_decimals)

        '''
        sort() Parameters
        By default, sort() doesn't require any extra parameters. 
            However, it has two optional parameters:

        reverse - If True, the sorted list is reversed 
            (or sorted in Descending order)
        key - function that serves as a key for the sort comparison

        '''

        if status == 'Size':
            self.bins.sort(
                key=lambda bin: bin.get_volume(), reverse=True
            )
            self.items.sort(
                key=lambda item: item.get_volume(), reverse=True
            )
        elif status == 'Height':
            self.bins.sort(
                key=lambda bin: bin.get_height(), reverse=True
            )
            self.items.sort(
                key=lambda item: item.get_height(), reverse=True
            )
        else:
            self.bins.sort(
                key=lambda bin: bin.get_volume(), reverse=False
            )
            self.items.sort(
                key=lambda item: item.get_volume(), reverse=False
            )

        for bin in self.bins:
            for item in self.items:
                self.pack_to_bin(bin, item)

            if distribute_items:
                for item in bin.items:
                    self.items.remove(item)
