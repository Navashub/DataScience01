# Challenge 3
# A caterer offers three different food packages
# bronze package: starch:rice stew:chicken curry vegetable:cabbages desert:melon
# silver package: starch:rice and chappati  stew:beef curry vegetable:spinach desert:melon and bananas
# gold package: starch:rice, chappati and mukimo stew: beef curry vegetable:spinach and managu desert: tart
# Create a dictionary that stores the above information then preview it
# Hint: You can store a dictionary within a dictionary
#
#Create a new dictionary
food_packages = {
    "bronze_package" : {
        "starch" : "rice",
        "stew" : "chicken curry",
        "vegetable" : "cabbages",
        "desert" : "melon"
    },
    "silver_package" : {
        "starch" : "rice and chapati",
        "stew" : "beef curry",
        "vegetable" : "spinach",
        "desert" : "melon and bananas"
    },
    "gold_package" : {
        "starch" : "rice, chapati and mukimo",
        "stew" : "beef curry",
        "vegetable" : "spinach and managu",
        "desert" : "tart"
    }

}

print(food_packages)