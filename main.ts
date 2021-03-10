namespace SpriteKind {
    export const item = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.item, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    can.setPosition(randint(0, 160), randint(0, 120))
    info.startCountdown(20)
    if (info.score() == 10) {
        game.over(true, effects.confetti)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeScoreBy(-1)
    mySprite.setPosition(randint(0, 160), randint(0, 120))
    if (info.score() == -5) {
        game.over(false)
    }
})
let mySprite: Sprite = null
let can: Sprite = null
scene.setBackgroundColor(11)
let mike = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mike)
can = sprites.create(img`
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
    `, SpriteKind.item)
mySprite = sprites.create(img`
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
    `, SpriteKind.Enemy)
