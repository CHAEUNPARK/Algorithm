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

record = [
    "Enter uid1234 Muzi"
    , "Enter uid4567 Prodo"
    , "Leave uid1234"
    , "Enter uid1234 Prodo"
    , "Change uid4567 Ryan"
]

answer = solution(record)

for ans in answer:
    print(ans)