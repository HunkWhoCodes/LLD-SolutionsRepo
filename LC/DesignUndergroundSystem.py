# https://leetcode.com/problems/design-underground-system/
# Difficulty: Medium

# Complexity:
# Time: O(1)
# Space: O(P + S^2)
# Where P = Number of Passengers making concurrent journey at peak time, stored in check_in table
# S = Number of stations in network, S^2 because we have in worst case all pair of stations as both to and fro

# Idea:
# In one hash table we keep a track of customer check-in station and times
# In another we store the start and end station tuple as key and total time so far and number of trips tuple as value
# When checkout is called, if new trip, we add it to the trips hash table
# If old trip is called (i.e. if already in hash tbale), then we add current time to total time and increment trips by 1

# When get avg is called, we simply get the total for the station tuple and divide it by corresponding trips count

# Note on storing avg times vs storing total times
# I had earlier used avg and count but it was not passing all test cases, not sure if due to Floating point error
# Or simply in calculating new average
# But I found it's much simpler to simply use a total time variable and total trip count variable
# And return the division result of these two

# Note on 2 vs 3 hash tables:
# In my solution first I used three hash maps, for check in, checkout and trips to store times and trip counts
# But the checkout hash map is not really needed as we don't need this data later / any time
# For checkout, function call params are enough and only time they're used
# So removed the checkout times hash table and this still works and saves little bit of memory

class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.trips = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:   
        time = t - self.check_in[id][1]
        start = self.check_in[id][0]  
                
        t = (start, stationName)
        
        if t not in self.trips:
            self.trips[t] = (time, 1)
        else:
            total_time = self.trips[t][0] + time
            trips = self.trips[t][1] + 1
            self.trips[t] = (total_time, trips)
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t = (startStation, endStation)
        return self.trips[t][0] / self.trips[t][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
