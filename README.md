# BoEnergoTestProject

### Стек технологий

- FastAPI
- docker
- pytest

### Функциональные возможности

- Решает квадратное уравнение
- Угадывает с определенной вероятностью цвет по номеру предмета

### Задание для второго пункта.

Есть группа из 100 предметов. Предметы могут быть синего, зелёного и красного цвета. Известно, что предметов синего цвета сильно больше, чем предметов зелёного цвета, а предметов зелёного цвета немного больше, чем предметов красного цвета. Напишите сервис, который будет принимать номер предмета и пытаться угадать его цвет. Логику работы сервиса определите самостоятельно.

### Логика работы

Данный сервис использует матрицу вероятностых переходов для цепей Маркова для определения вероятности определенного состояния после какого-то шага. Состояний в нашем случае всего 3, это 3 цвета: синий, зеленый, красный. Номер шага равен переданному пользователем номеру предмета. С помощью условия о соотношении количества предметов разного цвета задана матрица вероятностных переходов. После того как передан номер предмета вычисляется вероятность всех цветов, которые он может иметь. 

### Запуск

Проект упакован в докер, для запуска нужно воспользоваться следующими командами.

```
docker build . -t boenergo
docker run --rm -p 8000:8000 -d --name=boenergo boenergo
```

Документация находится на 127.0.0.1:8000/docs

### Тесты

Для запуска тестов

```
docker exec -it boenergo pytest
```

