def main():
    name = 'dog, cat, rabbit, horse'
    print(f"The name is {name}")
    animals = name.split(", ")
    for animal in animals:
        print(f"The name is {animal}")

if __name__ == "__main__":
    main()