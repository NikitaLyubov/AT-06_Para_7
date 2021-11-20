from PIL import Image
import numpy as np


def read(img_name):
    img = Image.open(img_name)
    return np.array(img)


def write(array, output_img):
    res = Image.fromarray(array)
    res.save(output_img)


def make_grayscale(x, y, array, puzzle_size):
    return np.mean(array[x: x + puzzle_size, y: y + puzzle_size])


def fill_array(array, x, y, puzzle_size, grayscale):
    array[x: x + puzzle_size, y: y + puzzle_size] = np.array(3 * [grayscale])


def paint_img(array, puzzle_size, grayscale):
    row = len(array)
    column = len(array[1])

    for x in range(0, row, puzzle_size):
        for y in range(0, column, puzzle_size):
            shade = make_grayscale(x, y, array, puzzle_size)
            fill_array(array, x, y, puzzle_size, int(shade // grayscale) * grayscale)


if __name__ == "__main__":
    try:
        arr = read(input("Введите имя изображение, которое хотите изменить: "))
        ceil_size = int(input("Введите размер мозайки: "))
        grad = int(input("Введите кол-во градаций серого цвета: "))
        paint_img(arr, ceil_size, grad)
        write(arr, input("Введите имя файла, в который сохранить картинку: "))
    except FileNotFoundError:
        print("Изображение не найдено")
