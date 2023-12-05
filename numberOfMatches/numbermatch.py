def num_matches(n):
    matches_played = 0

    while n > 1:
        matches_played += n // 2
        n = (n + 1) // 2  

    return matches_played


n = 7
result = num_matches(n)
print(f"Number of matches played for {n} teams: {result}")
