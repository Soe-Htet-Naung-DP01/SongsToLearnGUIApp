import csv
import sys
from song import Song
from songcollection import SongCollection
"""
Name: Soe Htet Naung
Date started:26 April 2020 (5pm)
GitHub URL:https://github.com/JCUS-CP1404/assignment-01-songs-app-Soe-Htet-Naung
"""
"""
This Program will help the users to make a list of the songs that the users wished to be learn
and keep track of the updated status of the learned songs and unlearned songs in the list.
The users may add more songs to the list and mark the songs as learned when they choose to complete them.
"""

song_list = SongCollection()


def main():
    """The main function will handle the menu input part and the rest by calling other functions"""
    song_list.load_songs('songs.csv')
    execute_menu()


def list_out_songs():
    """This will get the list of songs and get the counts of the list number(instead of using index) and unlearned"""
    list_numb = 0
    unlearned_songs = 0

    for row in song_list.songs:
        if row[3] == "Learned":
            list_numb += 1
            print("{:>2}. {:<{}} by {:>{}} Year {}".format(list_numb, row[0], 20, row[1], 20, row[2]))
        else:
            list_numb += 1
            print("*{}. {:<{}} by {:>{}} Year {}".format(list_numb, row[0], 20, row[1], 20, row[2]))
            unlearned_songs += 1
    return unlearned_songs


def show_menu():
    """Menu Output"""
    print("Menu:")
    print("L - List songs")
    print("A - Add new place")
    print("C - Mark a song as learned")
    print("Q - Quit")


def execute_menu():
    """Menu Function: this will execute and handle the whole process of menu and input errors
        Then add the newly input data to the list after verifying
    """
    show_menu()

    menu_choice = input("Please choose from options below: ").upper()
    if menu_choice == "L":
        unlearned_songs = list_out_songs()

        if unlearned_songs > 0:
            print("{} songs. You still have {} songs to learn.".format(unlearned_songs, unlearned_songs))
        else:
            print("No unlearned songs.")

    elif menu_choice == "A":
        title = input("Title: ")
        while title == "":
            print("Please enter a song!")
            title = input("Title: ")
        addition_list = []
        addition_list.append(title)

        artist = input("Artist: ")
        while artist == "":
            print("Please enter the name of artist!")
            artist = input("Artist: ")
        addition_list.append(artist)

        year = input("Year: ")
        while year != "":
            try:
                val = int(year)
                print("Input number value is: ", val)
                break
            except ValueError:
                print("That's not an number!")
                print("Please input a valid number.")
                year = input("Year: ")

        addition_list.append(year)
        addition_list.append("Unlearned")
        song_list.songs.append(addition_list)

    elif menu_choice == "C":
        unlearned_songs = list_out_songs()
        rows = 0
        if unlearned_songs == 0:
            print("There are no more unlearned places.")
        else:
            mark_as_learned = input("Which song would you like to mark as learned?: ")
            for song in song_list.songs:
                rows += 1
                if mark_as_learned in song:
                    index_numb = song_list.songs.index(song)
                    song_list.songs[index_numb][3] = "Learned"
                    print("The list has been updated!")
                    break
                else:
                    print("This is not in row {}.".format(rows))
    elif menu_choice == "Q":
        song_list.save_file('songs.csv')
        print("Thank you and goodbye!")
        sys.exit()
    else:
        print("That was an invalid input.")
        execute_menu()

    execute_menu()


if __name__ == '__main__':
    main()
