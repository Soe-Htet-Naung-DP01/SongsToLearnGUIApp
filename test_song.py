"""(Incomplete) Tests for Song class."""
from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)
    assert initial_song.title == "My Happiness"
    assert initial_song.artist == "Powderfinger"
    assert initial_song.year == 1996
    assert initial_song.is_learned

run_tests()
