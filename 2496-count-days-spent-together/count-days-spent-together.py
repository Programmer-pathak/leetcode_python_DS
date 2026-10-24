class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     
        def get_day_of_year(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_month[:month - 1]) + day
       
        arrive_a = get_day_of_year(arriveAlice)
        leave_a = get_day_of_year(leaveAlice)
        arrive_b = get_day_of_year(arriveBob)
        leave_b = get_day_of_year(leaveBob)
        overlap_start = max(arrive_a, arrive_b)
        overlap_end = min(leave_a, leave_b)
        
        return max(0, overlap_end - overlap_start + 1)