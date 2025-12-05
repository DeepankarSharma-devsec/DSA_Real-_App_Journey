from category_engine import CategoryEngine


def print_section(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)


if __name__ == "__main__":
    engine = CategoryEngine()

    # 1. LIST ALL DEFAULT CATEGORIES
    print_section("ALL DEFAULT CATEGORIES")
    print(engine.list_categories())

    # 2. CHECK EXISTS()
    print_section("CHECK IF CATEGORY EXISTS")
    print("Food exists?", engine.exists("Food"))
    print("Travel exists?", engine.exists("Travel"))

    # 3. GET CATEGORY INFO
    print_section("CATEGORY INFO: Food")
    print(engine.get_category_info("Food"))

    # 4. LIST ONLY EXPENSE CATEGORIES
    print_section("EXPENSE CATEGORIES")
    print(engine.list_by_type("expense"))

    # 5. LIST ONLY INCOME CATEGORIES
    print_section("INCOME CATEGORIES")
    print(engine.list_by_type("income"))

    # 6. ADD CATEGORY
    print_section("ADDING NEW CATEGORY: Travel")
    engine.add_category("Travel", "expense", 6000)
    print(engine.list_categories())

    # 7. REMOVE CATEGORY
    print_section("REMOVING CATEGORY: Shopping")
    engine.remove_category("Shopping")
    print(engine.list_categories())

    # 8. CHECK POST-REMOVAL EXISTS()
    print_section("CHECK SHOPPING AFTER REMOVAL")
    print("Shopping exists?", engine.exists("Shopping"))
