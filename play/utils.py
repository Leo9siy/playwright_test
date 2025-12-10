from pprint import pprint


def save_to_db():
    dict_ = get_item("https://brain.com.ua/ukr/")

    pprint(dict_)

    characteristics = []
    for char, value in dict_["characteristics"].items():
        character = Characteristic(name=char, value=value)
        characteristics.append(character)
        character.save()

    del dict_["characteristics"]

    item = Item(
        title=dict_["title"],
        colour=dict_["colour"],
        memory=dict_["memory"],
        price=dict_["price"],
        action_price=dict_["action_price"],
        code=dict_["code"],
        reviews_count=dict_["reviews_count"],
        screen_size=dict_["screen_size"],
        screen_power=dict_["screen_power"],
    )
    item.save()
    item.characteristics.set(characteristics)


    photos = []
    for link in dict_["photo_links"]:
        photo = Photo(link=link, item=item)
        photos.append(photo)
        photo.save()
    del dict_["photo_links"]