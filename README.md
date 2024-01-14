## Зверніть увагу, що для виведення результатів використовується бібліотека tabulate. Переконайтеся, що вона встановлена в вашому середовищі виконання Python:

`pip install tabulate`


# Ефективність алгоритмів сортування

## Огляд

У цьому завданні проведено порівняльний аналіз трьох алгоритмів сортування: **Insertion Sort**, **Merge Sort** та **Timsort** (представленого як `Time sort`). Також розглянуто оптимізацію шляхом використання методу `sort()` для списків (`Time sort speedup`).

## Результати вимірювань часу виконання

Нижче подана таблиця із часом виконання для кожного алгоритму на різних розмірах даних:

| Algorithm         | Time small data | Time medium data | Time large data |
|-------------------|------------------|-------------------|------------------|
| Insertion sort    | 0.00004511       | 0.00312734        | 0.31327929       |
| Merge sort        | 0.00011873       | 0.00160584        | 0.02266237       |
| Time sort         | 0.00000917       | 0.00005147        | 0.00102612       |
| Time sort speedup | 0.00000551       | 0.00004426        | 0.00134772       |

## Висновки

1. **Insertion Sort:** Найменший ефективний алгоритм для великих наборів даних, особливо на порівнянні з Merge та Timsort. Застосовний для невеликих наборів даних.

2. **Merge Sort:** Виявився більш ефективним, ніж Insertion Sort, особливо на великих наборах даних. Володіє стабільною ефективністю навіть для великих об'ємів даних.

3. **Timsort:** Єфективний алгоритм для різних розмірів даних, особливо для середніх і великих наборів. Використання вбудованого `sorted()` виявилося дуже швидким.

4. **Timsort Speedup:** Використання методу `sort()` для списків дав зростання продуктивності, особливо для середніх та великих даних, в порівнянні зі звичайним Timsort.

### Вплив на обрані алгоритми

- Для невеликих даних можна використовувати Insertion Sort, оскільки він проявив найкращі результати.

- Для середніх і великих наборів даних краще використовувати Timsort або Merge Sort, залежно від конкретного випадку.

- Використання оптимізації `sort()` для списків може бути доцільним для покращення ефективності Timsort, особливо на великих даних.
