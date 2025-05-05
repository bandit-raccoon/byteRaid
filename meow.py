import random
import time

# This program randomly selects a cat emoji from a list and prints it.
catMoji = [
    '🐱', '🐈', '🐈‍⬛', '😹', '😻', '🙀', '😿', '😸', '😺', '😾', '😼', '😽', '😺‍', '🐾',
    '🐶', '🐕', '🐕‍🦺', '🐩', '🦮', '🐺', '🦊', '🦝', '🐰', '🐇', '🐹', '🐭', '🐀', '🐁',
    '🐻', '🐻‍❄️', '🐨', '🐼', '🦥', '🦦', '🦨', '🦘', '🦡', '🐾', '🦃', '🐔', '🐓', '🐣',
    '🐤', '🐥', '🐦', '🐧', '🕊️', '🦅', '🦆', '🦉', '🦤', '🪶', '🦇', '🐗', '🐴', '🦄',
    '🐝', '🪲', '🐛', '🦋', '🐌', '🐞', '🐜', '🪳', '🦂', '🕷️', '🕸️', '🦟', '🦠', '🐢',
    '🐍', '🦎', '🐙', '🦑', '🦀', '🦞', '🦐', '🦪', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋',
    '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🦧', '🐘', '🦏', '🦛', '🐪', '🐫', '🦒', '🐃',
    '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🦙', '🐐', '🦌', '🐕‍🦺', '🐩', '🐕', '🐈', '🐓'
]
# Randomly select a cat emoji from the list
emoji = random.choice(catMoji)


def meow():
    print(emoji)
    time.sleep(0.01)

while emoji != catMoji[3]:
    emoji = random.choice(catMoji)
    meow()