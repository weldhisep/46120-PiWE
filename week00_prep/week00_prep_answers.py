# Week 00 prep answers
#weldhi Septian
#s250168
def greet(name):
    print(f"Hello, {name}!")


def goldilocks(bed_length_cm):
    if bed_length_cm < 140:
        print("Too small!")
    elif bed_length_cm > 150:
        print("Too large!")
    else:
        print("Just right. :)")


def square_list(numbers):
    return [n * n for n in numbers]


def fibonacci_stop(max_value):
    fibs = []
    a, b = 1, 1
    while a <= max_value:
        fibs.append(a)
        a, b = b, a + b
    return fibs


def clean_pitch(pitch_angles, status_signals):
    cleaned = []
    for angle, status in zip(pitch_angles, status_signals):
        if (angle < 0 or angle > 90) and status > 0:
            cleaned.append(-999)
        else:
            cleaned.append(angle)
    return cleaned


if __name__ == "__main__":
    print("1.")
    greet("world")

    print
    
    goldilocks(139)
    goldilocks(140)
    goldilocks(151)
    goldilocks(150)

    print(square_list([1, 2, 3]))
    print(fibonacci_stop(30))

    x = [-1, 2, 6, 95]
    status = [1, 0, 0, 0]
    print(clean_pitch(x, status))
