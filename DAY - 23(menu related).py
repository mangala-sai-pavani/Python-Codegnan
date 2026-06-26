class Menu:
    def veg_menu():
        print(" Vegitarian Items: \n Paneer Butter Masala\n Veg Biryani\n Chole Bhature\n Palak Paneer\n Aloo Gobi\n Dal Tadka\n Veg Pulao\n Malai Kofta\n Rajma Chawal\n Kadai Paneer\n Baingan Bharta\n Mix Veg Curry\n Mushroom Masala\n Jeera Rice\n Veg Fried Rice\n Pav Bhaji\n Dosa\n Idli Sambar\n Veg Manchurian\n Hakka Noodles\n Stuffed Paratha\n Poha\n Upma\n Pani Puri\n Dhokla\n Khandvi\n Samosa\n Spring Rolls\n Veg Cutlet\n Tomato Rice")
    
    def non_veg_menu():
        print(" Non-Vegitarian Items: \n Butter Chicken\n Chicken Biryani\n Mutton Rogan Josh\n Fish Curry\n Prawn Masala\n Chicken Tikka\n Tandoori Chicken\n Egg Curry\n Keema Masala\n Hyderabadi Chicken Dum Biryani\n Andhra Chicken Curry\n Crab Masala\n Fish Fry\n Chicken 65\n Mutton Biryani\n Pepper Chicken\n Prawn Biryani\n Chicken Fried Rice\n Chilli Chicken\n Chicken Noodles\n Egg Fried Rice\n Lamb Kebabs\n Duck Roast\n Grilled Fish\n Prawn Fry\n Chicken Korma\n Nihari\n Sheekh Kebabs\n Chicken Shawarma\n Garlic Butter Prawns")
    def menu(self):
        
        while True:
            print("Menu\n1.Vegetarian Dishes\n2.Non-Vegetarian Dishes\n3.Exit")
            choice = int(input())
            if choice == 1:
                Menu.veg_menu()
            elif choice == 2:
                Menu.non_veg_menu()
            elif choice == 3:
                exit()
m1 = Menu()
m1.menu()