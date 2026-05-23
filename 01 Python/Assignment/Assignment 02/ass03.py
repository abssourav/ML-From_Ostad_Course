#define tuple
tuple1 = ('Abu Bakkar', 23 , 'Siddique', 40.5)
tuple2 = ('Abu Bakkar', 22 , 'Siddique', 45.3)

#unpacked first tuple
(name,age,short_name,weight) = tuple1


#comparison
is_same_person = (tuple1==tuple2)
is_greater_than = (tuple1 > tuple2)


print(f"Are they same : {is_same_person}")
print(f"is tuple1 greater than tuple2 : {is_greater_than}")



"""

<--------Difference between list nad tuple --------->

                 List               vs                  tuple
        ----------------------                     -----------------------------
             mutable                                     immutable
            dynamic                                       static 
       assign by square bracket []                  assign by parentheses ()
       using for general data                       using for very sensitive data
 
"""