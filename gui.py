import tkinter as tk

root = tk.Tk(className='Watermark Image')
root.geometry("800x600")
root.configure(bg='white')


add_images = tk.Button(root, text='Add Images', width=25, command=root.destroy)
add_images.grid()

clear_images = tk.Button(root, text='Clear Images', width=25, command=root.destroy)
clear_images.grid()

next_step = tk.Button(root, text='Next Step', width=25, bg='green', fg='blue')
next_step.grid()

root.mainloop()