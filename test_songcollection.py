"""(Incomplete) Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection


def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert not song_collection.songs  # an empty list is considered False

    # Test loading songs
    print("Test loading songs:")
    song_collection.load_songs('songs.csv')
    print(song_collection)
    assert song_collection.songs  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)

    # Test sorting songs
    # Test sorting songs
    print("Test sorting - Title:")
    song_collection.sort_title(song_collection.songs)
    print(song_collection)

    print("Test sorting - Artist:")
    from operator import itemgetter
    song_collection.songs.sort(key=itemgetter(1))
    print(song_collection)

    print("Test sorting - by learning status")
    song_collection.sort_learned(song_collection.songs)
    print(song_collection)

    print("Test sorting - by Year")
    song_collection.sort_year(song_collection.songs)
    print(song_collection)

    """save file from songs list in csv file"""
    print("Test saving:")
    song_collection.save_file('songs.csv')



run_tests()
