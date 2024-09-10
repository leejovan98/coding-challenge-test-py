def kazuma_jovan(monsters):

    cache = {}

    def recurse_jovan(i, action):
        if i >= len(monsters):
            return 0

        if (i, action) in cache.keys():
            return cache[(i, action)]

        profit = 0
        new_i = i
        if action == "attack":
            profit += monsters[i]
            best = max(recurse_jovan(i + 2, "prepare"), recurse_jovan(i + 2, "back"))
            cache[(i, action)] = profit + best

        elif action == "prepare":
            profit -= monsters[i]
            best = max(recurse_jovan(i + 1, "attack"))
            cache[(i, action)] = profit + best

        else:
            new_i += 1

        best_subsequent_action = max(recurse_jovan(i + 1))





