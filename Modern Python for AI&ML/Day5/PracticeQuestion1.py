# Zodiac Prediction Application

print("Welcome to the Zodiac Prediction Application!")
name = input("Please enter your name: ")
zodiac = input("Please enter your zodiac sign (e.g., Aries, Taurus, Gemini, etc.): ")

# Define zodiac predictions
print(f"Hello {name}! Here is your Fortune for today:")
if zodiac.lower() == "aries":
    print("Today is a great day for new beginnings. Embrace change and take bold steps forward.")   
elif zodiac.lower() == "taurus":
    print("Patience is key today. Take your time to make important decisions and trust your instincts.")
elif zodiac.lower() == "gemini":
    print("Communication is your strength today. Reach out to friends and loved ones for support and advice.")
elif zodiac.lower() == "cancer":
    print("Focus on self-care and nurturing your emotional well-being. Take time to relax and recharge.")
elif zodiac.lower() == "leo":
    print("Your confidence and charisma will shine today. Take the lead in social situations and showcase your talents.")
elif zodiac.lower() == "virgo":
    print("Attention to detail will serve you well today. Stay organized and focused on your tasks.")
elif zodiac.lower() == "libra":
    print("Balance is important today. Seek harmony in your relationships and make time for self-reflection.")
elif zodiac.lower() == "scorpio":
    print("Your intuition is heightened today. Trust your gut feelings and explore new opportunities.")
elif zodiac.lower() == "sagittarius":
    print("Adventure awaits! Embrace new experiences and step out of your comfort zone.")
elif zodiac.lower() == "capricorn":
    print("Hard work and determination will pay off today. Stay focused on your goals and persevere.")
elif zodiac.lower() == "aquarius":
    print("Innovation and creativity are your strengths today. Think outside the box and explore new ideas.")
elif zodiac.lower() == "pisces":
    print("Your empathy and compassion will guide you today. Offer support to those in need and practice self-care.")
else:
    print("Invalid zodiac sign entered. Please check your input and try again.")