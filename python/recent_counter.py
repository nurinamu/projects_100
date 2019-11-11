class RecentCounter:
    def __init__(self):
        self.pings = []
        return

    def ping(self, t: int) -> int:
        self.pings.append(t)
        for idx in range(0,len(self.pings)) :
            if self.pings[idx] >= t - 3000 :
                self.pings = self.pings[idx:]
                break
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))
    print(rc.ping(100))
    print(rc.ping(3001))
    print(rc.ping(3002))