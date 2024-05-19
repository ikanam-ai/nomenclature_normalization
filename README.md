
<p align="center">
     <img src="./Inverse_Capital.png" alt="Логотип проекта" width="500" style="display: inline-block; vertical-align: middle; margin-right: 10px;"/>  <br/>
     <H2 align="center">Команда Ikanam 1218 </H2> 
    <H2 align="center">Кейс "Приведение номенклатуры участников рынка к официальному Классификатору Строительных Ресурсов"</H2> 
</p>


> Команда Ikanam 1218  представляет жюри программный модуль с использованием ИИ для сопоставление строительной номенклатуры со справочником
строительных ресурсов. Данный программный продукт является мощным инструментом для закупочной деятельности и логистики, а также упрощения взаимодействия между
различными участниками строительного процесса.


## Установка и запуск

**Наше решение разделено на две ключевые части. Первая часть включает в себя подробное руководство по развёртыванию без необходимости взаимодействия с интерфейсом, что обеспечивает быстрое и эффективное тестирование. Вторая часть предоставляет подробные инструкции по развертыванию решения с использованием интерфейса, обеспечивая при этом максимальное удобство для процесса верификации и классификации материалов.**

***Часть 1:***
----------

*1. Загрузите репозиторий на свой компьютер и откройте её в вашей предпочитаемой среде разработки (IDE).* 

*2. Откройте терминал в IDE и введите туда следующую команду:* 

```python
python -m venv .venv
```
*3. Дождитесь создание папки `.venv` затем введите следующую команду:*

```python
.\.venv\Scripts\activate
```
*4. После активации установите все библиотеки (весрия python==3.10+) при помощи данной команды:*

```python
pip install -r requirements.txt
```


*5. Прекрасно! Теперь в терминале введите команду для перехода к основной папке с кодом проекта.*

```shell
cd src 
```


*5.1 Необходимо использовать локальную ллм-модель или указать путь до собственной, предлагаемый пример ниже.*

```shell
wget -P /llm_model https://huggingface.co/IlyaGusev/saiga_mistral_7b_gguf/resolve/main/model-q4_K.gguf
```


*6. Для запуска локальной языковой модели, введите следующие команду.*

```shell
python3 llm_model/main_gguf.py
```


*7. Для запуска API, введите следующие команду.*

```shell
python3 run api.py
```



# Пример использования сервиса, иллюстрированный процессом обработки скринкаста.






https://github.com/ikanam-ai/nomenclature_normalization/assets/120698866/9bac5f92-b767-4623-bab4-7d94fe9da9c6


# Пример работы сервиса

***Часть 1:***


***Часть 2:***



***Часть 3:***


***Часть 4:***


