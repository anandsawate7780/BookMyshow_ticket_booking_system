#!/usr/bin/env python
# coding: utf-8

# # Ananta Sawate batch AE-28 

# In[3]:


def city():
    global x    # Variables that are created outside of a function
                # Global variables can be used by everyone, both inside of functions and outside.
    x=0
    x = x+1

    print("HI WELCOME TO BOOK_MY_MOVIE.COM: ")
    print("where you want to watch movie?:")
    print("1:  Kalyan")
    print("2:  Thane ")
    print("4:  Andheri")
    print("5:  Bandra")
    print("6:  Borivali.")
    print("7:  Dahisar")
    print("8:  Goregaon")
    print("9:  Jogeshwari.")
    print("10: Juhu.")
    print("11: Kandivali ")
    
    
    place = int(input("choose your option: "))
    center()
    
# this function is used to select theater
def center():
    print("which theater do you wish to see movie? ")
    print("1: Inox")
    print("2: Cinépolis")
    print("3: pvr")
    print("4: Carnival Cinemas")
    print("5: Eros Cinema")
    print("6: back")
    a = int(input("choose your option: "))
    
    t_movie()
    
def t_movie():
  
    print("which movie do you want to watch?")
    print("1: Drishyam 2 ")
    print("2: Bhediya ")
    print("3: Black Panther: Wakanda Forever")
    print("4: back")
    movie = int(input("choose your movie: "))

    Theater_class()
    
    
 # this theater function used to select CLASS
def Theater_class():
    print("which class do you want to prefer: ")
    print("1: AC First Class")
    print("2: NON-AC Second class")
 
    Theater_class= int(input("choose your Class: "))
   
    if Theater_class ==1:
        print("(1) AC First Class ")
    elif Theater_class ==2:
        print("(2)  NON-AC Second class")
    else:
        print("wrong choice")
    theater()    
    
# this timing function used to select timing for movie
def theater():
    print("which screen do you want to watch movie: ")
    print("1: SCREEN 1")
    print("2: SCREEN 2")
    print("3: SCREEN 3")
    a = int(input("choose your screen: "))
    ticket = int(input("number of ticket do you want?: "))
    timing(a)
 
# this timing function used to select timing for movie
def timing(a): 
    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("Booking successful!, enjoy movie at "+x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("Booking successful!, enjoy movie at "+x)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("Booking successful!, enjoy movie at "+x)
    return 0


city()   # it calls the function city


# In[ ]:




