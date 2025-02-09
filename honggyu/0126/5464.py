from collections import deque
import sys

def parking_lot_income(N, M, rates, weights, events):

    parking=[None]*N 
    q=deque()
    income=0 

    for event in events:
        if event>0:  
            
            car_index=event-1 
            q.append(car_index) 

            for i in range(N):

                if parking[i] is None: 
                    parked_car=q.popleft() 
                    parking[i]=parked_car 
                    break




        else: 

            car_index = -event-1 
            for i in range(N):

                if parking[i]==car_index:  
                    income+=rates[i]*weights[car_index]
                    parking[i]=None 


                    if q:
                        next_car = q.popleft()  
                        parking[i] = next_car 
                    break





    return income



input = sys.stdin.read
data = input().splitlines()


N, M = map(int, data[0].split())
rates = [int(data[i + 1]) for i in range(N)]
weights = [int(data[i + 1 + N]) for i in range(M)]
event = [int(data[i + 1 + N + M]) for i in range(2 * M)]



result = parking_lot_income(N, M, rates, weights, event)
print(result)
