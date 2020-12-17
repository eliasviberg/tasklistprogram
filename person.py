import dataseries


class Person:
    """Klass som låter användare skapa personer."""

    def __init__(self, name, birthyear, ID):
        """Skapar en person.

        name -- personens namn
        birthyear -- ett heltal som representerar då personen föddes
        ID -- personens unika kodifierade identitet
        """
        self.name = name
        self.birthyear = birthyear
        self.ID = ID
        # Ett godtyckligt antal mätserier
        self.dataseries_collection = []

    def add_dataseries(self, filename):
        """Lägger till en mätserie."""
        self.dataseries_collection.append(dataseries.DataSeries(filename))

    def __str__(self):
        """Returnerar en sträng med information om personen."""
        data_prints = []
        for dataser in self.dataseries_collection:
            data_prints.append(str(dataser))
            # Fråga om denna är för lång!!!
        return " Namn: {} \n Födelseår: {} \n Kod: {} \n Antal mätseries: {} \n {}".format(self.name, self.birthyear, self.ID, len(self.dataseries_collection), "\n ".join(data_prints))
