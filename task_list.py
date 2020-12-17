import task


class TaskList():

    def __init__(self, name, task_counter=0):
        self.task_counter = task_counter
        self.task_list = []
        self.name = name

    def create_task(self, description):
        self.task_counter += 1
        self.task_list.append(task.Task(self.task_counter, description, False))
        print("Du har lagt till {} i {}!".format(description, self.name))

    def mark_done(self, task_id):
        if task_id.isnumeric():
            for current_task in self.task_list:
                if int(task_id) == current_task.task_id:
                    current_task.mark_done()
                    return True
        return False

    def __str__(self):
        if self.task_counter == 0:
            return "Det finns inga uppgifter!!!"
        task_print = ""
        for task in self.task_list:
            task_print += (str(task) + "\n")
        return task_print
        
