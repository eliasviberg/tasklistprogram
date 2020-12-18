class Task:
    def __init__(self, task_id, description, done):
        """Initialiserar classvariabler.

        self.task_id är ett unikt id varje uppgift tilldelas
        self.description är beskrivningen av uppgiften
        self.done är en boolean som beskriver om en uppgift är klar eller ej
        """
        self.task_id = task_id
        self.description = description
        self.done = done

    def mark_done(self):
        """Markerar en uppgift som klar."""
        self.done = True

    def done_to_symbol(self):
        """Returnerar strängen X vid uppgiften om den är klar."""
        if self.done:
            return 'X'
        return ''

    def __str__(self):
        """Skriver task_id, done_to_symbol() och description som en sträng."""
        return "ID: {}. [{}] {}".format(self.task_id, self.done_to_symbol(), self.description)
