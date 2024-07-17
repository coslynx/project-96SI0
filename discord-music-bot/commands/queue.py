import discord

class Queue:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, song):
        self.queue.append(song)

    def remove_from_queue(self, index):
        if index < len(self.queue):
            del self.queue[index]

    def get_queue(self):
        return self.queue

    def clear_queue(self):
        self.queue = []

    def play_next_song(self):
        if len(self.queue) > 0:
            next_song = self.queue.pop(0)
            return next_song
        else:
            return None

    def shuffle_queue(self):
        import random
        random.shuffle(self.queue)

    def reorder_queue(self, old_index, new_index):
        if old_index < len(self.queue) and new_index < len(self.queue):
            song = self.queue.pop(old_index)
            self.queue.insert(new_index, song)

    def get_queue_length(self):
        return len(self.queue)