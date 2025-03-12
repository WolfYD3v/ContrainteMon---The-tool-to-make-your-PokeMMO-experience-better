# Créé par PC, le 11/03/2025 en Python 3.7
import random
import json

def calculate_events_probabilities() :
    for event in events :
        events_probabilities[event] = 100/len(events)

def get_events_probabilities() :
    return events_probabilities

def select_random_event() :
    random_event = ""
    event_probability = random.randint(0 , 100)
    temp_prob = 0.0
    for loop in range(len(events_probabilities)-1) :
        if temp_prob > event_probability < temp_prob + events_probabilities[events[loop+1]] :
            random_event = events[loop]
            return random_event
        temp_prob += events_probabilities[events[loop]]
    return events[0]

def re_calculate_events_probabilities(event_taken) :
    act_events = events.copy()
    if event_taken in events_probabilities :
        if events_probabilities[event_taken] > 0.0 :
            if events_probabilities[event_taken] - low_ev > 0.0 :
                events_probabilities[event_taken] -= low_ev
                act_events.remove(event_taken)
        for event in act_events :
            events_probabilities[event] += low_ev / len(act_events)
    return

datas = None
with open("C:/Users/PC/Desktop/ContrainteMon/datas.json", "r") as f:
    datas = json.load(f)
events = datas["events"]
events_probabilities = datas["event probabilities"]
low_ev = 1.5

def get_event() :
    if events_probabilities == {} :
        calculate_events_probabilities()
        print("Events probabilities has been calculated")
        get_event()
    else :
        ev = select_random_event()
        print(f"Selected event => {ev}")
        re_calculate_events_probabilities(ev)
    with open("C:/Users/PC/Desktop/ContrainteMon/datas.json", "w") as f:
        json.dump({"events" : events , "event probabilities" : events_probabilities} , f , indent=4)
    return "Event selected :" + "\n" + ev