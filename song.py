class Song:

    def __init__(self, name: str, length: float, single: bool) -> None:
        self.name = name
        self.length = length
        self.single = single

    def get_info(self) -> str:
        # Ensure length is displayed with two decimal places
        return f"{self.name} - {self.length:.2f}"
