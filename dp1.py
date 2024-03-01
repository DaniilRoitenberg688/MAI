subjects = [("Math", 1, 9), ("Bio", 0.5, 5), ("Rus", 1, 6), ("IT", 0.5, 7), ("Chn", 1.5, 9), ("Physics", 2, 10)]
amount_subjects = len(subjects)
amount_days = 3
amount_time_interval = int(3 / 0.5)
dp = [[[] for i in range(amount_subjects)] for j in range(amount_time_interval)]
i = 0
for j in range(amount_time_interval):
    current_time = (j + 1) * 0.5
    if subjects[i][1] <= current_time:
        dp[i][j] += [subjects[i]]
for i in range(1, amount_subjects):
    for j in range(amount_time_interval):
        current_time = (j + 1) * 0.5
        if current_time >= subjects[i][1]:
            main = subjects[i][2]
            index = int((current_time - subjects[i][1]) / 0.5) - 1
            if index >= 0:
                for k in dp[i - 1][index]:
                    main += k[2]
            main_prev = 0
            for k in dp[i - 1][j]:
                main_prev += k[2]
            if dp[i - 1][j] != []:
                if main >= main_prev:
                    if index >= 0:
                        dp[i][j] = dp[i - 1][index] + [subjects[i]]
                    else:
                        dp[i][j] = [subjects[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = [subjects[i]]
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])


