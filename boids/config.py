WINDOW_DIMENSIONS = (1000, 1000)
BACKGROUND = (255, 255, 255)
FOREGROUND = (0, 0, 0)

BOID_RADIUS = 5
NEIGHBOURHOOD_RADIUS = 15 * BOID_RADIUS

OBSTACLE_RADIUS = 3 * BOID_RADIUS

BOID_MAX_SPEED = 25.0
STEP_SCALE = 0.5

HI = 1.0
LO = 0.1

SCENARIOS = {
    1: (LO, LO, HI),
    2: (LO, HI, LO),
    3: (HI, LO, LO),
    4: (LO, HI, HI),
    5: (HI, LO, HI),
    6: (HI, HI, LO)
}

OBSTACLE_AVOIDANCE_WEIGHT = 2 * HI

ADJUST_WEIGHT = HI - LO

NUMBER_OF_BOIDS = 100

TICK = 0.0
ADJUST_TICK = 0.1
