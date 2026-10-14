# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
      self.tracks = []

    def add(self, track):
        # se:
        #   track: a string showing the track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        pass # No code here yet

    def show_tracks(self):
        # Returns:
        #   showing a list of tracks
        # Side-effects:

        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
check for a empty list

"""
tracker = MusicTracker()
assert tracker.show_tracks == []

"""
add track

"""
tracker = MusicTracker()
tracker.add("123 bob")
assert tracker.display() == ["123 bob"]


tracker = MusicTracker()
tracker.add("123 bob")
tracker.add("123456")
assert tracker.display() == ["123 bob", "123456"]

"""
show list of the tracks added

"""
tracker = MusicTracker()
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
