from flask import Flask, render_template_string, request

app = Flask(__name__)

class Eagle:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.coins = 0
        self.is_alive = True
        self.is_flying = False
        self.is_trained = False
        self.home = "Nest"
        self.play_count = 0
        self.has_shop = False
        self.shelves_filled = False
        self.is_cashier = False
        
    def age_up(self):
        self.age += 1
        self.coins += 1
    
        if self.age > 10:  
            self.die()
            return f"{self.name} has passed away."
        elif self.age > 3:
            if not self.is_flying:
                self.is_flying = True
                self.is_cashier = True
                return f"{self.name} can now fly and he/she can now work as a cashier !"
                
        
        
    
        return f"{self.name} aged up."

    def buy_food(self):
        if self.coins >= 10:
            self.coins -= 10
            return f"{self.name} bought food."
        else:
            return "Not enough coins to buy food."

    def play(self):
        if self.is_alive:
            self.coins += 5
            self.play_count += 1
            return f"{self.name} played and earned coins."
        else:
            return f"{self.name} is no longer alive."

    def train(self):
        if self.coins >= 20:
            self.coins -= 20
            self.is_trained = True
            return f"{self.name} is now trained."
        else:
            return "Not enough coins to train."

    def compete(self):
        if self.is_flying and self.is_trained:
            return f"{self.name} is participating in a flying competition!"
        else:
            return f"{self.name} needs more training to compete."

    def rename(self, new_name):
        self.name = new_name
        return f"{self.name} has been renamed to {new_name}."

    def change_home(self):
        if self.coins >= 100:
            self.coins -= 100
            self.home = "New Home"
            return f"{self.name} has a new home: {self.home}."
        else:
            return "Not enough coins to buy a new home."

    def die(self):
        self.is_alive = False
        return f"{self.name} has passed away."

    def buy_shop(self):
        if self.coins >= 200:
            self.coins -= 200
            self.has_shop = True
            return f"{self.name} bought a shop!"
        else:
            return "Not enough coins to buy a shop."

    def fill_shelves(self):
        if self.has_shop:
            self.shelves_filled = True
            return f"{self.name} filled the shelves."
        else:
            return f"{self.name} doesn't own a shop."

    def do_cashier_work(self):
        if self.has_shop and self.is_cashier:
            self.coins += 50
            return f"{self.name} worked as a cashier and earned coins."
        elif not self.is_cashier:
            return f"{self.name} is not a cashier."
        else:
            return f"{self.name} doesn't own a shop."

my_eagle = Eagle("My Eagle")

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    
    if request.method == "POST":
        choice = request.form.get("choice")
        
        if choice == "buy_food":
            message = my_eagle.buy_food()
        elif choice == "play":
            message = my_eagle.play()
        elif choice == "train":
            message = my_eagle.train()
        elif choice == "compete":
            message = my_eagle.compete()
        elif choice == "rename":
            new_name = request.form.get("new_name")
            message = my_eagle.rename(new_name)
        elif choice == "change_home":
            message = my_eagle.change_home()
        elif choice == "age_up":
            message = my_eagle.age_up()
        elif choice == "buy_shop":
            message = my_eagle.buy_shop()
        elif choice == "fill_shelves":
            message = my_eagle.fill_shelves()
        elif choice == "work_cashier":
            message = my_eagle.do_cashier_work()
    
    template = """
    <html>
    <head>
        <title>Eagle Life Simulator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f0f0f0;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 5px;
                margin-top: 40px;
            }
            h1 {
                color: #333;
                text-align: center;
                margin-top: 20px;
            }
            p {
                color: #555;
                margin: 5px 0;
            }
            form {
                margin-top: 20px;
                text-align: center;
            }
            select, input[type="text"], input[type="submit"] {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                width: 200px;
                margin-right: 10px;
            }
            input[type="submit"] {
                background-color: #333;
                color: white;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #555;
            }
            .message {
                margin-top: 20px;
                color: #333;
                text-align: center;
            }
            .eagle {
                width: 150px;
                height: 150px;
                font-size: 100px;
                text-align: center;
            }
            .eagle-details {
                border-top: 1px solid #ccc;
                padding-top: 10px;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the Eagle Life Simulator</h1>
            <div class="eagle">🦅</div>
            <p>Name: {{ eagle.name }}</p>
            <div class="eagle-details">
                <p>Age: {{ eagle.age }}</p>
                <p>Coins: {{ eagle.coins }}</p>
                <p>Home: {{ eagle.home }}</p>
                <p>Play Count: {{ eagle.play_count }}</p>
                <p>Shop: {{ "Yes" if eagle.has_shop else "No" }}</p>
                <p>Shelves Filled: {{ "Yes" if eagle.shelves_filled else "No" }}</p>
                <p>Cashier: {{ "Yes" if eagle.is_cashier else "No" }}</p>
            </div>
            
            <form method="POST">
                <select name="choice">
                    <option value="buy_food">Buy Food</option>
                    <option value="play">Play</option>
                    <option value="train">Train</option>
                    <option value="compete">Compete</option>
                    <option value="rename">Rename</option>
                    <option value="change_home">Change Home</option>
                    <option value="age_up">Age Up</option>
                    <option value="buy_shop">Buy Shop</option>
                    <option value="fill_shelves">Fill Shelves</option>
                    <option value="work_cashier">Work as Cashier</option>
                </select>
                <input type="text" name="new_name" placeholder="New Name">
                <input type="submit" value="Perform Action">
            </form>
            
            <p class="message">{{ message }}</p>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(template, eagle=my_eagle, message=message)

if __name__ == "__main__":
    app.run(debug=True)
