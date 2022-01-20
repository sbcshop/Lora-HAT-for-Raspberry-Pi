#! /usr/bin/python3

"""
This file contains GUI code for Configuring of SBS Servo
Developed by - SB Components
http://sb-components.co.uk
"""

from lora_hat import LoraHat
import logging
import os
from tkinter import font
import tkinter as tk
from tkinter import messagebox
import webbrowser


if os.name == "posix":
    COMPORT_BASE = "/dev/"
else:
    COMPORT_BASE = ""


class MainApp(tk.Tk, LoraHat):
    """
    This is a class for Creating Frames and Buttons for left and top frame
    """
    port = "COM10"
    current_baud = 9600

    def __init__(self, *args, **kwargs):
        global logo, img, xy_pos

        tk.Tk.__init__(self, *args, **kwargs)
        LoraHat.__init__(self)

        self.screen_width = tk.Tk.winfo_screenwidth(self)
        self.screen_height = tk.Tk.winfo_screenheight(self)
        self.app_width = 800
        self.app_height = 480
        self.xpos = (self.screen_width / 2) - (self.app_width / 2)
        self.ypos = (self.screen_height / 2) - (self.app_height / 2)
        xy_pos = self.xpos, self.ypos

        self.label_font = font.Font(family="Helvetica", size=10)
        self.heading_font = font.Font(family="Helvetica", size=12)

        self.geometry(
            "%dx%d+%d+%d" % (self.app_width, self.app_height, self.xpos,
                             self.ypos))
        if not self.screen_width > self.app_width:
            self.attributes('-fullscreen', True)

        self.title("LORA HAT")

        self.config(bg="gray85")

        self.label_font = font.Font(family="Helvetica", size=10)
        self.heading_font = font.Font(family="Helvetica", size=12)
        self.LARGE_FONT = ("Verdana", 12)

        img = tk.PhotoImage(file=path + '/Images/settings.png')
        logo = tk.PhotoImage(file=path + '/Images/sblogo.png')

        self.top_frame_color = "dimgray"
        self.left_frame_color = "gray21"
        self.right_frame_color = "gray24"

        self.top_frame = tk.Frame(self, height=int(self.app_height / 12), bd=2,
                                  width=self.app_width,
                                  bg=self.top_frame_color)
        self.top_frame.pack(side="top", fill="both")

        self.left_frame = tk.Frame(self, width=int(self.app_width / 4),
                                   bg=self.left_frame_color)
        self.left_frame.pack(side="left", fill="both", expand="True")
        self.left_frame.pack_propagate(0)

        self.right_frame = tk.Frame(self, bg=self.right_frame_color)
        self.right_frame.pack(side="right", fill="both", expand=True)
        self.right_frame.propagate(0)

        self.rtx_frame = TransceiverFrame(parent=self.right_frame,
                                          controller=self)
        self.rtx_frame.tkraise()

        #  Top Bar
        tk.Label(self.top_frame, bg="dimgray", fg="ghostwhite",
                 text="LORA HAT",
                 font=font.Font(family="Helvetica", size=20)).place(x=340)
        url = "https://shop.sb-components.co.uk/"
        LabelButton(self.top_frame, url=url, image=logo, height=30,
                    bg="dimgray", x_pos=580, y_pos=1)
        self.left_frame_contents()

    def left_frame_contents(self):
        """
        This function creates the left frame widgets
        """
        global logo
        x_ref, y_ref = 10, 20
        font_ = font.Font(family="Helvetica", size=11)

        self.baud_var = tk.StringVar()
        self.parity_var = tk.StringVar()
        self.air_rate_var = tk.StringVar()
        self.packet_var = tk.StringVar()
        self.ch_rssi_var = tk.StringVar()
        self.tx_power_var = tk.StringVar()
        self.packet_rssi_var = tk.StringVar()
        self.reply_var = tk.StringVar()
        self.lbt_var = tk.StringVar()
        self.wor_var = tk.StringVar()
        self.wor_cycle_var = tk.StringVar()

        self.address_var = tk.IntVar()
        self.net_id_var = tk.IntVar()
        self.channel_var = tk.IntVar()
        self.encrypt_key_var = tk.IntVar()
        self.transmission_mode_var = tk.StringVar()
        self._com_port = tk.StringVar()
        self._set_baud_rate_var = tk.IntVar()

        self.baud_var.set("9600")
        self.parity_var.set("8N1")
        self.air_rate_var.set("2.4K")
        self.packet_var.set("240 bytes")
        self.ch_rssi_var.set("DISABLE")
        self.tx_power_var.set("22dbm")
        self.packet_rssi_var.set("DISABLE")
        self.transmission_mode_var.set("Transparent")
        self.reply_var.set("DISABLE")
        self.lbt_var.set("DISABLE")
        self.wor_var.set("WOR Receiver")
        self.wor_cycle_var.set("2000 ms")
        self._com_port.set(self.port)
        self._set_baud_rate_var.set(self.current_baud)

        self.address_var.set(0)
        self.net_id_var.set(0)
        self.channel_var.set(0)
        self.encrypt_key_var.set(0)

        self.baud_options = ["1200", "2400", "4800", "9600", "19200", "38400",
                             "57600", "115200"]
        self._set_baud_rate_options = [1200, 2400, 4800, 9600, 19200, 38400,
                                       57600, 115200]
        self.parity_options = ["8N1", "8O1", "8E1"]
        self.air_rate_options = ["0.3K", "1.2K", "2.4K", "4.8K", "9.6K",
                                 "19.2K", "38.4K", "62.5K"]
        self.packet_options = ["240 bytes", "128 bytes", "64 bytes",
                               "32 bytes"]
        self.enable_disable_options = ["DISABLE", "ENABLE"]
        self.tx_power_options = ["22dbm", "17dbm", "13dbm", "10dbm"]
        self.transmission_mode_options = ["Transparent", "Fixed Point"]
        self.wor_control_options = ["WOR Receiver", "WOR Transmitter"]
        self.wor_cycle_options = ["500 ms", "1000 ms", "1500 ms", "2000 ms",
                                  "2500 ms", "3000 ms", "3500 ms", "4000 ms"]

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Baud Rate").place(x=x_ref, y=y_ref)

        tk.OptionMenu(self.left_frame, self.baud_var,
                      *self.baud_options).place(x=x_ref + 140, y=y_ref,
                                                width=100,
                                                height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Parity").place(x=x_ref, y=y_ref + 40)

        tk.OptionMenu(self.left_frame, self.parity_var,
                      *self.parity_options).place(x=x_ref + 140, y=y_ref + 40,
                                                  width=100,
                                                  height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Air Data Rate").place(x=x_ref, y=y_ref + 80)

        tk.OptionMenu(self.left_frame, self.air_rate_var,
                      *self.air_rate_options).place(x=x_ref + 140,
                                                    y=y_ref + 80,
                                                    width=100, height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Packet Size").place(x=x_ref, y=y_ref + 120)

        tk.OptionMenu(self.left_frame, self.packet_var,
                      *self.packet_options).place(x=x_ref + 140, y=y_ref + 120,
                                                  width=100, height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Packet RSSI").place(x=x_ref, y=y_ref + 160)

        tk.OptionMenu(self.left_frame, self.packet_rssi_var,
                      *self.enable_disable_options).place(x=x_ref + 140,
                                                          y=y_ref + 160,
                                                          width=100,
                                                          height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Transmit Power").place(x=x_ref, y=y_ref + 200)

        tk.OptionMenu(self.left_frame, self.tx_power_var,
                      *self.tx_power_options).place(x=x_ref + 140,
                                                    y=y_ref + 200,
                                                    width=100,
                                                    height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Channel RSSI").place(x=x_ref, y=y_ref + 240)

        tk.OptionMenu(self.left_frame, self.ch_rssi_var,
                      *self.enable_disable_options).place(x=x_ref + 140,
                                                          y=y_ref + 240,
                                                          width=100,
                                                          height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Transmission Mode").place(x=x_ref, y=y_ref + 280)

        tk.OptionMenu(self.left_frame, self.transmission_mode_var,
                      *self.transmission_mode_options).place(x=x_ref + 140,
                                                             y=y_ref + 280,
                                                             width=100,
                                                             height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Reply").place(x=x_ref, y=y_ref + 320)

        tk.OptionMenu(self.left_frame, self.reply_var,
                      *self.enable_disable_options).place(x=x_ref + 140,
                                                          y=y_ref + 320,
                                                          width=100,
                                                          height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="LBT").place(x=x_ref, y=y_ref + 360)

        tk.OptionMenu(self.left_frame, self.lbt_var,
                      *self.enable_disable_options).place(x=x_ref + 140,
                                                          y=y_ref + 360,
                                                          width=100,
                                                          height=23)

        # Right Side
        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="WOR Control").place(x=x_ref + 270, y=y_ref)
        tk.OptionMenu(self.left_frame, self.wor_var,
                      *self.wor_control_options).place(x=x_ref + 370,
                                                       y=y_ref,
                                                       width=110,
                                                       height=23)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="WOR Cycle").place(x=x_ref + 270, y=y_ref + 40)

        tk.OptionMenu(self.left_frame, self.wor_cycle_var,
                      *self.wor_cycle_options).place(x=x_ref + 370,
                                                     y=y_ref + 40,
                                                     width=110,
                                                     height=23)

        # Module Address
        address_vcmd = (self.register(self.address_validate), '%P')
        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Address").place(x=x_ref + 270, y=y_ref + 80)
        tk.Entry(self.left_frame, fg="black", font=font_, width=12,
                 validate="key", validatecommand=address_vcmd,
                 textvariable=self.address_var).place(x=x_ref + 370,
                                                      y=y_ref + 80)

        net_id_vcmd = (self.register(self.net_id_validate), '%P')
        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Net ID").place(x=x_ref + 270, y=y_ref + 120)
        tk.Entry(self.left_frame, fg="black", font=font_, width=12,
                 validate="key", validatecommand=net_id_vcmd,
                 textvariable=self.net_id_var).place(x=x_ref + 370,
                                                     y=y_ref + 120)

        #  Channel
        channel_vcmd = (self.register(self.channel_validate), '%P')
        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Channel").place(x=x_ref + 270, y=y_ref + 160)
        tk.Entry(self.left_frame, fg="black", font=font_, width=12,
                 validate="key", validatecommand=channel_vcmd,
                 textvariable=self.channel_var).place(x=x_ref + 370,
                                                      y=y_ref + 160)

        encrypt_vcmd = (self.register(self.encrypt_validate), '%P')
        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=font_,
                 text="Encrypt Key").place(x=x_ref + 270, y=y_ref + 200)
        tk.Entry(self.left_frame, fg="black", font=font_, width=12,
                 validate="key", validatecommand=encrypt_vcmd,
                 textvariable=self.encrypt_key_var).place(x=x_ref + 370,
                                                          y=y_ref + 200)

        self.write_button = tk.Button(self.left_frame, text='Write',
                                      fg="white", bg="gray30", relief="raised",
                                      font=self.LARGE_FONT, bd=2,
                                      highlightthickness=0, width=8,
                                      command=self.write_to_lora)
        self.write_button.place(x=x_ref + 270, y=y_ref + 240)

        self.read_button = tk.Button(self.left_frame, text='Read',
                                     fg="white", bg="gray30", relief="raised",
                                     font=self.LARGE_FONT, bd=2,
                                     highlightthickness=0, width=8,
                                     command=self.read_from_lora)
        self.read_button.place(x=x_ref + 370, y=y_ref + 240)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=self.LARGE_FONT, text="Port").place(x=x_ref + 270,
                                                          y=y_ref + 290)
        self.com_entry = tk.Entry(self.left_frame, fg="black",
                             font=self.label_font, width=14,
                 textvariable=self._com_port)
        self.com_entry.place(x=x_ref + 370, y=y_ref + 290)

        tk.Label(self.left_frame, fg="white", bg=self.left_frame_color,
                 font=self.LARGE_FONT, text="Baudrate").place(x=x_ref + 270,
                                                              y=y_ref + 330)

        tk.OptionMenu(self.left_frame, self._set_baud_rate_var,
                      *self._set_baud_rate_options).place(x=x_ref + 370,
                                                          y=y_ref + 330,
                                                          width=110,
                                                          height=23)
        self.connect_button = tk.Button(self.left_frame, text="Connect",
                                        fg="white", bg=self.left_frame_color,
                                        font=self.LARGE_FONT, width=9,
                                        command=self.connect_lora_hat)
        self.connect_button.place(x=x_ref + 370, y=y_ref + 370)

        self.circle = tk.Canvas(self.left_frame, height=40, width=40,
                                bg=self.left_frame_color, bd=0,
                                highlightthickness=0)
        self.indication = self.circle.create_oval(10, 10, 25, 25, fill="red")
        self.circle.place(x=x_ref + 290, y=y_ref + 365)

    def write_to_lora(self):
        self.rtx_frame.talk_var.set(0)
        if self.alive:
            self.write_all_configuration()
        else:
            messagebox.showerror("Port Error",
                                 "Serial port not connected!")

    def read_from_lora(self):
        self.rtx_frame.talk_var.set(0)
        if self.alive:
            self.read_configuration_data()
        else:
            messagebox.showerror("Port Error",
                                 "Serial port not connected!")

    def set_variables(self):
        """
        Set Variables to send to LORA module
        """
        self._module_address = self.address_var.get()
        self._net_id = self.net_id_var.get()

        self._baud_rate = self.baud_options.index(self.baud_var.get())
        self._parity = self.parity_options.index(self.parity_var.get())
        self._air_data_rate = self.air_rate_options.index(
            self.air_rate_var.get())

        self._packet_size = self.packet_options.index(self.packet_var.get())
        self._packet_rssi = 0 if self.packet_rssi_var.get() == "DISABLE" else 1
        self._transmit_power = \
            self.tx_power_options.index(self.tx_power_var.get())

        self._channel = self.channel_var.get()

        self._channel_rssi = 0 if self.ch_rssi_var.get() == "DISABLE" else 1
        self._transmission_mode = \
            self.transmission_mode_options.index(self.transmission_mode_var \
                                                 .get())
        self._reply = 0 if self.reply_var.get() == "DISABLE" else 1
        self._lbt = 0 if self.lbt_var.get() == "DISABLE" else 1
        self._wor_tx_control = self.wor_control_options.index(
            self.wor_var.get())
        self._wor_cycle = self.wor_cycle_options.index(
            self.wor_cycle_var.get())

        self._encrypt_key = self.encrypt_key_var.get()

    def get_values(self, data):
        """
        Read data and set GUI variables
        Parameters
        ----------
        data: Data array from slave

        Returns
        -------
        None
        """
        self.address_var.set(data[3] << 8 | data[4])
        self.net_id_var.set(data[5])

        self.baud_var.set(self.baud_options[data[6] >> 5])
        self.parity_var.set(self.parity_options[(data[6] & 0b11000) >> 3])
        self.air_rate_var.set(self.air_rate_options[data[6] & 0b111])

        self.packet_var.set(self.packet_options[data[7] >> 6])
        self.packet_rssi_var.set("ENABLE" if (data[7] & 0b100000) else "DISABLE")
        self.tx_power_var.set(self.tx_power_options[data[7] & 0b11])

        self.channel_var.set(data[8])

        self.ch_rssi_var.set("ENABLE" if (data[9] & 0x80) else "DISABLE")
        self.transmission_mode_var.set(self.transmission_mode_options[(data[
                                                                           9] & 0x40) >> 6])
        self.reply_var.set("ENABLE" if (data[9] & 0x20) else "DISABLE")
        self.lbt_var.set("ENABLE" if (data[9] & 0x10) else "DISABLE")
        self.wor_var.set(self.wor_control_options[data[9] & 0x08])
        self.wor_cycle_var.set(self.wor_cycle_options[data[9] & 0b111])

        self.encrypt_key_var.set(data[10] << 8 | data[11])

    def connect_lora_hat(self):
        """
        This function connects the serial port
        """
        if self.connect_button.cget(
                'text') == 'Connect' and self._com_port.get():
            self.connect_hat(port=COMPORT_BASE + self._com_port.get(),
                             baud_rate=self._set_baud_rate_var.get())
            if self.alive:
                self.connect_button.config(relief="sunken", text="Disconnect")
                self.circle.itemconfigure(self.indication, fill="green3")
                self.com_entry.config(state="readonly")
            else:
                messagebox.showerror("Port Error",
                                     "Couldn't Connect with {} ".format(self._com_port.get(), self._set_baud_rate_var.get()))

        elif self.connect_button.cget('text') == 'Disconnect':
            self.connect_button.config(relief="raised", text="Connect")
            self.circle.itemconfigure(self.indication, fill="red")
            self.com_entry.config(state="normal")
            self.disconnect_hat()

    def update_rx_data(self, data):
        try:
            if self.rtx_frame.talk_var.get():
                data = data.decode("utf-8")
                self.rtx_frame.rx_text.set(data + "\n")
            else:
                self.get_values(data)
            self.rxData = []
        except:
            pass

    def address_validate(self, new_value):
        try:
            if not new_value or 0 <= int(new_value) <= 0xFFFF:
                return True
            else:
                self.bell()
                return False
        except ValueError:
            self.bell()
            return False

    def net_id_validate(self, new_value):
        try:
            if not new_value or 0 <= int(new_value) <= 0xFF:
                return True
            else:
                self.bell()
                return False
        except ValueError:
            self.bell()
            return False

    def channel_validate(self, new_value):
        try:
            if not new_value or 0 <= int(new_value) <= 80:
                return True
            else:
                self.bell()
                return False
        except ValueError:
            self.bell()
            return False

    def encrypt_validate(self, new_value):
        try:
            if not new_value or 0 <= int(new_value) <= 0xffff:
                return True
            else:
                self.bell()
                return False
        except ValueError:
            self.bell()
            return False


class TransceiverFrame(tk.Frame):
    """
    This is a class for Creating widgets for Matplotlib Graph
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.LARGE_FONT = self.controller.LARGE_FONT
        self.bg_color = self.controller.right_frame_color

        self.talk_var = tk.IntVar()
        self.talk_var.set(0)
        self.rx_text = tk.StringVar()

        tk.Label(parent, fg="white", bg=self.bg_color, font=font.Font(
            family="Helvetica", size=11), text="Talk Mode").place(x=10, y=15)

        tk.Radiobutton(parent, text="On", variable=self.talk_var, value=1,
                       command=self.set_talk_mode).place(x=150, y=15)

        tk.Radiobutton(parent, text="Off", variable=self.talk_var, value=0,
                       command=self.set_talk_mode).place(x=230, y=15)

        # Receiver Label Box
        self.rx_label = tk.Label(parent, justify="left", anchor="nw",
                                 wraplength=270,
                                 bg="gray80", fg="black",
                                 bd=2, height=5, width=37, padx=10, pady=10,
                                 textvariable=self.rx_text)
        self.rx_label.place(x=10, y=60)

        tk.Label(parent, fg="white", bg=self.bg_color, font=font.Font(
            family="Helvetica", size=11), text="Rx Message").place(x=10, y=160)

        # Transmitter Text Box
        self.tx_text = tk.Text(parent, padx=10, pady=10, bg="gray80",
                               fg="black", height=6, width=33,
                               wrap="word",
                               relief="sunken", state="normal")
        self.tx_text.place(x=10, y=200)
        tk.Label(parent, fg="white", bg=self.bg_color, font=font.Font(
            family="Helvetica", size=11), text="Type Tx Message").place(x=10,
                                                                        y=320)

        self.send_button = tk.Button(parent, text='Send',
                                     fg="white", bg="gray30", relief="raised",
                                     font=self.LARGE_FONT, bd=2,
                                     highlightthickness=0, width=20,
                                     command=self.send_msg)
        self.send_button.place(x=50, y=360)

    def set_talk_mode(self):
        if self.talk_var.get():
            self.controller.normal_mode()
        else:
            self.controller.deep_sleep_mode()

    def send_msg(self):
        if not self.talk_var.get():
            self.talk_var.set(1)
            self.controller.normal_mode()
        if self.controller.alive:
            msg = self.tx_text.get("1.0", "end")
            self.controller.transmit_message(msg.encode("utf-8"))
        else:
            messagebox.showerror("Port Error",
                                 "Serial port not connected!")


class LabelButton(object):
    def __init__(self, master, image=None, height=40, width=250, bg="white",
                 url=None, x_pos=7, y_pos=700):
        global logo
        # if image is None:
        image = logo
        self.url = url
        self.label = tk.Label(master, image=logo, height=height,
                              width=width, bg=bg)
        self.label.place(x=x_pos, y=y_pos)
        self.label.bind("<Button-1>", self.open_url)

    def open_url(self, tmp):
        webbrowser.open(self.url, new=1)


logo = None
img = None
path = os.path.abspath(os.path.dirname(__file__))
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

if __name__ == "__main__":
    app = MainApp()
    app.tk.call('wm', 'iconphoto', app._w, img)
    app.resizable(0, 0)
    app.mainloop()
