from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
#Global Vars and Functions

def chooseRandLaunchDeg():
    randomNum = randint(0, 1)
    if randomNum == 0:
        allLaunchDeg = []
        for i in range(35, -1, -1):
            allLaunchDeg.append(i)
        for j in range(360, 324, -1):
            allLaunchDeg.append(j)
        k = randint(0, len(allLaunchDeg) - 1)
        randomLaunchDeg = allLaunchDeg[k]
    elif randomNum == 1:
        randomLaunchDeg = randint(90, 175)
    return randomLaunchDeg

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=Vector(1, 1).rotate(chooseRandLaunchDeg())):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()
        self.player1.center_y = self.ball.y
        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=Vector(2, 2).rotate(chooseRandLaunchDeg()))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=Vector(2, 2).rotate(chooseRandLaunchDeg()))

    def on_touch_move(self, touch):            
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1 / 1080)
        
        return game


if __name__ == '__main__':
    PongApp().run()