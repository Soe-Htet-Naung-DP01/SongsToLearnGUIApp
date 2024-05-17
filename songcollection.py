import csv
from song import Song


class SongCollection:

    def __init__(self, songs=[]):
        """This function will initialize the song list"""
        self.songs = songs

    def load_songs(self, file):
        """This function will load the songs from the song.csv file that is passed into the parameter and
            change u and l into unlearned and learned
        """
        with open(file, 'r') as f:
            reader = csv.reader(f)
            self.songs = list(reader)
            for i in self.songs:
                i[2] = int(i[2])
                if i[3] == 'u':
                    i[3] = 'Unlearned'
                elif i[3] == 'l':
                    i[3] = 'Learned'
            return self.songs

    def add_song(self, song):
        """
        this function will create a temporary list for newly added songs before saving them into the actual song.csv
        """
        temp_list = []
        temp_list.append(song.title)
        temp_list.append(song.artist)
        temp_list.append((song.year))
        temp_list.append(song.check_learned())
        self.songs.append(temp_list)
        return self.songs

    def save_file(self, file):
        """This function will saves the updated song list"""
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.songs)
        print("Your file has been updated and saved!")

    def sort_title(self, list_to_sort):
        """this function will sort the list of songs by the order of title alphabetically"""
        list_to_sort.sort()
        return list_to_sort

    def sort_artist(self, list_to_sort):
        """this function will sort the list of songs by the order of artist alphabetically"""
        from operator import itemgetter
        list_to_sort.sort(key=itemgetter(1))
        return list_to_sort

    def sort_year(self, list_to_sort):
        """this function will sort the list of songs by the ascending order of years released"""
        from operator import itemgetter
        list_to_sort.sort(key=itemgetter(2))
        return list_to_sort

    def sort_learned(self, list_to_sort):
        """this function will sort the list of songs by the order of learning status"""
        from operator import itemgetter
        list_to_sort.sort(key=itemgetter(3), reverse=False)
        return list_to_sort

    def __repr__(self):
        return str(self.songs)

    pass
