sandwich_orders = []

print("Enter sandwich orders.")
print("Type 'done' when finished.\n")

while True:
    sandwich = input("Enter a sandwich order: ")

    if sandwich.lower() == "done":
        break

    sandwich_orders.append(sandwich)

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"\n✅ I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(f"🥪 {sandwich}")