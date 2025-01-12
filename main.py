def calculate_payouts():

    num_players = int(input("number of players: "))
    bet_amount = float(input("einsatz: "))

    print("namen: ")
    player_names = []
    for i in range(num_players):
        name = input(f"Player {i + 1} name: ")
        player_names.append(name)

    print("final tally:")
    final_euros = []
    for name in player_names:
        euros = float(input(f"{name}'s euros: "))
        final_euros.append(euros)

    balances = [final - bet_amount for final in final_euros]

    debtors = [(i, -balance) for i, balance in enumerate(balances) if balance < 0]
    creditors = [(i, balance) for i, balance in enumerate(balances) if balance > 0]

    if sum(final_euros) != num_players * bet_amount:
        print(f"insgesamt gibts {sum(final_euros)}, aber es sollten {num_players * bet_amount} vorhanden sein, sie negah")
        raise "kanak"

    print("\njeder muss zahlen:")
    while debtors and creditors:
        debtor_idx, debtor_amount = debtors.pop(0)
        creditor_idx, creditor_amount = creditors.pop(0)

        settlement_amount = min(debtor_amount, creditor_amount)

        print(f"{player_names[debtor_idx]} gibt {player_names[creditor_idx]} {settlement_amount:.2f}€")

        if debtor_amount > settlement_amount:
            debtors.insert(0, (debtor_idx, debtor_amount - settlement_amount))
        if creditor_amount > settlement_amount:
            creditors.insert(0, (creditor_idx, creditor_amount - settlement_amount))

    print("\nHurruh, fertig!")

if __name__ == "__main__":
    calculate_payouts()