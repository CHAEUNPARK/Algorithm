# 예외처리 아직 안됨

def solution(record):
    answer = []
    events = []
    dict = {}
    for i in record:
        split = i.split(" ")
        if split[0] == "Enter" or split[0] == "Leave":
            events.append([split[0], split[1]])
        if split[0] == "Enter" or split[0] == "Change":
            dict[split[1]] = split[2]

    for event in events:
        result = f"{dict[event[1]]}"
        if event[0] == "Enter":
            result = result + "님이 들어왔습니다."
        else:
            result = result + "님이 나갔습니다."
        answer.append(result)
    return answer

idDict = dict()
def solution_else(record):
    answer = []
    logList = []
    for e in record:
        dataList = e.split(" ")
        if dataList[0] == "Leave":
            logList.append([dataList[1], "님이 나갔습니다."])
        elif dataList[0] == "Enter":
            idDict[dataList[1]] = dataList[2]
            logList.append([dataList[1], "님이 들어왔습니다."])
        elif dataList[0] == "Change":
            idDict[dataList[1]] = dataList[2]
    print(logList)
    for log in logList:
        answer.append(idDict[log[0]] + log[1])
    return answer
record = [
    "Enter uid1234 Muzi"
    , "Enter uid4567 Prodo"
    , "Leave uid1234"
    , "Enter uid1234 Prodo"
    , "Change uid4567 Ryan"
]

answer = solution(record)
answer_else = solution_else(record)
for ans in answer:
    print(ans)

for ans in answer_else:
    print(ans)