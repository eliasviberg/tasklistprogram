import task


class TaskList():

    def __init__(self, name, task_counter=0):
        """Initialiserar classvariabler.
        
        self.task_counter räknar antalet uppgifter i listan
        self.task_list är listan där uppgifter lagras
        self.name är namnet på den specifika listan
        """
        self.task_counter = task_counter
        self.task_list = []
        self.name = name

    def create_task(self, description):
        """Lägger till en ny uppgift i listan task_list.
        
        namges genom description som tas in som argument
        skriver ut namn på uppgift och namn på listan'
        """
        self.task_counter += 1
        self.task_list.append(task.Task(self.task_counter, description, False))
        print("Du har lagt till {} i {}!".format(description, self.name))

    def mark_done(self, task_id):
        """Markerar en uppgift som klar baserat på argumentet task_id.

        kallar på funktionen mark_done()
        returnerar en boolean
        """
        for current_task in self.task_list:
            if int(task_id) == current_task.task_id:
                current_task.mark_done()
                return True
        return False

    def __str__(self):
        """Skriver ut alla task i task_list som en sträng."""
        if self.task_counter == 0:
            return "Det finns inga uppgifter!!!"
        task_print = ""
        for task in self.task_list:
            task_print += (str(task) + "\n")
        return task_print
        


        
