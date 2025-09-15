class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        f_str = s.lower().strip()
        f_str_arr = list(filter(lambda c: c.isalnum(), f_str))
        if len(f_str_arr) < 2:
            return True

        s_ptr = 0
        e_ptr = len(f_str_arr) - 1

        while s_ptr < e_ptr:
            if f_str_arr[s_ptr] != f_str_arr[e_ptr]:
                return False
            s_ptr += 1
            e_ptr -= 1
        
        return True