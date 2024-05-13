import classes
import datetime
import random

Booked_dates=[]
hotels=[]

def booking(date, hotel, room, name):
    if check_room_status(room.number)==False:
        
        Booked_dates.append(classes.Booking(name, hotel, room, date))
        return room.price     
    else:
        return "Ez a szoba már foglalt!"
   
def Delete_booked_date(name):
    for i in range(len(Booked_dates)):
        if Booked_dates[i].costumer_name.lower()==name.lower():
            Booked_dates[i].remove()
            Booked_dates.pop(i)
            break
    print("Foglalását töröltük!")
def list_out_rooms(hotel):
    for i in hotels:
        if i ==hotel:
            return i.list_rooms()

def list_out_occupied_rooms(hotel):
    string=""
    for i in Booked_dates:
        if hotel==i.hotel_name:
            time=i.date.strftime("%m-%d")
            string+=f"Room number: {i.room.number} For this period: {time}\n"
    print(string)
        
def check_room_status(number, date):
    occupied=False
    for i in range(len(Booked_dates)):
        if Booked_dates[i].room.number==number and Booked_dates[i].date==date:
            occupied=True
    return occupied

def add(name,hotel,room_number,date):
     for i in hotels:
         for j in i.roomlist:
             if room_number==j.number:
                 room=j
                 break
     Booked_dates.append(classes.Booking(name,hotel,room,date))
     return "Sikeres foglalás!"
 
def input_to_date(month, day): 
     month=int(month); day=int(day)
     year=datetime.datetime.now().year
     date=datetime.date(year,month,day)
     return date
 
def create_rooms(one_bed_count, two_bed_count):
     room_list=[]
     max_room=one_bed_count+two_bed_count
     count_two_bed=0
     for i in range(1, max_room+1):
         is_it_two_bed=bool(random.randint(0,1))
         if count_two_bed<two_bed_count and is_it_two_bed==True:
             room_list.append(classes.Twobed(i))
             count_two_bed+=1
         else:
             room_list.append(classes.Onebed(i))
     return room_list
        
def Create_hotel(name, one_bed_count, two_bed_count):
    roomlist=create_rooms(one_bed_count,two_bed_count)
    hot=classes.Hotel(name, roomlist)
    hotels.append(hot)

#region examples
Create_hotel("Golden Coast Hotel",100,50)
add("Gizi", "Golden Coast Hotel", random.randint(1,150), datetime.datetime.now())
add("Dani", "Golden Coast Hotel", random.randint(1,150), datetime.datetime.now())
add("Bianka", "Golden Coast Hotel", random.randint(1,150), datetime.datetime.now())
add("Bence", "Golden Coast Hotel", random.randint(1,150), datetime.datetime.now())
add("Tibor", "Golden Coast Hotel", random.randint(1,150), datetime.datetime.now())
add("Andris", "Golden Coast Hotel", random.randint(1,150), datetime.datetime.now())
add("Alexa", "Golden Coast Hotel", random.randint(1,150), datetime.datetime.now())
add("Mia", "Golden Coast Hotel", random.randint(1,150), datetime.datetime.now())
add("まひろ", "Golden Coast Hotel", random.randint(1,150), datetime.datetime.now())
#endregion    
