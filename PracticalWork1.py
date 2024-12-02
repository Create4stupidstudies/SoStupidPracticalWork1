class Game:
    def __init__(self):
        self.inventory = []
        self.levels = {
            1: {
                "description": "Вы находитесь в комнате с яркими флюоресцентными стенами. Вы видите дверь на юг.",
                "actions": [
                    "поискать ключи",
                    "идти на юг"
                ],
                "items": {"ключи": "Ключи от двери."}
            },
            2: {
                "description": "Вы входите в маленький коридор, и тут появляется противник! Это Громила Смешарик!",
                "actions": [
                    "сражаться с Громилой",
                    "использовать ключи"
                ],
                "items": {}
            },
            3: {
                "description": "Вы попали в тронный зал. На троне сидит Принц Рогатик и шутит: 'Что у меня на уме?'",
                "actions": [
                    "покаяться",
                    "разгадать загадку"
                ],
                "items": {}
            },
            4: {
                "description": "Вы оказались в кухне, где приготовлена суперспециальная еда - Суп из Крокодила! Чтобы выбраться, вам нужно его отведать.",
                "actions": [
                    "отведать суп",
                    "попробовать убежать",
                    "взять ловкую ложку",
                    "сразиться с Лерой"
                ],
                "items": {"ловкая ложка": "Ложка с прекрасными свойствами, помогающая быстро и спокойно есть суп."}
            },
            5: {
                "description": "Вы столкнулись с боссом KFC - Лерой! Она требует сражения!",
                "actions": [
                    "сразиться с Лерой",
                    "использовать ловкую ложку"
                ],
                "items": {}
            }
        }
        self.current_level = 1

    def start_game(self):
        print("Добро пожаловать в 'Приключение в смешном замке'!")
        print("\nВы ищете приключения и смешные истории!")
        while self.current_level <= 5:
            self.play_level()
        print("Поздравляю! Вы завершили игру!")

    def play_level(self):
        level_data = self.levels[self.current_level]
        print("\n" + level_data["description"])

        if level_data["items"]:
            print("Вы можете взять:", ", ".join(level_data["items"].keys()))

        self.display_actions(level_data["actions"])

        try:
            action_index = int(input("Введите номер действия: ")) - 1

            if action_index < 0 or action_index >= len(level_data["actions"]):
                raise ValueError

            action = level_data["actions"][action_index]

            # Логику действий
            if action == "поискать ключи":
                if "ключи" not in self.inventory:
                    self.inventory.append("ключи")
                    print("Вы нашли ключи от двери.")
                else:
                    print("Ключи у вас уже есть!")

            elif action == "идти на юг":
                if "ключи" in self.inventory:
                    print("Вы открываете дверь и переходите на следующий уровень.")
                    self.current_level += 1
                else:
                    print("Вы не можете открыть дверь, вам нужны ключи!")

            elif action == "сражаться с Громилой":
                if "ключи" in self.inventory:
                    print("Громила Смешарик испугался вашего умения решать загадки и убегает!")
                    self.current_level += 1
                else:
                    print("Громила Смешарик вас поймал! Но он слишком смешной, чтобы вас обидеть.")
                    return

            elif action == "разгадать загадку":
                print("Принц Рогатик говорит: 'Почему ласточка не летает зимой?'")
                input("Ваш ответ: ")
                print("Отлично! Принц Рогатик смеется и открывает выход!")
                self.current_level += 1

            elif action == "отведать суп":
                if "ловкая ложка" in self.inventory:
                    print(
                        "Вы съедаете Суп из Крокодила с использованием ловкой ложки и испытываете необычные ощущения! Это вам не простое блюдо!")
                    print("Теперь вы можете сразиться с Лерой!")
                    self.current_level += 1
                else:
                    print("Чтобы отведать суп, вам нужна ловкая ложка!")

            elif action == "попробовать убежать":
                print("Вы пытались убежать, но призрак Лохматого Патрика остановил вас.")
                print("Но, к счастью, пугал только на словах и не сделал вам ничего плохого.")

            elif action == "взять ловкую ложку":
                if "ловкая ложка" not in self.inventory:
                    self.inventory.append("ловкая ложка")
                    print("Вы взяли ловкую ложку.")
                else:
                    print("Ловкая ложка уже у вас!")

            elif action == "сразиться с Лерой":
                print("Вы сражаетесь с Лерой!")
                if "ловкая ложка" in self.inventory:
                    print("Вы используете ловкую ложку, чтобы победить Леру!")
                    print("Лера повержена! Вы можете покинуть замок.")
                    self.current_level += 1
                else:
                    print("Лера слишком сильна! Вам нужно что-то, чтобы победить её.")

            else:
                print("Неверное действие.")
        except (ValueError, IndexError):
            print("Ошибка: введён неверный номер действия.")

        self.show_inventory()

    def display_actions(self, actions):
        print("\nДоступные действия:")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")

    def show_inventory(self):
        if self.inventory:
            print("Ваш инвентарь:", ", ".join(self.inventory))
        else:
            print("Ваш инвентарь пуст.")


if __name__ == "__main__":
    game = Game()
    game.start_game()
