class Pet:
    """Ramverk som låter användare skapa husdjur."""

    def __init__(self, name=' '):
        """Initialisera variabler som namn, art och en lista med leksaker.

        name -- husdjurets namn
        """
        self.name = name
        self.kind = ""
        self.toys = []

    def add_toy(self, toy):
        """Lägger till en leksak i husdjurets lista med leksaker."""
        self.toys.append(toy)

    def __str__(self):
        """Returnerar en string med info om husdjurets."""
        if len(self.toys) > 0:
            return "{} är en {} som har följande leksaker: {}.".format(
                self.name, self.kind, ", ".join(self.toys))
        return "{} är en {} som inte har några leksaker.".format(
            self.name, self.kind)
