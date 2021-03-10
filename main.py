@namespace
class SpriteKind:
    item = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    can.set_position(randint(0, 160), randint(0, 120))
    info.start_countdown(20)
    if info.score() == 10:
        game.over(True, effects.confetti)
sprites.on_overlap(SpriteKind.player, SpriteKind.item, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    info.change_score_by(-1)
    mySprite.set_position(randint(0, 160), randint(0, 120))
    if info.score() == -5:
        game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite: Sprite = None
can: Sprite = None
scene.set_background_color(11)
mike = sprites.create(img("""
        . . . . . 7 7 7 7 7 7 . . . . . 
            . . . . 7 7 7 7 7 7 7 7 . . . . 
            . . 7 7 7 7 7 7 7 7 7 7 7 7 . . 
            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
            7 7 7 7 7 7 1 1 1 1 7 7 7 7 7 7 
            7 7 7 7 7 1 8 8 8 8 1 7 7 7 7 7 
            7 7 7 7 7 1 8 1 8 8 1 7 7 7 7 7 
            7 7 7 7 7 1 8 8 8 8 1 7 7 7 7 7 
            7 7 7 7 7 7 1 1 1 1 7 7 7 7 7 7 
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
            7 7 7 2 2 7 7 7 7 7 7 2 2 7 7 7 
            7 7 7 7 2 2 2 2 2 2 2 2 7 7 7 7 
            . 7 7 7 7 2 2 2 2 2 2 7 7 7 7 . 
            . . . 7 7 7 7 7 7 7 7 7 7 . . . 
            . . . . 7 7 7 7 7 7 7 7 . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mike)
can = sprites.create(img("""
        . . . . 5 5 5 5 5 5 5 5 . . . . 
            . . . 5 5 5 5 5 5 5 5 5 5 . . . 
            . . . d d d d d d d d d d . . . 
            . . . 5 d 5 5 5 5 5 5 d 5 . . . 
            . . . 5 5 5 d d d d 5 5 5 . . . 
            . . . 5 5 5 d 2 2 d 5 5 5 . . . 
            . . . 5 5 5 d 2 2 d 5 5 5 . . . 
            . . . 5 5 5 d 2 2 d 5 5 5 . . . 
            . . . 5 5 5 d 2 2 d 5 5 5 . . . 
            . . . 5 5 5 d 2 2 d 5 5 5 . . . 
            . . . 5 5 5 d 2 2 d 5 5 5 . . . 
            . . . 5 5 5 d d d d 5 5 5 . . . 
            . . . 5 d 5 5 5 5 5 5 d 5 . . . 
            . . . d d d d d d d d d d . . . 
            . . . 5 5 5 5 5 5 5 5 5 5 . . . 
            . . . . 5 5 5 5 5 5 5 5 . . . .
    """),
    SpriteKind.item)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            a a a a a a a a . . . . . . . . 
            a a a a a a a a . . . . . . . . 
            3 3 3 3 3 3 3 3 . . . . . . . . 
            3 3 3 3 3 3 3 3 . . . . . . . . 
            3 3 3 3 3 3 3 3 . . . . . . . . 
            3 3 3 3 3 3 3 3 . . . . . . . . 
            3 3 3 3 3 3 3 3 3 3 3 3 3 . . . 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 a a 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 a a 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 a a 
            a a a a a 3 3 3 3 3 3 3 3 3 a a 
            a a a a a 3 3 3 3 3 3 3 3 3 a a 
            a a a a a 3 3 3 3 3 3 3 3 3 . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)