import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class ResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Резюме")
        self.root.geometry("600x650")
        self.root.configure(bg='#f8f9fa')

        self.load_images()
        self.create_widgets()

    def load_images(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            images_dir = os.path.join(script_dir, "images")

            profile_path = os.path.join(images_dir, "profile_image.jpg")
            profile_img = Image.open(profile_path)
            profile_img = profile_img.resize((100, 100), Image.LANCZOS)
            self.profile_photo = ImageTk.PhotoImage(profile_img)

            background_path = os.path.join(images_dir, "fon.webp")
            background_img = Image.open(background_path)
            background_img = background_img.resize((600, 300), Image.LANCZOS)  
            self.background_photo = ImageTk.PhotoImage(background_img)
        
        except FileNotFoundError as error:
            print(f"Ошибка загрузки фото:\n{error}")
            self.profile_photo = None
            self.background_photo = None

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg='#f8f9fa')
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        header_frame = tk.Frame(main_frame, bg='#2c3e50', height=100)
        header_frame.pack(fill="x", pady=(0, 0)) 
        header_frame.pack_propagate(False)

        if self.background_photo:
            bg_label = tk.Label(header_frame, image=self.background_photo, bg='#2c3e50')
            bg_label.place(relx=0.5, rely=0.5, anchor="center")  

        profile_container = tk.Frame(main_frame, bg='#f8f9fa')  
        profile_container.place(relx=0.5, y=80, anchor="center")  

        if self.profile_photo:
            profile_circle = tk.Frame(profile_container, bg='white', width=110, height=110, 
                                    relief='solid', borderwidth=2)
            profile_circle.pack_propagate(False)
            profile_circle.pack()
            
            profile_label = tk.Label(profile_circle, image=self.profile_photo, bg="white")
            profile_label.pack(expand=True)

        info_frame = tk.Frame(main_frame, bg='white', relief='flat', borderwidth=1)
        info_frame.pack(fill="x", pady=(60, 10))  

        name_label = tk.Label(info_frame, text="Кувшинов Максим", bg="white", 
                            fg='#2c3e50', font=("Arial", 18, "bold"))
        name_label.pack(pady=(15, 2)) 

        position_label = tk.Label(info_frame, text="Full-Stack Разработчик", bg="white", 
                                fg='#e74c3c', font=("Arial", 11, "bold"))
        position_label.pack(pady=(0, 15))

        content_frame = tk.Frame(main_frame, bg='#f8f9fa')
        content_frame.pack(fill="both", expand=True)

        left_column = tk.Frame(content_frame, bg='#f8f9fa', width=280)
        left_column.pack(side="left", fill="both", expand=True, padx=(0, 8))

        right_column = tk.Frame(content_frame, bg='#f8f9fa', width=280)
        right_column.pack(side="right", fill="both", expand=True, padx=(8, 0))

        self.create_contacts_section(left_column)
        self.create_skills_section(left_column)

        self.create_experience_section(right_column)

    def create_contacts_section(self, parent):
        section_frame = tk.Frame(parent, bg='white', relief='flat', borderwidth=1)
        section_frame.pack(fill="x", pady=(0, 8))

        title_label = tk.Label(section_frame, text="📞 Контакты", bg='#3498db', fg='white', 
                             font=("Arial", 11, "bold"), anchor="w")
        title_label.pack(fill="x", padx=8, pady=6)

        content_frame = tk.Frame(section_frame, bg='white')
        content_frame.pack(fill="x", padx=12, pady=8)

        contacts = [
            "📧 maxim.kuvshinov@email.com",
            "📱 +7 (999) 123-45-67", 
            "📍 Москва, Россия",
            "🔗 github.com/maxinkuvshinov"
        ]

        for contact in contacts:
            contact_label = tk.Label(content_frame, text=contact, bg='white', fg='#2c3e50',
                                   font=("Arial", 9), anchor="w", justify="left")
            contact_label.pack(fill="x", pady=3)

    def create_skills_section(self, parent):
        section_frame = tk.Frame(parent, bg='white', relief='flat', borderwidth=1)
        section_frame.pack(fill="x", pady=(0, 8))

        title_label = tk.Label(section_frame, text="🛠️ Навыки", bg='#27ae60', fg='white', 
                             font=("Arial", 11, "bold"), anchor="w")
        title_label.pack(fill="x", padx=8, pady=6)

        content_frame = tk.Frame(section_frame, bg='white')
        content_frame.pack(fill="x", padx=12, pady=8)

        skills = [
            "• Python (Django, Flask)",
            "• JavaScript (React, Node.js)", 
            "• PHP (Laravel)",
            "• SQL (PostgreSQL, MySQL)"
        ]

        for skill in skills:
            skill_label = tk.Label(content_frame, text=skill, bg='white', fg='#2c3e50',
                                 font=("Arial", 9), anchor="w", justify="left")
            skill_label.pack(fill="x", pady=2)

    def create_experience_section(self, parent):
        section_frame = tk.Frame(parent, bg='white', relief='flat', borderwidth=1)
        section_frame.pack(fill="x", pady=(0, 8))

        title_label = tk.Label(section_frame, text="💼 Опыт работы", bg='#e74c3c', fg='white', 
                             font=("Arial", 11, "bold"), anchor="w")
        title_label.pack(fill="x", padx=8, pady=6)

        content_frame = tk.Frame(section_frame, bg='white')
        content_frame.pack(fill="x", padx=12, pady=8)

        experiences = [
            {
                "title": "Senior Python Developer",
                "company": "TechSolutions Inc.",
                "period": "Январь 2023 – настоящее время",
                "description": "Разработка высоконагруженных веб-приложений, руководство командой из 3 разработчиков"
            },
            {
                "title": "Full-Stack Developer", 
                "company": "DigitalAgency Pro",
                "period": "Март 2020 – Декабрь 2022",
                "description": "Создание клиентских проектов на Python и JavaScript, интеграция с API"
            }
        ]

        for i, exp in enumerate(experiences):
            exp_frame = tk.Frame(content_frame, bg='white')
            exp_frame.pack(fill="x", pady=(0, 8))

            title_label = tk.Label(exp_frame, text=exp["title"], bg='white', 
                                 fg='#2c3e50', font=("Arial", 10, "bold"), anchor="w")
            title_label.pack(fill="x", pady=(0, 1))

            company_label = tk.Label(exp_frame, 
                                   text=f"{exp['company']} | {exp['period']}", 
                                   bg='white', fg='#7f8c8d', font=("Arial", 8), 
                                   anchor="w")
            company_label.pack(fill="x", pady=(0, 2))

            desc_label = tk.Label(exp_frame, text=exp["description"], bg='white', 
                                fg='#2c3e50', font=("Arial", 8), anchor="w", 
                                justify="left", wraplength=240)
            desc_label.pack(fill="x", pady=(0, 3))

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()