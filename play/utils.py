from pprint import pprint

from modules.scratch_item import getItem
from play.models import Characteristic, Photo, Item


def save_to_db():
    dict_ = getItem("https://brain.com.ua/")

    pprint(dict_)

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

    characteristics = []
    for char, value in dict_["characteristics"].items():
        character = Characteristic(name=char, value=value, item=item)
        characteristics.append(character)
        character.save()

    photos = []
    for link in dict_["photo_links"]:
        photo = Photo(link=link, item=item)
        photos.append(photo)
        photo.save()
