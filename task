class Task:
    def __init__(self, task_id, description, done):
        self.task_id = task_id
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True

    def done_to_symbol(self):
        if self.done:
            return 'X'
        return ''

    def __str__(self):
        return "ID: {}. [{}] {}".format(self.task_id, self.done_to_symbol(), self.description)
