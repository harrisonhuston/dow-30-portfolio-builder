# Creates class Rating
class Rating:
    """The class is used to allow the user to rate the portfolio."""

    # Def __init__ rate, upper_rate, lower_rate, score
    def __init__(self, rate, upper_rate, lower_rate, score):
        """__init__ constructor for class Rating."""
        self.__rate = rate
        self.upper_rate = upper_rate
        self.lower_rate = lower_rate
        self.score = score

    # Def __lt__ returns true if rate is less than the upper rate
    def __lt__(self, rate, upper_rate):
        """Less than dunder/magic method for class Rating."""
        self.__rate = rate
        self.upper_rate = upper_rate
        return self.__rate < upper_rate

    # Def __gt-- returns true if rate is greater than the lower rate
    def __gt__(self, rate, lower_rate):
        """Greater than dunder/magic method for class Rating."""
        self.__rate = rate
        self.lower_rate = lower_rate
        return self.__rate > lower_rate

    # Def rating, if rating is less than 4 return low rate, greater than 7 return high rate
    # If rating is either equal to 4 or higher and either equal to 7 or lower, return mid rate
    def rating(self, low_rate, mid_rate, high_rate, rate):
        """Rating method for class Rating. Used to segment rating scale."""
        self.__rate = rate
        self.low_rate = low_rate
        self.mid_rate = mid_rate
        self.high_rate = high_rate
        if self.__rate < 4:
            return self.low_rate
        if 4 <= self.__rate <= 7:
            return self.mid_rate
        if self.__rate > 7:
            return self.high_rate

    # Def __repr__ returns score as repr
    def __repr__(self):
        """__repr__ method for class Rating."""
        self.score = repr(self.score)
        return self.score

# Portfolio testing with assert and prints for if __name == "__main__"
# Correct prints are '5', True, True, mid rate
if __name__ == "__main__":
    rate = 5
    portfolio_name = "Test Portfolio"
    p = Rating(rate=rate, upper_rate=11, lower_rate=0, score=rate)
    assert p.__repr__()
    print(p.__repr__())
    assert p.__lt__(rate=rate, upper_rate=11)
    print(p.__lt__(rate=rate, upper_rate=11))
    assert p.__gt__(rate=rate,lower_rate=0)
    print(p.__gt__(rate=rate,lower_rate=0))
    assert p.rating(rate=rate, low_rate="low rate", mid_rate="mid rate", high_rate="high rate")
    print(p.rating(rate=rate, low_rate="low rate", mid_rate="mid rate", high_rate="high rate"))


