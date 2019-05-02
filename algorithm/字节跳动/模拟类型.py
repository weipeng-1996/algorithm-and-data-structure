


def find_finsh_time(time_ideas, n_chengxuyuan, n_idea):
    time = 0
    zhixining_ideas = []
    finsh_ideas = []
    pm_ideas_dic = {}
    n_xinyou_ideas = 0
    while True:
        time += 1
        if zhixining_ideas != []:
            deleted_ideas = []
            for i in zhixining_ideas:
                i[3] -= 1
                if i[3] == 0:
                    deleted_ideas.append(i)
            for i in deleted_ideas:
                zhixining_ideas.remove(i)
                n_chengxuyuan += 1
                i.append(time)   # 5:执行完成时间
                finsh_ideas.append(i)
        if zhixining_ideas == [] and n_idea == 0:
            break
        for t in time_ideas:
            if t == time:
                for i in time_ideas[t]:
                    if i[0] not in pm_ideas_dic:
                        pm_ideas_dic[i[0]] = []
                    pm_ideas_dic[i[0]].append(i)
                    n_xinyou_ideas += 1
                break
        while n_chengxuyuan > 0 and n_xinyou_ideas > 0:
            pm_want_idea = []
            for i in pm_ideas_dic:
                if pm_ideas_dic[i] != []:
                    pm_want_idea.append(
                        min(pm_ideas_dic[i], key=lambda s: (-s[2], s[3], s[1])))
            if pm_want_idea != []:
                want_idea = min(pm_want_idea, key=lambda s: (s[3], s[0]))
                zhixining_ideas.append(want_idea)
                pm_ideas_dic[want_idea[0]].remove(want_idea)
                n_idea -= 1
                n_xinyou_ideas -= 1
                n_chengxuyuan -= 1
    finsh_ideas = sorted(finsh_ideas, key=lambda s: s[4])
    for i in finsh_ideas:
        print(i[5])


[n_pm, n_chengxuyuan, n_idea] = [int(i) for i in input().strip().split()]
time_ideas = {}
for i in range(n_idea):
    # 0:pm序号，1：提出时间，2：优先等级，3：所需时间,4：任务序号
    idea = [int(i) for i in input().strip().split()]
    idea.append(i)
    if idea[1] not in time_ideas:
        time_ideas[idea[1]] = []
    time_ideas[idea[1]].append(idea)
find_finsh_time(time_ideas, n_chengxuyuan, n_idea)
