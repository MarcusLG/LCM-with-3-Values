import numpy as np
import pair

from prime_calculator import PrimeCalculator

def main():
    num_1 = int(input("Enter number 1: "))
    num_2 = int(input("Enter number 2: "))
    num_lcm = int(input("Enter LCM: "))
    if (num_lcm % num_1 != 0) | (num_lcm % num_2 != 0):
        print("The input value is invalid.")
    pf_lcm = calc.prime_factors_list(num_lcm)
    pf_1 = calc.prime_factors_list(num_1)
    pf_2 = calc.prime_factors_list(num_2)
    pf_3 = []
    # max_length = len(pf_lcm)-1
    # max_loc = []
    # if_3_has_max = 0
    # for i in range(0, max_length):
    #     if (pf_lcm[i] > pf_1[i]) & (pf_lcm[i] > pf_2[i]):
    #         pf_3.append(pf_lcm[i])
    #         if_3_has_max = 1
    #         max_loc.append(3)
    #     else:
    #         pf_3.append(0)
    #         if pf_lcm[i] == pf_1[i]:
    #             max_loc.append(1)
    #         elif pf_lcm[i] == pf_2[i]:
    #             max_loc.append(2)
    # max_component = list(set(pf_lcm[max_length]))
    # num_3 = 1
    # for i in range(0, max_length):
    #     num_3 = num_3*pow(max_component[i], pf_3[i])
    # pf_3 = prime_factor(num_3, True)
    # num = [num_1, num_2, num_3]
    # pf_all = [pf_1, pf_2, pf_3]
    # num_3_list = [num_3]
    # element_list = pf_lcm[max_length]
    # pf_diff = list(np.array(pf_lcm[0:max_length])-np.array(pf_3[0:max_length]))
    # multi_coff = list(pair.pair_main(pf_diff, max_component))
    # for element in multi_coff:
    #     num_3_list.append(num_3*element)
    # print("Possible values of Num 3 are :")
    # print(num_3_list)

calc = PrimeCalculator()

while True:
    main()