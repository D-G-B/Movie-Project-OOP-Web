class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

    def to_dict(self):
        return {
            "year": self.year,
            "rating": self.rating,
        }

    @classmethod
    def from_dict(cls, title, data):
        return cls(title, data["year"], data["rating"])

    def __str__(self):
        return f"{self.title} ({self.year}) : {self.rating}"
