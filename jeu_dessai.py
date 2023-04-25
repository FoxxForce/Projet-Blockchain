#!/usr/bin/env python3
from node import * 

# BLOC n°1
# med fabr
transaction_1 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='PziferMedFacility', transported_to='',
                            date='01/01/2023')
transaction_1.sign_transaction(private_key)

# paquet transp au distrib
transaction_2 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='PziferMedFacility', transported_to='JonathanDistrib',
                            date='01/01/2023')
transaction_2.sign_transaction(private_key)

# med fabr
transaction_4 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferAYAYA', batch_id='0003', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='PziferMedFacility', transported_to='',
                            date='01/01/2023')
transaction_4.sign_transaction(private_key)

# paquet transp au distrib
transaction_5 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferAYAYA', batch_id='0003', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='PziferMedFacility', transported_to='JosephDistrib',
                            date='01/01/2023')
transaction_5.sign_transaction(private_key)





# BLOC n°2 chez JosephDistrib
# paquet arrivé au distrib
transaction_1 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferAYAYA', batch_id='0003', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='JosephDistrib', transported_to='',
                            date='02/01/2023')
transaction_1.sign_transaction(private_key)

# paquet transp au magasin
transaction_2 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferAYAYA', batch_id='0003', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='JosephDistrib', transported_to='MartWall',
                            date='02/01/2023')
transaction_2.sign_transaction(private_key)





# BLOC n°3
# med fabr
transaction_4 = Transaction(prodution_place='DoliMedFacility', production_date='01/01/2023', 
                            product_name='DoliCrane', batch_id='0002', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='DoliMedFacility', transported_to='',
                            date='03/01/2023')
transaction_4.sign_transaction(private_key)

# paquet transp au distrib
transaction_1 = Transaction(prodution_place='DoliMedFacility', production_date='01/01/2023', 
                            product_name='DoliCrane', batch_id='0002', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='DoliMedFacility', transported_to='JonathanDistrib',
                            date='03/01/2023')
transaction_1.sign_transaction(private_key)





# BLOC n°4 chez JonathanDistrib
# paquet arrivé au distrib
transaction_1 = Transaction(prodution_place='DoliMedFacility', production_date='01/01/2023', 
                            product_name='DoliCrane', batch_id='0002', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='JonathanDistrib', transported_to='',
                            date='04/01/2023')
transaction_1.sign_transaction(private_key)

# paquet arrivé au distrib
transaction_2 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='JonathanDistrib', transported_to='',
                            date='04/01/2023')
transaction_2.sign_transaction(private_key)

# paquet transp au magasin
transaction_2 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='JonathanDistrib', transported_to='MartWall',
                            date='04/01/2023')
transaction_2.sign_transaction(private_key)

# paquet transp au magasin
transaction_2 = Transaction(prodution_place='DoliMedFacility', production_date='01/01/2023', 
                            product_name='DoliCrane', batch_id='0002', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='JonathanDistrib', transported_to='MartWall',
                            date='04/01/2023')
transaction_2.sign_transaction(private_key)




# BLOC n°5 chez MartWall
# paquet arrivé au magasin
transaction_1 = Transaction(prodution_place='DoliMedFacility', production_date='01/01/2023', 
                            product_name='DoliCrane', batch_id='0002', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='MartWall', transported_to='',
                            date='04/01/2023')
transaction_1.sign_transaction(private_key)

# paquet arrivé au magasin
transaction_2 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='MartWall', transported_to='',
                            date='04/01/2023')
transaction_2.sign_transaction(private_key)

# paquet arrivé au magasin
transaction_2 = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferAYAYA', batch_id='0003', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='MartWall', transported_to='',
                            date='04/01/2023')
transaction_2.sign_transaction(private_key)







''' template pour les états des transactions 

# BLOC n°X
# med fabr
transaction_X = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='PziferMedFacility', transported_to='',
                            date='XX/01/2023')
transaction_X.sign_transaction(private_key)

# paquet transp au distrib
transaction_X = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='PziferMedFacility', transported_to='JonathanDistribution',
                            date='XX/01/2023')
transaction_X.sign_transaction(private_key)

# paquet arrivé au distrib
transaction_X = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='JonathanDistribution', transported_to='',
                            date='XX/01/2023')
transaction_X.sign_transaction(private_key)

# paquet transp au magasin
transaction_X = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='JonathanDistribution', transported_to='Martwall',
                            date='XX/01/2023')
transaction_X.sign_transaction(private_key)

# paquet arrivé au magasin
transaction_X = Transaction(prodution_place='PziferMedFacility', production_date='01/01/2023', 
                            product_name='PziferPshht', batch_id='0001', 
                            sender_public_key=public_key.save_pkcs1().decode(), 
                            current_location='Martwall', transported_to='',
                            date='XX/01/2023')
transaction_X.sign_transaction(private_key)

'''