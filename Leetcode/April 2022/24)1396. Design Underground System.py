class UndergroundSystem:

    def __init__(self):
        self.travel_count = defaultdict(int) # (station_1, station_2) -> count
        self.travel_time = defaultdict(int) # (station_1, station_2) -> time
        self.checked_into = {} # customer_id -> (station, time)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checked_into: return
        self.checked_into[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checked_into: return
        from_station, start_time = self.checked_into.pop(id)
        self.travel_count[(from_station, stationName)] += 1
        self.travel_time[(from_station, stationName)] += t - start_time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        if key not in self.travel_count: return 0
        return self.travel_time[key] / self.travel_count[key]
    