import task
import task_list
import os


class TodoApp():
    """Program som låter användare skapa todolistor i terminalen."""

    def __init__(self):
        """Skapar kommandon och startar main funktionen."""
        # Ett dictionary med kommandon där key'n är kommandot
        # och value är en beskrivning av kommandot
        self.commands = {
            "?": "Hjälp - används för att visa listan av kommando",
            "q": "Avsluta - avslutar programmet",
            "add": "Lägg till - Lägger till en uppgift",
            "tasks": "Uppgifter - visar kommandon",
            "finish": "Avsluta - avslutar en uppgift",
            "change": "Ändra - Ändra vilken tasklist du vill arbeta med",
            "add_list": "Lägg till - Lägger till en uppgiftslista",
            "show_lists": "Visa listor - visar alla uppgiftslistor"}

        # 'game-loop' programmet körs / 'uppdateras' då update är sant
        self.update = True
        # en lista av tasklistor
        self.tasklists = []
        # uppgiftslistan som användaren behandlar
        self.current_tasklist = None
        self.main()

    def show_commands(self):
        """Printar ut alla kommandon och deras beskrivningar."""
        for command, command_description in self.commands.items():
            print(" " + command + ": " + command_description)

    def add_tasklist(self):
        """Lägger till en uppgiftslista."""
        # Frågar användaren om namnet på den nya uppgiftslistan
        name = input("Ange namn på ny uppgiftslista: ")
        # Returnerar ett error-meddelande om listan med namnet redan finns
        if bool(self.get_tasklist(name)):
            return("ERROR!! uppgiftslistan finns redan!!")
        self.tasklists.append(task_list.TaskList(name))
        self.open_tasklist(name)
        return("{} har lagts till!!".format(name))

    def get_tasklist(self, name):
        """Returnerar uppgiftslistan med namnet 'name' (om den finns)."""
        for tasklist in self.tasklists:
            if name == tasklist.name:
                return tasklist
        return None

    def show_tasklists(self):
        """Printar ut alla uppgiftslistor."""
        for tasklist in self.tasklists:
            print(tasklist.name)

    def open_tasklist(self, name):
        """Öppnar uppgiftslistan med namnet 'name'."""
        self.current_tasklist = self.get_tasklist(name)

    def change_tasklist(self):
        """Ändrar uppgiftslistan som användaren hanterar."""
        self.show_tasklists()
        # Öppnar uppgiftslistan med namnet som användaren anger
        # om den finns, annars returneras ett error meddelande
        name = input("Ange namnet på listan du vill byta till: ")
        if bool(self.get_tasklist(name)):
            self.open_tasklist(name)
            return "Du har ändrar lista till {}!".format(name)
        return "AJ! listan finns ej!"

    def new_task(self):
        """Lägger till en uppgift i den nuvarande uppgiftslistan."""
        description = input("Ange beskrivning: ")
        self.current_tasklist.create_task(description)

    def show_tasks(self):
        """Visar uppgiftslistan som användaren arbetar med."""
        print(self.current_tasklist)

    def mark_done(self):
        """Markerar en uppgift som klar."""
        print("Ange uppgift ID't")
        self.show_tasks()
        # Frågar användaren om ID'et av uppgiften som den vill slutföra
        # och slutför uppgiften om den finns, annars returneras ett
        # felmeddelande
        task_id = input("ID: ")
        if self.current_tasklist.mark_done(task_id):
            self.show_tasks()
            return "uppgiften är klar"
        return "Denna uppgift finns inte!! Försök igen."

    def is_command_valid(self, user_command):
        """Returnerar sant eller falskt baserat på om en kommand finns."""
        for command in self.commands.keys():
            if user_command == command:
                return True
        return False

    def does_tasklists_exist(self):
        """Returnerar sant om uppgiftslistor finns, annars falskt."""
        if len(self.tasklists) > 0:
            return True
        return False

    def quit(self):
        """Avslutar programmet genom att få det att sluta uppdatera."""
        self.update = False

    def enter_command(self, user_command):
        """Utför en funktion baserat på kommanden användaren anger.

        user_command -- en string command som användaren har angett
        """
        # Kollar om kommanden finns, printar annars ett felmeddelande
        if self.is_command_valid(user_command):
            command_keys = list(self.commands.keys())
            # Visar kommandon om kommanden är hjälp
            if user_command == command_keys[0]:
                self.show_commands()
            # Avslutar programmet
            if user_command == command_keys[1]:
                self.quit()
            # Skapar en ny uppgift
            if user_command == command_keys[2]:
                self.new_task()
            # Visar uppgifterna
            if user_command == command_keys[3]:
                self.show_tasks()
            # Markerar en uppgift som klar
            if user_command == command_keys[4]:
                print(self.mark_done())
            # Ändrar uppgiftslista
            if user_command == command_keys[5]:
                print(self.change_tasklist())
            # Lägger till en uppgiftslista
            if user_command == command_keys[6]:
                self.add_tasklist()
            # Visar alla listor
            if user_command == command_keys[7]:
                self.show_tasklists()
        else:
            print("ERROR! kommanden '{}' finns inte!!".format(user_command))

    def main(self):
        """Huvud funktion, kör igenom programmet tills update är falskt."""
        while self.update:
            # Clearar konsol fönstret
            os.system('cls' if os.name == 'nt' else 'clear')
            # Om uppgiftslistor existerar körs programmet som vanligt
            # annars begärs användaren att skapa en uppgiftlista
            if self.does_tasklists_exist():
                print("Välkommen! Du befinner dig i listan {}".format(
                    self.current_tasklist.name))
                self.enter_command(input("Ange kommando (q=avsluta, ?=hjälp): "))
            else:
                print("Välkommen, det finns inga uppgiftslistor!")
                print(self.add_tasklist())
            # Input funktion som väntar på användaren
            input()
        exit()

