from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        
        # Check palindrome feasibility
        odd_chars = [c for c, count in freq.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Available counts for the first half
        half_counts = {c: count // 2 for c, count in freq.items()}
        half_len = n // 2
        
        # Helper to construct full palindrome from first half
        def make_palindrome(first_half: str) -> str:
            if n % 2 == 1:
                return first_half + mid_char + first_half[::-1]
            return first_half + first_half[::-1]

        # 1. Check if the minimal palindrome matching target's first half works
        # Try to build prefix matching target[:half_len] exactly
        target_half = target[:half_len]
        curr_counts = half_counts.copy()
        possible = True
        
        for ch in target_half:
            if curr_counts.get(ch, 0) > 0:
                curr_counts[ch] -= 1
            else:
                possible = False
                break
                
        if possible:
            candidate = make_palindrome(target_half)
            if candidate > target:
                return candidate

        # 2. Try prefix matches of length i (from half_len down to 0)
        # and branch with a strictly larger character at index i
        prefix_counts = half_counts.copy()
        prefix = []
        
        # Pre-calculate counts for prefix of length i
        prefixes = [[]]
        temp_counts = half_counts.copy()
        
        valid_prefix_len = 0
        for i in range(half_len):
            ch = target[i]
            if temp_counts.get(ch, 0) > 0:
                temp_counts[ch] -= 1
                valid_prefix_len += 1
            else:
                break

        # Iterate back from longest matching prefix to 0
        for i in range(valid_prefix_len, -1, -1):
            # Reconstruct counts remaining after using target[:i]
            rem_counts = half_counts.copy()
            for j in range(i):
                rem_counts[target[j]] -= 1
            
            # Try placing character > target[i] at position i
            target_char = target[i] if i < half_len else ""
            
            available_chars = sorted([c for c, cnt in rem_counts.items() if cnt > 0])
            for ch in available_chars:
                if i < half_len and ch <= target_char:
                    continue
                
                # Place ch at position i
                rem_counts[ch] -= 1
                
                # Fill remaining first half greedily with smallest available characters
                rest = []
                for c in sorted(rem_counts.keys()):
                    rest.extend([c] * rem_counts[c])
                
                first_half = target[:i] + ch + "".join(rest)
                cand = make_palindrome(first_half)
                
                if cand > target:
                    return cand

        return ""