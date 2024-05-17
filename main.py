"""
Name: Soe Htet Naung
Date: 27/5/2020
Brief Project Description: This application/program will keep track of a list of songs that user wants to learn.
user may also add new songs to the list and edit the status of learned and unlearned. User may also see how many of
songs are learned and how many are left to learn.
GitHub URL: https://github.com/JCUS-CP1404/assignment-02-songs-app-Soe-Htet-Naung
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from songcollection import SongCollection
from song import Song


class SongsToLearnApp(App):
    status_text = StringProperty()
    current_sort = StringProperty()
    learning_status_text = StringProperty()

    def __init__(self, **kwargs):
        """This initializes the song list"""
        super().__init__(**kwargs)
        song_lists = SongCollection()
        self.app_list = song_lists.load_songs('songs.csv')

    def build(self):
        """This will build the kivy app"""
        self.title = "Songs to Learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()

        return self.root

    def clear_input(self):
        """Resets the text entry/input fields"""
        self.root.ids.input_title.text = ""
        self.root.ids.input_artist.text = ""
        self.root.ids.input_year.text = ""

    def create_widgets(self):
        """Creates buttons from list of objects and add them to the GUI along with some labels after formatting them."""
        self.status_text = "Click on a song to change it to To Learn/Learned."
        for song in self.app_list:
            temp_button = Button(
                text="{} by {}, ({}) ({})".format(song[0], song[1], song[2], song[3]))
            temp_button.bind(on_release=self.press_entry)
            temp_button.song = song
            if song[3] == "Unlearned":
                temp_button.background_color = [1, 0.5, 0.5, 1]
            else:
                temp_button.background_color = [0.5, 1, 1, 0.5]
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """this function will change the songs' learned/unlearned status when pressed
            at the same time, it will also update the songs how many are left to learn and
            how many of them are learned
        """
        learned_songs = 0
        unlearned_songs = 0
        song = instance.song
        if song[3] == "Learned":
            song[3] = "Unlearned"
        else:
            song[3] = "Learned"
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()
        """
        This part will get the counts of learned and to learn songs from the entire list including unsaved ones
        """
        if song[3] == "Learned":
            self.status_text = "You learned {}.".format(song[0])
        elif song[3] == "Unlearned":
            self.status_text = "You need to learn {}.".format(song[0])
        for song in self.app_list:
            if song[3] == "Learned":
                learned_songs += 1
            else:
                unlearned_songs += 1
        self.learning_status_text = "To Learn: {}, Learned: {}".format(unlearned_songs, learned_songs)

    def add_song(self):
        """This will add new song to the list if add song button is pressed"""
        temp_list = []
        title = self.root.ids.input_title.text
        artist = self.root.ids.input_artist.text
        try:
            """
            This part will catch the errors and return error messages accordingly
            """
            year = int(self.root.ids.input_year.text)
            if year <= 0:
                self.status_text = "Year must be >= 0"
            elif title.strip() == "" or artist.strip() == "" or year == "":
                self.status_text = "All fields must be filled in."
            else:
                """If there is no error being caught, the data will be added to temporary list"""
                temp_list.append(title)
                temp_list.append(artist)
                temp_list.append(year)
                temp_list.append("Unlearned")
                self.app_list.append(temp_list)
                self.root.ids.entries_box.clear_widgets()
                self.create_widgets()
                self.status_text = "{} has been added.".format(title)
        except ValueError:
            self.status_text = "Please Enter a valid number for Year"

    def sort_artist(self):
        """sort the list based on artist names"""
        from operator import itemgetter
        self.app_list.sort(key=itemgetter(1))
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        # gets rid of the old widgets
        self.create_widgets()

    def sort_year(self):
        """sort the list based on the year released"""
        from operator import itemgetter
        self.app_list.sort(key=itemgetter(2))
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        # gets rid of the old widgets
        self.create_widgets()

    def sort_title(self):
        """sort the list on alphabetical order by name of songs/titles"""
        self.app_list.sort()
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        # gets rid of the old widgets
        self.create_widgets()

    def sort_learned(self):
        """sort the list according to learned or not"""
        from operator import itemgetter
        self.app_list.sort(key=itemgetter(3), reverse=False)
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        # gets rid of the old widgets
        self.create_widgets()

    def on_stop(self):
        """writes the newly updated csv file/ the temporary list from add_song will now be saved"""
        import csv
        with open('songs.csv', 'w', newline='') as f:
            # takes out the empty row in between
            writer = csv.writer(f)
            writer.writerows(self.app_list)

    pass


if __name__ == '__main__':
    SongsToLearnApp().run()
