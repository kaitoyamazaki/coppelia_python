import numpy as np


def test_return():
    target_pos = np.empty((1,2))
    target_pos[0][0] = 0.7
    target_pos[0][1] = 1.3

    return target_pos

def main():
    target_pos = test_return()
    print(target_pos)
    print(f"target_pos is {target_pos.shape[0]}")

if __name__ == '__main__':
    main()