from lib.music_tracker import *


def test_check_for_empty_list():
    tracker = MusicTracker()
    assert tracker.show_tracks() == []

def test_add_tracks():
    tracker = MusicTracker()
    tracker.add("123 bob")
    assert tracker.show_tracks() == ["123 bob"]

def test_add_multiple_tracks():
    tracker = MusicTracker()
    tracker.add("123 bob")
    tracker.add("123456")
    assert tracker.show_tracks() == ["123 bob", "123456"]
