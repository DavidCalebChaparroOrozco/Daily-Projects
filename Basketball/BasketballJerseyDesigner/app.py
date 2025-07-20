# Import necessary libraries
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Define the path to the jersey template image
JERSEY_TEMPLATE_PATH = "images/Jersey.png"

# Define the main class for the Basketball Jersey Designer application
class BasketballJerseyDesigner:
    def __init__(self, root):
        self.root = root
        self.root.title("Basketball Jersey Designer by David Caleb")
        self.root.geometry("700x600")

        self.jersey_color = "#FFFFFF"
        self.shorts_color = "#FFFFFF"
        self.text_color = "#000000"
        self.player_name = "PLAYER"
        self.player_number = "00"

        self.create_widgets()

    # Create the main widgets for the application
    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg='white')
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        controls_frame = tk.Frame(self.root)
        controls_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        tk.Label(controls_frame, text="Player Name:").pack()
        self.name_entry = tk.Entry(controls_frame)
        self.name_entry.insert(0, self.player_name)
        self.name_entry.pack()

        tk.Label(controls_frame, text="Player Number:").pack()
        self.number_entry = tk.Entry(controls_frame)
        self.number_entry.insert(0, self.player_number)
        self.number_entry.pack()

        tk.Button(controls_frame, text="Choose Jersey Color", command=self.choose_jersey_color).pack(pady=5)
        tk.Button(controls_frame, text="Choose Shorts Color", command=self.choose_shorts_color).pack(pady=5)
        tk.Button(controls_frame, text="Choose Text Color", command=self.choose_text_color).pack(pady=5)
        tk.Button(controls_frame, text="Update Design", command=self.update_design).pack(pady=5)
        tk.Button(controls_frame, text="Save Design", command=self.save_design).pack(pady=5)

        self.update_design()

    # Define methods for choosing colors, updating the design, and saving the design
    def choose_jersey_color(self):
        color = colorchooser.askcolor(title="Choose Jersey Color")
        if color[1]:
            self.jersey_color = color[1]
            self.update_design()

    def choose_shorts_color(self):
        color = colorchooser.askcolor(title="Choose Shorts Color")
        if color[1]:
            self.shorts_color = color[1]
            self.update_design()

    def choose_text_color(self):
        color = colorchooser.askcolor(title="Choose Text Color")
        if color[1]:
            self.text_color = color[1]
            self.update_design()

    def fill_polygon(self, draw, coords, color):
        points = [(coords[i], coords[i+1]) for i in range(0, len(coords), 2)]
        draw.polygon(points, fill=color)

    def update_design(self):
        self.player_name = self.name_entry.get()
        self.player_number = self.number_entry.get()

        base_img = Image.open(JERSEY_TEMPLATE_PATH).convert("RGBA")
        draw = ImageDraw.Draw(base_img)

        jersey_front_coords = [400,247,397,545,495,566,561,565,631,562,695,546,696,463,695,253,658,217,635,139,642,87,610,77,591,139,552,162,500,138,482,78,457,83,458,148,444,210]
        shorts_front_coords = [397,635,540,633,693,633,716,835,710,866,650,887,572,888,545,738,523,883,445,885,383,862,377,835]
        jersey_back_coords = [775,546,860,563,1017,563,1073,544,1071,247,1038,222,1017,183,1014,88,978,73,956,99,919,103,878,92,867,71,832,86,826,193,800,231,775,247]
        shorts_back_coords = [777,632,1070,631,1092,833,1084,863,1027,884,946,881,923,733,901,880,827,885,762,864,753,835]

        self.fill_polygon(draw, jersey_front_coords, self.jersey_color)
        self.fill_polygon(draw, shorts_front_coords, self.shorts_color)
        self.fill_polygon(draw, jersey_back_coords, self.jersey_color)
        self.fill_polygon(draw, shorts_back_coords, self.shorts_color)

        try:
            font_name = ImageFont.truetype("Fonts/trebuchet-ms-2/trebuc.ttf", 50)
            font_number = ImageFont.truetype("Fonts/trebuchet-ms-2/trebuc.ttf", 60)
        except:
            font_name = ImageFont.load_default()
            font_number = ImageFont.load_default()

        bbox_name = draw.textbbox((0, 0), self.player_name, font=font_name)
        w_name = bbox_name[2] - bbox_name[0]
        draw.text((540 - w_name/2, 200), self.player_name, font=font_name, fill=self.text_color)

        bbox_number = draw.textbbox((0, 0), self.player_number, font=font_number)
        w_number = bbox_number[2] - bbox_number[0]
        draw.text((540 - w_number/2, 250), self.player_number, font=font_number, fill=self.text_color)

        # Draw text on the jersey back
        bbox_name_back = draw.textbbox((0, 0), self.player_name, font=font_name)
        w_name_back = bbox_name_back[2] - bbox_name_back[0]
        draw.text((925 - w_name_back/2, 150), self.player_name, font=font_name, fill=self.text_color)

        bbox_number_back = draw.textbbox((0, 0), self.player_number, font=font_number)
        w_number_back = bbox_number_back[2] - bbox_number_back[0]
        draw.text((925 - w_number_back/2, 250), self.player_number, font=font_number, fill=self.text_color)

        self.current_image = ImageTk.PhotoImage(base_img.resize((500, 500)))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.current_image)

    # Method to save the designed jersey as an image file
    def save_design(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                    filetypes=[("PNG files", "*.png")])
        if file_path:
            base_img = Image.open(JERSEY_TEMPLATE_PATH).convert("RGBA")
            draw = ImageDraw.Draw(base_img)

            jersey_front_coords = [400,247,397,545,495,566,561,565,631,562,695,546,696,463,695,253,658,217,635,139,642,87,610,77,591,139,552,162,500,138,482,78,457,83,458,148,444,210]
            shorts_front_coords = [397,635,540,633,693,633,716,835,710,866,650,887,572,888,545,738,523,883,445,885,383,862,377,835]
            jersey_back_coords = [775,546,860,563,1017,563,1073,544,1071,247,1038,222,1017,183,1014,88,978,73,956,99,919,103,878,92,867,71,832,86,826,193,800,231,775,247]
            shorts_back_coords = [777,632,1070,631,1092,833,1084,863,1027,884,946,881,923,733,901,880,827,885,762,864,753,835]

            self.fill_polygon(draw, jersey_front_coords, self.jersey_color)
            self.fill_polygon(draw, shorts_front_coords, self.shorts_color)
            self.fill_polygon(draw, jersey_back_coords, self.jersey_color)
            self.fill_polygon(draw, shorts_back_coords, self.shorts_color)

            try:
                font_name = ImageFont.truetype("Fonts/trebuchet-ms-2/trebuc.ttf", 50)
                font_number = ImageFont.truetype("Fonts/trebuchet-ms-2/trebuc.ttf", 60)
            except:
                messagebox.showwarning("Font Not Found", "Trebuchet MS font not found. Using default font.")
                font_name = ImageFont.load_default()
                font_number = ImageFont.load_default()

            bbox_name = draw.textbbox((0, 0), self.player_name, font=font_name)
            w_name = bbox_name[2] - bbox_name[0]
            draw.text((495 - w_name/2, 350), self.player_name, font=font_name, fill=self.text_color)

            bbox_number = draw.textbbox((0, 0), self.player_number, font=font_number)
            w_number = bbox_number[2] - bbox_number[0]
            draw.text((495 - w_number/2, 380), self.player_number, font=font_number, fill=self.text_color)

            bbox_name_back = draw.textbbox((0, 0), self.player_name, font=font_name)
            w_name_back = bbox_name_back[2] - bbox_name_back[0]
            draw.text((900 - w_name_back/2, 350), self.player_name, font=font_name, fill=self.text_color)

            bbox_number_back = draw.textbbox((0, 0), self.player_number, font=font_number)
            w_number_back = bbox_number_back[2] - bbox_number_back[0]
            draw.text((900 - w_number_back/2, 380), self.player_number, font=font_number, fill=self.text_color)

            base_img.save(file_path)
            messagebox.showinfo("Saved", f"Jersey design saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BasketballJerseyDesigner(root)
    root.mainloop()

# rgb(147, 150, 182)
# rgb(12, 15, 15)
# rgb(68, 76, 108)

# rgb(191, 162, 110)
# rgb(52, 36, 30)
# rgb(124, 64, 46)
