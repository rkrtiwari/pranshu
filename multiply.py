import pgzrun

import numpy as np
from random import randint

WIDTH = 1280
HEIGHT = 900
score = 0


def get_input_output():
    num1 = randint(1,5)
    num2 = randint(2,5)
    true_ans = num1*num2
    return num1, num2, true_ans

def get_dots(num1, num2):
    dots = []
    X = 190
    Y = 610
    
    for i in range(0, num2):
        for j in range(0, num1):
            actor = Actor("dot")
            actor.pos = X + i*80, Y + j*40
            dots.append(actor)
    return dots

def get_all_boxes():    
    main_box = Rect(0,0,820, 150)
    score_box = Rect(0, 0, 240, 150)
    answer_box1 = Rect(0, 0, 495, 100)
    answer_box2 = Rect(0, 0, 495, 100)
    answer_box3 = Rect(0, 0, 495, 100)
    answer_box4 = Rect(0, 0, 495, 100)
    hint_box = Rect(0, 0, 1000, 250)

    main_box.move_ip(50,40)
    score_box.move_ip(990, 40)
    answer_box1.move_ip(50, 250)
    answer_box2.move_ip(735, 250)
    answer_box3.move_ip(50, 400)
    answer_box4.move_ip(735, 400)
    hint_box.move_ip(150, 550)

    answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

    return main_box, score_box, answer_boxes, hint_box

main_box, score_box, answer_boxes, hint_box = get_all_boxes()

def get_wrong_ans(true_ans):
    wrong_ans = []
    for i in range(3):
        lower_limit = 1-true_ans
        add_val = np.random.randint(lower_limit,10)
        if add_val == 0:
            add_val += 11
        wrong_ans.append(str(true_ans + add_val))
    return wrong_ans

def get_ans_list(true_ans, wrong_ans):
    loc = np.random.randint(1,5)
    ans = []
    for i in range(1,5):
        if i == loc:
            ans.append(str(true_ans))
        else:
            ans.append(str(wrong_ans.pop()))

    ans.append(loc)
    return(ans)

def get_ques_list(num1, num2):
    ques = [str(num1) + ' * ' + str(num2)]
    return ques

def get_all_list(ques_list, ans_list):
    ques_list.extend(ans_list)
    return ques_list


def get_question(num1, num2, true_ans):
    wrong_ans = get_wrong_ans(true_ans)
    ans_list = get_ans_list(true_ans, wrong_ans)
    ques_list = get_ques_list(num1, num2)
    question = get_all_list(ques_list, ans_list)
    return question


def get_bounding_boxes(num1, num2):
    bounding_boxes = []    
    for i in range(num2):
        bounding_box = Rect(215 + i*35 + (i-1)*45, 595, 40, num1*38)
        bounding_boxes.append(bounding_box)
    return bounding_boxes

num1, num2, true_ans = get_input_output()
question = get_question(num1, num2, true_ans)
dots = get_dots(num1, num2)
bounding_boxes = get_bounding_boxes(num1, num2)

    
        
def draw():
        
    screen.fill("dim gray")
    number = 1
    
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.textbox(question[0], main_box, color = ('black'))

    screen.draw.filled_rect(score_box, "sky blue")
#    text = 'Reward: $' + str(score)
    text = str(score)
    screen.draw.textbox(text, score_box, color = ('black'))

    screen.draw.filled_rect(hint_box, "green")
    screen.draw.text("Hint", (550, 550), color="black", fontsize = 50)
    for j in range(num2):
        if j == (num2-1):
            screen.draw.text(str(num1), (180 + j*80, 560), color="black", fontsize = 50)
        else:
            screen.draw.text(str(num1)+ '   +', (180 + j*80, 560), color="black", fontsize = 50)
            
        
        
        
        
    

    for box in bounding_boxes:
        screen.draw.filled_rect(box, "red")
            
    
    for dot in dots:
        dot.draw()
  

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color = ('black'))
        index = index + 1

    

def correct_answer():
    global question, score, num1, num2, true_ans, dots, bounding_boxes
    score += 1
#    score = round(score,1)
    sounds.correct_sound.play()
    num1, num2, true_ans = get_input_output()
    question = get_question(num1, num2, true_ans)
    dots = get_dots(num1, num2)
    bounding_boxes = get_bounding_boxes(num1, num2)
    

def wrong_answer():
    global question, score, num1, num2, true_ans, dots, bounding_boxes
    score -= 1
    score = round(score,1)
    sounds.wrong_sound.play()
    num1, num2, true_ans = get_input_output()
    question = get_question(num1, num2, true_ans)
    dots = get_dots(num1, num2)
    bounding_boxes = get_bounding_boxes(num1, num2)
    
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index == question[5]:
                correct_answer()                
                print('you got it right')                
            else:
                print('you got it wrong')
                wrong_answer()
        index += 1


##def update():
##    global score, num1, num2, true_ans, question, dots


    
pgzrun.go()
