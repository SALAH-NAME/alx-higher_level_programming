#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        This method prints the list in ascending order.
        """
        print(sorted(self))
