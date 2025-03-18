"""
The accounts of the "Fat to Fit Club (FFC)" association are supervised by John as a volunteered accountant. The association is funded through financial donations from generous benefactors. John has a list of the first n donations: [14, 30, 5, 7, 9, 11, 15] He wants to know how much the next benefactor should give to the association so that the average of the first n + 1 donations should reach an average of 30. After doing the math he found 149. He thinks that he could have made a mistake.

Could you help him?

"""
import math

def new_avg(arr, newavg):
    try:
        n = len(arr)
        new_len = n + 1
        new_total = newavg * new_len
        assert new_total > sum(arr)
        new_donation = math.ceil(new_total - sum(arr))
        return new_donation
    except AssertionError:
        print("Error expected")

arr = [14, 30, 5, 7, 9, 11, 16]
newavg = 30


print(new_avg(arr, newavg))