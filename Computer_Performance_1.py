from tkinter import *
import psutil
import math
import speedtest
from PIL import Image,ImageTk # 'PIL' stands for pillow

def usage(): # 2nd approach

    cpus = psutil.cpu_count()
    cpus_label.config(text=cpus,image=tk_image,compound='center',fg='#00ffff') # 'fg' indicates foreground color and '.config' indicates
                                                                               # that we are configuring it to a new value

    cpu_usage = psutil.cpu_percent(1) # It will only count the CPU usage as soon as we run the code 
                                    # at that instane where we run the code. '1' indicate 1 sec
    cpu_usage_label.config(text=cpu_usage,image=tk_image,compound='center',fg='#00ffff')
    cpu_usage_label.after(100,usage) # We are repeating the usage function for every sec
                                     # and '100' indicates milli sec
    
    ram_count=math.floor(psutil.virtual_memory()[0]/1000000000)
    ram_count_text=str(ram_count)+"GB"
    ram_count_label.config(text=ram_count_text,image=tk_image,compound='center',fg='#00ffff')

    ram_usage=math.floor(psutil.virtual_memory()[2])
    ram_usage_text=str(ram_usage)+"%"
    ram_usage_label.config(text=ram_usage_text,image=tk_image,compound='center',fg='#00ffff')

    available_ram=math.floor(psutil.virtual_memory()[1]/1000000000)
    available_ram_text=str(available_ram)+"GB"
    ram_available_label.config(text=available_ram_text,image=tk_image,compound='center',fg='#00ffff')


def internet_speed():

    print("Testing internet speed")
    st=speedtest.Speedtest() # Creating speedtest object or speedtest instance
    Download_speed=str(math.floor(st.download()/1000000))+"Mb/s" # Converting bytes per sec to megabytes per sec
    Upload_speed=str(math.floor(st.upload()/1000000))+"Mb/s"
    Ping=str("%.0f"%(st.results.ping))+"Ms"

    download_label.config(text=Download_speed)
    upload_label.config(text=Upload_speed)
    ping_label.config(text=Ping)
    


# Create an instance of that particular 'Tkinter' library
root=Tk() # This will go ahead and create the instance of that particular app
root.config(bg='black')

# Once you have this app instance, you could set the different properties of your application

image=Image.open(r'C:\Users\f8\Desktop\Campus Interviews\Python Programming\Python Projects\Computer Performance & Internet Speed Monitor Using Tkinter\Python_Code\single.png') # This 'single.png' file contains our speedometer img
tk_image=ImageTk.PhotoImage(image) # We are converting our img to the 'Tkinter' img

root.geometry("1700x1080") # We are setting the geometry of our root window
root.title('CPU Status') # We are setting the title of our root window



# Code for CPU count

cpus_label=Label(root,font=("Orbitron",40,'bold'),text="0",bd=-4) # Label is created and 'bd' indicates border. We have included
                                                                  # 'root' inside the 'Label' in order to specify that this label
                                                                  # belongs to this 'root' window
# cpus_label=Label(root,text=psutil.cpu_count()) # 1st approach

cpus_label.grid(row=0,column=0) # Now we are placing the label in the 1st row and also in the 
                                # 1st column with the help of 'grid' layout manager
l1 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="CPUs")
l1.grid(row=1,column=0)



# Code for CPU usage in terms of %

cpu_usage_label = Label(root,font=("Orbitron",40,'bold'),text="0",bd=-4)
cpu_usage_label.grid(row=0,column=1)

l2 = Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="CPU Usage In %")
l2.grid(row=1,column=1)


# Code for the total RAM

ram_count_label=Label(root,font=("Orbitron",40,'bold'),text='0',bd=-4)
ram_count_label.grid(row=0,column=2)

l3=Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Total RAM")
l3.grid(row=1,column=2)



# Code for the RAM usage in %

ram_usage_label=Label(root,font=("Orbitron",40,'bold'),text='0',bd=-4)
ram_usage_label.grid(row=0,column=3)

l4=Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="RAM usage in %")
l4.grid(row=1,column=3)


# Code for the available RAM

ram_available_label=Label(root,font=("Orbitron",40,'bold'),text='0',bd=-4)
ram_available_label.grid(row=0,column=4)

l5=Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Available RAM")
l5.grid(row=1,column=4)


# Code for the Network speed

speed_button=Button(root,text="Test internet speed",command=internet_speed,width=15,height=3,font=("orbitron",20,'bold')) # 'internet_speed' is a function
speed_button.grid(row=3,column=0)

download_label=Label(root,font=("Orbitron",40,'bold'),text="0 Mb/s",image=tk_image,compound='center',fg='#00ffff',bd=-4)
download_label.grid(row=3, column=1)

l6=Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Download speed")
l6.grid(row=4,column=1)

upload_label=Label(root,font=("Orbitron",40,'bold'),text="0 Mb/s",image=tk_image,compound='center',fg='#00ffff',bd=-4)
upload_label.grid(row=3, column=2)

l7=Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Upload speed")
l7.grid(row=4,column=2)

ping_label=Label(root,font=("Orbitron",40,'bold'),text="0 Mb/s",image=tk_image,compound='center',fg='#00ffff',bd=-4)
ping_label.grid(row=3, column=3)

l8=Label(root,font=("Orbitron",20,'bold'),bg='black',fg='#fcba03',text="Ping")
l8.grid(row=4,column=3)

usage() # We are calling the function
root.mainloop() # Create a root window and displays it until and unless you quit that window

