class PrimeNumberCalculator():
    def __init__(self):
        self.prime_num_list = self.find_prime_list_calc()
        
    def find_prime_list_calc(self):
        num_prime = [2]
        for i in range(3, 1000):
            is_prime = self.check_if_its_prime(i)
            if is_prime:
                num_prime.append(i)
        return num_prime

    def check_if_its_prime(self, num):
        for idx in range(2, num+1):
            if (num != idx) & (num % idx == 0):
                return False
        return True

    def prime_factors_list(self, num_x):
        pf_x = {}
        for element in self.ranged_prime_nums(num_x):
            while (num_x % element == 0):
                pf_x = self.pf_counter(element, pf_x)
                num_x //= element
        return pf_x

    def ranged_prime_nums(self, limit):
        return [prime for prime in self.prime_num_list if prime <= limit]

    def pf_counter(self, num, pf_dict):
        if num not in pf_dict:
            pf_dict[num] = 1
        elif num in pf_dict:
            pf_dict[num] += 1
        return pf_dict