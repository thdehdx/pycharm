def solution(bridge_length, weight, truck_weights):
    answer = 0
    listTrack=[]
    waitNum=len(truck_weights)
    passNum=0
    while(True):
        answer+=1
        if len(listTrack)==bridge_length:
            if listTrack[0]!=0:
                passNum+=1
                if passNum==waitNum:
                    break
            del listTrack[0]#앞차 다리 건넘

        if len(truck_weights)!=0:
            if sum(listTrack)+truck_weights[0]<=weight:
                listTrack.append(truck_weights[0])
                del truck_weights[0]
            else:
                listTrack.append(0)
        else:
            listTrack.append(0)
    return answer