"""
Starttheparty.py

Bepaalt met bepaalde condities of een feest kan beginnen, op basis van
de aanwezigheid van een gastheer, gasten, drank en chips.
"""

gastheer = True
gasten = True
drank = True
chips = True

# een feest kan beginnen als er een gastheer is, of als er gasten zijn
start_condition_1 = gastheer or gasten

# een feest kan beginnen als er een gastheer is, of als er gasten zijn en er zijn chips en drank
start_condition_2 = gastheer or (gasten and chips and drank)

# een feest kan beginnen als er geen chips zijn, of als er drank is
start_condition_3 = (not chips) or drank

# een feest kan beginnen als er geen gasten zijn, of als er chips of drank is
start_condition_4 = (not gasten) or chips or drank

# een feest kan beginnen als er geen gastheer is, of als er drank is
start_condition_5 = (not gastheer) or drank

# alleen chips zijn niet genoeg om een feest te beginnen, er moet ook een gastheer, gasten of drank aanwezig zijn
start_condition_6 = not (chips and not gastheer and not gasten and not drank)

if (start_condition_1 and start_condition_2 and start_condition_3
        and start_condition_4 and start_condition_5 and start_condition_6):
    print('Start the Party')
else:
    print('No Party')