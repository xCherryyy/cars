import random


class Cars:
    def __init__(self, category, model, price):
        self.category = category
        self.model = model
        self.price = price


car1 = Cars('sportCar', 'Nissan GTR', 280000)
car2 = Cars('sportCar', 'Porsche 911', 500000)
car3 = Cars('sportCar', 'BMW M3 Competition', 520000)
car4 = Cars('normalCar', 'Lexus UX', 190000)
car5 = Cars('normalCar', 'Mazda 6', 170000)
car6 = Cars('normalCar', 'Audi A4', 170000)
car7 = Cars('deliveryCar', 'Renault Master', 50000)
car8 = Cars('deliveryCar', 'Iveco Daily', 150000)
car9 = Cars('deliveryCar', 'Fiat Ducato', 40000)

arr = [car1, car2, car3, car4, car5, car6, car7, car8, car9]

inputModel = 0
randomInt = random.randint(1000, 8000)


def menu():
    print('--- Aukcje samochodowe ---')
    print('1. Samochody sportowe')
    print('2. Samochody osobowe')
    print('3. Samochody dostawcze')
    category = input('wybierz kategorię: ')

    if category == '1':
        print(f'1. model: {car1.model}, cena: {car1.price}')
        print(f'2. model: {car2.model}, cena: {car2.price}')
        print(f'3. model: {car3.model}, cena: {car3.price}')
        offerInputs(1, 3, 0)

    elif category == '2':
        print(f'4. model: {car4.model}, cena: {car4.price}')
        print(f'5. model: {car5.model}, cena: {car5.price}')
        print(f'6. model: {car6.model}, cena: {car6.price}')
        offerInputs(4, 6, 0)

    elif category == '3':
        print(f'7. model: {car7.model}, cena: {car7.price}')
        print(f'8. model: {car8.model}, cena: {car8.price}')
        print(f'9. model: {car9.model}, cena: {car9.price}')
        offerInputs(7, 9, 0)

    else:
        print('Nie wybrałeś niczego, wpisz jeszcze raz...')
        menu()


def offerInputs(arrMinLength, arrMaxLength, newPrice):
    inputModel = int(input('Wybierz interesujący cię model: '))
    if arrMinLength <= inputModel <= arrMaxLength:
        userOffer = int(input('Podaj swoją ofertę(0 aby anulować): '))
        checkPrice(userOffer, inputModel, newPrice)
    else:
        print('Podałeś złą wartość...')
        offerInputs(arrMinLength, arrMaxLength, 0)


def checkPrice(userOffer, model, newPrice):
    if userOffer >= arr[int(model) - 1].price - randomInt:
        toggleBot(newPrice, userOffer)

    elif userOffer == 0:
        menu()
    else:
        print('Oferujesz mi za mało')
        if 1 >= inputModel <= 3:
            offerInputs(1, 3, 0)
        elif 4 >= inputModel <= 6:
            offerInputs(4, 6, 0)
        elif 7 >= inputModel <= 9:
            offerInputs(7, 9, 0)


def toggleBot(newPrice, userOffer):  # losuje czy bot podbije cenę, czy odpuści
    number = random.randint(0, 10)
    if number > 5:
        checkNewPrice(newPrice, userOffer)
        return
    else:
        print('Akceptuję twoją ofertę. Auto należy do ciebie!')
        return


def checkNewPrice(newPrice, userOffer):
    raisedPrice = random.randint(300, 1000)
    newPrice = userOffer + raisedPrice
    print(f'Mamy ofertę od kogoś innego na: {newPrice}')
    userOffer = int(input('Podaj kontrofertę: '))
    if userOffer < newPrice or userOffer == newPrice:
        print('Twoja oferta jest zbyt niska, przegrałeś licytację.')
    else:
        toggleBot(newPrice, userOffer)

menu()
