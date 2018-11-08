#방송하고자 하는 주
states_needed = set(["mt", "wa", "or", "id", "nv","ut", "ca","az"])

#방송국 목록
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

#방문할 방송국의 목록
final_stations = set()

while states_needed:

    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():

        covered = states_needed & states_for_station

        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
