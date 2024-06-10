class Pet:
    pass

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
             self._pet_type = pet_type
        else:
            raise Exception("Pet type must be a valid Pet in list")

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception("Object is not of type Owner")
        self._owner = owner
        
class Owner:
    pass

    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if type(pet) == Pet:
            pet.owner = self
        else:
            raise Exception("Pet must be of type Pet")            

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


owner = Owner("John")
print(owner.name)

pet = Pet("Fido", "dog")
print(pet.name)
print(pet.pet_type)

owner = Owner("Jim")
pet = Pet("Clifford", "dog", owner)
print(pet.name, pet.pet_type)
print(pet.owner.name)


print(pet.PET_TYPES)

# pet_1 = Pet("Jim Jr.", "panda")

pet1 = Pet("Whiskers", "cat")
pet2 = Pet("Jerry", "reptile")
print(pet1 in Pet.all)
print(pet2 in Pet.all)
print(len(Pet.all))

print(owner.pets()[0].name)
print(owner.pets()[0].owner.name)

owner = Owner("Sunak")
pet1 = Pet("Beast", "dog", owner)
pet2 = Pet("Beauty", "dog", owner)
pet3 = Pet("Tom", "cat", owner)
pet4 = Pet("Bosco", "reptile", owner)
print(owner.name)
print(owner.pets()[3].name)
owner.get_sorted_pets()
print(owner.get_sorted_pets()[3].name)






