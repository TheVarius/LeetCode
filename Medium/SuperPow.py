class Solution(object):
    def superPow(self, a, b):
        MOD = 1337
        
        def quick_pow(base, power):
            res = 1
            base %= MOD
            while power > 0:
                if power % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                power //= 2
            return res

        if not b:
            return 1
        
        last_digit = b.pop()
        
        part1 = quick_pow(self.superPow(a, b), 10)
        part2 = quick_pow(a, last_digit)
        
        return (part1 * part2) % MOD
