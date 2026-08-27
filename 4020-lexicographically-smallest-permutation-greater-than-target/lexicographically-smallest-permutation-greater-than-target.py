from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        # Check if s has enough characters to cover target prefix
        prefix_counts = [total_counts.copy()]
        curr_counts = total_counts.copy()
        
        matched_length = 0
        for i in range(n):
            c = target[i]
            if curr_counts[c] > 0:
                curr_counts[c] -= 1
                prefix_counts.append(curr_counts.copy())
                matched_length += 1
            else:
                break
                
        # Backtrack from the maximum matched prefix length down to 0
        for i in range(matched_length, -1, -1):
            if i == n:
                continue  # String is equal to target, need strictly greater
            
            avail = prefix_counts[i]
            target_char = target[i]
            
            # Find the smallest available character strictly greater than target[i]
            for ch_code in range(ord(target_char) + 1, ord('z') + 1):
                ch = chr(ch_code)
                if avail[ch] > 0:
                    # Found a valid split point
                    result = list(target[:i])
                    result.append(ch)
                    
                    # Remaining available characters
                    remaining_counts = avail.copy()
                    remaining_counts[ch] -= 1
                    
                    # Append remaining characters in sorted order
                    for char_code in range(ord('a'), ord('z') + 1):
                        c = chr(char_code)
                        if remaining_counts[c] > 0:
                            result.append(c * remaining_counts[c])
                            
                    return "".join(result)
                    
        return ""