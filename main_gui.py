import tkinter as tk
from tkinter import messagebox

def calculate_payouts():
    def submit_data():
        try:
            num_players = int(num_players_entry.get())
            bet_amount = float(bet_amount_entry.get())

            player_names = []
            final_euros = []

            for i in range(num_players):
                name = player_entries[i]["name"].get()
                if not name:
                    raise ValueError(f"Player {i + 1} name cannot be empty.")
                player_names.append(name)

                euros = player_entries[i]["euros"].get()
                if not euros:
                    raise ValueError(f"Player {i + 1}'s final euros cannot be empty.")
                final_euros.append(float(euros))

            balances = [final - bet_amount for final in final_euros]

            debtors = [(i, -balance) for i, balance in enumerate(balances) if balance < 0]
            creditors = [(i, balance) for i, balance in enumerate(balances) if balance > 0]

            if sum(final_euros) != num_players * bet_amount:
                raise ValueError(f"insgesamt gibts {sum(final_euros)}, aber es sollten {num_players * bet_amount} vorhanden sein, sie negah")

            settlements = []
            while debtors and creditors:
                debtor_idx, debtor_amount = debtors.pop(0)
                creditor_idx, creditor_amount = creditors.pop(0)

                settlement_amount = min(debtor_amount, creditor_amount)
                settlements.append((player_names[debtor_idx], player_names[creditor_idx], settlement_amount))

                if debtor_amount > settlement_amount:
                    debtors.insert(0, (debtor_idx, debtor_amount - settlement_amount))
                if creditor_amount > settlement_amount:
                    creditors.insert(0, (creditor_idx, creditor_amount - settlement_amount))

            settlement_message = "\nFolgendes muss gem8 werden:\n\n"
            for debtor, creditor, amount in settlements:
                settlement_message += f"{debtor} schickt {creditor} {amount:.2f}€\n"

            messagebox.showinfo("Jeder muss zahlen!", settlement_message)
        except ValueError as e:
            messagebox.showerror("Geschissen!", str(e))

    def create_player_inputs():
        try:
            num_players = int(num_players_entry.get())
            for widget in player_frame.winfo_children():
                widget.destroy()

            global player_entries
            player_entries = []

            for i in range(num_players):
                tk.Label(player_frame, text=f"Player {i + 1} Name:", bg="#2b2b2b", fg="#ffffff", font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
                name_entry = tk.Entry(player_frame, bg="#404040", fg="#ffffff", font=("Arial", 12))
                name_entry.grid(row=i, column=1, padx=10, pady=5)

                tk.Label(player_frame, text=f"Final Euros:", bg="#2b2b2b", fg="#ffffff", font=("Arial", 12)).grid(row=i, column=2, padx=10, pady=5)
                euros_entry = tk.Entry(player_frame, bg="#404040", fg="#ffffff", font=("Arial", 12))
                euros_entry.grid(row=i, column=3, padx=10, pady=5)

                player_entries.append({"name": name_entry, "euros": euros_entry})
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of players.")

    root = tk.Tk()
    root.title("Pokerabend rechner")
    root.configure(bg="#2b2b2b")
    root.geometry("800x600")

    tk.Label(root, text="Anzahl Spieler:", bg="#2b2b2b", fg="#ffffff", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
    num_players_entry = tk.Entry(root, bg="#404040", fg="#ffffff", font=("Arial", 14))
    num_players_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Button(root, text="lock the fuck in", command=create_player_inputs, bg="#005f87", fg="#ffffff", activebackground="#0078a0", activeforeground="#ffffff", font=("Arial", 14)).grid(row=0, column=2, padx=10, pady=10)

    tk.Label(root, text="Einsatz:", bg="#2b2b2b", fg="#ffffff", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
    bet_amount_entry = tk.Entry(root, bg="#404040", fg="#ffffff", font=("Arial", 14))
    bet_amount_entry.grid(row=1, column=1, padx=10, pady=10)

    player_frame = tk.Frame(root, bg="#2b2b2b")
    player_frame.grid(row=2, column=0, columnspan=3, pady=20)

    tk.Button(root, text="Ausrechnen", command=submit_data, bg="#005f87", fg="#ffffff", activebackground="#0078a0", activeforeground="#ffffff", font=("Arial", 14)).grid(row=3, column=0, columnspan=3, pady=20)

    root.mainloop()

if __name__ == "__main__":
    calculate_payouts()
