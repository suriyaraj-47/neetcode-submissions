

class Solution:

    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Step 1: Count task frequencies (fixed size array of 26)
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord("A")] += 1

        # Step 2: Identify the maximum frequency and count how many tasks share it
        max_freq = max(freq)
        max_freq_count = freq.count(max_freq)

        # Step 3: Calculate minimum cycles required by the bottleneck task
        # Format: (max_freq - 1) chunks of (n + 1) size, plus remaining max-            frequency tasks
        min_cycles = (max_freq - 1) * (n + 1) + max_freq_count

        # Step 4: If total tasks exceed required idle slots, total task count is the answer
        return max(len(tasks), min_cycles)