
## 1. Game Intorduction

### Zombie game
Simple game created in pygame lib shows zombie attack on one of corporation floor called 'clab'. Main character has access to weapons like pistol, shotgun, rifle or Uzi and some bonuses. Game ends when player kills all zombies. 


### How to run

Create virtualenv and install all requirements and run command:
`python3 main.py`



## 2. Unittesting 

### * Run Code

    python3 -m unittest test_{function name}.py
    
    OR
    
    python3 test_{function name}.py


### Overview

### * Topic

2D shooting Game with unittesting


### * Target

- Our target is to write an unittesting framework for a 2D shooting game
- The game will have players, attackers and multiple game scenes(front-end)
- With our testing code, we hope each functions could run smoothly without any error
- error examples: player’s life bar doesn’t reduce when being attacked, bullet isn’t triggered…



### * Approaches

1. Spy
    - spy on objects
2. Stub
    - stub on random objects (ex. enemy/bullet…)
3. Mock
    - events
4. Coverage
    - check if all functions are tested


```
    coverage run -m unittest test{function name}.py
    coverage report -m   
    
```
    
    




[![2023-05-07-10-34-06.png](https://i.postimg.cc/G2TTqKx0/2023-05-07-10-34-06.png)](https://postimg.cc/xJYddKZg)




### * Contributors

    311551143 謝秉錦
    311554058 陳昱宏
    310706043 肇綺筠

