from locators.order_page_first_locators import OrderPageFirstLocators
from locators.order_page_second_locators import OrderPageSecondLocators


class UserData:
    FIRST_DATA_SET = ['Ян', 'Кин', 'Томск', 'Сокольники', OrderPageFirstLocators.FIRST_METRO,
                      '88005553535', '24.04.2024', OrderPageSecondLocators.FIRST_PERIOD_DAY,
                      OrderPageSecondLocators.COLOR_SCOOTER_BLACK, 'Привет, курьер!',
                      OrderPageFirstLocators.HEADER_BUTTON_ORDER]

    SECOND_DATA_SET = ['Алексей', 'Григорович', 'Москва', 'Митино', OrderPageFirstLocators.SECOND_METRO,
                       '+75004589093', '31.12.2025', OrderPageSecondLocators.SECOND_PERIOD_DAY,
                       OrderPageSecondLocators.COLOR_SCOOTER_GREY, 'Пока!',
                       OrderPageFirstLocators.BUTTON_ON_MIDDLE_PAGE_ORDER]

    # Ответы на вопросы на основной странице
    QUESTION_CHECKING_TEXT = [
        'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',

        'Пока что у нас так: один заказ — один самокат. '
        'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',

        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
        'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
        'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',

        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',

        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',

        'Самокат приезжает к вам с полной зарядкой. '
        'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',

        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',

        'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    ]
