import numpy as np

# Параметры
lmb = 2
myu = 10
array_length = 1000000


# Генерация входных данных
def generate_nonzero_poisson(size, mu):
    array = np.random.poisson(mu, size)
    while (array == 0).any():
        array[array == 0] = np.random.poisson(mu, np.sum(array == 0))
    return array


# Генерация массивов
input_array = np.random.poisson(lmb, array_length)
firsthandler = generate_nonzero_poisson(array_length, myu)
secondhandler = generate_nonzero_poisson(array_length, myu)
thirdhandler = generate_nonzero_poisson(array_length, myu)


# Симуляция обработки запросов
def simulate(input_array, firsthandler, secondhandler, thirdhandler):
    first, second, third = np.zeros_like(input_array, dtype=float), np.zeros_like(input_array,
                                                                                  dtype=float), np.zeros_like(
        input_array, dtype=float)
    for i in range(array_length):
        remaining = input_array[i]

        # Первый сервер
        if remaining <= firsthandler[i]:
            first[i] = remaining / firsthandler[i]
        else:
            first[i] = 1
            remaining -= firsthandler[i]

            # Второй сервер
            if remaining <= secondhandler[i]:
                second[i] = remaining / secondhandler[i]
            else:
                second[i] = 1
                remaining -= secondhandler[i]

                # Третий сервер
                if remaining <= thirdhandler[i]:
                    third[i] = remaining / thirdhandler[i]
                else:
                    third[i] = 1
    return first, second, third


# Выполнение симуляции
first, second, third = simulate(input_array, firsthandler, secondhandler, thirdhandler)


# Подсчет вероятностей
def calculate_probabilities(first, second, third):
    t0 = np.sum(first == 0)
    t1 = np.sum((second < 1) & (first > 0))
    t2 = np.sum((third < 1) & (second == 1))
    t3 = np.sum(third == 1)
    return t0 / array_length, t1 / array_length, t2 / array_length, t3 / array_length


P0_sim, P1_sim, P2_sim, P3_sim = calculate_probabilities(first, second, third)

# Теоретические расчеты по формуле Эрланга
ro = lmb / myu
P0_theory = 1 / (1 + ro / 1 + ro ** 2 / 2 + ro ** 3 / 6)
P1_theory = ro / 1 * P0_theory
P2_theory = ro ** 2 / 2 * P0_theory
P3_theory = ro ** 3 / 6 * P0_theory

# Вывод результатов
print("Симуляция:")
print(f"P0 = {P0_sim:.5f}, P1 = {P1_sim:.5f}, P2 = {P2_sim:.5f}, P3 = {P3_sim:.5f}")
print(f"Сумма вероятностей (симуляция) = {P0_sim + P1_sim + P2_sim + P3_sim:.5f}")

print("\nТеоретические значения:")
print(f"P0 = {P0_theory:.5f}, P1 = {P1_theory:.5f}, P2 = {P2_theory:.5f}, P3 = {P3_theory:.5f}")
print(f"Сумма вероятностей (теория) = {P0_theory + P1_theory + P2_theory + P3_theory:.5f}")
