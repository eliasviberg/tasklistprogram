class DataSeries:
    """DataSeries klass som låter användare konvertera data filer till kod."""

    def __init__(self, filename):
        """Skapar och laddar in en dataserie till listan 'values'.

        filename -- namnet på filen som DataSeries ska ladda in data från
        """
        self.values = []
        self.load_data(filename)

    def load_data(self, filename):
        """Laddar data från 'filename' och mappar den till listan 'values'."""
        with open("/" + filename, 'r') as reader:
            self.values = list(map(int, reader.readlines()))

    def get_max_value(self):
        """Returnerar det högsta värdet i values."""
        return max(self.values)

    def get_min_value(self):
        """Returnerar det lägsta värdet i values."""
        return min(self.values)

    def get_avg_value(self):
        """Returnerar det genomsnittliga värdet i values."""
        return sum(self.values) / len(self.values)

    def __str__(self):
        """Returenar en sträng med information om dataserien."""
        return "{} mätpunkter. Max: {}. Min: {}. Medel:{}".format(
            len(self.values), self.get_max_value(),
            self.get_min_value(), self.get_avg_value())
