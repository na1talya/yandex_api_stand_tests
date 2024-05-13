import sender_stand_request
import data

# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Создание функции для позитивных проверок
def positive_assert(name):
	kit_body = get_kit_body(name)
	kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.get_token())
	assert kit_response.json()["name"] == kit_body["name"]
	assert kit_response.status_code == 201

# Создание функции для негативных проверок
def negative_assert_code_400(name):
	kit_body = get_kit_body(name)
	kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.get_token())
	assert kit_response.status_code == 400

# Функция для негативной проверки, когда тело запроса пустое
def negative_assert_code_400_no_name(kit_body):
    kit_no_name = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.get_token())
    assert kit_no_name.status_code == 400




#Тест 1.Допустимое количество символов (1):
def test_create_kit_1_symbol_in_name_get_success_response():
	positive_assert("a")

#Тест 2. Допустимое количество символов (511)
def test_create_kit_511_symbols_in_name_get_success_response():
	positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Количество символов меньше допустимого (0)
def test_create_kit_0_symbol_in_name_get_error_response():
    negative_assert_code_400("")

# Тест 4. Количество символов больше допустимого (512)
def test_create_kit_512_symbols_in_name_get_success_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Разрешены английские буквы
def test_create_kit_eng_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы
def test_create_kit_rus_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы
def test_create_kit_special_in_name_get_success_response():
    positive_assert("№%@",)

# Тест 8. Разрешены пробелы
def test_create_kit_whitespace_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(123)

# Тест 10. Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
	current_kit_body = data.kit_body.copy()
	current_kit_body.pop("name")
	negative_assert_code_400_no_name(current_kit_body)

# Тест 11. Передан другой тип параметра
def test_create_kit_numeric_type_name_get_error_response():
	negative_assert_code_400(123)