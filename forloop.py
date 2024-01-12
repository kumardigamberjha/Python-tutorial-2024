# 1,2,3,4,5,6,7,8,9

arr = [1,"Apple",3,"Coding India",5,"MCA",7,8,9]

print(arr)

# for i in arr:
#     print(i)

# 1, 7 (7-1)=6
# for i in range(1,11, 3):
#     print(i)



for chsadh in range(len(arr)):
    print(arr[chsadh])


str1 = "Coding India"
print(str1)

# for i in str1:
#     print(i)

#     if i == "g":
#         break

#     print(i)

str1 = "Coding India is great"

for i in str1:

    if i == " ":
        break

    print(i)


else:
    print("Finished")


# Nested For Loops

arr = [1,2,3,4,5,"MCA",7,8,9]

arr2 = ["digamber", 'coding India', "MCA"]

for i in range(len(arr)):
    print(arr[i])

    for j in range(len(arr2)):
        print(arr2[j])

        if arr2[j] == arr[i]:
            print("MAtched")
        
    break