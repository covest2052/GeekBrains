import os

def load_data(file_name):
    if not os.path.exists(file_name):
        return []
    
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    directory = []
    for line in lines:
        line = line.strip()
        if line:
            directory.append(tuple(line.split(', ')))
    return directory

def save_data(file_name, directory):
    with open(file_name, 'w', encoding='utf-8') as file:
        for entry in directory:
            file.write(', '.join(entry) + '\n')

def add_entry(directory, surname, name, patronymic, phone_number):
    directory.append((surname, name, patronymic, phone_number))

def update_entry(directory, index, surname, name, patronymic, phone_number):
    if 0 <= index < len(directory):
        directory[index] = (surname, name, patronymic, phone_number)
    else:
        print("Неверный индекс записи.")

def display_entries(directory):
    if not directory:
        print("Справочник пуст.")
    else:
        for i, entry in enumerate(directory, 1):
            print(f"{i}. Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}")

def search_entries(directory, query, search_by="name"):
    results = []
    if search_by == "name":
        results = [entry for entry in directory if query.lower() in entry[0].lower()]
    elif search_by == "phone":
        results = [entry for entry in directory if query.lower() in entry[3].lower()]
    return results

def display_search_results(results):
    if not results:
        print("Записи не найдены.")
    else:
        for i, entry in enumerate(results, 1):
            print(f"{i}. Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}")

def copy_entry_to_other_file(directory, index, target_file_name):
    if 0 <= index < len(directory):
        target_directory = load_data(target_file_name)
        target_directory.append(directory[index])
        save_data(target_file_name, target_directory)
        print(f"Запись успешно скопирована в файл {target_file_name}.")
    else:
        print("Неверный индекс записи.")

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные абонента\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Копировать запись в другой файл\n"
          "8. Закончить работу")
    choice = int(input("Введите номер действия: "))
    return choice

def main():
    file_name = "phone_directory.txt"
    directory = load_data(file_name)
    
    while True:
        choice = show_menu()
        
        if choice == 1:
            display_entries(directory)
        elif choice == 2:
            query = input("Введите фамилию для поиска: ")
            results = search_entries(directory, query, search_by="name")
            display_search_results(results)
        elif choice == 3:
            query = input("Введите номер телефона для поиска: ")
            results = search_entries(directory, query, search_by="phone")
            display_search_results(results)
        elif choice == 4:
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            add_entry(directory, surname, name, patronymic, phone_number)
        elif choice == 5:
            display_entries(directory)
            index = int(input("Введите номер записи для изменения: ")) - 1
            surname = input("Введите новую фамилию: ")
            name = input("Введите новое имя: ")
            patronymic = input("Введите новое отчество: ")
            phone_number = input("Введите новый номер телефона: ")
            update_entry(directory, index, surname, name, patronymic, phone_number)
        elif choice == 6:
            save_data(file_name, directory)
            print("Данные сохранены.")
        elif choice == 7:
            display_entries(directory)
            index = int(input("Введите номер записи для копирования: ")) - 1
            target_file_name = input("Введите имя целевого файла (с расширением .txt): ")
            copy_entry_to_other_file(directory, index, target_file_name)
        elif choice == 8:
            save_data(file_name, directory)
            print("Данные сохранены. Выход.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите опцию от 1 до 8.")

if __name__ == "__main__":
    main()
