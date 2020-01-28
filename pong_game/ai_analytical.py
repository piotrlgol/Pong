class AI_analytical():
    @staticmethod
    def compute_move(paddle_pos, ball_pos, ball_vel):
        left_attaced = paddle_pos[0] == 20 and ball_vel[0]<0
        right_attaced = paddle_pos[0] == 670 and ball_vel[0]>0
        if(left_attaced or right_attaced):
            y2 = ball_pos[1]+ball_vel[1]
            x2 = ball_pos[0]+ball_vel[0]
            y = ((y2-ball_pos[1])/(x2-ball_pos[0]))*(paddle_pos[0]-x2)+y2
            y = abs(y)
            while(y>490):
                y = 980 - y
                y = abs(y)
            if(paddle_pos[1]-3>y):
                return 'up'
            elif(paddle_pos[1]+3<y):
                return 'down'
        return ' '