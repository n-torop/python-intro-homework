import re

#####################Version1
temp=input("Enter temperature in F: ")
temp_only=int(re.sub(r'\D', '', temp))
formula=(temp_only-32)*5/9
upd_form=round(formula, 1)
print (f'{temp_only}°F is {upd_form}°C.')

#####################Version2

# while True:
#     temp=input("Enter temperature in F: ")
#     try:
#         temp=float(temp)
#         formula=(temp-32)*5/9
#         upd_form=round(formula, 1)
#         print (f'{temp}°F is {upd_form}°C.')
#         break

#     except:
#         try:
#             if not temp:
#                 print ("Empty field. Try again")
#             else:
#                 temp_only=float(re.sub(r'[^\d.]', '', temp))
#                 formula=(temp_only-32)*5/9
#                 upd_form=round(formula, 1)
#                 print (f'{temp_only}°F is {upd_form}°C.')
#                 break
#         except:
#             print ("Program failed. Try again")
        
    
#####################Version3
# while True:
#     from_user_scale=input("Convert from F, C, or K or Q for 'quit' (type letter): ").upper()
#     if from_user_scale=="Q":
#         break
#     to_user_scale=(input("Convert to F, C, or K (type letter): ")).upper()
#     temp=input ("Type current temperature: ")
#     temp=float(temp)
    

#     def FC(temp): 
#         formula_FC=(temp-32)*5/9
#         return formula_FC
#     def CF( temp): 
#         formula_CF=(temp*1.8)+32
#         return formula_CF
#     def CK(temp): 
#         formula_CK=temp+273.15
#         return formula_CK
#     def FK(ftemp): 
#         formula_FK=(temp-32)/1.8+273.15
#         return formula_FK
#     def KF( temp): 
#         formula_KF=(temp*1.8)-459.67
#         return formula_KF
#     def KC(temp): 
#         formula_KC=temp-273.15
#         return formula_KC

#     operations={
#         ("F", "C"): FC,
#         ("C", "F"): CF,
#         ("C", "K"): CK,
#         ("F", "K"): FK,
#         ("K", "F"): KF,
#         ("K", "C"): KC,
#     }

#     current_op=operations.get((from_user_scale, to_user_scale))

#     result=current_op(temp)
#     print (round(result, 1))
    

